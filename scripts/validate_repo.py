#!/usr/bin/env python3
"""Lightweight repository validation for tuiwen-grok-flow."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "configs/default_project_config.json",
    "schemas/shot_control_card.schema.json",
    "examples/shot_control_card.example.json",
    "prompts/01_reference_video_style_extract.md",
    "prompts/02_original_commentary_rewrite.md",
    "prompts/03_segment_10s.md",
    "prompts/04_shot_control_card.md",
    "prompts/05_gpt_image_2_prompt.md",
    "prompts/06_grok_video_prompt.md",
    "templates/ui_overlay_templates.md",
]


def load_json(relative_path: str) -> object:
    path = ROOT / relative_path
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def validate_required_files() -> None:
    missing = [path for path in REQUIRED_FILES if not (ROOT / path).is_file()]
    require(not missing, "Missing required files: " + ", ".join(missing))


def validate_json_files() -> None:
    json_paths = [
        "configs/default_project_config.json",
        "schemas/shot_control_card.schema.json",
        "examples/shot_control_card.example.json",
    ]
    for relative_path in json_paths:
        load_json(relative_path)


def validate_shot_control_card_example() -> None:
    schema = load_json("schemas/shot_control_card.schema.json")
    example = load_json("examples/shot_control_card.example.json")

    require(isinstance(schema, dict), "Shot control card schema must be a JSON object")
    require(isinstance(example, dict), "Shot control card example must be a JSON object")

    required = schema.get("required", [])
    require(isinstance(required, list), "Schema required field must be a list")

    missing = [field for field in required if field not in example]
    require(not missing, "Example card missing required fields: " + ", ".join(missing))

    properties = schema.get("properties", {})
    require(isinstance(properties, dict), "Schema properties field must be an object")

    story_function = properties.get("story_function", {})
    story_enum = story_function.get("enum", []) if isinstance(story_function, dict) else []
    require(
        example.get("story_function") in story_enum,
        "Example story_function is not allowed by schema",
    )

    generation_mode = properties.get("generation_mode", {})
    mode_enum = generation_mode.get("enum", []) if isinstance(generation_mode, dict) else []
    require(
        example.get("generation_mode") in mode_enum,
        "Example generation_mode is not allowed by schema",
    )

    ui_overlay = example.get("ui_overlay")
    require(isinstance(ui_overlay, dict), "Example ui_overlay must be an object")
    for field in ("needed", "type", "content"):
        require(field in ui_overlay, f"Example ui_overlay missing field: {field}")


def main() -> int:
    checks = [
        validate_required_files,
        validate_json_files,
        validate_shot_control_card_example,
    ]

    for check in checks:
        check()

    print("Repository validation passed.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except AssertionError as exc:
        print(f"Repository validation failed: {exc}", file=sys.stderr)
        raise SystemExit(1)
