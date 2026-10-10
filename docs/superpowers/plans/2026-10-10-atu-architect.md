# ATU Architect Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 支持主动架构设计及 PRD 中按影响自动前置，并将批准约束传递到实施。

**Architecture:** 一个架构入口及两份按需参考，衔接现有 PRD 与 S1–S3，不建立另一套任务或审计状态机。沿用源码 main 与现有独立安装方式。

**Tech Stack:** Markdown Skills、现有 Python 标准库校验、Codex 行为回放、Git。

## Global Constraints

- 用户已批准设计并明确要求直接 main 实施。
- 先单独提交已有精简改动；不删除环境，不修改无关配置。
- 关键架构决定需用户确认；普通小功能不增加架构阶段；显式 atu-quick 不受新分流影响。
- Git 提交自然语言使用中文；完成后推送至用户指定 ATU531/atu-workflow，禁止强推。
- 架构文档为技术约束补充，不替代 PRD、功能三份权威文档或 UI 设计确认。

### Task 1: 完整架构入口及工作流衔接

**Files:**
- Create: `skills/atu-architect/SKILL.md`, `skills/atu-architect/references/architecture-contract.md`, `skills/atu-architect/references/design-guide.md`
- Modify: `skills/atu-prd/SKILL.md`, `skills/atu-prd/references/standard-workflow.md`, `skills/atu-prd/references/spec-contract.md`, `skills/atu-prd/references/quick-spec-contract.md`
- Modify: `skills/atu-ai/references/S1-boundary.md`, `skills/atu-ai/references/S2-implement.md`, `skills/atu-ai/references/S3-verify.md`, `skills/atu-ai/references/quick-execution.md`
- Modify: `.codex-plugin/plugin.json`, `README.md`, `tests/validate_reference_packaging.py`, `tests/validate_workflow.py`, `tests/test_reference_packaging.py`
- Create: `tests/architect-evidence.md`

**Interfaces:**
- Consumes: 原始 PRD、现有代码/约束、明确用户确认。
- Produces: 文档路径 + 批准版本 + 适用决定/小节 + 确认依据；PRD 显式引用，AI 检查适用性。

- [x] 保存原有变更为独立提交 `44a9436`；运行现有校验。
- [x] RED：独立代理读取旧 PRD 处理新建多租户设备系统。结果只能进入来源/开放问题处理，缺少架构设计与确认产物路径；不把已有安全阻塞误报为失败。
- [x] 补充打包反例并观察新增 architect 调用不被旧入口集合接受。

```python
def test_architect_can_be_consumed_by_prd(self):
    self.write("skills/atu-architect/SKILL.md", "# Architecture\n")
    self.write("skills/atu-prd/SKILL.md", "Use $atu-architect; [architecture](../atu-architect/SKILL.md).\n")
    self.assertEqual(validate_bundle(self.root), [])
```

- [x] GREEN：实现设计文档中的触发、架构产物、确认、版本保留、来源隔离和执行衔接；更新打包入口及引用图检查。
- [x] 运行 `python -B -m unittest discover -s tests -p 'test_*.py'` 与 README 四项现有合同校验、引用校验、Skill 元数据校验。
- [x] 独立前向回放新系统入口及已有系统复用/小改动场景；记录真实输出与限制，不提供预期答案给执行代理。
- [x] 一次聚焦最终审查路由、批准状态、跨文件冲突与轻量边界；只修复证据支持的问题。
- [x] 比较本地安装副本，备份并同步受影响 Skill，逐文件哈希验证。

交付动作：更新已执行证据与计划后提交 `feat: 增加架构设计入口并衔接规格开发`；检查远程历史和待推送内容，普通推送 main，并核对远程提交。提交和推送状态以实际 Git 历史及远程引用为准，不在提交前预记成功。

## 验证边界

本地标准 Python 和应用内置 Python 缺 PyYAML；额外 Skill 校验须复用现成依赖或隔离补装。旧 README 的 plugin-creator 脚本不存在，使用仓库现有清单/引用校验，不声称执行该脚本。新会话 `$` 自动发现需用户新开会话验证。
