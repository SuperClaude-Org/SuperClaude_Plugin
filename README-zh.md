<div align="center">

# 🚀 SuperClaude 框架

### **将 Claude Code 转变为结构化开发平台**

<p align="center">
  <a href="https://github.com/hesreallyhim/awesome-claude-code/">
  <img src="https://awesome.re/mentioned-badge-flat.svg" alt="Mentioned in Awesome Claude Code">
  </a>
<a href="https://github.com/SuperClaude-Org/SuperGemini_Framework" target="_blank">
  <img src="https://img.shields.io/badge/Try-SuperGemini_Framework-blue" alt="Try SuperGemini Framework"/>
</a>
<a href="https://github.com/SuperClaude-Org/SuperQwen_Framework" target="_blank">
  <img src="https://img.shields.io/badge/Try-SuperQwen_Framework-orange" alt="Try SuperQwen Framework"/>
</a>
  <img src="https://img.shields.io/badge/version-4.3.2-blue" alt="Version">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License">
  <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg" alt="PRs Welcome">
</p>

<p align="center">
  <a href="https://superclaude.netlify.app/">
    <img src="https://img.shields.io/badge/🌐_访问网站-blue" alt="Website">
  </a>
  <a href="https://github.com/SuperClaude-Org/SuperClaude_Plugin">
    <img src="https://img.shields.io/badge/🔌_插件分发-green" alt="Plugin Distribution">
  </a>
</p>

<p align="center">
  <a href="README.md">
    <img src="https://img.shields.io/badge/🇺🇸_English-blue" alt="English">
  </a>
  <a href="README-zh.md">
    <img src="https://img.shields.io/badge/🇨🇳_中文-red" alt="中文">
  </a>
  <a href="README-ja.md">
    <img src="https://img.shields.io/badge/🇯🇵_日本語-green" alt="日本語">
  </a>
</p>

<p align="center">
  <a href="#-快速安装">快速开始</a> •
  <a href="#-支持项目">支持</a> •
  <a href="#-v4-新特性">特性</a> •
  <a href="#-文档">文档</a> •
  <a href="#-贡献">贡献</a>
</p>

</div>

---

<div align="center">

## 📊 **框架统计**

| **命令** | **代理** | **模式** | **MCP服务器** |
|:------------:|:----------:|:---------:|:---------------:|
| **25** | **15** | **7** | **8** |
| 斜杠命令 | 专业AI | 行为模式 | 集成功能 |

使用新的 `/sc:help` 命令查看所有可用命令的完整列表。

</div>

---

<div align="center">

## 🎯 **概述**

SuperClaude 是一个**元编程配置框架**，通过行为指令注入和组件编排将 Claude Code 转变为结构化开发平台。它提供系统化的工作流自动化，配备强大的工具和智能代理。

## 免责声明

本项目未获得 Anthropic 的关联或认可。
Claude Code 是由 [Anthropic](https://www.anthropic.com/) 构建和维护的产品。

---

## ⚠️ **重要：Beta 版本说明**

> **此插件版本目前处于 Beta 阶段。**

### **关键兼容性信息：**

与以前的 SuperClaude 安装**不兼容**：
- pip 版本 (`pip install SuperClaude`)
- pipx 版本 (`pipx install SuperClaude`)
- npm 版本 (`npm install -g @bifrost_inc/superclaude`)
- uv 版本 (`uv tool install SuperClaude`)

### **安装前的必要步骤：**

1. **备份** 您现有的 SuperClaude 配置
2. **卸载** 以前的版本：
   ```bash
   # pip 用户
   pip uninstall SuperClaude

   # pipx 用户
   pipx uninstall SuperClaude

   # npm 用户
   npm uninstall -g @bifrost_inc/superclaude

   # uv 用户
   uv tool uninstall SuperClaude
   ```
3. **然后** 继续安装插件

⚠️ **Beta 版限制：**
- 可能包含错误或不完整的功能
- 配置格式可能会更改
- 尚不推荐用于生产关键工作
- 非常欢迎反馈和问题报告！

---

## ⚡ **快速安装**

SuperClaude 作为原生 Claude Code 插件提供，便于安装和自动更新。

```shell
# 添加 SuperClaude 市场
/plugin marketplace add SuperClaude-Org/SuperClaude_Plugin

# 安装插件
/plugin install sc@superclaude-official

# 重启 Claude Code 以激活
```

**插件优势：**
- ✅ **简单安装**：一条命令完成，无需 Python/Node.js
- ✅ **自动更新**：由 Claude Code 管理
- ✅ **无冲突**：与系统包隔离
- ✅ **团队共享**：通过市场轻松分发
- ✅ **原生集成**：无缝的 Claude Code 体验
- ✅ **自动 MCP 设置**：AIRIS MCP Gateway 自动配置

### **MCP 服务器设置**

插件自动配置 **AIRIS MCP Gateway**，包含 10 个集成工具。

**前提条件**（一次性设置）：
```bash
# 安装 uvx（MCP 服务器所需）
pip install uv
# 或
brew install uv
```

**验证设置**：
```shell
/sc:setup-mcp   # 交互式设置向导
/sc:verify-mcp  # 检查 MCP 状态
```

**可选 API 密钥**（用于高级功能）：
```bash
# Tavily（网络搜索） - 在 https://tavily.com 获取密钥
export TAVILY_API_KEY="your-key"

# Magic（UI 生成） - 在 https://21st.dev 获取密钥
export TWENTYFIRST_API_KEY="your-key"
```

### **快速开始**

安装后，重启 Claude Code 并尝试：

```shell
# 查看所有命令
/sc:help

# 开始头脑风暴
/sc:brainstorm "您的项目想法"

# 分析代码库
/sc:analyze

# 深度研究
/sc:research "您想研究的主题"
```

</div>

<details>
<summary><b>📦 替代方案：pip/npm 安装</b></summary>

> ⚠️ **警告：** pip/npm 版本与此插件版本不兼容。
>
> 如果选择使用 pip/npm 安装：
> 1. 请勿同时安装插件版本和 pip/npm 版本
> 2. 如果已安装，请先卸载此插件
> 3. 它们使用不同的配置格式，无法共存

SuperClaude V4 也可通过包管理器获得。有关 pip/npm 安装说明，请参阅主 [SuperClaude Framework 仓库](https://github.com/SuperClaude-Org/SuperClaude_Framework)。

</details>

---

<div align="center">

## 💖 **支持项目**

> 坦白说 - 维护 SuperClaude 需要时间和资源。
>
> *仅用于测试的 Claude Max 订阅每月就需要 $100，这还不包括花在文档编写、错误修复和功能开发上的时间。*
> *如果您在日常工作中发现 SuperClaude 有价值，请考虑支持该项目。*
> *即使是少量资金也能帮助覆盖基本费用并保持开发活跃。*
>
> 每个贡献者都很重要，无论是通过代码、反馈还是支持。感谢您成为这个社区的一员！🙏

<table>
<tr>
<td align="center" width="33%">

### ☕ **Ko-fi**
[![Ko-fi](https://img.shields.io/badge/Support_on-Ko--fi-ff5e5b?logo=ko-fi)](https://ko-fi.com/superclaude)

*一次性捐赠*

</td>
<td align="center" width="33%">

### 🎯 **Patreon**
[![Patreon](https://img.shields.io/badge/Become_a-Patron-f96854?logo=patreon)](https://patreon.com/superclaude)

*每月支持*

</td>
<td align="center" width="33%">

### 💜 **GitHub**
[![GitHub Sponsors](https://img.shields.io/badge/GitHub-Sponsor-30363D?logo=github-sponsors)](https://github.com/sponsors/SuperClaude-Org)

*灵活的等级*

</td>
</tr>
</table>

### **您的支持使以下成为可能：**

| 项目 | 成本/影响 |
|------|-------------|
| 🔬 **Claude Max 测试** | 每月 $100 用于验证和测试 |
| ⚡ **功能开发** | 新功能和改进 |
| 📚 **文档** | 全面的指南和示例 |
| 🤝 **社区支持** | 快速响应问题和帮助 |
| 🔧 **MCP 集成** | 测试新的服务器连接 |
| 🌐 **基础设施** | 托管和部署成本 |

> **注意：** 没有压力 - 无论如何框架都将保持开源。只要知道有人使用和欣赏它就很有动力。贡献代码、文档或传播消息也会有所帮助！🙏

</div>

---

<div align="center">

## 🎉 **V4 新特性**

> *版本 4 基于社区反馈和实际使用模式带来了重大改进。*

<table>
<tr>
<td width="50%">

### 🤖 **智能代理系统**
**15 个专业代理**具有领域专业知识：
- Deep Research 代理用于自主网络研究
- 安全工程师捕获真实漏洞
- 前端架构师理解 UI 模式
- 基于上下文的自动协调
- 按需提供领域专业知识

</td>
<td width="50%">

### 📝 **改进的命名空间**
所有命令使用 **`/sc:` 前缀**：
- 与自定义命令无冲突
- 涵盖完整生命周期的 25 个命令
- 从头脑风暴到部署
- 清晰、有组织的命令结构

</td>
</tr>
<tr>
<td width="50%">

### 🔧 **MCP 服务器集成**
**自动设置** 通过 AIRIS MCP Gateway：
- **10 个集成工具** 在一个统一网关中
- **无需手动配置** - 开箱即用
- **上下文优化** - 减少 40% 令牌
- **只需 uvx** - `pip install uv` 或 `brew install uv`

**包含的工具**：
- sequential-thinking, context7, magic, playwright
- serena, morphllm, tavily, chrome-devtools
- git, puppeteer

运行 `/sc:setup-mcp` 验证安装

</td>
<td width="50%">

### 🎯 **行为模式**
**7 种适应性模式**用于不同上下文：
- **Brainstorming** → 提出正确的问题
- **Business Panel** → 多专家战略分析
- **Deep Research** → 自主网络研究
- **Orchestration** → 高效的工具协调
- **Token-Efficiency** → 30-50% 的上下文节省
- **Task Management** → 系统化组织
- **Introspection** → 元认知分析

</td>
</tr>
<tr>
<td width="50%">

### ⚡ **优化的性能**
**更小的框架，更大的项目：**
- 减少的框架占用空间
- 为代码提供更多上下文
- 可能进行更长的对话
- 启用复杂操作

</td>
<td width="50%">

### 📚 **文档改造**
**面向开发者的完全重写：**
- 真实示例和用例
- 记录常见陷阱
- 包含实用工作流程
- 更好的导航结构

</td>
</tr>
</table>

</div>

---

<div align="center">

## 🔬 **Deep Research 能力**

### **与 DR Agent 架构对齐的自主网络研究**

SuperClaude v4.2 引入了全面的 Deep Research 能力，实现自主、适应性和智能的网络研究。

<table>
<tr>
<td width="50%">

### 🎯 **适应性规划**
**三种智能策略：**
- **Planning-Only**：对清晰查询的直接执行
- **Intent-Planning**：对模糊请求的澄清
- **Unified**：协作计划改进（默认）

</td>
<td width="50%">

### 🔄 **多跳推理**
**最多 5 次迭代搜索：**
- 实体扩展（论文 → 作者 → 作品）
- 概念深化（主题 → 详细信息 → 示例）
- 时间推进（当前 → 历史）
- 因果链（效果 → 原因 → 预防）

</td>
</tr>
<tr>
<td width="50%">

### 📊 **质量评分**
**基于置信度的验证：**
- 来源可信度评估（0.0-1.0）
- 覆盖完整性跟踪
- 综合一致性评估
- 最低阈值：0.6，目标：0.8

</td>
<td width="50%">

### 🧠 **基于案例的学习**
**跨会话智能：**
- 模式识别和重用
- 随时间优化策略
- 保存成功的查询公式
- 性能改进跟踪

</td>
</tr>
</table>

### **研究命令用法**

```bash
# 具有自动深度的基本研究
/sc:research "2024 年最新 AI 发展"

# 控制的研究深度
/sc:research "量子计算突破" --depth exhaustive

# 特定策略选择
/sc:research "市场分析" --strategy planning-only

# 领域过滤的研究
/sc:research "React 模式" --domains "reactjs.org,github.com"
```

### **研究深度级别**

| 深度 | 来源 | 跳数 | 时间 | 最适合 |
|:-----:|:-------:|:----:|:----:|----------|
| **Quick** | 5-10 | 1 | ~2分钟 | 快速事实、简单查询 |
| **Standard** | 10-20 | 3 | ~5分钟 | 一般研究（默认） |
| **Deep** | 20-40 | 4 | ~8分钟 | 全面分析 |
| **Exhaustive** | 40+ | 5 | ~10分钟 | 学术级研究 |

### **集成工具编排**

Deep Research 系统智能协调多个工具：
- **Tavily MCP**：主要网络搜索和发现
- **Playwright MCP**：复杂内容提取
- **Sequential MCP**：多步推理和综合
- **Serena MCP**：记忆和学习持久化
- **Context7 MCP**：技术文档查找

</div>

---

<div align="center">

## 📚 **文档**

### **SuperClaude 完整指南**

<table>
<tr>
<th align="center">🚀 入门</th>
<th align="center">📖 用户指南</th>
<th align="center">🛠️ 开发者资源</th>
<th align="center">📋 参考</th>
</tr>
<tr>
<td valign="top">

- 📝 [**快速入门指南**](Docs/Getting-Started/quick-start.md)
  *快速启动和运行*

- 💾 [**安装指南**](Docs/Getting-Started/installation.md)
  *详细的设置说明*

</td>
<td valign="top">

- 🎯 [**命令参考**](Docs/User-Guide/commands.md)
  *全部 25 个斜杠命令*

- 🤖 [**代理指南**](Docs/User-Guide/agents.md)
  *15 个专业代理*

- 🎨 [**行为模式**](Docs/User-Guide/modes.md)
  *7 种适应性模式*

- 🚩 [**标志指南**](Docs/User-Guide/flags.md)
  *控制行为*

- 🔧 [**MCP 服务器**](Docs/User-Guide/mcp-servers.md)
  *7 个服务器集成*

- 💼 [**会话管理**](Docs/User-Guide/session-management.md)
  *保存和恢复状态*

</td>
<td valign="top">

- 🏗️ [**技术架构**](Docs/Developer-Guide/technical-architecture.md)
  *系统设计详细信息*

- 💻 [**贡献代码**](Docs/Developer-Guide/contributing-code.md)
  *开发工作流程*

- 🧪 [**测试和调试**](Docs/Developer-Guide/testing-debugging.md)
  *质量保证*

</td>
<td valign="top">
- 📓 [**示例手册**](Docs/Reference/examples-cookbook.md)
  *真实世界的配方*

- 🔍 [**故障排除**](Docs/Reference/troubleshooting.md)
  *常见问题和修复*

</td>
</tr>
</table>

</div>

---

<div align="center">

## 🤝 **贡献**

### **加入 SuperClaude 社区**

我们欢迎各种形式的贡献！以下是您可以提供帮助的方式：

| 优先级 | 领域 | 描述 |
|:--------:|------|-------------|
| 📝 **高** | 文档 | 改进指南、添加示例、修复拼写错误 |
| 🔧 **高** | MCP 集成 | 添加服务器配置、测试集成 |
| 🎯 **中** | 工作流程 | 创建命令模式和配方 |
| 🧪 **中** | 测试 | 添加测试、验证功能 |
| 🌐 **低** | i18n | 将文档翻译成其他语言 |

<p align="center">
  <a href="CONTRIBUTING.md">
    <img src="https://img.shields.io/badge/📖_Read-Contributing_Guide-blue" alt="Contributing Guide">
  </a>
  <a href="https://github.com/SuperClaude-Org/SuperClaude_Framework/graphs/contributors">
    <img src="https://img.shields.io/badge/👥_View-All_Contributors-green" alt="Contributors">
  </a>
</p>

</div>

---

<div align="center">

## ⚖️ **许可证**

本项目根据 **MIT 许可证**授权 - 详情请参阅 [LICENSE](LICENSE) 文件。

<p align="center">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg?" alt="MIT License">
</p>

</div>

---

<div align="center">

## ⭐ **Star 历史**

<a href="https://www.star-history.com/#SuperClaude-Org/SuperClaude_Framework&Timeline">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=SuperClaude-Org/SuperClaude_Framework&type=Timeline&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=SuperClaude-Org/SuperClaude_Framework&type=Timeline" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=SuperClaude-Org/SuperClaude_Framework&type=Timeline" />
 </picture>
</a>


</div>

---

<div align="center">

### **🚀 由 SuperClaude 社区倾情打造**

<p align="center">
  <sub>为突破界限的开发者用❤️制作</sub>
</p>

<p align="center">
  <a href="#-superclaude-框架">返回顶部 ↑</a>
</p>

</div>
