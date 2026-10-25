#!/usr/bin/env python3
"""每周上游检查:仓库更新检测 + 镜像刷新 + 关注对象新仓库 + 更新汇总 issue。

由 .github/workflows/track.yml 调用;也可本地手动运行(需 GH_TOKEN)。
环境变量:
  GH_TOKEN       必需,调用 GitHub API(Actions 自带 GITHUB_TOKEN 即可)
  ARCHIVE_PAT    可选,用于向 lhg-idea-archive 推送镜像;缺失则跳过镜像并在报告中提示
  ARCHIVE_REPO   默认 lhg-skills/lhg-idea-archive
  IDEA_REPO      默认 lhg-skills/lhg-idea
"""

import json
import os
import shutil
import subprocess
import tempfile
from datetime import date, datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TRACKED = ROOT / "data" / "tracked.json"
IDEA_REPO = os.environ.get("IDEA_REPO", "lhg-skills/lhg-idea")
ARCHIVE_REPO = os.environ.get("ARCHIVE_REPO", "lhg-skills/lhg-idea-archive")
ARCHIVE_PAT = os.environ.get("ARCHIVE_PAT", "")
ISSUE_LABEL = "updates"
ISSUE_TITLE = "📥 上游更新汇总"
CLONE_TIMEOUT = 5400  # 大仓库(mg-styles-15 约 570MB)需要充裕时间


def run(cmd, timeout=120, check=True, input_text=None):
    return subprocess.run(
        cmd, capture_output=True, text=True, timeout=timeout, check=check,
        input=input_text,
    ).stdout.strip()


def gh(path, method="GET", json_body=None, **kwargs):
    cmd = ["gh", "api", path, "--method", method]
    if json_body is not None:
        cmd += ["--input", "-"]
        out = run(cmd, timeout=120, input_text=json.dumps(json_body))
        return json.loads(out) if out else None
    for k, v in kwargs.items():
        if v is not None:
            cmd += ["-f", k, v]
    out = run(cmd, timeout=120)
    return json.loads(out) if out else None


def mirror(repo):
    """整包镜像 owner/name 到 archive:heads 与 tags 全部推到 mirror/<owner>/<name>/ 命名空间。"""
    if not ARCHIVE_PAT:
        return False, "未配置 ARCHIVE_PAT,镜像未刷新"
    tmp = tempfile.mkdtemp(prefix="idea-mirror-")
    try:
        run(["git", "clone", "--mirror", f"https://github.com/{repo}.git", f"{tmp}/m.git"],
            timeout=CLONE_TIMEOUT)
        url = f"https://x-access-token:{ARCHIVE_PAT}@github.com/{ARCHIVE_REPO}.git"
        run(["git", "-C", f"{tmp}/m.git", "push", "--force", url,
             f"+refs/heads/*:refs/heads/mirror/{repo}/*",
             f"+refs/tags/*:refs/tags/mirror/{repo}/*"],
            timeout=CLONE_TIMEOUT)
        return True, "镜像已刷新"
    except (subprocess.TimeoutExpired, subprocess.CalledProcessError) as e:
        detail = (getattr(e, "stderr", "") or str(e))[-400:]
        return False, f"镜像失败:{detail}"
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def check_repos(data):
    """返回待写入报告的行;同时原位更新 data['repos']。"""
    lines, today = [], date.today().isoformat()
    for entry in data.get("repos", []):
        repo = entry["repo"]
        try:
            meta = gh(f"repos/{repo}")
            branch = meta.get("default_branch", "main")
            sha_now = gh(f"repos/{repo}/commits/{branch}")["sha"]
        except Exception as e:
            lines.append(f"- ⚠️ `{repo}` 检查失败:{e}")
            continue
        if sha_now == entry.get("last_sha"):
            entry["last_check"] = today
            continue
        note = f"sha `{(entry.get('last_sha') or '?')[:7]}` → `{sha_now[:7]}`"
        try:
            cmp = gh(f"repos/{repo}/compare/{entry['last_sha']}...{sha_now}")
            note += f",新增 {cmp['total_commits']} 个提交"
        except Exception:
            pass
        ok, msg = (mirror(repo) if entry.get("mirrored", True) else (True, "未启用镜像"))
        lines.append(f"- {'✅' if ok else '⚠️'} [{repo}](https://github.com/{repo}):{note};{msg}")
        entry["last_sha"] = sha_now
        entry["last_check"] = today
    return lines


def check_people(data):
    """关注对象的 GitHub 名下出现新仓库时进入报告;基线原位更新。"""
    lines, today = [], date.today().isoformat()
    for entry in data.get("people", []):
        user = entry.get("github")
        if not user:
            continue
        try:
            repos = gh(f"users/{user}/repos?sort=created&direction=desc&per_page=100")
        except Exception as e:
            lines.append(f"- ⚠️ [{user}](https://github.com/{user}) 检查失败:{e}")
            continue
        names = [r["name"] for r in repos]
        known = set(entry.get("known_repos", []))
        fresh = [r for r in repos if r["name"] not in known] if known else []
        for r in fresh:
            desc = (r.get("description") or "").strip()
            stars = r.get("stargazers_count", 0)
            desc = f" — {desc}" if desc else ""
            lines.append(
                f"- 🆕 [{user}/{r['name']}](https://github.com/{user}/{r['name']})"
                f"(⭐ {stars}){desc}"
            )
        entry["known_repos"] = names
        entry["last_check"] = today
    return lines


def save_issue(report):
    """更新(或创建)带 updates 标签的汇总 issue。"""
    ensure_label()
    open_issues = gh(f"repos/{IDEA_REPO}/issues?state=open&per_page=50") or []
    target = next(
        (i for i in open_issues
         if not i.get("pull_request") and any(l["name"] == ISSUE_LABEL for l in i["labels"])),
        None,
    )
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    body = f"{report}\n\n---\n_由 track.yml 自动更新于 {now}_"
    if target:
        gh(f"repos/{IDEA_REPO}/issues/{target['number']}", "PATCH",
           json_body={"body": body, "title": ISSUE_TITLE})
        print(f"issue #{target['number']} 已更新")
    else:
        created = gh(f"repos/{IDEA_REPO}/issues", "POST",
                     json_body={"title": ISSUE_TITLE, "body": body,
                                "labels": [ISSUE_LABEL]})
        print(f"issue #{created['number']} 已创建")


def ensure_label():
    try:
        gh(f"repos/{IDEA_REPO}/labels", "POST", name=ISSUE_LABEL, color="1D76DB")
    except Exception:
        pass  # 已存在


def main():
    data = json.loads(TRACKED.read_text())
    repo_lines = check_repos(data)
    people_lines = check_people(data)
    TRACKED.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")

    pat_note = "" if ARCHIVE_PAT else (
        "\n> ⚠️ 未配置 `ARCHIVE_PAT`,本周镜像刷新被跳过。"
        "配置方法见主库 README。\n"
    )
    if not repo_lines and not people_lines:
        body = "## 本周无上游变化 ✅"
    else:
        parts = []
        if repo_lines:
            parts.append("## 收藏的仓库\n" + "\n".join(repo_lines))
        if people_lines:
            parts.append("## 关注的人\n" + "\n".join(people_lines))
        body = pat_note + "\n\n".join(parts)
    save_issue(body)
    print("track done")


if __name__ == "__main__":
    main()
