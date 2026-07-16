# 单本书项目结构

Google Drive 中，每本书建议单独建立一个项目文件夹：

```text
书名_平台_日期/
  00_参考视频/
  01_原文免费部分/
  02_主线分析/
  03_原创解说文案/
  04_SRT与音频/
  05_分镜控制卡/
  06_图片提示词/
  07_Grok视频提示词/
  08_系统UI与字幕模板/
  09_出图与视频片段/
  10_预览成片/
  99_归档/
```

GitHub 中只保存可复用内容：

```text
configs/
docs/
prompts/
schemas/
templates/
skills/
scripts/
```

## 文件命名建议

```text
EP01_0000-0090_测试闭环.md
EP01_0000-0010_segment_card.json
EP01_0000-0010_image_prompt.md
EP01_0000-0010_grok_prompt.md
```

