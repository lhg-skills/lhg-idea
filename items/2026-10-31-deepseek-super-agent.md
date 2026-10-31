---
title: DeepSeek《Super-agent 设计探索:迈向更自主的 Agent 系统》
type: article
source: https://mp.weixin.qq.com/s/zoS7GlReWPhfCjENGxXCdg
author: DeepSeek Harness 团队(DeepSeek 产品部)
topics: [AI基础设施, agent技能, skill工程]
status: digested
added: 2026-10-31
---

## 一句话
DeepSeek 发布的 Super-agent 架构方法论:四特征(连续/高效/主动/持久)+ 五模块,全部用计算机系统经典思想构建,附消融实验数据。

## 触发场景
- 设计自己的多任务/常驻 Agent 系统时(目前最完整的中文一手架构参考)
- 上下文窗口不够用/注意力被稀释时,套用"窗口当 Cache 管理"(Inline & Spill + 链式召回)
- 研究 Agent 持久在线方案(存算分离/BYOM 端侧 daemon/脑手分离对照)时
- 做 Agent 可靠性(Watchdog 监控"任务进展"而非进程探活)时

## 要点

### 四特征 → 五模块映射
连续/高效 ← 双层架构;主动 ← 事件驱动;连续+高效 ← 面向人的交互;持久 ← 存算分离 + Watchdog

### 双层架构
- Router 层:常驻、只承接交互与分派(甚至可不配 Bash),用轻量模型;Worker 层:上下文隔离、挂全工具、用最强模型,不直接对人类输出
- "让用户手动管理 Session 是从底层 LLM API 延续的设计惯性;Session 应当是实现细节,不应是用户的认知负担"
- Router 不做水平切分就能够用的原因:积压 Trigger 自动批处理(Prefill 并行,单决定分摊推理时间随积压下降)

### 事件驱动(全部是计算机系统经典思想)
- 两级过滤:程序层 Fast Path(白名单/来源规则)+ 语义层 Slow Path(LLM 按提示词策略判断)
- 订阅直通:同 Thread 后续事件程序直通已订阅 Worker,不经 Router(实验:省约 37% Router token,不降完成质量);订阅多对多,多 Worker 同 Thread 可自行发现冲突
- Inline & Spill:窗口当 Cache,最少信息起步→按局部性内联(相邻消息/前50字/关联ID)→超限 Spill 留续读入口
- 链式召回:Trigger/Thread/Worker 赋唯一 ID 构成引用图,每次召回内联下一跳 ID,按需多跳展开
- 投机执行:群内还在讨论时,Agent 已在后台静默复现并提交修复 PR,确认有价值才交付,否则保持安静
- 异步 ReAct Loop:start()/stop() 替代阻塞 run(),全双工(已实现未默认开启)
- 多信道交互:IM 单次回复硬性 ≤100 词;GitHub/邮件走结构化高密度交付

### 存算分离(持久在线)
- 第一步:Agent Loop 无状态容器 + 会话状态入数据库(摆脱单机生命周期)
- 第二步:执行环境留原地,端侧只装不存会话状态的轻量 daemon;支持 BYOM(用户开发机接入)与间歇在线设备(重新上线后云端 Agent 自动触发该设备上的任务)
- 与 Anthropic"脑手分离"一致;差异:这里接入的是用户日常间歇在线的个人机器(未提交修改/本地凭据),托管文讲的是沙箱与 VPC

### Watchdog
- 主系统外部的独立 Control Loop(定时消息驱动的 Agent Session)
- 不止探活:由模型判断各 Worker"是否有实质进展/方向是否偏离目标";可用自然语言在线修正主系统(增删提示词/调整触发规则)

### 消融实验(第 7 节,含金量最高)
- 300 条消息合成负载(约 20 条工作请求),4 方案 × 5 次:Super-agent p50/p95=12.4/15.7 分钟,显著优于单 Session+Subagent(中性提示 5 次实验 0 次委派,p95 29.5 分钟;提示优先委派 4/5 次委派仍慢且有"自己干"长尾)——**系统层面解决分工,优于提示词工程**
- 去掉直通:完成时间基本不变,Router 决定数 +30%,缓存 token 2323万→3177万(+37%)
- Router 批处理压测:到达率 1→40 条/分钟,batch 1.0→2.8,单请求 2.5s→3.9s,单决定分摊 6.4s→1.6s

### 开放问题
- 双层架构扩展(Router 何时切分/Worker 协作拓扑/长程记忆)、脱离 Session 后的项目管理交互、多实例 A2A 边界、安全与隐私(云端 Loop 被提示词注入→全部端侧设备暴露;需"不接触凭据本身即可用凭据"的机制)
- 结语定位:"没有提出全新理论,而是把计算机系统经典工程思想应用到 Agent 系统"
