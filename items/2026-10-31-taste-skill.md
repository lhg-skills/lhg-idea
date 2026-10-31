---
title: taste-skill
type: repo
source: https://github.com/Leonxlnx/taste-skill
author: Leonxlnx
topics: [agent技能, 前端, 产品设计]
status: digested
added: 2026-10-31
mirror: mirror/Leonxlnx/taste-skill
---

## 一句话
给 AI 的反油腻美术指导：发牌选方向＋无装饰 house style＋真浏览器截图质检。

## 触发场景
- 做的落地页/营销页/作品集被说"AI 味太重、像模板"，想去油腻时
- 想给生成类技能（如 lls-pptx）加一套可执行的审美规则，而不是凭感觉调时
- 需要现成的配色/字体/版式库（247 个获奖站点研究沉淀）时
- 想建立"截图→打分→改"的视觉质检闭环时

## 要点
- 流程：draw.mjs 从 20 个美术方向发牌三选一 → 写论点与文案 → 按蓝图建造 → inspect.mjs 真浏览器量尺寸（标题行数/字号/边距/空屏）→ 按 critique.md 看截图评审 → 动效 → 出报告
- house rules（无装饰）：禁渐变/阴影/图标卡片阵列/细线/eyebrow 小标签/标题双色字；配色=1底+1墨+1强调；字体≤2套；标题≤2行；等宽外边距；字号对比拉开（标题:正文约 4:1）
- library 可直接借用：56 套配色（palettes.json，ground/ink/accent/fields 四角色）、字体系统、20 方向、版式蓝图
- 实证底子：247 站点研究，获奖站图标卡片 1% vs 弱站 28%、渐变 22% vs 52% 等对照数据
- SKILL.md 注册名 design-taste-frontend；安装 `npx skills add https://github.com/Leonxlnx/taste-skill` 或直接复制仓库 SKILL.md
- MIT；106k 星（2026-10-31 在查）；持续更新中
