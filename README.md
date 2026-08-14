# ATU Workflow

ATU Workflow 是个人 Codex 插件，用于把项目初始化、PRD 拆解和规格驱动开发串成可审计的工作流。插件移植自 `C:\Users\17321\.claude` 中的既有工作方式；该 Claude 源目录始终只读，不从中复制凭证，也不修改其内容。

## 入口

Codex 通过 Skill 名称调用插件能力，三个主入口是：

- `$atu-init`：从仓库证据识别项目根与获准写入范围，增量创建或更新 `AGENTS.md` 等开发约定。只检查凭证文件是否存在，不读取 `.env`、密钥或证书内容；不凭空编造命令；默认不新建 Claude 兼容文件。
- `$atu-prd`：把权威需求整理为 `specs/` 下的 `PLAN.md`、`LESSONS.md` 和按功能拆分的需求、设计、任务文档，不修改业务代码。关键商业、安全、权限、数据或外部契约决定未确认时，阻塞受影响功能并保留开放问题，不把建议写成既定决定。
- `$atu-ai`：按 N1 至 N8 状态机一次推进一个规格任务，依次执行实现、评审、QA、完成标记和文档同步。保护已有 dirty 改动；未实际运行的检查不得声称通过；用应用快照与规格契约双重哈希绑定证据；默认不推送、发布、部署或执行生产迁移。

调用示例：

```text
$atu-init D:\Workspace\psy_mini_program
$atu-prd D:\Workspace\psy_mini_program\docs\C端心理测评小程序PRD.md
$atu-ai D:\Workspace\psy_mini_program
```

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

Get-ChildItem C:\Users\17321\plugins\atu-workflow\skills -Directory |
  ForEach-Object {
    python C:\Users\17321\.codex\skills\.system\skill-creator\scripts\quick_validate.py $_.FullName
  }

python C:\Users\17321\.codex\skills\.system\plugin-creator\scripts\validate_plugin.py C:\Users\17321\plugins\atu-workflow
```

第一条检查插件所需 Skill、节点、评审清单和 Codex 调用约定；第二组逐一校验 Skill 元数据与结构；第三条校验插件清单及整体目录。
