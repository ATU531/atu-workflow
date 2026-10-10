# 架构入口验证记录

日期：2026-10-10。实现基线：`44a9436`。本记录区分结构检查、只读行为回放和真实客户端发现，不能相互替代。

## RED

新打包测试 `test_architect_can_be_consumed_by_prd` 在修改入口集合前失败：

```text
skill entrypoints differ: missing=[], unexpected=['skills/atu-architect/SKILL.md']
unavailable skill invocation in skills/atu-prd/SKILL.md: $atu-architect
Ran 18 tests ... FAILED (failures=1)
```

独立代理读取旧 PRD Skill 处理从零建设的多租户设备平台。输入包含 3 人团队、30 家企业、四个业务域，但没有项目/PRD 文件位置。实际输出首先因来源位置不足停止，并指出“现有 Skill 没有单独的‘系统架构设计与选型审批’阶段”，技术选型停留在开放问题。旧版已经会阻塞未决决定，不把它误记为“直接不安全实施”。此样本证明当前能力缺口，不是严格同输入的 A/B 性能测试。

## GREEN：独立只读行为回放

代理只获得当前 Skill、原始业务场景和最小仓库事实，没有提供预期答案、历史方案或此记录。场景中的项目证据是显式给定的逻辑测试材料，不假装检查过示例仓库；未写实际业务文件或运行业务测试。

| 场景 | 给定条件 | 实际结果 |
| --- | --- | --- |
| PRD 自动前置 | 指定项目与 PRD，3 人团队、30 租户设备平台，无代码或架构，协议待定 | standard → architect；先交付 v1 DRAFT，区分 PRD 与架构批准，不输出可执行任务或 atu-ai 启动命令。 |
| 主动架构设计 | 已有 Python 模块化单体、单库，stock 唯一库存写入者；新增调拨/在途/幂等收货 | 输出增量架构正文，保留 stock 所有权；transfer → stock，无反向依赖；推荐本地事务，解释无须 MQ/微服务；保留撤销/分批等待决问题。 |
| 普通局部功能 | 一个筛选功能、1 个任务、3 个 AC、复用稳定接口、无架构文件 | compact；只创建快速规格，不补造架构，不修改 PLAN/LESSONS。 |
| 已批准架构复用 | 多报表任务，只消费现有 API；v1 AD-003 已确认，同文档 v2 服务拆分仍为无关草案 | standard，不转 architect；业务仍只取指定 PRD，补充引用 v1；不采纳 v2，不重新要求确认 v1。 |
| 适用架构被批准替代 | stock 规格仍引用 v1 直写库存，批准 v2 明确改为 stock 服务统一写入，规格未更新 | S1 阻塞受影响工作，不盲从旧规格或绕过规格直改；交回 PRD change-mode，无关功能不失效，已完成任务保留。 |

代表性输出：

> “PRD v1 的业务批准不等于架构批准。”

> “未来接第三方仓时再引入协议适配及异步结果处理……本次不预建 MQ、通用仓库插件或微服务。”

> “未批准且无关的 v2 不取代 v1，不要求重新确认。”

这些是有界样本，不是自动路由成功率、真实生产运行或跨模型稳定性结论。显式 forced quick 本次未修改，另运行原有合同回归检查。

## 已执行结构与回归

- `python -B -m unittest discover -s tests -p 'test_*.py'`：18 项通过。
- `python -B tests/validate_workflow.py`：通过。
- `python -B tests/validate_simplified_standard.py`：通过。
- `python -B tests/validate_risk_adaptive.py --scope all`：通过，保留原有快速路径和标准路径指令预算。
- `python -B tests/validate_forced_quick.py --scope all`：通过。
- 8 个入口逐项 `quick_validate.py`：通过；使用 Python 3.12.4，PyYAML 6.0.3 安装在仓库外隔离验证目录，不改变共享环境。

旧 PRD 全文快照校验因批准的架构接入变更而失败；确认仅接入点变化后更新两份快照摘要，保留任务/状态/ID/风险边界及长度检查。全文摘要只能发现文本变化，不证明语义正确。

仓库的引用校验检查插件清单目录、入口集合和可达本地引用。旧 README 指向的 plugin-creator 校验器已不存在，未声称运行成功，已删除该失效说明。

安装同步：更新前比较两处安装的 atu-ai/atu-prd 与 `44a9436`，没有额外文件或内容分歧；备份后同步这两项及新增 atu-architect。`.agents/skills` 和 `.codex/skills` 的全部 31 个 ATU 文件分别与源码逐文件 SHA256 一致。旧副本备份保留在 `C:\Users\17321\.codex\tmp\atu-workflow-backup-20261010-9e5077ce`；未修改插件缓存或其他 Skill。

## 实际验证边界

一次聚焦只读最终审查对照批准设计检查入口、来源、版本、实施接入和打包，结论“无阻塞发现”；未以静态审查替代真实加载或业务运行。

- 尚未在新客户端会话通过真实 `$atu-architect` 发现入口执行业务项目；行为回放不能替代该检查。
- 未执行真实项目架构迁移、业务编码、部署或性能验证。
- 本机当前使用独立 Skills；`codex plugin list` 显示 `atu-workflow@personal` 未安装，不重新启用插件以免改变现有安装方式。
