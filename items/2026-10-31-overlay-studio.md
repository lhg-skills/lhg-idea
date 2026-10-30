---
title: overlay-studio
type: repo
source: https://github.com/jeszhou/overlay-studio
author: jeszhou (Jessie Zhou)
topics: [视频制作, 剪映, agent技能, skill工程]
status: digested
added: 2026-10-31
mirror: mirror/jeszhou/overlay-studio
---

## 一句话
给口播视频加动效层的免费工作台:20 张预制动效卡,AI 只挑卡和对时间,导出透明层直接盖进剪映。

## 触发场景
- 做/改 jianyingskill 时对标它的工作流与"透明层导出进剪映"实现(无头 Chrome 逐帧渲染 29.97fps 透明 MOV/WebM)
- 研究"反 AI 抽卡"的卡片库设计时(卡预先做好调好,AI 只做语义编排:哪句话配哪张卡、几秒进几秒出)
- 口播视频需要动效层时,直接用它:SRT → AI 编排 JSON → 编辑台手调 → 透明 MOV → 剪映置顶轨道
- 学"编排即 JSON(可 diff 可手改)+ 体检器(占位文案/时间越界/快闪检查,用户决定最大)"的交付物设计

## 要点
- 核心思想:大模型不再现场发挥,token 只花在"读字幕生成编排 JSON"一步;改色/大小/时间全在可视化编辑台(实时预览+时间轴+参数面板),滑杆五秒见效零 token
- 20 张动效卡覆盖 11 个用途分组:章节进度条/双语字幕层/要点钉板/数字圆环计数器/双栏对比/金句定格/步骤时间线/术语卡/界面标注/人物名牌/运镜与终端演示
- 工作流:口播视频 → SRT(剪映识别或 Whisper)→ 内置 overlay-fx-generator skill 生成编排 JSON → Studio 导入打磨 → 导出透明 MOV(29.97fps NTSC)→ 剪映盖原片零转换零对位
- 多 Agent 入口:同一 skill 生成 .claude/.agents/.codebuddy/.workbuddy 四套目录——与 lhg-* 多 runtime 思路一致
- 技术:TypeScript + Vite(motion-playground 目录,npm run dev 端口 5177);导出需 Node ≥22.12 + ffmpeg;编排质量取决于所用模型强弱,卡片与导出固定
- License:source-available 自定义协议(免费使用、成片归你可商用;软件本身禁转售与商业再分发)——私有镜像合规
- 2026-09 创建;433 星;2.8MB;无 CI 文件;已整包镜像
