[README.md](https://github.com/user-attachments/files/28956535/README.md)
# 🌱 双碳合规审查系统

> 基于 AI 的智能合规审查平台，助力企业双碳目标达成

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org)
[![Vue](https://img.shields.io/badge/vue-3.3-green.svg)](https://vuejs.org)
[![Node](https://img.shields.io/badge/node-18+-green.svg)](https://nodejs.org)

---

## 📋 目录

- [项目简介](#项目简介)
- [功能特性](#功能特性)
- [技术架构](#技术架构)
- [项目结构](#项目结构)
- [快速开始](#快速开始)
  - [后端启动](#后端启动)
  - [前端启动](#前端启动)
- [环境变量说明](#环境变量说明)
- [API 接口文档](#api-接口文档)
- [IP 形象说明](#ip-形象说明)
- [常见问题](#常见问题)
- [贡献指南](#贡献指南)
- [开源协议](#开源协议)

---

## 项目简介

**双碳合规审查系统**是一套面向企业的智能化双碳合规管理平台，基于 AI 大语言模型与 RAG（检索增强生成）技术，精准匹配国家"1+N"双碳政策体系，为企业提供政策问答、项目合规审查、碳核算与合规报告一键生成等核心功能。

系统由**Python Flask 后端**与 **Vue 3 前端**组成，支持管理员与普通用户双角色，覆盖从政策查询到合规报告输出的完整业务闭环。

---

## 功能特性

### 🔐 用户认证
- 基于 Flask-JWT 的用户注册 / 登录 / Token 刷新
- 管理员 / 普通用户双角色权限隔离
- 全局 JWT 鉴权中间件，保护所有受控接口

### 💬 智能政策问答
- 基于 LangChain + FAISS 向量检索的 RAG 问答引擎
- 支持上传政策 PDF / Word 文档自动入库建索引
- 引用来源可追溯，回答附带原文出处

### 📝 项目合规审查
- 多类型材料上传（PDF / Word / 图片）
- 基于合规规则引擎自动评分（0~100 分）
- 生成结构化审查报告，逐条标注合规 / 不合规 / 建议项

### 📊 碳核算管理
- 范围一 / 范围二 / 范围三排放数据填报
- 历史数据趋势分析与图表展示
- 排放数据导出 Excel

### 📄 合规报告生成
- 一键生成符合规范的合规报告（.docx）
- 报告内含政策依据、审查结果、排放汇总、改进建议
- 报告自动归档，支持历史报告在线预览与下载

### 🛠️ 管理后台
- 政策文档库管理（上传 / 删除 / 重新向量化）
- 用户账号管理（禁用 / 重置密码 / 角色调整）
- 系统配置（AI 模型参数、合规规则阈值）

---

## 技术架构

### 系统架构图

```
┌──────────────────────────────────────────────────────┐
│                  浏览器 / 客户端                    │
└──────────────────────┬───────────────────────────┘
                           │ HTTPS
┌──────────────────────▼───────────────────────────┐
│                  Vue 3 前端（Vite）               │
│  Login / Home / PolicyQA / ProjectReview / ...   │
└──────────────────────┬───────────────────────────┘
                           │ REST API
┌──────────────────────▼───────────────────────────┐
│                Flask 后端（Python 3.9+）          │
│  /api/auth  /api/qa  /api/review  /api/policy │
└──┬──────────────┬──────────────┬───────────────┘
   │              │              │
┌──▼──────┐ ┌▼──────────┐ ┌▼──────────────┐
│  MySQL   │ │  FAISS     │ │  LangChain     │
│  (用户/  │ │  向量数据库  │ │  (RAG 引擎)   │
│  项目数据) │ │             │ │                │
└───────────┘ └────────────┘ └────────────────┘
```

### 技术栈

| 层级 | 技术 |
|------|------|
| **前端** | Vue 3.3+、TypeScript、Vite 5、Element Plus 2.4+、Vue Router 4、Axios |
| **后端** | Python 3.9+、Flask 2.3、Flask-SQLAlchemy、PyMySQL |
| **AI 引擎** | LangChain 0.1、FAISS-CPU 1.8、sentence-transformers 2.2、HuggingFace Hub |
| **文档处理** | PyPDF 3.17、python-docx 0.8 |
| **数据库** | MySQL 5.7+ |
| **向量检索** | FAISS 1.8（本地向量索引） |

---

## 项目结构

```
double_c/
├── backend/                          # Flask 后端
│   ├── app.py                       # 应用入口，注册 Blueprint
│   ├── config.py                    # 配置（数据库 / JWT / AI 模型）
│   ├── db.py                       # SQLAlchemy 初始化
│   ├── models.py                   # ORM 模型（User / Project / Report / Message）
│   ├── requirements.txt             # Python 依赖清单
│   ├── .env                         # 环境变量（不提交，参考 .env.example）
│   ├── api/                        # 业务接口层
│   │   ├── auth.py                 # 认证接口（注册 / 登录 / 刷新 Token）
│   │   ├── policy.py              # 政策文档管理接口
│   │   ├── qa.py                 # 智能问答接口（RAG）
│   │   └── review.py             # 项目审查接口
│   ├── utils/                      # 工具层
│   │   ├── rag_engine.py          # RAG 引擎（向量化 / 检索 / 问答链）
│   │   ├── compliance_engine.py   # 合规规则引擎（评分 / 报告解析）
│   │   ├── report_generator.py    # 合规报告生成（.docx）
│   │   └── document_processor.py # 文档解析（PDF / Word → 文本分块）
│   └── docs/                      # 后端文档
│       ├── api_document.md         # API 接口文档
│       └── database_design.md    # 数据库设计文档
│
├── frontend/                         # Vue 3 前端
│   ├── index.html                  # SPA 入口 HTML
│   ├── package.json               # Node 依赖配置
│   ├── vite.config.ts            # Vite 构建配置
│   ├── tsconfig.json             # TypeScript 配置
│   ├── public/
│   │   └── img/
│   │       ├── logo.jpg          # 系统 Logo
│   │       └── ip_character.png # IP 形象「碳小碳」
│   ├── src/
│   │   ├── main.ts              # 应用入口（挂载 App、Router、Element Plus）
│   │   ├── App.vue              # 根组件（全局布局）
│   │   ├── api/
│   │   │   └── index.ts        # Axios 实例封装（拦截器 / Token 注入）
│   │   ├── router/
│   │   │   └── index.ts        # 路由配置（守卫 / 懒加载）
│   │   ├── styles/
│   │   │   └── theme.css       # 全局主题变量
│   │   └── views/
│   │       ├── Login.vue                # 登录页（UI 设计还原）
│   │       ├── Home.vue                 # 首页（用户入口）
│   │       ├── AdminLayout.vue         # 管理员布局（侧边栏）
│   │       └── admin/
│   │           ├── Dashboard.vue       # 管理员仪表盘
│   │           ├── PolicyManage.vue    # 政策文档管理
│   │           └── SystemSettings.vue  # 系统设置
│   └── dist/                        # 构建产物（npm run build 生成）
│
└── README.md                        # 本文件
```

---

## 快速开始

### 环境要求

| 依赖 | 版本要求 |
|------|-----------|
| Python | ≥ 3.9 |
| Node.js | ≥ 18 |
| MySQL | ≥ 5.7 |
| pip | 最新版 |

---

### 后端启动

```bash
# 进入后端目录
cd backend

# 安装 Python 依赖
pip install -r requirements.txt

# 配置环境变量（参考下方「环境变量说明」）
cp .env.example .env
# 然后编辑 .env 填入你的数据库密码、JWT 密钥等

# 初始化数据库
python -c "from app import app, db; app.app_context().push(); db.create_all()"

# 启动后端服务（默认 http://localhost:5000）
python app.py
```

### 前端启动

```bash
# 进入前端目录
cd frontend

# 安装 Node 依赖
npm install

# 启动开发服务器（默认 http://localhost:5173）
npm run dev

# 构建生产版本（输出到 dist/）
npm run build
```

---

## 环境变量说明

后端 `backend/.env` 配置项：

| 变量名 | 说明 | 示例 |
|--------|------|------|
| `DB_HOST` | MySQL 主机地址 | `localhost` |
| `DB_PORT` | MySQL 端口 | `3306` |
| `DB_USER` | 数据库用户名 | `root` |
| `DB_PASSWORD` | 数据库密码 | `your_password` |
| `DB_NAME` | 数据库名 | `double_c` |
| `JWT_SECRET_KEY` | JWT 签名密钥（请修改为随机字符串） | `your-secret-key` |
| `HF_HOME` | HuggingFace 模型缓存目录 | `D:/hf_cache` |

> ⚠️ **重要**：`.env` 文件已加入 `.gitignore`，请勿提交到远程仓库。

---

## API 接口文档

完整接口文档见 `backend/docs/api_document.md`，以下为概览：

### 认证模块 `/api/auth`

| 方法 | 路径 | 说明 |
|------|------|------|
| POST | `/api/auth/register` | 用户注册 |
| POST | `/api/auth/login` | 用户登录，返回 `access_token` |
| POST | `/api/auth/refresh` | 刷新 Token |

### 政策问答模块 `/api/qa`

| 方法 | 路径 | 说明 |
|------|------|------|
| POST | `/api/qa/ask` | 提交问题，返回 AI 回答 + 引用来源 |
| POST | `/api/qa/upload_doc` | 上传政策文档（PDF / Word），自动向量化 |

### 项目审查模块 `/api/review`

| 方法 | 路径 | 说明 |
|------|------|------|
| POST | `/api/review/upload` | 上传项目材料，触发合规审查 |
| GET | `/api/review/:id` | 获取审查报告详情 |

### 政策管理模块 `/api/policy`（管理员）

| 方法 | 路径 | 说明 |
|------|------|------|
| POST | `/api/policy/upload` | 上传政策文档 |
| DELETE | `/api/policy/:id` | 删除政策文档 |
| POST | `/api/policy/rebuild_index` | 重新构建 FAISS 向量索引 |

---

## IP 形象说明

系统官方 IP 形象 **「碳小碳」**：

- 图片路径：`frontend/public/img/ip_character.png`
- 在登录页（`Login.vue`）中以浮动动画展示
- 底部配有柔和光晕与投影，增强场景融入感
- 设计风格：清新绿色系，契合双碳主题

---

## 常见问题

### Q：后端启动后前端无法访问接口？
**A**：检查后端是否运行在 `localhost:5000`，且前端 `src/api/index.ts` 中的 `baseURL` 是否与之匹配。跨域问题已由 `flask-cors` 处理，若仍有问题请确认 `flask-cors` 已安装。

### Q：FAISS 向量索引如何重新构建？
**A**：调用 `POST /api/policy/rebuild_index` 接口，或删除 `backend/data/faiss_index/` 目录后重启后端，系统会自动重新向量化所有政策文档。

### Q：登录后跳转 404？
**A**：确认前端路由配置正确，且 `frontend/dist/` 目录已生成（执行 `npm run build`）。开发模式下由 Vite 处理路由，生产模式需确保服务器配置了 SPA fallback。

---

## 贡献指南

1. Fork 本仓库
2. 新建功能分支（`git checkout -b feature/your-feature`）
3. 提交更改（`git commit -m 'feat: 描述你的更改'`）
4. 推送到分支（`git push origin feature/your-feature`）
5. 提交 Pull Request

### 分支说明

| 分支 | 说明 |
|------|------|
| `main` | 生产环境分支，受保护 |
| `dev` | 开发集成分支，所有功能分支合并至此 |
| `feature/*` | 功能开发分支 |

---

## 开源协议

本项目采用 MIT 协议开源。详见 [LICENSE](LICENSE) 文件。

---

## 致谢

- [Vue 3](https://vuejs.org) — 渐进式前端框架
- [Element Plus](https://element-plus.org) — Vue 3 组件库
- [Flask](https://flask.palletsprojects.com) — 轻量级 Python Web 框架
- [LangChain](https://www.langchain.com) — LLM 应用开发框架
- [FAISS](https://github.com/facebookresearch/faiss) — 高效向量检索库

---

<p align="center">Made with ❤️ for a greener future 🌱</p>
