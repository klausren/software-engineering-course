#!/usr/bin/env python3
"""Put the bilingual figures into the slide decks.

The problem this solves
-----------------------
Each figure page in the decks carries the diagram's *labels* as loose text
boxes and no diagram. Dropping a picture on top would leave both, so the
orphan labels have to go -- but only the labels, never the prose. Deleting the
wrong shape in a teaching deck is expensive and silent, so the rule is narrow
and the plan is printable:

  A shape is an orphan label when EVERY token of its text is in the figure's
  own label vocabulary (a token is a run of letters/digits/CJK). Prose has
  words the diagram does not ("Drawbacks", "sequential", "expensive"), so it
  survives. The title placeholder is never touched, and neither is a shape
  already holding a picture.

Run --dry-run first. It prints exactly what would be deleted and what stays.
Nothing is written until you drop the flag.

Usage
-----
    python3 figures/insert.py --dry-run
    python3 figures/insert.py
"""

import argparse
import os
import re
import shutil
import sys

from pptx import Presentation
from pptx.util import Emu, Inches

HERE = os.path.dirname(os.path.abspath(__file__))
DECK = os.path.dirname(HERE)
PNG = os.path.join(HERE, "png")

TOKEN = re.compile(r"[A-Za-z]+|[\u4e00-\u9fff]+|\d+")

# slide number (1-based, as the deck counts) -> (png, label vocabulary)
# The vocabulary is the set of words the diagram itself uses. Keep it tight:
# every word added here is a word that can no longer protect a prose shape.
PLAN = {
    13: ("w02-process-vocabulary", ["Process", "model", "Framework", "activity", "frame",
                                    "Entry", "criteria", "Task", "set", "Milestones",
                                    "Exit", "communication", "planning", "modeling",
                                    "construction", "deployment", "waterfall", "V",
                                    "incremental", "prototyping", "spiral", "agile",
                                    "过程", "模型", "框架", "活动", "过程帧", "入口条件",
                                    "任务集", "里程碑", "出口条件", "沟通", "策划", "建模",
                                    "构建", "部署"]),
    15: ("w02-waterfall", ["Communication", "Planning", "Modeling", "Construction",
                           "Deployment", "requirements", "plan", "analysis", "design",
                           "code", "test", "delivery", "support", "feedback",
                           "沟通", "策划", "建模", "构建", "部署", "需求收集", "项目计划",
                           "分析与设计", "编码与测试", "交付与维护"]),
    19: ("w02-v-model", ["Left", "leg", "requirements", "design", "code", "Right",
                         "testing", "unit", "integration", "system", "acceptance",
                         "development", "verification", "validation", "V",
                         "左腿", "右腿", "需求", "设计", "编码", "测试", "单元", "集成",
                         "系统", "验收", "开发", "验证", "确认"]),
    20: ("w02-incremental", ["Increment", "core", "features", "more", "full", "product",
                             "Comm", "Plan", "Model", "Build", "Deploy", "Communication",
                             "增量", "核心功能", "更多功能", "完整产品", "沟通", "策划",
                             "建模", "构建", "部署"]),
    23: ("w02-one-project-two-models", ["Increment", "monitor", "alert", "escalate",
                                        "harden", "feedback", "增量", "监测", "告警",
                                        "升级", "加固", "反馈"]),
    24: ("w02-prototyping", ["Prototype", "quick", "working", "model", "Listen", "user",
                             "Build", "revise", "mock-up", "test", "drive", "Feedback",
                             "on", "repeat", "原型", "快速可运行模型", "听取用户",
                             "构建", "修改", "用户试用", "用户反馈", "倾听", "循环"]),
    26: ("w02-spiral", ["Risk", "Determine", "objectives", "alternatives", "and",
                        "constraints", "Evaluate", "resolve", "risks", "Develop",
                        "verify", "next-level", "product", "Plan", "the", "next",
                        "iteration", "风险", "确定目标", "评估", "解决", "开发", "验证",
                        "计划", "迭代"]),
    31: ("w02-model-selection", ["Model", "Waterfall", "Incremental", "Prototyping",
                                 "Spiral", "Requirements", "Delivery", "Risk", "Typical",
                                 "Use", "模型", "瀑布", "增量", "原型", "螺旋", "需求",
                                 "交付", "风险"]),
    32: ("w02-ai-model-selection", ["HUMAN", "AI", "CHECK", "ARTEFACT", "context",
                                    "clarity", "volatility", "team", "size", "risk",
                                    "level", "drafts", "candidates", "recommendation",
                                    "ASSUMPTION", "flags", "cost", "ceremony", "choice",
                                    "模型", "需求", "团队", "规模", "风险", "建议", "假设"]),
}


def norm_tokens(text):
    return [t.lower() for t in TOKEN.findall(text)]


def is_title(shape):
    return shape.has_text_frame and shape.is_placeholder and shape.placeholder_format.idx == 0


def classify(slide, vocab):
    """Return (orphans, keepers, has_picture) for one slide."""
    v = {w.lower() for w in vocab}
    orphans, keepers, pic = [], [], False
    for shape in slide.shapes:
        if shape.shape_type == 13 or shape.__class__.__name__ == "Picture":
            pic = True
            continue
        if not shape.has_text_frame:
            continue
        text = shape.text_frame.text.strip()
        if not text:
            continue
        if is_title(shape):
            keepers.append(("TITLE", text))
            continue
        toks = norm_tokens(text)
        if toks and all(t in v for t in toks) and len(text) <= 40:
            orphans.append((shape, text))
        else:
            keepers.append(("prose", text))
    return orphans, keepers, pic


def place(slide, png_path):
    """Fit the figure into the content area under the title, centred."""
    from PIL import Image
    with Image.open(png_path) as im:
        ar = im.width / im.height
    box_l, box_t = Inches(0.45), Inches(1.25)
    box_w, box_h = Inches(12.43), Inches(5.85)
    if ar > box_w / box_h:
        w, h = box_w, Emu(int(box_w / ar))
    else:
        h, w = box_h, Emu(int(box_h * ar))
    left = Emu(int(box_l + (box_w - w) / 2))
    top = Emu(int(box_t + (box_h - h) / 2))
    slide.shapes.add_picture(png_path, left, top, width=w, height=h)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("deck", help="path to the .pptx")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if not args.dry_run:
        backup = args.deck + ".pre-figures.bak"
        if not os.path.exists(backup):
            shutil.copy2(args.deck, backup)
            print(f"backup: {os.path.basename(backup)}")

    prs = Presentation(args.deck)
    todo = 0
    for n, slide in enumerate(prs.slides, 1):
        if n not in PLAN:
            continue
        name, vocab = PLAN[n]
        png = os.path.join(PNG, name + ".png")
        if not os.path.exists(png):
            print(f"slide {n}: MISSING {name}.png -- skipped")
            continue
        orphans, keepers, has_pic = classify(slide, vocab)
        title = next((t for k, t in keepers if k == "TITLE"), "(no title)")
        print(f"\n--- slide {n}: {title}")
        print(f"    figure  {name}.png" + ("   [already has a picture]" if has_pic else ""))
        print(f"    DELETE {len(orphans)} orphan label shape(s):")
        for _, t in orphans:
            print(f"        - {t!r}")
        prose = [t for k, t in keepers if k == "prose"]
        print(f"    KEEP   {len(prose)} prose shape(s)" +
              (f", first: {prose[0][:60]!r}" if prose else ""))
        todo += 1
        if not args.dry_run:
            for shape, _ in orphans:
                shape._element.getparent().remove(shape._element)
            place(slide, png)

    print(f"\n{todo} slide(s) planned")
    if args.dry_run:
        print("dry run -- nothing written. Re-run without --dry-run to apply.")
    else:
        prs.save(args.deck)
        print(f"wrote {os.path.basename(args.deck)}")


if __name__ == "__main__":
    sys.exit(main())
