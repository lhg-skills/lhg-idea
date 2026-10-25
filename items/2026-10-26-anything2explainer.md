---
title: anything2explainer
type: repo
source: https://github.com/Vincentwei1021/anything2explainer
author: Vincentwei1021
topics: [视频制作, TTS字幕, agent技能, skill工程, prompt工程]
status: digested
added: 2026-10-26
mirror: mirror/Vincentwei1021/anything2explainer
---

## 一句话
话题进,带旁白/字幕/进度条的黑底动效科普片出,9 阶段流水线全自动。

## 触发场景
- 想把一个话题/论文做成讲解视频时
- 设计多阶段 agent 流水线时(研究→叙事→TTS→分镜→试点→并行构建→渲染→QC)
- 需要词级时间戳对齐字幕和动画时
- 想抄"少打扰用户"的检查点设计时(全程只问 4 次,全卡在改一次代价最大的节点)

## 要点
- 流水线:研究(屏幕上每个数字必须有来源)→ 叙事定稿 → TTS 词级时间轴 → 分镜 → 30 秒试点片确认风格 → 4-14 个 agent 并行构建分镜组 → 渲染 → 每章 QC agent 复查
- 配音后旁白冻结:"改一个字,全片重新对时"——检查点放在不可逆节点之前
- TTS:中文 edge-tts zh-CN-YunxiNeural(云),英文 kokoro-82m 本地 CPU
- 确定性渲染:动画是帧号的纯函数 + 固定种子,无 GPU(headless Chromium)
- reference/ 里有六套 prompt 模板和 lessons learned,examples/rag/ 有完整过程留痕
- 中文/英文双语输出;1280×720@30fps;PolyForm Noncommercial(商用需授权)
