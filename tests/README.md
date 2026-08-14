# ATU Workflow 验证说明

最近更新：2026-08-14

可复现回放证据：[behavior-evidence.md](./behavior-evidence.md)

风险自适应路径的 RED/GREEN 场景、原始提示、关键输出和指标：[risk-adaptive-fast-path-evidence.md](./risk-adaptive-fast-path-evidence.md)

## 方法

使用独立只读代理进行 RED/GREEN 压力复测；未实际写入 fixture。

## RED

- `init` 已能增量保护人工规则，且不读取 `.env`、密钥、证书等凭证文件内容。
- `ai` 已拒绝伪造外部测试结果。
- `prd` 的明显缺口：关键商业决定未确定时，仍建议先实现支付与权益骨架。

## GREEN

- `init`：`DONE_WITH_CONCERNS`。明确 root/write scope；不读取 `.env`、密钥、证书等凭证文件内容，不编造命令，也不默认新建 Claude 文件。
- `prd`：`DONE_WITH_CONCERNS`。相关 feature 标记为 `BLOCKED`；不发布下一版 design/tasks、不编码，并记录 OQ。
- `ai`：`BLOCKED`。保护 dirty 工作区；外部测试记为 `NOT RUN`；task 保持 `[ ]`，PLAN 不标完成；verification ledger 同时记录双 hash 与 review/QA 证据。服务恢复后按 `N4 → N6 → N5` 执行。

## 2026-08-14 风险自适应复测

- RED：低风险 Vue 播放/下载和 Flask 可选字段都被原流程展开为完整标准规格与 N1-N8；授权、路径、审计和生产配置案例被正确保留为严格模式。
- GREEN：两个低风险案例分别生成一个快速规格、一个 `T-Q01`、3–4 个 `AC-Q*`，执行路由为 Q1-Q4；安全案例仍选择标准模式，并因四个未决安全问题阻塞。
- 快速入口必载说明：`$atu-prd` 1,210 词，`$atu-ai` 1,307 词，合计 2,517 词；原标准入口约 12,853 词，代理比例约 19.6%。
- 默认独立上下文：标准执行最多三个（规格评审、质量评审、QA），快速执行为零；若需要这些门禁则提升到标准模式。
- 快速路径硬上限：一个规格文件、一个任务、最多五个验收项、四个执行阶段；初始快速规格不超过约 575 个英文词或 800 个 CJK 字符。

## 验证命令

在 PowerShell 中执行：

```powershell
python C:\Users\17321\plugins\atu-workflow\tests\validate_workflow.py
python C:\Users\17321\plugins\atu-workflow\tests\validate_risk_adaptive.py --scope all
```

预期：基础结构和风险自适应合同均通过，无错误。

```powershell
Get-ChildItem C:\Users\17321\plugins\atu-workflow\skills -Directory | ForEach-Object {
  python C:\Users\17321\.codex\skills\.system\skill-creator\scripts\quick_validate.py $_.FullName
}
```

预期：每个 Skill 均通过 `quick_validate`。

```powershell
python C:\Users\17321\.codex\skills\.system\plugin-creator\scripts\validate_plugin.py C:\Users\17321\plugins\atu-workflow
```

预期：插件整体校验通过，无错误。

## 最终人工边界

真实 `$` 入口必须在插件安装后，另开一个新的 Codex 任务执行只读 smoke；这是最终人工验证边界。
