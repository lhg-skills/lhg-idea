---
title: lemo-opuscar
type: repo
source: https://github.com/lemomo-ai/lemo-opuscar
author: lemomo-ai
topics: [视频制作, 动效库, prompt工程, agent技能]
status: digested
added: 2026-10-26
mirror: mirror/lemomo-ai/lemo-opuscar
---

## 一句话
59 种现成影片风格的 prompt 工具箱,每种配一支纯代码短片,可直接装成 skill。

## 触发场景
- 想给视频项目选/造特定影片风格时(59 现成 + 98 风格示范片,比 mg-styles-15 覆盖面更大)
- 想研究"风格 prompt"怎么写才能稳定复现时(每风格 = prompt + 对照成片)
- 需要纪录片/证据片风格时(2026-10 新增 Edit & Documentary 8 种、Evidence Films 8 种,后者每个数字有来源)
- 想自定义并保存自己的风格时("Make a style your own"流程)

## 要点
- 画面 canvas/WebGL 逐帧渲染,配乐来自免费采样库,旁白 TTS;无生成模型、无素材片
- 示范片 OPUSCAR 98:98 座最佳影片各配一种风格(77 个 2D / 4 个 2.5D / 17 个 3D)
- 明确针对 Claude Opus 5.5 调校,其他模型复现效果打折
- 安装方式:官方推荐直接装成 skill;gallery 在 lemomo-ai.github.io/lemo-opuscar
- MIT(代码)+ CC BY 4.0(内容);约 145MB;7218 星
- 镜像待授权后补推(含 1 个 workflow 文件)
