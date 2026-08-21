# AI 秽土转生 / Edo Tensei AI

> **平台可以换，模型可以换，账号可以换。AI 对你的理解，跟你走。**
>
> **Switch platforms, models, or accounts. Let the next AI inherit the understanding the last one built.**

## 中文

### 这是什么

你用了一个 AI 很久，它终于认识你。

然后账号被封、价格上涨、产品变差，或者另一家 AI 更好用。

但你不敢换，因为换一个 AI，就要重新花很久让它认识你。

**AI 秽土转生**把旧 AI 对你的理解保存下来，让新的 AI 继承。

不用重新从陌生人开始。

**平台拥有模型。你拥有 AI 对你的理解。**

GPT、Claude、Gemini，谁好用就用谁。

**万花丛中过，片叶不沾身。**

---

### 它怎么做

它不会备份全部聊天记录，而是把长期有效的信息提炼成普通 Markdown：

```text
personal-ai-memory/
├── memory-index.md
├── identity.md
├── values-and-worldview.md
├── thinking-and-collaboration.md
├── career-and-projects.md
├── interests-and-life.md
├── tools-and-skills.md
├── open-questions.md
├── archive/
└── history/
    └── change-log.md
```

主要保存：

- 你是谁
- 你在意什么
- 你怎么思考
- AI 应该怎么和你协作
- 长期项目和兴趣
- 少量重要历史讨论
- 值得迁移的 Skills 和工作流

**只保存值得被下一个 AI 继承的东西。**

---

### 设计原则

- **用户拥有**：普通 Markdown，不绑定任何平台。
- **提炼优先**：记长期有效的信息，不囤聊天流水。
- **按需读取**：先读核心画像，相关时再读深层内容。
- **事实与推测分开**：用户明确说过的，和 AI 推断的，不是一回事。
- **允许变化**：新的用户陈述优先于旧记忆。
- **控制膨胀**：只保留少量真正重要的长期主题。
- **可追溯**：重要修改进入 `change-log.md`。
- **Skills 也是资产**：高频或高重建成本的 Skill 和工作流一起迁移。

---

### 安装

```bash
git clone https://github.com/yangguoguo/edo-tensei-ai.git ~/.codex/skills/edo-tensei-ai
```

然后：

```text
Use $edo-tensei-ai to initialize my personal AI memory.
```

也可以直接：

```bash
python3 scripts/init_memory.py --destination /absolute/path/to/personal-ai-memory
```

检查记忆库：

```bash
python3 scripts/check_memory.py /absolute/path/to/personal-ai-memory
```

---

### 自动维护

初始化后，可以选择定期让 AI 检查最近的信息，只把真正发生变化的长期内容写入记忆。

**没有值得长期保存的新信息，就什么都不写。**

Skill 负责定义怎么维护；Automation 只负责按时启动。

AI 只能整理当前实际可见的信息，不能凭空读取其他平台或账号的历史记录。

---

### 一条重要规则

**公开 Skill 和私人 Memory 分开。**

这个仓库保存“怎么做秽土转生”。

你的私人记忆，自己保管。

不要保存密码、Token、Cookie、私钥、证件号码、精确金融账户信息，以及不必要的第三方隐私。

---

### 为什么叫“秽土转生”

原来的 AI 不会真的回来。

但它对你的理解，可以被新的 AI 继承。

**AI 可以换，理解不用重建。**

---

## English

### What is this?

You use an AI for months. It finally gets you.

Then your account gets banned, the price goes up, the product gets worse, or another model simply becomes better.

But switching means teaching a new AI who you are all over again.

**Edo Tensei AI** preserves what the old AI learned about you, so the next AI can inherit it.

No need to start from strangers again.

**Platforms own the models. You own the understanding built about you.**

Use GPT, Claude, Gemini, or whatever works best.

**Use any model. Belong to none.**

---

### How it works

It does not back up every conversation. It distills durable personal context into plain Markdown:

```text
personal-ai-memory/
├── memory-index.md
├── identity.md
├── values-and-worldview.md
├── thinking-and-collaboration.md
├── career-and-projects.md
├── interests-and-life.md
├── tools-and-skills.md
├── open-questions.md
├── archive/
└── history/
    └── change-log.md
```

It keeps things like:

- who you are
- what matters to you
- how you think
- how an AI should work with you
- long-term projects and interests
- a small number of important past discussions
- Skills and workflows worth carrying forward

**Keep only what the next AI should inherit.**

---

### Design principles

- **User-owned**: plain Markdown, not tied to one platform.
- **Distill, don't hoard**: preserve durable understanding, not chat logs.
- **Read progressively**: load core context first, deeper material only when relevant.
- **Separate facts from inference**: what the user said and what the AI inferred are not the same.
- **Let people change**: newer user statements override old memory.
- **Control growth**: keep only a small number of high-value long-term themes.
- **Keep changes traceable**: meaningful edits go into `change-log.md`.
- **Skills are assets too**: portable capabilities and costly-to-rebuild workflows should travel with you.

---

### Install

```bash
git clone https://github.com/yangguoguo/edo-tensei-ai.git ~/.codex/skills/edo-tensei-ai
```

Then:

```text
Use $edo-tensei-ai to initialize my personal AI memory.
```

Or:

```bash
python3 scripts/init_memory.py --destination /absolute/path/to/personal-ai-memory
```

Validate the memory library:

```bash
python3 scripts/check_memory.py /absolute/path/to/personal-ai-memory
```

---

### Automatic maintenance

You can optionally run periodic reviews that write only durable changes into memory.

**If nothing important changed, write nothing.**

The Skill defines how maintenance works. Automation only decides when it runs.

A scheduled AI can only use information actually visible to that task. It cannot silently read every conversation across other accounts or platforms.

---

### One important rule

**Keep the public Skill and private Memory separate.**

This repository stores the technique.

Your personal memory stays with you.

Do not store passwords, tokens, cookies, private keys, identity-document numbers, precise financial account information, or unnecessary third-party private data.

---

### Why “Edo Tensei”?

The old AI does not literally come back.

But its understanding of you can be inherited by the next one.

**Change the AI. Keep the understanding.**

---

## License

MIT
