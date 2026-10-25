---
title: video-talkcraft
type: repo
source: https://github.com/Vincentwei1021/video-talkcraft
author: Vincentwei1021
topics: [视频制作, TTS字幕, agent技能, skill工程]
status: digested
added: 2026-10-26
mirror: mirror/Vincentwei1021/video-talkcraft
---

## 一句话
词级时间戳驱动运镜的口播视频 skill,专治"PPT 感"。

## 触发场景
- 做口播/旁白驱动的讲解视频时
- 动效跟着语音节奏走(词级对齐,不是句级)时
- 想抄它的 demo 卡片结构时(demos/ 下每个动效一个可运行目录,如 douyin-follow-card、keyword-pop-highlight)
- 需要竖屏 9:16 抖音风格卡片时

## 要点
- 本地词级时间对齐 → 运镜节奏跟人声,避免匀速 slideshow
- 目录结构与 video-shotcraft 同源:SKILL.md + references/ + demos/ + template/ + workbench/
- 本地已安装:~/.zcode/skills/video-talkcraft,可直接拆解学习
- 1.8k stars;适合作为"口播类视频 skill"的参考实现
