# Portable AI Memory

一个用 Markdown 保存、由用户自己掌握的个人 AI 上下文系统。

它的目标不是保存全部聊天记录，也不是“复制人格”，而是把长期有效的身份背景、价值观、思考方式、兴趣、职业信息和少量代表性讨论提炼成可携带文件。更换 AI、Agent 或账号后，新 AI 可以通过这些文件更快理解用户，减少反复自我介绍。

## 设计理念

- **用户拥有**：记忆保存为普通 Markdown，不绑定某个模型、账号或平台。
- **提炼优先**：保存长期有效的信息，而不是囤积聊天流水。
- **渐进读取**：先读目录和核心画像，只有相关问题才读取深层主题。
- **区分确定性**：把事实、偏好、AI 推测、矛盾信息和开放问题分开处理。
- **最小必要记忆**：不保存密码、Token、Cookie、证件号码或不必要的敏感信息。
- **可追溯纠错**：用精简修改记录说明 AI 改了什么、依据是什么。
- **控制膨胀**：代表性主题最多 6 个，详细修改记录最多 12 次。
- **能力可迁移**：高频 Skill 及其公开安装来源也是个人资产，通过真实使用证据和定期淘汰控制清单质量。

## 记忆结构

```text
personal-ai-memory/
├── README.md
├── memory-index.md
├── identity.md
├── values-and-worldview.md
├── thinking-and-collaboration.md
├── career-and-projects.md
├── interests-and-life.md
├── tools-and-skills.md       # 高频或高重建成本 Skill
├── open-questions.md
├── archive/               # 最多 6 个代表性主题摘要
└── history/
    └── change-log.md      # 最多 12 次详细修改记录
```

核心档案回答“我是谁、我重视什么、怎样与我协作”；`archive/` 保存少数无法压缩成一句偏好的深层思想脉络；`change-log.md` 只用于追溯实际修改，不是聊天历史。

`tools-and-skills.md` 回答“我已经积累了哪些值得跨环境恢复的能力”。它只记录实际复用过或重建成本很高的 Skill，以及经过确认的公开来源、安装方式和非敏感依赖，不保存账号凭证或所有已安装软件。

## 什么是代表性主题

一个讨论只有在会明显影响未来 AI 对用户价值判断、重要选择或长期问题的理解时，才值得进入 `archive/`。它还应至少满足一项：

- 保留无法压缩成核心档案一条信息的推理过程；
- 记录观点的重要变化或内在张力；
- 解释某项长期偏好为什么重要。

仅仅有趣、详细、情绪强烈或表达精彩，不构成长期保存的理由。达到 6 个主题后，必须合并已有主题或经用户确认后替换，不能创建第 7 个。

## 安装

将仓库下载或克隆到 Codex 的 Skills 目录：

```bash
git clone https://github.com/YOUR-USER/portable-ai-memory.git ~/.codex/skills/portable-ai-memory
```

重新打开 Codex 后，可以这样调用：

```text
Use $portable-ai-memory to initialize my portable AI memory library.
```

也可以直接运行初始化脚本：

```bash
python3 scripts/init_memory.py --destination /absolute/path/to/personal-ai-memory
```

Skill 文件和私人记忆库必须放在不同目录。分享仓库时，只分享 Skill，不要提交生成后的私人记忆库。

初始化和验证完成后，Skill 会询问是否创建“每周自动维护”。只有用户明确同意，才会继续询问星期和本地时间，并创建 Codex Automation。建议默认值是每周日 20:00，但用户可以自行选择。

需要区分：**Skill 负责规定如何维护，Automation 负责按时启动。**只下载或安装 Skill，不会自动产生后台定时任务。创建后应确认任务状态为 `ACTIVE`，并核对项目、记忆库路径和运行时间。

## 常见用法

- 初始化一套新的个人 AI 记忆库；
- 从旧的个人说明、笔记或对话摘要迁移信息；
- 切换 AI 后恢复基本背景和协作偏好；
- 定期提炼真正发生变化的长期信息；
- 检查代表性主题数量和明显的密钥泄露风险。

检查记忆库结构：

```bash
python3 scripts/check_memory.py /absolute/path/to/personal-ai-memory
```

## 自动更新的边界

定时运行的 AI 只能使用当前任务实际可见、或用户明确提供的信息。它不能天然读取其他账号和平台的全部聊天，也不应该维护近期对话仓库。没有长期有效的新信息时，不修改核心档案，也不写入空的更新记录。

因此，这套系统恢复的是**个人背景与协作连续性**，不是意识、人格或关系的完整复制。

不同 AI 产品未必提供 Codex Automation。遇到不支持定时任务的环境时，Skill 应输出同一份每周维护提示词，由用户在该产品的计划任务、系统定时器或其他自动化工具中配置，而不能假装已经创建成功。

## 隐私提醒

不要在记忆库中保存：

- 密码、Token、Cookie、私钥或恢复码；
- 证件号码和精确金融账户信息；
- 不必要的第三方隐私；
- AI 根据一次对话做出的诊断或人格定型。

新的用户陈述始终优先于旧记忆。

## License

MIT
