---
title: REA 作者的逆向工程全环境套件(20 仓库清单)
type: tool
source: https://github.com/morluto/awesome-reverse-engineering
author: morluto(REA 作者)
topics: [AI基础设施, agent技能, 效率工具]
status: digested
added: 2026-11-02
---

## 一句话
REA 作者配套放出的逆向工程全环境:5 大类 17 个顶级工具 + 2 个 awesome 清单 + "净室循环"方法论闭环。

## 触发场景
- 需要逆向某个 App/二进制/协议时,按五大类直接查工具(本条目就是导航页)
- 研究"净室循环"(SPEC→重建→判定→迭代)逆向复刻方法论时
- 给 agent 接逆向能力时选 MCP 桥(GhidraMCP vs ida-pro-mcp)
- 找 AI 逆向工具时查 awesome-ai-reverse-engineering(122 个仓库带评分)

## 要点

### 五大类工具清单(星数为 2026-11-02 核实值)
- **分析内核**:ghidra(97k,NSA,Apache-2.0)· GhidraMCP(11.7k,agent 直接操作 Ghidra)· ida-pro-mcp(13.3k,MIT)· rea(41.7万,已单独收藏)
- **移动端/App**:jadx(51.5k,APK→Java)· Apktool(26.9k,拆包重打包)· Frida(22.6k,运行时挂钩)· ILSpy(26.9k,.NET 反编译)
- **二进制/底层**:radare2(25.2k)· x64dbg(50.2k,Windows 调试)· ImHex(55.7k,模式语言十六进制)· angr(9.3k,符号执行)
- **网络/运行**:mitmproxy(46.6k,TLS 中间人)· dnSpyEx/dnSpy(11.4k,.NET 调试修改)· rizin(4.1k,radare2 分支)· raddebugger(8.7k,Epic Games 出品,MIT)
- **重建/验证**:zhuyansen/awesome-ai-reverse-engineering(33⭐,122 个 AI 逆向仓库全打分)· morluto/awesome-reverse-engineering(1531⭐,CC0,作者亲选)· REA 工作流提示词(随 REA 分发)· 净室循环

### 净室循环(方法论闭环,最有价值的部分)
```
二进制 → REA → SPEC.md → 重建 → 判定 → 不行就再来
```
逆向的目标不是"看懂"而是"复刻":用 SPEC.md 固化行为规格,按规格重建,用判定标准校验行为一致性,迭代到对得上为止。与 overlay-studio 的"编排即 JSON"、lhg-craft 的"断言先行"同一思想家族:规格先行、证据闭环、迭代收敛。

### 使用说明
- 工具本身巨大(ghidra/frida 数 GB)且为老牌稳定项目,不镜像不逐个跟踪;需要哪个直接 clone 上游
- 清单主入口:morluto/awesome-reverse-engineering(CC0,可自由复用)
- 边界:学习/安全研究/互操作正途;绕过授权做盗版侵权不碰
