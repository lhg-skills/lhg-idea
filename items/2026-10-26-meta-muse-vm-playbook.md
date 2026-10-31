---
title: Meta Muse 免费云电脑全玩法(公众号文章)
type: article
source: https://mp.weixin.qq.com/s/uuE6CUrm3XhbkLhsZTeAcg
author: Hami_Xinjiang(雪xue)
topics: [AI基础设施, agent技能, 效率工具]
status: digested
added: 2026-10-26
---

## 一句话
Meta Muse(代号 Hatch)给每个用户免费配 8核/7.7G/100G 云 VM,文章是开通、接管、自愈的完整操作手册。

## 触发场景
- 研究或设计"云端沙盒型 Agent 产品"(VM 分配、持久层、自愈 Hook)时,Muse 是最新真实样本
- 想了解 Meta 免费算力入口的架构边界(出口网关/TUN 限制/70+ CLI)时
- 做 agent 安全研究(宿主侧 Sentinel/eBPF 如何约束 Agent VM)时
- 需要海外无头浏览器环境的备选方案调研时

## 要点(用户确认:全文照记,含注册与套娃方法;使用风险自担)

### 产品事实
- 2026-09 上线,muse.ai,登顶美区应用商店;每位用户免费分配独立专用 VM:8 核 CPU / 7.7 GiB 内存 / 100GB 独立块存储,公测期 $0/月,无自动扣款绑定

### 注册(卡点:美区 IP + 金融级风控 + 18+ 核验)
- 根因:Muse 是可订机票/购物/代付的 Action Agent,部署金融级反欺诈;机房 IP 秒判脏 IP 进 Waitlist;部分账户需 Visa/Mastercard 1 美元预授权(实测随后撤销)
- 文章解法:用 Gemini Pro/Advanced 的 Spark 模式(谷歌云端原生 Chrome,出口在 Google 美国骨干网,IP 信誉高)——指令"帮我使用远程桌面打开 https://muse.ai/join",在远程窗口完成邮箱验证+年龄(填 20+)+验卡;通过后送 10 亿计算 Token 额度;之后本地直接登录不受 Waitlist 限制

### 套娃玩法(利用 Meta 高信誉出口)
- 让 Muse 开 Claude 账号:"请打开浏览器访问 claude.ai,帮我注册一个新的 Claude 账号",验证码交给它,由 Meta 网络环境包办,成功率远超普通环境
- AWS:用 Muse 内置浏览器开 AWS Free Tier / Builder ID,规避国内 IP 风控
- 注:Amazon.com 电商端已被亚马逊官方封锁(防爬虫/比价/代下单),但 AWS 开发者服务端仍可用
- 其他:Stripe/Shopify 沙盒、机票酒店比价、论文与 GitHub 自动抓取归档

### 架构陷阱与核心事实(全文最值钱部分)
- 双层存储:根目录仅 7.5GB,基于内存 overlay tmpfs,重启全清(/etc、/usr/local/bin、/opt 全还原);/home/<user> 挂独立块设备 /dev/mapper/rv,100GB 跨重启永久保留
- 铁律:所有脚本/软件包/配置/数据必须放 /home/<user>/workspace/
- 容器无 TUN 设备:tailscale up 报 ioctl(TUNSETIFF): Operation not permitted,必须 --tun=userspace-networking 用户态模式(--state 也指到持久区)
- 出口安全网关:所有外联走 hatch-egress-proxy:3128,FRP 等非 HTTP 外联必须显式注入 http_proxy/https_proxy/all_proxy 网关变量才能出去

### 接管四步
1. 带外中控:让 Muse 执行 komari-agent 接入 Komari 面板,面板终端直出 root Shell
2. FRP 公网主轨:持久区缓存 openssh deb 离线包 → 公钥免密 → frpc.toml(serverAddr/remotePort 2222)→ start_frpc.sh 注入网关变量;本地 ~/.ssh/config 配 Host muse,1 秒免密登入
3. Tailscale 内网直轨:官方二进制 + userspace-networking + state 持久化 + socks5 :1055,与 NAS/台式机组网
4. 平台原生 Hook 自愈:/home/<user>/hooks/definitions/home-init.json 定义 runtime-boot 触发器执行 restore_all.sh(恢复 openssh+FRP+Tailscale),实例冷启动 60 秒内全部复活

### 70+ 官方免密工具(/opt/<user>/bin/)
- web-search:免限流实时搜索,返回干净 Markdown+引用
- media-generation:Muse Image/Video 大模型,秒级高清生图生视频,托管 Meta CDN,免费
- tts:Shortwave 引擎高保真语音合成
- hatch_gws_cli:Gmail(+triage)/Google Drive 已授权直连;outlook-mail:微软 Graph 直通;notion-cli:标准 MCP 协议查改 Notion

### 适用边界(作者自评)
- 适合:缺海外大内存节点的极客(无头浏览器自动化/爬虫/重计算)、被风控困扰的海外开发者、想免配置 OAuth 的效率用户
- 不适合:当通用长周期梯子(出口网关审计,非 HTTP 被掐)、无 Linux 基础的小白、挂生产级核心数据库(有冷迁移风险)
- 安全底线:容器内改进程名≠宿主不可见,Meta 宿主侧有 Sentinel 与 eBPF 监控;正确定位是"按需唤醒、高并发爬虫、免风控浏览器代工与重型计算外包战术沙盒"

### 风险备忘(收藏时确认:全文照记,风险自担)
- 绕地区限制与 18+ 核验、代开 Claude/AWS 均违反对应平台 ToS,存在封号/法律风险;AWS 已对 Muse 电商端实施封锁,风控可能随时扩大
- 宿主侧有监控,不要在 VM 内存敏感凭证或做依赖隐私的操作

## 补记：web-search CLI 实测深挖（2026-10-31，用户亲手 SSH 进 VM 后逐条核验）

### 路径与数量纠正（原文有误）
- 原文 `/opt/<user>/bin/` 有误，实测为 `/opt/hatch/bin/`；`/opt` 重启还原、只读是对的
- 实测数量：`/opt/hatch/bin` 112 个可执行文件、`/opt/hatch/connectors` 73 个连接器、`/opt/muse/skills` 56 个系统 skill——"70+" 对应的是 connectors 数

### "免密"到底免了什么（两层）
- Meta 自家三件套（web-search、media-generation、tts）：走平台侧官方鉴权，真免配置。tts help 注明 via Meta Shortwave API，media-generation 注明 via Meta's media generation API
- 第三方（hatch_gws_cli、outlook-mail、notion-cli）：第一次仍需用户亲手点一次 OAuth，之后 CLI 用存好的连接，skill/脚本里永不出现密钥。免的是"管密钥"，不是免认证
- notion-cli 走标准 MCP 协议，gmail/outlook 走自家 CLI——/opt 工具箱里 MCP 只是接入形态之一

### browser.search vs web-search CLI：同一后端，两扇门（实锤）
- CLI 返回 JSON 里白纸黑字 `"tool":"browser_search"`，help 写 "via web-search-tool"
- 窗口里助手调的是 `browser.search` 工具；终端手敲 `/opt/hatch/bin/web-search` 走同一服务。结果、引用、抓取时间一致，只是参数旋钮略有不同（工具侧有垂直频道，CLI 侧有 --max-age-days 等）

### 用量与计费（2026-10-31 实查 subscription-status）
- 窗口搜索计入每周免费额度：用户当前免费档（无订阅），已用 37%，11/2 6:46 CST 重置；另有 30B 额外 token 池 0% 未动
- 平台按整轮任务打包计量，不单独列"搜索花了多少 token"
- CLI 手动调用的计费归属查不到（subscription-status 只给总数不分项）；原文"免限流"说法无依据，存疑

### 调用方式
- 普通用法：窗口说人话（"帮我搜一下 XX"），命令由助手下，用户不用碰终端
- 极客接管玩法：SSH 进 VM 后手敲（用户 2026-10-31 已亲手跑通 root@htch-runtime）

### 常用命令
- `/opt/hatch/bin/web-search "关键词"`（多词自动空格拼接）
- `/opt/hatch/bin/web-search "关键词" --language zh`
- `/opt/hatch/bin/web-search "关键词" --max-age-days 7 --max-age-keep-undated`（追热点：新鲜优先、没日期的不冤杀）
- `/opt/hatch/bin/web-search "关键词" --out ~/workspace/search-$(date +%F).md`（落盘）
- 通用套路：`/opt/hatch/bin/<工具名> --help`（如 tts、media-generation）

### help 全解要点
- `--max-age-*` 一家子：默认关闭；`--max-age-days N` 丢掉 N 天前及无日期结果；三个逃生舱 `--max-age-keep-when-empty`（全过期标过期照给）、`--max-age-keep-undated`（无日期排后面保留）、`--max-age-keep-stale`（过期排新鲜后面保留）
- `--verticals` 可重复传，news/sports/weather/finance/datetime，与窗口垂直频道同源
- `--location-context`：正常由 daemon 从会话状态自动注入位置（IP/经纬度/时区）；SSH 手敲没有，搜"附近/天气"类强位置查询吃亏——这是手敲与窗口调用的真实差异
- `--serving-config-name`：覆盖后端排序策略（如 hatch_space_sports_news_obm_merged），高级旋钮
- `--conversation-id` / `--request-id` / `--iteration-index`：可把手敲调用挂进某轮对话的审计链，可观测性做到命令级
- `--allow-stub`：默认后端返回 mock 数据直接报错，防拿到假结果
- `--stdout` 打抽取正文（关摘要）、`--out` 写文件、`--json`/`--raw` 包裹很大（help 自注 not recommended）

## 补记：112 CLI + 组合技能清单（2026-10-31，用户贴入；已逐条实测核验）

> 以下分类清单为用户 2026-10-31 贴入的转述材料，**每条已用 `ls /opt/hatch/bin` 全量实测核验**，核验结论标在里。

### 转贴原文（分类整理）

**一、AI 生成与媒体**：media-generation、avatar-media-generation、edits、media-library、tts、image-search、genui-display-render、pickup-briefing-animation

**二、办公与效率**：hatch_gws_cli、outlook-mail/outlook-calendar/outlook-contacts、notion-cli、evernote、granola-cli、slack、zoom、todoist、asana、calendly、linear、dropbox、box-cli（原文写 box，实为 box-cli）、readwise-mcp

**三、开发工具**：github、vercel、replit、lovable、figma、canva

**四、社交与通讯**：instagram-cli、threads-cli、facebook-cli、messenger、whatsapp

**五、商业与金融**：stripe、plaid、coinbase、shopify、etsy-cli、printify、gumroad-mcp、quickbooks、meta-ads-cli、klaviyo、ghl

**六、生活服务**：duffel、opentable、ticketmaster、instacart、zocdoc、philips-hue、tessie-api、withings

**七、平台基础设施**：hatch、hatch-vault、hatch-multicall、hatch-execd、hatch-rescue*、browser-broker/browser-service

**八、"55 个组合技能（/opt/hatch/skills/）"**：实测 `/opt/hatch/skills` 有 **150** 项（如 asana/box/duffel/evernote/facebook/coinbase-mcp…），`/opt/hatch/workflow-skills` 56 项，`/opt/muse/skills` 56 项。"55"疑为 56 之误，且指错了目录

### 存疑/无法验证的表述
- "Zero-Exposure Vault"：机器上有 `hatch-vault`（凭据保险库），但该英文名在机器上找不到出处，疑为转述包装，记为存疑
- "150+ 服务""hatch（559MB 主程序）"：未验证，原样转贴
- "配合 C 机的自动化流可以做成矩阵运营"：原文如此，"C 机"指代不明，原样转贴

### bin 全量 112 名单（2026-10-31 实测 `ls /opt/hatch/bin`）
aftership、agoda、asana、authdc、avatar-media-generation、box-cli、browser-broker、browser-service、builtin-artifacts、calendly、canva、device-data、dropbox、duffel、edits、etsy-cli、evernote、facebook-cli、feature-request、figma、flightaware、function-health、genui-display-render、geocode、ghl、github、granola-cli、gumroad-mcp、hatch、hatch-browser-lease-helper、hatch-connector-output、hatch-doctor、hatch-execd、hatch-healthd、hatch-multicall、hatch-rescue、hatch-rescue-systemctl、hatch-rescuectl、hatch-slide-style、hatch-vault、hatch-ws-client、hatch-zeitgeist、hatch_gws_auth、hatch_gws_cli、hatch_igd_cli、hatch_messenger_cli、health-cli、healthex、healthkit-cli、image-search、imap-email、ingress-rev-proxy、instagram-cli、instagram-messages-cli、klaviyo、linear、local-search、lovable、media-generation、media-library、meta-ads-cli、meta-catalog-search、moneyforward-me、muse-mail、native-comms-cli、notion-cli、nutrition-cli、onepassword、opentable、outlook-calendar、outlook-contacts、outlook-mail、peloton、philips-hue、pickup-briefing-animation、places、plaid、printify、privsep-test-fully-isolated、quickbooks、readwise-mcp、remote-storage、replit、runway-mcp、save-to-spotify、share、shop-wallet-cli、shopback-mcp、shopify、shopify-ucp-cli、shopping、slack、spawnd、spotify-api、stripe、stripe-link、subscription-status、tailscale、tessie-api、threads-cli、threads-messages-cli、ticketmaster、todoist、tts、vercel、vidiq-mcp、wearables-display、web-search、withings、zapier、zbar-lib、zoom
