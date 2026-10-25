---
title: huashu-motion
type: repo
source: https://github.com/alchaincyf/huashu-motion
author: alchaincyf
topics: [视频制作, agent技能, skill工程, Remotion]
status: digested
added: 2026-10-26
mirror: mirror/alchaincyf/huashu-motion
---

## 一句话
一句话直出商业级产品宣传片:agent 会作曲、会拍片,还能"指着画面改"。

## 触发场景
- 做"说一句话就出宣传片"的产品体验时(与 video-shotcraft 直接对标,交互设计不同)
- 研究"点画面改一处"的编辑器交互时:按 C 点击元素 → 评论带时间点/场景/源码位置 → agent 只改那一处,预览原位刷新,每版可回退
- 需要"画面配乐"方案时:作曲家模式先写 ABC 记谱乐谱(标记对齐场景),再由真乐器采样演奏,全本机零 API 费
- 做标题/数字/颜色/时长这类"参数化属性面板"时

## 要点
- 流程:读产品 → 给三个方向挑 → 写整支片 → 自写谱配乐 → 浏览器编辑器交付
- 点改交互:agent 先把那一帧+点中的小块截图放大看,再只改那一处;属性变成右侧输入框,不用等 agent
- README 里所有动画都是它自己做的(自举展示);发布片在 releases 下 1080p MP4
- MIT;43MB;1.7k 星;README 中英双语;`npx skills add alchaincyf/huashu-motion` 一行装
- 镜像已入库(无 workflow 文件,首次镜像本地完成)
