# ATU Workflow

ATU Workflow 是个人 Codex 插件，用于把项目初始化、PRD 拆解和规格驱动开发串成可审计的工作流。插件移植自 `C:\Users\17321\.claude` 中的既有工作方式；该 Claude 源目录始终只读，不从中复制凭证，也不修改其内容。

## 入口

Codex 通过 Skill 名称调用插件能力，四个主入口是：

- `$atu-init`：从仓库证据识别项目根与获准写入范围，增量创建或更新 `AGENTS.md` 等开发约定。只检查凭证文件是否存在，不读取 `.env`、密钥或证书内容；不凭空编造命令；默认不新建 Claude 兼容文件。
- `$atu-prd`：先按仓库证据自动选择快速或严格模式，不修改业务代码。边界清晰、复用稳定契约的小改动生成一个 `specs/quick/*.md`；高风险、含未决问题、多任务或范围不确定的需求仍生成 `PLAN.md`、`LESSONS.md` 和编号功能规格。
- `$atu-ai`：识别规格类型后只加载对应执行流程。快速规格按 Q1 至 Q4 执行；标准规格按 S1 至 S4 完成边界确认、逐任务测试驱动实现、一次功能级合并验证和收尾恢复。独立审查与 QA 只在关键风险或真实验收边界需要时启用。
- `$atu-quick`：仅在显式调用时启用，在同一次调用中生成或恢复一个 forced quick 规格并直接执行 Q1 至 Q4。权限、支付、迁移、公共 API 等类别不会自动升级，但缺少真实决定、必需证据或外部操作授权时仍会如实阻塞。

调用示例：

```text
$atu-init D:\Workspace\psy_mini_program
$atu-prd D:\Workspace\psy_mini_program\docs\C端心理测评小程序PRD.md
$atu-ai D:\Workspace\psy_mini_program
$atu-quick D:\Workspace\example "修改支付回调并补齐迁移"
```

## 风险自适应快速路径

快速模式适合一个仓库内的一项局部行为或有界垂直切片：产品和技术决策已闭合，只需一个实现与验证任务，最多五个可观察验收结果，复用现有架构/接口，并能通过聚焦测试和有限回归验证。使用现有已认证 API 不会自动升级为严格模式，前提是认证、权限、所有权、协议、数据生命周期和错误契约都不改变。

以下情况始终使用严格模式：新增或修改认证、授权、隐私、支付、审计策略、数据库结构/迁移/回填、保留期或数据生命周期、破坏性数据操作、公共 API 或兼容性契约、外部服务/回调/队列、生产配置、部署拓扑、跨仓库或广泛共享状态；存在实质未决问题、多项独立任务或分类不确定时也一样。用户可以要求严格模式，但不能用“这是小功能”绕过这些边界。

典型快速流程：

```text
$atu-prd D:\Workspace\example\docs\small-change.md
# 自动生成：specs/quick/20260814-small-change.md

$atu-ai D:\Workspace\example\specs\quick\20260814-small-change.md
# 执行：Q1 → Q2 → Q3 → Q4
```

快速规格只有一个文件、一个 `T-Q01` 和至多 `AC-Q05`，状态为 `READY / IN_PROGRESS / DONE / BLOCKED / ESCALATED`。它同时保存实现后的命令结果和验收矩阵，不额外创建 `verification.md`。若规划或实现时发现严格触发条件，保留现有文件和用户改动，标记 `ESCALATED`，再由 `$atu-prd` 按标准流程提升；不会重置或静默吸收未验证工作。

标准执行流程为 `S1 边界确认 → S2 测试驱动实现 → S3 功能级合并验证 → S4 收尾与恢复`。普通标准任务不再默认进行每任务独立规格审查、独立质量审查和独立 QA；认证/授权、支付资金、破坏性迁移、公共兼容契约或生产变更才在功能级增加一次独立代码审查，真实浏览器、设备或外部服务验收按需要增加一次独立 QA。`verification.md` 仅用于跨会话、多任务交接或项目明确要求的持久证据。

## 强制快速入口

自动快速路径仍由 `$atu-prd/$atu-ai` 按风险证据分类；显式 `$atu-quick` 则代表用户主动选择 forced quick，不会因认证/授权、支付、迁移/回填、公共 API/兼容性、外部服务、生产配置、跨模块或跨仓库等类别自动进入标准流程。

`$atu-quick` 使用一个 `specs/quick/*.md`、一个 `T-Q01`、至多五个 `AC-Q*` 和 `READY / IN_PROGRESS / DONE / BLOCKED` 四种状态，不自动产生 `ESCALATED`。自然语言需求会先写入简短规格并在同一调用继续 Q1-Q4；已有 forced 文件可用 `$atu-quick <路径>` 恢复。真正缺少决定、必需环境/证据或操作授权时保持 `BLOCKED`，不会编造结论，也不会自行转成标准模式。

入口选择本身只授权工作流，不等于授权提交、推送、发布、部署、真实支付、生产迁移、删除数据或外部写入；这些动作必须在请求或项目规则中明确写出动作和目标。

无论哪种模式，测试、安全边界、真实浏览器/设备或外部环境证据都不能省略；不可用的必要证据必须记录为 `NOT RUN` 或 `MANUAL REQUIRED`。完成工作也不会自动授权提交、推送、部署或生产变更。

Claude 原斜杠入口无法原样注册为 Codex 入口：Codex 插件发现的是 `SKILL.md` 中以连字符命名的 Skill，并使用 `$atu-init` 这类名称调用；两者属于不同的命令注册模型。

## 专项 Skill 与按需参考

插件保留四个主入口和三个专项 Skill，共七个独立入口：

- `atu-android-engineer`：Android、WebView 与 kiosk 实现和验证。
- `atu-code-reviewer`：只读代码评审、缺陷与安全风险报告。
- `atu-miniprogram-engineer`：原生微信小程序页面、接口与隐私边界。

其余工程指导由执行流程按实际任务读取，不再注册独立角色入口：

| 任务边界 | 参考 |
| --- | --- |
| Web 页面、交互与浏览器验收 | [前端](skills/atu-ai/references/domains/frontend.md) |
| API、服务集成、队列 | [后端](skills/atu-ai/references/domains/backend.md) |
| 数据结构、迁移、事务、Redis | [数据库](skills/atu-ai/references/domains/database.md) |
| 测试任务、运行验收、独立 QA 交接 | [验证](skills/atu-ai/references/verification.md) |
| 已验证行为对应的文档同步 | [文档](skills/atu-ai/references/documentation.md) |

普通编辑无需额外角色上下文；跨边界任务可读多份相关参考，不强制“恰好一个领域技能”。独立 QA 仍由所选工作流和用户要求决定；读取验证参考不增加默认验收轮次。四个主入口、规格格式、状态与授权合同保持不变；原角色调用可改为相应主入口加具体任务说明。

## 安装与加载

- 插件源：`C:\Users\17321\plugins\atu-workflow`
- 个人 Marketplace：`C:\Users\17321\.agents\plugins\marketplace.json`
- Marketplace 名称：`personal`
- Marketplace 本地源：`./plugins/atu-workflow`

安装命令：

```powershell
codex plugin add atu-workflow@personal
codex plugin list
```

安装或重新安装后，必须新建一个 Codex 任务再调用入口；当前任务不会动态加载刚安装或刚更新的插件。

## 结构

```text
atu-workflow/
├─ .codex-plugin/plugin.json
├─ skills/
│  ├─ atu-init/
│  ├─ atu-prd/
│  ├─ atu-ai/
│  ├─ atu-quick/
│  ├─ atu-android-engineer/
│  ├─ atu-code-reviewer/
│  └─ atu-miniprogram-engineer/
│     # 共享工程参考位于 atu-ai/references/domains/、verification.md 和 documentation.md
└─ tests/
   ├─ validate_workflow.py
   └─ validate_forced_quick.py
```

## 验证

在 PowerShell 中运行：

```powershell
python C:\Users\17321\plugins\atu-workflow\tests\validate_workflow.py
python C:\Users\17321\plugins\atu-workflow\tests\validate_simplified_standard.py
python C:\Users\17321\plugins\atu-workflow\tests\validate_risk_adaptive.py --scope all
python C:\Users\17321\plugins\atu-workflow\tests\validate_forced_quick.py --scope all
python C:\Users\17321\plugins\atu-workflow\tests\validate_reference_packaging.py
python C:\Users\17321\plugins\atu-workflow\tests\test_reference_packaging.py

Get-ChildItem C:\Users\17321\plugins\atu-workflow\skills -Directory |
  ForEach-Object {
    python C:\Users\17321\.codex\skills\.system\skill-creator\scripts\quick_validate.py $_.FullName
  }

python C:\Users\17321\.codex\skills\.system\plugin-creator\scripts\validate_plugin.py C:\Users\17321\plugins\atu-workflow
```

前四条分别检查基础结构、精简标准执行、自动快速/严格路由和显式 forced quick 合同；引用校验检查七个入口、按需参考及其链接完整性，并用缺失文件/旧调用等反例验证检查器；随后逐一校验 Skill 元数据与结构，最后校验插件清单及整体目录。
