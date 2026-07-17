# 推文解说 Grok 一键流程

这个仓库用于沉淀“小说推文解说 + Grok 10 秒视频段”的自动化流程、提示词模板、分镜控制卡协议和基础校验工具。

素材、参考视频、音频、SRT、生成图片、视频片段和成片不放在 GitHub。GitHub 只保存可以复用的流程和工具。

## 当前目标

先跑通 60-90 秒测试闭环，再扩展到整本免费部分或授权文本。

```text
书名/链接/文本
  -> 免费内容提取
  -> 主线梳理
  -> 原创解说稿
  -> 10 秒段落
  -> 分镜控制卡
  -> GPT Image 2 图片提示词
  -> Grok 视频提示词
  -> UI/字幕/音效叠加
  -> 预览 MP4 或剪映素材包
```

## 默认规格

- 视频比例：16:9 横屏
- 单段时长：10 秒优先，后续根据控制力再评估 15 秒
- 出图模型：GPT Image 2
- 视频模型：Grok
- 字幕：底部黄色大字幕，描边/阴影，保持安全区
- UI 文字：由代码模板叠加，不交给图片模型生成中文正文
- 音频：用户自配旁白和 SRT，视频提示词默认不生成旁白和 BGM

## 内容边界

- 只处理公开免费章节、用户上传文本、或用户已获得授权的内容。
- 不绕过 VIP、付费墙、登录权限或平台限制抓取内容。
- 文案采用原创解说重构，不做逐句同义词替换。
- 保留主线、人物关系、核心爽点，但改写叙述顺序、表达方式和短视频节奏。

## 目录

```text
configs/                  项目默认配置
docs/                     流程说明和项目结构
prompts/                  各环节提示词模板
schemas/                  分镜控制卡结构约束
templates/                UI 叠加模板
skills/                   后续 skill 化计划
examples/                 可校验示例
scripts/                  仓库校验脚本
.github/workflows/        GitHub Actions 工作流
```

## 分镜控制卡

分镜控制卡是自动化流程的后台中控协议，用来把旁白、画面任务、UI 叠加、人物/场景和生成方式对齐。

示例文件：

```text
examples/shot_control_card.example.json
```

结构文件：

```text
schemas/shot_control_card.schema.json
```

## 本地校验

当前校验脚本不依赖第三方库。

```bash
python3 scripts/validate_repo.py
```

校验内容：

- 必要文件是否存在
- JSON 文件是否能正常解析
- 示例控制卡是否包含必填字段
- 示例控制卡的枚举值是否符合 schema

## GitHub Actions

`.github/workflows/validate.yml` 会在 push 和 pull request 时运行基础校验。

## 推荐开发流

1. 从 `main` 新建分支。
2. 修改流程、模板、schema 或脚本。
3. 运行 `python3 scripts/validate_repo.py`。
4. 推送分支并开 draft PR。
5. 审核通过后再合并。
