#!/usr/bin/env python3
"""Week 2 figures: software process models. Bilingual, for the slide deck.

Each figure corresponds to a figure page in W02-Software-Process-Models.pptx.
Those pages currently carry the diagram's labels but no diagram, so these are
drawn fresh rather than lifted: the textbook's own versions are English-only,
and they are laid out on a 760 canvas with no room for a Chinese line.

Run:  python3 figures/gen/figs_w02.py && node figures/render.js
"""

import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import Fig, wrap   # noqa: E402

W = 960
GRAY = "#6B7280"


def _seg(f, x1, y1, x2, y2, tone="#6B7280", width=1.8, dashed=True):
    d = ' stroke-dasharray="6 5"' if dashed else ''
    f.parts.append(f'<path d="M{x1},{y1} L{x2},{y2}" fill="none" stroke="{tone}" '
                   f'stroke-width="{width}"{d}/>')
    f._touch(max(y1, y2))


def _card(f, x, y, w, h, title, zh, body, body_zh, tone="blue"):
    f.box(x, y, w, title, zh, None, tone=tone, h=52, size=13)
    yy = y + 52 + 24
    for ln in wrap(body, w - 40, 12):
        f.free(x + 20, yy, ln, size=12, tone="gray", anchor="start")
        yy += 17
    yy += 2
    for ln in wrap(body_zh, w - 40, 11, zh=True):
        f.free(x + 20, yy, ln, size=11, tone="gray", anchor="start")
        yy += 15
    f._touch(yy)
    return yy


# --------------------------------------------------------------- figures

def v_model():
    """The V: down the left leg, up the right; each artefact verified by a test."""
    f = Fig(W)
    f.arrow(110, 90, 480, 420, tone="blue", width=3)
    f.arrow(480, 420, 850, 90, tone="green", width=3)

    left = [("Requirements", "需求", "what the user needs"),
            ("Design", "设计", "architecture, components"),
            ("Coding", "编码", "units implemented")]
    right = [("Acceptance test", "验收测试", "against the requirements"),
             ("System test", "系统测试", "the product as a whole"),
             ("Unit & integration", "单元与集成测试", "each unit, then the seams")]

    bw, bh = 168, 62
    ts = [0.15, 0.45, 0.72]
    for t, (en, zh, sub) in zip(ts, left):
        f.box(110 + t * 370 - bw / 2, 90 + t * 330 - bh / 2, bw, en, zh, sub, tone="blue", h=bh, size=12)
    for t, (en, zh, sub) in zip(ts, right):
        f.box(850 - t * 370 - bw / 2, 90 + t * 330 - bh / 2, bw, en, zh, sub, tone="green", h=bh, size=12)

    for t in (0.15, 0.45):
        x1 = 110 + t * 370 + bw / 2
        x2 = 850 - t * 370 - bw / 2
        y = 90 + t * 330
        f.arrow(x1, y, x2, y, tone="gray", dashed=True, width=1.8)
        f.free((x1 + x2) / 2, y - 8, "verifies  验证", size=11.5, tone="gray", italic=True)

    f.parts.append(f'<text x="34" y="255" text-anchor="middle" font-size="12.5" fill="#2563EB" '
                   f'font-weight="bold" transform="rotate(-90 34 255)">development · 开发</text>')
    f.parts.append(f'<text x="926" y="255" text-anchor="middle" font-size="12.5" fill="#2E7D46" '
                   f'font-weight="bold" transform="rotate(-90 926 255)">testing · 测试</text>')
    f._touch(280)

    f.free(480, 452, "the vertex: construction ends, verification begins",
           "顶点：构建结束，验证开始", size=12.5, tone="gray", italic=True)
    f.caption(480, 496, "The V pairs every artefact on the left with the test written to verify it,")
    f.free(480, 512, "so test design starts at requirements time.",
           "V 模型把左边每个制品与验证它的测试配对，所以测试设计从需求阶段就开始。")
    f.credit(480, 556)
    return f.save("w02-v-model")


def waterfall():
    """Five sequential phases, and the feedback that only arrives at the end."""
    f = Fig(W)
    phases = [("Communication", "沟通", "requirements"),
              ("Planning", "策划", "project plan"),
              ("Modeling", "建模", "analysis & design"),
              ("Construction", "构建", "code & test"),
              ("Deployment", "部署", "delivery & support")]
    bw, gap, x0, y, h = 170, 17, 21, 104, 66
    centers = []
    for i, (en, zh, sub) in enumerate(phases):
        x = x0 + i * (bw + gap)
        f.box(x, y, bw, en, zh, sub, tone="blue", h=h, size=12)
        centers.append(x + bw / 2)
        if i:
            f.arrow(x0 + (i - 1) * (bw + gap) + bw + 2, y + h / 2, x - 4, y + h / 2,
                    tone="gray", width=2)
    yb = y + h + 56
    _seg(f, centers[-1], y + h, centers[-1], yb, "#DC2626")
    _seg(f, centers[0], y + h, centers[0], yb, "#DC2626")
    f.arrow(centers[-1], yb, centers[0] + 2, yb, tone="red", dashed=True)
    f.free(480, yb - 10, "feedback arrives only here — 反馈只在最后出现", size=11.5, tone="red")

    f.free(480, yb + 46, "each phase completes before the next begins", "每个阶段完成后才进入下一阶段",
           size=12.5, tone="gray", italic=True)
    f.caption(480, yb + 86, "Simple and documentation-driven, but uncertainty has nowhere to go:")
    f.free(480, yb + 102, "defects and wrong requirements surface when they are dearest to fix.",
           "简单、文档驱动；但不确定性无处安放——缺陷与需求错误在最贵的时候才暴露。")
    f.credit(480, yb + 146)
    return f.save("w02-waterfall")


def incremental():
    """Three increments, each running the five activities; core features first.

    The "what this increment ships" note goes UNDER its row, left-aligned. It
    was on the right first, where it ran straight over the Deploy chip: five
    chips already fill the width, so there is no right margin to put it in.
    """
    f = Fig(W)
    rows = [("Increment 1", "增量 1", "core features · 核心功能",
             "ships working software: core monitoring", "交付可用软件：核心监测"),
            ("Increment 2", "增量 2", "+ more features · 更多功能",
             "ships working software: + alerts", "交付可用软件：+ 告警"),
            ("Increment 3", "增量 3", "full product · 完整产品",
             "ships working software: full product", "交付可用软件：完整产品")]
    steps = [("Comm", "沟通"), ("Plan", "策划"), ("Model", "建模"), ("Build", "构建"), ("Deploy", "部署")]
    labels = ["talk", "estimate", "design", "code & test", "deliver"]

    cx0, cw, cgap = 250, 128, 9
    for r, (en, zh, sub, ship, ship_zh) in enumerate(rows):
        y = 88 + r * 128
        f.box(20, y, 210, en, zh, sub, tone="teal", h=64, size=12.5)
        for c, (sen, szh) in enumerate(steps):
            f.box(cx0 + c * (cw + cgap), y, cw, sen, szh, labels[c], tone="blue", h=64, size=11.5)
        f.free(20, y + 92, ship, size=11.5, tone="gray", anchor="start")
        f.free(20, y + 108, ship_zh, size=11, tone="gray", anchor="start")

    f.free(480, 500, "the whole product is planned up-front — only its delivery is sliced",
           "最终产品一次规划完成，只是交付被切块", size=12.5, tone="gray", italic=True)
    f.caption(480, 544, "Each increment carries its own plan, design, build and demo, so working")
    f.free(480, 560, "software exists from the end of the first increment.",
           "每个增量都有自己的策划、设计、构建与演示，所以第一个增量结束就有可用软件。")
    f.credit(480, 604)
    return f.save("w02-incremental")


def spiral():
    """Boehm's risk-driven spiral: each loop is one iteration, radius = cost."""
    f = Fig(W)
    cx, cy = 245, 258
    pts = []
    for i in range(0, 719, 3):
        th = math.radians(i - 90)
        r = 16 + 152 * (i / 718)
        pts.append(f"{cx + r * math.cos(th):.1f},{cy + r * math.sin(th):.1f}")
    f.parts.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="#2563EB" stroke-width="2.6"/>')
    f.parts.append(f'<circle cx="{cx}" cy="{cy}" r="4" fill="#2563EB"/>')
    for ang, num in ((-45, "1"), (45, "2"), (135, "3"), (-135, "4")):
        t = math.radians(ang)
        x, y = cx + 176 * math.cos(t), cy + 176 * math.sin(t) + 5
        f.parts.append(f'<circle cx="{x:.0f}" cy="{y - 4:.0f}" r="13" fill="#DBEAFE" stroke="#2563EB" stroke-width="1.5"/>')
        f.parts.append(f'<text x="{x:.0f}" y="{y:.0f}" text-anchor="middle" font-size="12.5" '
                       f'fill="#2563EB" font-weight="bold">{num}</text>')
    f.free(cx, cy + 208, "each loop = one iteration", "每圈 = 一轮迭代", size=12, tone="gray", italic=True)
    f._touch(cy + 230)

    items = [("1", "Determine objectives, alternatives & constraints", "确定目标、备选方案与约束"),
             ("2", "Evaluate alternatives, identify & resolve risks", "评估备选方案，识别并解决风险"),
             ("3", "Develop & verify the next-level product", "开发并验证下一级产品"),
             ("4", "Plan the next iteration", "计划下一轮迭代")]
    yy = 96
    for num, en, zh in items:
        f.parts.append(f'<circle cx="510" cy="{yy - 4}" r="13" fill="#DBEAFE" stroke="#2563EB" stroke-width="1.5"/>')
        f.parts.append(f'<text x="510" y="{yy}" text-anchor="middle" font-size="12.5" fill="#2563EB" '
                       f'font-weight="bold">{num}</text>')
        x = 536
        for ln in wrap(en, 400, 12.5):
            f.free(x, yy, ln, size=12.5, tone="ink", anchor="start")
            yy += 17
        for ln in wrap(zh, 400, 11.5, zh=True):
            f.free(x, yy, ln, size=11.5, tone="gray", anchor="start")
            yy += 15
        yy += 30
    f._touch(yy)
    f.free(500, 300, "the growing radius ≈ cumulative cost", "半径随累积成本增大",
           size=12, tone="gray", anchor="start", italic=True)

    f.caption(480, yy + 26, "Risk is addressed explicitly and early, which is why the spiral suits large")
    f.free(480, yy + 42, "or high-risk work — and why its ceremony is hard to justify on a small one.",
           "风险被显式且及早处理，所以螺旋适合大型或高风险项目——也正因如此，小型项目负担不起它的仪式。")
    f.credit(480, yy + 86)
    return f.save("w02-spiral")


def process_vocabulary():
    """Three levels of the same idea: model, activity, frame."""
    f = Fig(W)
    f.box(20, 84, 920, "Process model", "过程模型",
          "the ordered arrangement of the five activities for one project", tone="teal", h=84, size=14)
    f.free(40, 148, "waterfall · V model · incremental · prototyping · spiral · agile", size=11.5,
           tone="gray", anchor="start")

    f.box(20, 190, 920, "Framework activity", "框架活动",
          "communication · planning · modeling · construction · deployment", tone="blue", h=84, size=14)
    f.free(40, 254, "the five things every project does, whatever the model", "无论用什么模型，每个项目都要做的五件事",
           size=11.5, tone="gray", anchor="start")

    f.box(20, 296, 920, "Process frame", "过程帧",
          "one activity, described precisely enough to be run and checked", tone="violet", h=84, size=14)

    cells = [("Entry criteria", "入口条件", "what must be true before the work starts", "开始前必须满足的条件"),
             ("Task set", "任务集", "the work itself, scaled to fit the activity", "要做的工作，按活动规模伸缩"),
             ("Milestones", "里程碑", "measurable checkpoints along the way", "路上可度量的检查点"),
             ("Exit criteria", "出口条件", "what must be true to call the activity done", "判定活动完成的条件")]
    cw, cg = 218, 16
    for i, (en, zh, sub, subzh) in enumerate(cells):
        x = 20 + i * (cw + cg)
        f.box(x, 396, cw, en, zh, sub, tone="gray", h=84, size=12)
        f.free(x + cw / 2, 470, subzh, size=11, tone="gray")

    f.free(480, 524, "\u201cAre we done with design?\u201d really means \u201chave we met the exit criteria?\u201d",
           "“设计做完了吗？”其实是在问“出口条件满足了吗？”", size=12.5, tone="gray", italic=True)
    f.caption(480, 566, "Same idea at three scales: the model orders the activities, each activity is a")
    f.free(480, 582, "frame, and a frame is only usable when its criteria can be checked.",
           "同一个概念在三个尺度上：模型排列活动，每个活动是一个过程帧，而过程帧只有在条件可检验时才有用。")
    f.credit(480, 626)
    return f.save("w02-process-vocabulary")


def prototyping():
    """The listen-build-test-revise loop, and the two roads out of it."""
    f = Fig(W)
    steps = [("Listen", "倾听", "collect a wish, not a spec", "收集愿望，而不是规格"),
             ("Build", "构建", "a mock-up in days, not months", "用几天而不是几个月做原型"),
             ("Test", "试用", "watch what they do, do not ask", "看用户怎么做，而不是问"),
             ("Revise", "修改", "the requirement moves as you build", "边做边改，需求随之移动")]
    bw, gap, x0, y, h = 215, 20, 20, 96, 84
    centers = []
    for i, (en, zh, sub, subzh) in enumerate(steps):
        x = x0 + i * (bw + gap)
        f.box(x, y, bw, en, zh, sub, tone="amber", h=h, size=13)
        f.free(x + bw / 2, y + 70, subzh, size=11, tone="gray")
        centers.append(x + bw / 2)
        if i:
            f.arrow(x0 + (i - 1) * (bw + gap) + bw + 2, y + h / 2, x - 4, y + h / 2, tone="gray", width=2)
    yb = y + h + 44
    _seg(f, centers[-1], y + h, centers[-1], yb, "#D97706")
    _seg(f, centers[0], y + h, centers[0], yb, "#D97706")
    f.arrow(centers[-1], yb, centers[0] + 2, yb, tone="amber", dashed=True)
    f.free(480, yb - 8, "repeat until the requirements become clear  循环直到需求清晰", size=11.5, tone="amber")

    f.free(480, yb + 42, "then the team chooses one of two roads", "然后团队在两条路中选一条",
           size=12.5, tone="gray", italic=True)
    _card(f, 20, yb + 62, 440, 52, "Throwaway prototyping", "抛弃型原型",
          "The mock-up taught you what to build. Discard it and build the real system properly.",
          "原型帮你搞清要做什么。丢掉它，认真做真正的系统。", tone="green")
    _card(f, 500, yb + 62, 440, 52, "Evolutionary prototyping", "演化型原型",
          "The prototype is promoted to the product, defensible only if it was built to be maintained.",
          "原型直接升级为产品；只有当初就按可维护做的原型才站得住脚。", tone="red")

    f.caption(480, yb + 248, "The classic failure is not the prototype. It is shipping it.")
    f.free(480, yb + 264, "原型本身从来不是灾难，把它当成产品发出去才是。", size=13, tone="gray", italic=True)
    f.credit(480, yb + 308)
    return f.save("w02-prototyping")


def model_selection():
    """Five models against the question that actually decides: can we pay for it?"""
    f = Fig(W)
    cols = [("Model", "模型", 150), ("Choose it when", "什么时候选", 300),
            ("Its real cost", "真实代价", 280), ("For CareLink", "CareLink 的选择", 190)]
    rows = [("Waterfall", "瀑布",
             "requirements are stable and fixed by contract", "需求稳定、由合同固定",
             "feedback arrives at the end, when it is dearest", "反馈在最后才到，代价最高", "no feedback before week 16", "16 周前没有反馈"),
            ("V model", "V 模型",
             "test discipline must start at requirements time", "测试纪律必须从需求阶段开始",
             "still a single pass, so late change stays expensive", "仍是单趟，后期变更依然昂贵", "the same rigidity remains", "刚性不变"),
            ("Incremental", "增量",
             "the whole is known and delivery can be sliced", "整体已知，交付可以切块",
             "each increment needs its own plan and demo", "每个增量都要自己的计划与演示", "the chosen backbone", "选定的主干"),
            ("Prototyping", "原型",
             "the requirements are vague or contested", "需求模糊或有争议",
             "a week-old mock-up gets pressure to ship", "放了一周的原型会被逼着上线", "a short loop inside increment 1", "放在增量 1 里的短循环"),
            ("Spiral", "螺旋",
             "large, high-risk work with a disciplined team", "大型高风险、团队有纪律",
             "quarterly risk reviews cost more than they save", "季度风险评审的成本高于收益", "ceremony unmatched to risk", "仪式与风险不匹配")]
    x0, y = 20, 84
    hh = 34
    for i, (en, zh, cw) in enumerate(cols):
        x = x0 + sum(c[2] for c in cols[:i])
        f.parts.append(f'<rect x="{x}" y="{y}" width="{cw}" height="{hh}" fill="#E5E7EB" stroke="#6B7280" stroke-width="1.2"/>')
        f.parts.append(f'<text x="{x + 12}" y="{y + 15}" font-size="12" fill="#1F2937" font-weight="bold">{en}</text>')
        f.parts.append(f'<text x="{x + 12}" y="{y + 29}" font-size="11" fill="#6B7280" font-family="Hiragino Sans GB">{zh}</text>')
    yy = y + hh
    rh = 82
    for r, row in enumerate(rows):
        x = x0
        tone = "green" if r == 2 else "gray"
        for c, cw in enumerate([c[2] for c in cols]):
            f.wrapbox(x, yy, cw, rh, row[2 * c], row[2 * c + 1], tone=tone, size=11.5)
            x += cw
        yy += rh
    f._touch(yy)

    f.caption(480, yy + 34, "The right model is the one whose costs this project can actually afford.")
    f.free(480, yy + 50, "对的模型，是这个项目真正付得起代价的那个。", size=13, tone="gray", italic=True)
    f.credit(480, yy + 94)
    return f.save("w02-model-selection")


def one_project_two_models():
    """Same requirements, same team, same sixteen weeks — the model decides
    when reality gets to talk back."""
    f = Fig(W)
    x0, x1 = 70, 930
    weeks = [1, 4, 8, 12, 16]
    def wx(wk):
        return x0 + (wk - 1) / 15 * (x1 - x0)

    f.free(x0 - 34, 96, "W1", size=11.5, tone="gray")
    for wk in weeks[1:]:
        f.free(wx(wk), 96, f"W{wk}", size=11.5, tone="gray")
        _seg(f, wx(wk), 106, wx(wk), 372, "#E5E7EB", width=1, dashed=False)

    f.free(20, 138, "Waterfall", "瀑布", size=12.5, tone="blue", anchor="start", bold=True)
    phases = [("Requirements", "需求", 1, 4), ("Design", "设计", 4, 7),
              ("Construction", "构建", 7, 12), ("Test and acceptance", "测试与验收", 12, 16)]
    for i, (en, zh, a, b) in enumerate(phases):
        x, w = wx(a), wx(b) - wx(a)
        f.parts.append(f'<rect x="{x}" y="122" width="{w}" height="46" rx="6" fill="#DBEAFE" stroke="#2563EB" stroke-width="2"/>')
        f.parts.append(f'<text x="{x + w / 2}" y="141" text-anchor="middle" font-size="11.5" fill="#1F2937" font-weight="bold">{en}</text>')
        f.parts.append(f'<text x="{x + w / 2}" y="156" text-anchor="middle" font-size="11" fill="#6B7280" font-family="Hiragino Sans GB">{zh}</text>')
    f.arrow(wx(7), 190, wx(15), 190, tone="red", dashed=True)
    f.free(wx(11), 204, "first user feedback arrives here — expensive to act on",
           "用户第一次看到东西在这里——此时改动已经很贵", size=11.5, tone="red")

    f.free(20, 278, "Incremental", "增量", size=12.5, tone="teal", anchor="start", bold=True)
    inc = [("Increment 1", "增量 1", "monitor", "监测", 1, 4), ("Increment 2", "增量 2", "alert", "告警", 5, 8),
           ("Increment 3", "增量 3", "escalate", "升级", 9, 12), ("Increment 4", "增量 4", "harden", "加固", 13, 16)]
    for en, zh, ship, shipzh, a, b in inc:
        x, w = wx(a), wx(b) - wx(a)
        f.parts.append(f'<rect x="{x}" y="262" width="{w}" height="46" rx="6" fill="#CCFBF1" stroke="#0D9488" stroke-width="2"/>')
        f.parts.append(f'<text x="{x + w / 2}" y="281" text-anchor="middle" font-size="11.5" fill="#1F2937" font-weight="bold">{en}</text>')
        f.parts.append(f'<text x="{x + w / 2}" y="296" text-anchor="middle" font-size="11" fill="#6B7280" font-family="Hiragino Sans GB">{zh} · {ship} {shipzh}</text>')
        f.arrow(x + w / 2, 330, x + w / 2, 348, tone="green", width=1.8)
    f.free(480, 366, "working software every four weeks — feedback from week 4",
           "每四周就有可用软件——从第 4 周起就有反馈", size=11.5, tone="green")

    f.caption(480, 418, "Same requirements, same team, same sixteen weeks.")
    f.free(480, 434, "The model decides when reality is allowed to talk back.",
           "需求相同、团队相同、周数相同。模型决定的，是现实什么时候被允许说话。", size=13, tone="gray", italic=True)
    f.credit(480, 478)
    return f.save("w02-one-project-two-models")


def ai_model_selection():
    """The AI Companion loop: you state the context, AI drafts, you cost the
    ceremony, and the artefact is a choice you can defend."""
    f = Fig(W)
    steps = [("HUMAN", "你来", "You state the context",
              "requirement clarity, volatility, team size, risk level",
              "需求清晰度、变动性、团队规模、风险高低", "blue"),
             ("AI", "AI", "AI drafts candidates",
              "a comparison table and a recommendation, with [ASSUMPTION] flags",
              "一张对比表和一条建议，并标出 [假设]", "violet"),
             ("CHECK", "你来核对", "You cost the ceremony",
              "does the model exist, and can this team pay for its rituals",
              "这个模型真的存在吗？团队付得起它的仪式吗", "amber"),
             ("ARTEFACT", "产出", "A choice you can defend",
              "the model, the reason, and what would change your mind",
              "选定的模型、理由，以及什么会让你改主意", "green")]
    # 4 x 212 + 3 x 24 = 920: the row is sized to the canvas, because 4 x 222
    # ran the last column 20 units off the right edge.
    bw, gap, x0, y = 212, 24, 20, 96
    for i, (en, zh, ttl, body, bodyzh, tone) in enumerate(steps):
        x = x0 + i * (bw + gap)
        f.box(x, y, bw, en, zh, None, tone=tone, h=52, size=13)
        yy = y + 74
        for ln in wrap(ttl, bw - 20, 12.5):
            f.free(x + bw / 2, yy, ln, size=12.5, tone="ink", bold=True)
            yy += 17
        yy += 3
        for ln in wrap(body, bw - 20, 11.5):
            f.free(x + bw / 2, yy, ln, size=11.5, tone="gray")
            yy += 15
        for ln in wrap(bodyzh, bw - 20, 11, zh=True):
            f.free(x + bw / 2, yy, ln, size=11, tone="gray")
            yy += 14
        f._touch(yy)
        if i:
            f.arrow(x0 + (i - 1) * (bw + gap) + bw + 3, y + 26, x - 5, y + 26, tone="gray", width=2)

    yb = 300
    f.parts.append(f'<rect x="20" y="{yb}" width="920" height="96" rx="8" fill="#FEE2E2" stroke="#DC2626" stroke-width="2"/>')
    f.free(44, yb + 28, "What the AI says when you do not cost the ceremony:", size=12.5, tone="red", anchor="start", bold=True)
    f.free(44, yb + 50, "\u201cUse spiral — it is the most thorough (for a six-person course project)\u201d",
           size=13, tone="ink", anchor="start", italic=True)
    f.free(44, yb + 72, "Thorough is not a reason. Six students cannot pay for quarterly risk reviews.",
           "“彻底”不是理由：六个学生付不起季度风险评审的成本。", size=12, tone="red", anchor="start")
    f._touch(yb + 96)

    f.caption(480, yb + 136, "Match the model to the risk profile, and write down the reason.")
    f.free(480, yb + 152, "让模型匹配风险画像，并把理由写下来。", size=13, tone="gray", italic=True)
    f.credit(480, yb + 196)
    return f.save("w02-ai-model-selection")


if __name__ == "__main__":
    for fn in (v_model, waterfall, incremental, spiral, process_vocabulary, prototyping,
               model_selection, one_project_two_models, ai_model_selection):
        fn()
