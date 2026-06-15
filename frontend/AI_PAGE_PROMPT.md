# AI 前端页面生成提示词 - 双碳合规审查系统首页

## 使用说明
将以下提示词复制到 AI 工具（v0.dev、Bolt.new、ChatGPT、Claude）中，即可生成与 UI 设计高度一致的 Vue 3 前端页面。

---

## 完整提示词

```markdown
我需要一个 Vue 3 + TypeScript + Element Plus 的首页组件，用于"双碳合规审查系统"。

## 技术栈要求
- Vue 3 Composition API (`<script setup lang="ts">`)
- TypeScript
- Element Plus UI 框架
- 响应式设计（flex 布局）
- 图片资源放在 `public/img/` 目录下，通过 `/img/xxx` 引用

## 页面结构设计

### 1. Header 导航栏
- 固定在顶部，白色背景，底部细微阴影
- 高度：64px
- 内容居中，最大宽度 1200px，左右 padding 24px
- 布局：flex row，space-between，align-center
- 左侧：
  - Logo 图片：`/img/logo.jpg`（高度 40px，保持宽高比）
  - 系统名称："双碳合规审查系统"（字体 18px，font-weight 600，颜色 #1a1a1a）
- 右侧导航菜单：
  - 菜单项：首页 | 合规审查 | 数据填报 | 碳核算 | 系统管理
  - 当前页面高亮（首页），颜色 #409EFF
  - 默认颜色 #606266，hover 变 #409EFF
  - 字体 14px

### 2. Hero 主视觉区域
- 高度：calc(100vh - 64px) 或最小 600px
- 背景：渐变色 linear-gradient(135deg, #0a1628 0%, #1a3a5c 50%, #0d2137 100%)
- 整体布局：flex row，align-center，justify-center
- 内容居中，最大宽度 1200px，左右 padding 24px

#### 左侧文字区域（占 50% 宽度）
- 主标题："双碳合规审查系统"
  - 字体大小：48px（桌面端），32px（移动端）
  - font-weight: 700
  - 颜色：白色
  - 行高：1.2
  - margin-bottom: 24px
- 副标题/描述文字：
  - "基于 AI 的智能合规审查平台，助力企业双碳目标达成"
  - 字体大小：18px
  - 颜色：rgba(255, 255, 255, 0.85)
  - line-height: 1.6
  - margin-bottom: 40px
  - max-width: 500px
- CTA 按钮组：
  - 主按钮："立即体验"（蓝色 #409EFF，白色文字，padding 12px 32px，border-radius 8px）
  - 次按钮："了解更多"（透明背景，白色边框 2px，白色文字，padding 12px 32px，border-radius 8px）
  - 按钮间距 16px

#### 右侧 IP 形象区域（占 50% 宽度）
- 显示 IP 形象图片：`/img/ip_character.png`
- 图片尺寸：最大宽度 400px，自适应高度
- 添加轻微的浮动动画效果（CSS animation，上下浮动 20px，周期 3s，ease-in-out）
- 图片下方有柔和的光晕效果（radial-gradient，半透明蓝色）

### 3. 底部装饰条
- 位于 Hero 区域底部
- 高度：80px
- 背景：线性渐变，从透明到浅蓝色 #f0f9ff
- 可能有波浪形装饰（SVG wave）

## 样式细节
- 字体家族：系统默认，-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif
- 所有链接使用 `<router-link>` 而不是 `<a>` 标签
- 响应式断点：
  - 桌面端：> 768px，左右分栏
  - 移动端：≤ 768px，上下堆叠，文字居中
- 动画：CSS transition，0.3s ease
- 禁止引入 Tailwind CSS，使用纯 CSS + Element Plus 内置样式

## 文件结构
生成以下文件：
1. `src/views/Home.vue` - 主页面组件
2. `src/router/index.ts` - 路由配置（如果需要）
3. 确保图片路径正确指向 `/img/logo.jpg` 和 `/img/ip_character.png`

## 额外要求
- 代码简洁，注释清晰
- 使用 scoped CSS（`<style scoped>`）
- 确保图片加载失败时有 fallback
- 页面在 1920x1080 和 375x667 分辨率下都显示正常
```

---

## 使用方法

1. **复制提示词**：复制上面代码块中的内容
2. **选择 AI 工具**：
   - **v0.dev**（推荐）：专为前端生成优化，代码质量高
   - **Bolt.new**：可实时预览和调试
   - **Claude 3.5 Sonnet**：理解设计细节能力强
   - **ChatGPT 4o**：快速原型生成

3. **粘贴并生成**：将提示词粘贴到 AI 工具中，等待生成

4. **微调优化**：根据生成结果，提出具体修改要求（如"把主标题颜色改为渐变色"）

## 图片资源确认

确保你的项目目录结构如下：
```
frontend/
  public/
    img/
      logo.jpg          # 系统 Logo
      ip_character.png  # IP 形象（碳小碳）
  src/
    views/
      Home.vue          # 生成的首页组件
```

## 提示词优化技巧

如果生成结果不准确，可以添加以下细节：

1. **颜色精确值**：在提示词中指定具体的 hex 颜色码
2. **间距数值**：明确 margin、padding、gap 的具体像素值
3. **字体大小**：为每个文本元素指定精确的 font-size
4. **参考图片**：如果 AI 工具支持图片上传，上传你的 UI 设计稿作为参考

## 常见问题

**Q: 生成的代码引入了 Tailwind CSS？**
A: 在提示词中明确写"禁止引入 Tailwind CSS，使用纯 CSS"

**Q: 图片不显示？**
A: 检查图片是否放在 `public/img/` 目录下，并使用 `/img/xxx` 路径引用

**Q: 响应式效果不好？**
A: 在提示词中明确指定移动端的具体样式（字体大小、布局方式等）
