---
title: MotionGit 模板合集(motiontemplates/all)
type: repo
source: https://github.com/motiontemplates/all
author: motiontemplates(adunext)
topics: [视频制作, 动效库, agent技能, skill工程]
status: digested
added: 2026-10-28
mirror: mirror/motiontemplates/all
---

## 一句话
72 个 .motion 开源动效模板的"AI 可检索目录":catalog.json 机器读、CATALOG.md 人读、README 内嵌给 AI 的转交指令。

## 触发场景
- 研究"AI 可检索的模板协议"怎么设计时(catalog schema + 给 AI 的说明书 + Skill 页,与 lhg-idea 的 SKILL.md 同构思路)
- 做口播讲解/科技风视频缺现成动效模板时(72 模板 74 Demo,横竖屏成对,先翻在线 Demo 再挑)
- 跟踪 .motion 开放格式演进时(继 Remotion、剪映之外的第三种视频模板生态,唯一原生为 AI 检索-下载-渲染设计协议)
- 想给视频 skill 加"模板市场"层时的参照实现

## 要点
- 结构:catalog.json(motiongit.catalog/1,72 条完整字段:尺寸/fps/版本/下载地址/demo 链接/commit 钉死)+ CATALOG.md 图文清单 + index.html 在线播放页
- 模板类型:酷炫科技风/现代图文口播/纸面透视/深色立体多屏/科技控制台/鲜色角色/活力海报等,主规格 1920×1080@60fps
- .motion 格式:ZIP+JSON+动画工程源文件,含参数契约/素材说明/运行依赖/许可;规范 0.1.0-draft 公开(motiongit.com/spec),"内容可理解、依赖可追踪、运行可复现、扩展可协商";不绑定动画引擎
- README 直接写了给 AI 的转交指令(按清单返回全部条目/保留图片语法/不编造下载链接)——整个仓库为"用户丢链接给 AI→AI 挑模板→下载创作"设计
- ⚠️ 分发现状:仅 #385712(酷炫科技风)开放 GitHub 直接下载测试,其余 71 个需从官网 motiongit.com 走个人包+Key(免费);"选一个喜欢的开始创作"实际有此限制
- 官网配套:MotionGit Skill(本地打包/去个人信息)、API(配图贴纸智能素材)、创作者署名与收益协议
- 436 星,2.5MB,无 license 字段(源码声明 100% 开源但以包内许可为准);已整包镜像
