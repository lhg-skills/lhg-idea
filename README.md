# lhg-idea

私有收藏/想法库,`lhg-idea` skill 的存储后端。收录我收藏的项目、工具、想关注的人、以及自己的想法,并为将来的某个需求保留检索入口。

- **主库(本仓库)**:条目 + 清单 + 自动化配置,永远轻量
- **[lhg-idea-archive](https://github.com/lhg-skills/lhg-idea-archive)**:收藏的 GitHub 项目整包镜像(分支 `mirror/<owner>/<repo>/*`),仅个人使用,勿公开重分发
- **自动化**:`.github/workflows/track.yml` 每周一 09:00(UTC+8)检查上游更新与关注对象的新仓库,汇总到本仓库标签为 `updates` 的 issue

## 目录

```
SKILL.md            skill 的完整指令(交互流程、命令、模板)
items/              正式条目,一物一文件,平铺
inbox/              未消化的原始收藏(status: seed)
data/tracked.json   自动化跟踪清单(仓库 SHA、关注对象的仓库基线)
scripts/track.py    定时检查脚本,由 workflow 调用
```

## 受控主题词表(topics)

新增词需在此登记。初始词表:

`视频制作` `动效库` `agent技能` `skill工程` `prompt工程` `TTS字幕` `剪映` `Remotion` `前端` `数据可视化` `金融数据` `宏观资讯` `写作` `效率工具` `AI基础设施` `产品设计` `运营增长`

## 检索

不靠文件夹分类,靠条目里的**触发场景**段 + frontmatter topics。使用方式:

```
找 我想去做一个产品宣传片        → skill 返回最匹配的收藏
收藏 https://github.com/xxx     → 研究 → 确认理由 → 收藏或丢弃
更新                            → 汇报本周上游动态
```

## 维护

- 每周 workflow 需要一个 secret `ARCHIVE_PAT`(可访问 lhg-idea-archive 的 fine-grained PAT)用于刷新镜像;未配置时检查照常、镜像跳过并在 issue 中提示
- 手动触发检查:Actions → track-upstream → Run workflow,或 `gh workflow run track.yml -R lhg-skills/lhg-idea`
