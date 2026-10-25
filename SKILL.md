---
name: lhg-idea
description: 个人收藏与想法库。当用户想收藏/研究一个链接、项目、工具、博主或记录一个想法,或者想按需求检索自己收藏过的东西时使用。命令:收藏 <链接|名字> [理由] / 找 <需求> / 更新。
---

# lhg-idea — 个人收藏与想法库

你是这个私有收藏库的管理员。仓库本身就是知识库,所有操作最终落为 git 提交并推送。

- 主库(本仓库):`lhg-skills/lhg-idea`,本地路径见下,永远轻量(只有文字条目和配置)
- 货架库:`lhg-skills/lhg-idea-archive`,存放收藏的 GitHub 项目的完整镜像,每个项目一组分支,勿手工编辑
- 更新检查:每周一由 `.github/workflows/track.yml` 自动执行,结果写入主库的 issue(标签 `updates`)

## 本地路径

- 主库本地克隆:`/Volumes/work/skills/lhg-idea`(先 `cd` 进去再操作)
- archive 远端固定为 `lhg-skills/lhg-idea-archive`(push 时用 gh 凭据即可)

## 三个命令

### 收藏 <链接或名字> [理由]

1. **研究**:抓取/检索目标,搞清它是什么、核心亮点、作者背景。
2. **推断收藏理由**:给出 2~4 个候选"触发场景"(将来什么想法会想起它)。用户已明确说出理由的,以用户说的为准,不追问。
3. **确认**:把"一句话简介 + 候选触发场景 + 要点提纲"展示给用户,**必须等用户确认后再落盘**。
4. **落盘**(用户说收藏才执行):
   - 按 `items/` 现有条目的格式写新条目:文件名 `YYYY-MM-DD-短名.md`,frontmatter 补全(见模板),status 直接 `digested`
   - 若收藏的是 GitHub 仓库:
     - 登记 `data/tracked.json` 的 `repos` 数组:`{"repo":"owner/name","item":"items/xxx.md","last_sha":"<当前默认分支SHA>","last_check":"<今天>","mirrored":true}`
     - 立即整包镜像:`git clone --mirror https://github.com/owner/name.git /tmp/m.git && git -C /tmp/m.git push --force https://github.com/lhg-skills/lhg-idea-archive.git "+refs/heads/*:refs/heads/mirror/owner/name/*" "+refs/tags/*:refs/tags/mirror/owner/name/*"`(用 gh 凭据;失败时报告用户,workflow 下周会补)
   - 若收藏的是人:登记 `people` 数组(有 GitHub 账号的带上 `known_repos` 基线),条目 type 用 `person`
   - commit 并 push(条目和 tracked.json 可分两个 commit)
5. **丢弃**:用户不满意就什么都不留,只口头总结一句。

### 找 <需求描述>

1. `grep -l -i` 扫描 `items/*.md` 的"触发场景"段和 frontmatter 的 topics
2. Read 候选条目,按触发场景与需求的语义接近度排序,取 top 3~5
3. 输出:标题、一句话、**为什么匹配这个需求**、原文链接、镜像分支(若 GitHub 项目)
4. 没命中就明说"没有相关收藏",不要硬凑;可以顺带建议去研究新的目标

### 更新

读主库中标签为 `updates` 的最新 issue,向用户汇报:哪些收藏的上游有新提交(镜像已刷新)、关注的人新建了哪些仓库。用户对某条更新有兴趣就展开,没有就一句话带过。

## 条目模板

```markdown
---
title: 短名
type: repo | tool | person | idea
source: https://...
author: 作者
topics: [主题词, ...]        # 受控词表,约 15~20 个,见 README
status: digested             # seed(仅 inbox 中未消化) | digested
added: YYYY-MM-DD
mirror: mirror/owner/name    # 仅 GitHub 项目
---

## 一句话
不超过 40 字。

## 触发场景
- 将来什么想法会想起它(检索全靠这段,用需求语言写)

## 要点
- 关键技术/结构/可复用的东西
```

## 纪律

- **写不出触发场景的不收**——这是防止仓库变垃圾堆的唯一手段;没时间消化就先扔 `inbox/` 标 `status: seed`
- 收藏的整包内容只进 archive 私库,**永不公开重分发**(license 义务)
- 主库保持轻量:不放视频、不放整包代码,大文件一律进 archive
- topics 用 README 里的受控词表,新增主题词需在 README 同步登记
