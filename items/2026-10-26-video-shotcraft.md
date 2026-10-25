---
title: video-shotcraft
type: repo
source: https://github.com/Vincentwei1021/video-shotcraft
author: Vincentwei1021
topics: [视频制作, 动效库, agent技能, skill工程, 剪映, Remotion]
status: digested
added: 2026-10-26
mirror: mirror/Vincentwei1021/video-shotcraft
---

## 一句话
124 张镜头配方卡 + Remotion,让 agent 用代码给产品拍电影感宣传片。

## 触发场景
- 想给自己的产品/网页做一支宣传片时
- 想研究 skill 如何组织"可检索的配方卡片库"时(每张卡 = Markdown 配方 + 可运行 demo)
- 想把 Remotion 成片导入剪映二次剪辑时(内置剪映草稿导出)
- 想做卡音乐节拍剪辑 / 帧级视觉 QA 时

## 要点
- 菜谱卡片模式:10 大类(开场/运镜/转场/字体/UI入场/交互/数据/光影/节奏/片尾),每卡写清 timing、easing、编舞,demos/<类别>/<卡片>/ 有参考实现
- 目录分层范本:SKILL.md(核心规则)+ references/(管线/美学QA/节拍)+ template/(可编译脚手架)+ workbench/(类剪映浏览器编辑器)
- 每一帧都是代码画的,不是生成模型——截图真实网页 → 选镜 → Remotion 动画 → 帧级 QA
- 149 个 SFX + 5 首 BGM,可选 Upload-Post 社媒发布
- 配方来源:拆解 ClickUp/Perplexity/Slack/Notion/Figma/Raycast 的宣传片后从零重写
- Apache-2.0;注意 Remotion 本身商用需单独 license
- 13.6k stars,是"卡片库模式"跑通的最强证据
