---
title: vibe-motion/skills
type: repo
source: https://github.com/vibe-motion/skills
author: vibe-motion
topics: [视频制作, 动效库, agent技能, skill工程, Remotion]
status: digested
added: 2026-10-31
mirror: mirror/vibe-motion/skills
---

## 一句话
16 个"vibe motion"代码渲染 skill 合集(1454⭐),每个 skill = demo GIF + 完整制作过程沉淀 + 可执行渲染流水线。

## 触发场景
- 做"人生/人物故事K线"视频时(remotion-candlestick 是 K 线渲染底座:Yahoo Finance 数据 + Canvas 逐帧 + 深色交易终端风;配 lifeline-k-skill 的数据思路可复刻许家印/李白式视频)
- 代码动画显得僵硬/轻飘/机械时,用 disney-animation-rule-skill(迪士尼 12 原则→代码动画审查标准)做体检
- 视频项目需要现成渲染能力时(黑胶唱机/鱼眼屏摄/线帘物理/克拉尼粒子/3D 地球/打字机等 16 种)
- 学"skill = 完整制作过程记录 + demo GIF"的写法时

## 要点
- 16 skill 分四类:金融可视化(remotion-candlestick / remotion-3d-ticker)、品牌动效(pixel2motion 位图→SVG logo 动效、brand-launch-video-star、light-spotlight、claude-typer)、物理模拟(printed-curtain p5.js 线帘、3d-chladni 克拉尼粒子确定性导出、procedural-fish、fisheye-motion 屏摄鱼眼)、复古媒体(remotion-vinyl-player 黑胶唱机)
- 方法论亮点:disney-animation-rule-skill 把迪士尼 12 原则变成代码动画的创建/审查清单,治"僵硬、轻飘、物理正确但表现力不足"——与 mg-styles-15 的 rubric 评审同源
- 安装:`npx skills add vibe-motion/skills`(交互式,选 agent 对应目录)
- 注意:README 标注**已停止维护,迁至 motionface.cc**;仓库无统一 license 字段(线帘引擎 CC BY-SA 4.0、克拉尼预览 CC BY-NC 4.0,按包内许可);63MB 含大量 demo GIF
- 已整包镜像 mirror/vibe-motion/skills
