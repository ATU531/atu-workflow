# ATU Workflow

ATU Workflow 是个人 Codex 插件，用于把项目初始化、PRD 拆解和规格驱动开发串成可审计的工作流。插件移植自 `C:\Users\17321\.claude` 中的既有工作方式；该 Claude 源目录始终只读，不从中复制凭证，也不修改其内容。

## 入口

Codex 通过 Skill 名称调用插件能力，三个主入口是：

- `$atu-init`：从仓库证据识别项目根与获准写入范围，增量创建或更新 `AGENTS.md` 等开发约定。只检查凭证文件是否存在，不读取 `.env`、密钥或证书内容；不凭空编造命令；默认不新建 Claude 兼容文件。
- `$atu-prd`：先按仓库证据自动选择快速或严格模式，不修改业务代码。边界清晰、复用稳定契约的小改动生成一个 `specs/quick/*.md`；高风险、含未决问题、多任务或范围不确定的需求仍生成 `PLAN.md`、`LESSONS.md` 和编号功能规格。
- `$atu-ai`：识别规格类型后只加载对应执行流程。快速规格按 Q1 至 Q4 完成边界确认、测试驱动实现、一次合并验证和收尾；标准规格继续使用原 N1 至 N8、双重哈希、独立评审、QA 和恢复机制。

调用示例：

```text
$atu-init D:\Workspace\psy_mini_program
$atu-prd D:\Workspace\psy_mini_program\docs\C端心理测评小程序PRD.md
$atu-ai D:\Workspace\psy_mini_program
```

## 风险自适应快速路径

快速模式适合一个仓库内的一项局部行为或有界垂直切片：产品和技术决策已闭合，只需一个实现与验证任务，最多五个可观察验收结果，复用现有架构/接口，并能通过聚焦测试和有限回归验证。使用现有已认证 API 不会自动升级为严格模式，前提是认证、权限、所有权、协议、数据生命周期和错误契约都不改变。

以下情况始终使用严格模式：新增或修改认证、授权、隐私、支付、审计策略、数据库结构/迁移/回填、破坏性数据操作、公共 API 或兼容性契约、外部服务/回调/队列、生产配置、部署拓扑、跨仓库或广泛共享状态；存在实质未决问题、多项独立任务或分类不确定时也一样。用户可以要求严格模式，但不能用“这是小功能”绕过这些边界。

典型快速流程：

```text
$atu-prd D:\Workspace\example\docs\small-change.md
# 自动生成：specs/quick/20260814-small-change.md

$atu-ai D:\Workspace\example\specs\quick\20260814-small-change.md
# 执行：Q1 → Q2 → Q3 → Q4
```

快速规格只有一个文件、一个 `T-Q01` 和至多 `AC-Q05`，状态为 `READY / IN_PROGRESS / DONE / BLOCKED / ESCALATED`。它同时保存实现后的命令结果和验收矩阵，不额外创建 `verification.md`。若规划或实现时发现严格触发条件，保留现有文件和用户改动，标记 `ESCALATED`，再由 `$atu-prd` 按标准流程提升；不会重置或静默吸收未验证工作。

无论哪种模式，测试、安全边界、真实浏览器/设备或外部环境证据都不能省略；不可用的必要证据必须记录为 `NOT RUN` 或 `MANUAL REQUIRED`。完成工作也不会自动授权提交、推送、部署或生产变更。

Claude 原斜杠入口无法原样注册为 Codex 入口：Codex 插件发现的是 `SKILL.md` 中以连字符命名的 Skill，并使用 `$atu-init` 这类名称调用；两者属于不同的命令注册模型。

## 支持 Skill

三个主入口可按任务需要使用八个专业支持 Skill：

- `atu-android-engineer`：Android、WebView 与 kiosk 实现和验证。
- `atu-backend-engineer`：后端 API、鉴权、业务逻辑、队列与集成。
- `atu-code-reviewer`：只读代码评审、缺陷与安全风险报告。
- `atu-database-engineer`：模型、迁移、查询、事务与 Redis。
- `atu-doc-syncer`：按已验证实现同步项目文档。
- `atu-frontend-engineer`：Web 前端页面、状态、样式与可访问性。
- `atu-miniprogram-engineer`：原生微信小程序页面、接口与隐私边界。
- `atu-qa-engineer`：独立测试、验收证据与残余风险报告。

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
│  └─ 八个专业支持 Skill
└─ tests/validate_workflow.py
```

## 验证

在 PowerShell 中运行：

```powershell
python C:\Users\17321\plugins\atu-workflow\tests\validate_workflow.py
python C:\Users\17321\plugins\atu-workflow\tests\validate_risk_adaptive.py --scope all

Get-ChildItem C:\Users\17321\plugins\atu-workflow\skills -Directory |
  ForEach-Object {
    python C:\Users\17321\.codex\skills\.system\skill-creator\scripts\quick_validate.py $_.FullName
  }

python C:\Users\17321\.codex\skills\.system\plugin-creator\scripts\validate_plugin.py C:\Users\17321\plugins\atu-workflow
```

前两条分别检查基础结构约定与快速/严格路由、资源链接、安全不变量和词数预算；随后逐一校验 Skill 元数据与结构，最后校验插件清单及整体目录。
