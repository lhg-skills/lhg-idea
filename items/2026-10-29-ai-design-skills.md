---
title: AI Design Skills
type: repo
source: https://github.com/elayadesign/ai-design-skills
author: elayadesign(Elaya)
topics: [前端, agent技能, skill工程, 产品设计]
status: digested
added: 2026-10-29
mirror: mirror/elayadesign/ai-design-skills
---

## 一句话
给 AI 编程工具用的落地页设计规则库，让 AI 按一套视觉系统出能转化的落地页。

## 触发场景
- 想让 Claude Code / Cursor / Codex 做落地页，不想每次都出千篇一律的 AI 味页面时
- 做产品、课程、活动落地页，需要页面结构和转化文案一起给出来时
- 研究 agent skill 该怎么写时，规则文件加设计值集中改的写法值得参照
- 想把落地页换成自己品牌风格，只改几行设计值时

## 要点
- 现状(2026-10-29 核实):合集目前只有一个技能 `landing-page-design`，README 说更多在路上；MIT 协议，11,528 星、831 fork，默认分支 main
- `landing-page-design`:从零建落地页，含 intake 提问、页面结构、转化文案，外加字体、间距、圆角、动效一整套视觉系统
- 安装:Claude Code 拷到 `.claude/skills/`；Cursor 把 SKILL.md 拷到 `.cursor/rules/` 或贴进 Settings → Rules for AI；Codex 放 `AGENTS.md`，Windsurf 放 `.windsurfrules`，Cline 放 `.clinerules`，通用工具可直接贴进 system prompt
- 设计值集中:字体、颜色、间距、动效等设计值都集中在文件底部附近的一节，fork 后改那一节，整套技能跟随变化
- 风格意见比较强:用之前先核对 SKILL.md 里的硬性规则是否与自有品牌冲突
- 同作者另有独立仓 `elayadesign/redesign-skill`(升级已有网站而非从零新建)，不在本合集内
- 已整包镜像到私库 lhg-idea-archive，分支 `mirror/elayadesign/ai-design-skills/main`
