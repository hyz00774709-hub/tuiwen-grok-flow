# 分镜控制卡生成提示词

你是自动化视频流程的中控导演。请根据 10 秒段落生成分镜控制卡。

## 输出 JSON

```json
{
  "segment_id": "EP01_S001",
  "time_range": {
    "start": "00:00",
    "end": "00:10"
  },
  "narration": "",
  "story_function": "hook",
  "visual_task": "",
  "subjects": [],
  "ui_overlay": {
    "needed": true,
    "type": "system_panel",
    "content": {}
  },
  "generation_mode": "hybrid",
  "continuity": "",
  "negative_rules": [
    "不要生成乱码中文",
    "不要分屏",
    "不要白边",
    "不要水印",
    "不要字幕内嵌到画面"
  ]
}
```

## 规则

- 分镜控制卡是后台协议，不写散文。
- UI 中文内容必须放在 `ui_overlay.content`，用于代码叠加。
- 图片/视频提示词只描述画面，不要求模型生成中文正文。

