# 双碳合规审查平台 API 接口文档

## 基础信息

- **基础路径**：`/api`
- **认证方式**：Session Cookie
- **返回格式**：
  ```json
  {"code": 200, "message": "成功", "data": {...}}
  ```

---

## 1. 认证接口

### 1.1 登录
- **路径**：`POST /api/auth/login`
- **请求体**：
  ```json
  {"username": "admin", "password": "admin123"}
  ```
- **响应**：
  ```json
  {"code": 200, "data": {"username": "admin", "role": "admin"}}
  ```

### 1.2 退出登录
- **路径**：`POST /api/auth/logout`

### 1.3 获取当前用户
- **路径**：`GET /api/auth/me`

---

## 2. 政策管理接口

### 2.1 政策列表
- **路径**：`GET /api/policy/list`

### 2.2 上传政策文件
- **路径**：`POST /api/policy/upload`
- **请求**：`FormData`（字段：`file`, `title`, `industry`, `region`）

### 2.3 删除政策
- **路径**：`DELETE /api/policy/:id`

---

## 3. 智能问答接口

### 3.1 提问
- **路径**：`POST /api/qa/ask`
- **请求体**：
  ```json
  {"question": "能耗标准是什么？", "policy_id": 1}
  ```

### 3.2 问答历史
- **路径**：`GET /api/qa/history`

---

## 4. 项目审查接口

### 4.1 提交审查
- **路径**：`POST /api/review/submit`
- **请求体**：
  ```json
  {
    "project_name": "XX钢铁项目",
    "industry": "钢铁",
    "region": "北京",
    "energy_consumption": 1000.5
  }
  ```

### 4.2 查看审查结果
- **路径**：`GET /api/review/:id`

### 4.3 审查历史
- **路径**：`GET /api/review/history`

---

## 错误码

| code | 含义 |
|---|---|
| 200 | 成功 |
| 400 | 请求参数错误 |
| 401 | 未登录 / 认证失败 |
| 404 | 资源不存在 |
| 500 | 服务器内部错误 |
