---
title: lieflat-less-ai-tone
type: repo
source: https://github.com/larashero3-dotcom/lieflat-less-ai-tone
author: larashero3-dotcom(躺在废墟里 Lieflat)
topics: [写作, agent技能, skill工程, prompt工程]
status: digested
added: 2026-11-06
mirror: mirror/larashero3-dotcom/lieflat-less-ai-tone
---

## 一句话
520 万字语料、1,169 篇对照、100+ 项指标、约 50 万次模型语义判断做出来的"去 AI 味"skill,5136⭐。

## 触发场景
- 中文稿要去 AI 味时(白名单式改写只动清单内规则,没命中的逐字保留,不误伤正常表达)
- 研究"用大规模实测数据蒸馏 skill"的方法论时(两轮对照研究:先量化筛选特征,再实测验证)
- lhg-writing 迭代时做对照参考(lhg-writing 靠人工总结的 AI 味指纹,这个靠 50 万次语义判断实测,互为印证)
- 禁用词表/去 AI 味 prompt 失效时(案例:满篇避开"赋能/闭环/抓手"依然一眼 AI)

## 要点
- 工作流设计:先交付**检测报告**(指标+研究参照+原文例句+改法),用户回复后再改写并复测——诊断与改写分离,不一把梭
- 两轮对照研究筛选"值得处理"的写作特征;实测对比 300 篇 AI 输出 vs 329 篇真实文章;每条规则有可定位的触发标记
- 完整研究方法、数据与**被推翻的预设**全部公开——skill 即研究论文
- 痛点洞察:禁用词表管不住深层 AI 味;攒十几条经验规则直接喂模型改稿,会误伤设问句/小标题、把顺畅句子硬拆
- 本地联动:你装的 writing-dna-skill(同一作者)已内置本规则集作为成稿最后一道工序
- Python;license 为自定义(NOASSERTION);2026-08-20 创建;5136⭐;已整包镜像
