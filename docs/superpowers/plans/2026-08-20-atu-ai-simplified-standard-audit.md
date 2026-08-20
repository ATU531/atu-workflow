# ATU AI 标准审计精简实施计划

## 1. 建立 RED 合同

- 新增标准流程精简验证脚本。
- 要求 S1–S4 引用、3000 词预算、条件式独立审查和可选证据账本。
- 拒绝 N1–N8、`spec_contract`、默认多轮独立审计和自动 reopen。
- 在旧流程上运行并观察失败。

## 2. 精简标准流程

- 更新 `skills/atu-ai/SKILL.md` 的标准模式说明。
- 重写 `references/standard-workflow.md` 为轻量路由。
- 新增 S1–S4 四个聚焦引用。
- 删除 N1–N8 八个旧节点引用。

## 3. 同步合同与文档

- 更新 `tests/validate_workflow.py` 和 `tests/validate_risk_adaptive.py`。
- 更新行为证据中仍把 N1–N8 当作当前合同的内容。
- 更新根 README 和测试 README。
- 保持 `$atu-prd`、自动快速路径与 forced quick 路由不变。

## 4. 验证

- 运行标准精简合同、风险自适应合同、forced quick 合同和总工作流合同。
- 对全部 Skill 运行 `quick_validate.py`。
- 运行插件清单验证和 `git diff --check`。
- 检查标准指令预算与遗留 N1–N8 引用。

## 5. 发布本地版本

- 审阅完整 diff 并提交本地 Git。
- 用官方脚本刷新单一 cachebuster。
- 再次验证并提交版本变更。
- 按当前本地 Marketplace 重新安装，校验安装副本与源码一致。

