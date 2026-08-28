# Software Engineering I 软件工程 I

A complete, bilingual (English-primary with Chinese annotations) open course for **Software Engineering I** — a 16-week, 32-hour undergraduate course for international students, taught with a project-driven approach built around the **SafeHome** home-security system case.

面向国际学生的《软件工程 I》开源课程：16 周 / 32 学时，英文主讲、中文注释，以 SafeHome 智能家居安全系统项目贯穿全学期。

> **Course status** 课程状态：Teaching in progress (Semester 2026-2027-1). Slides are rebuilt weekly and published progressively — **W01–W03 released, W04–W16 in production.**
> 课程进行中（2026-2027-1 学期）。课件按周重制并陆续发布——**已发布 W01–W03，W04–W16 制作中。**

---

## Course Overview 课程简介

| Item 项目 | Detail 内容 |
|---|---|
| Course 课程 | Software Engineering I 软件工程 I |
| Credits / Hours 学分 / 学时 | 2 credits / 32 hours (Theory 24 + Practice 8) |
| Duration 周期 | 16 weeks, 2 hours per week |
| Language 语言 | English with Chinese annotations 英文主讲、中文注释 |
| Textbook 参考教材 | R. S. Pressman, *Software Engineering: A Practitioner's Approach* (9th ed.) |
| Project 项目 | SafeHome — a home security system built by student teams all semester |

**Teaching design 教学特色**

- **Project-driven 项目驱动**：one semester-long team project (SafeHome); every modeling technique learned in class is immediately applied to the project. 每周所学建模技术即刻应用于团队项目。
- **Bilingual 双语**：English-primary slides with concise Chinese annotations to help international students master technical terms. 英文主讲，中文注释辅助术语理解。
- **Hands-on 每课练习**：each week includes 2–3 in-class exercises with answers. 每周 2–3 个课堂练习（含答案）。

## Weekly Syllabus 教学大纲

| Week 周 | Topic 主题 | Slides 课件 |
|---|---|---|
| 01 | Introduction to Software Engineering 软件工程导论 | [W01](01-slides/W01-Introduction-to-Software-Engineering.pptx) |
| 02 | Software Process Models 软件开发过程模型 | [W02](01-slides/W02-Software-Process-Models.pptx) |
| 03 | Agile Development & Scrum 敏捷开发与 Scrum | [W03](01-slides/W03-Agile-Development-and-Scrum.pptx) |
| 04 | Requirements Inception & Elicitation 需求启始与获取 | in production 制作中 |
| 05 | Requirements Gathering & Practice I 需求收集实践 | in production 制作中 |
| 06 | Requirements Modeling: Business Process 业务流程建模 | in production 制作中 |
| 07 | Requirements Modeling: Use Case 用例建模 | in production 制作中 |
| 08 | Requirements Modeling: Use Case Specification 用例描述 | in production 制作中 |
| 09 | Requirements Modeling: Domain Model 领域模型 | in production 制作中 |
| 10 | Domain Model (Cont.) 领域模型实践 | in production 制作中 |
| 11 | Behavior-Based Modeling 行为建模 | in production 制作中 |
| 12 | Behavior-Based Modeling (Cont.) 行为建模实践 | in production 制作中 |
| 13 | Class-Based Modeling 类建模 | in production 制作中 |
| 14 | Class-Based Modeling (Cont.) 类建模实践 | in production 制作中 |
| 15 | User Interface Design 用户界面设计 | in production 制作中 |
| 16 | Architectural Design & Final Defense 架构设计与项目验收答辩 | in production 制作中 |

## Repository Structure 目录结构

```
.
├── README.md                     # This file 本说明
├── LICENSE                       # CC BY-NC-SA 4.0
├── 01-slides/                    # Weekly lecture slides (rebuild version) 每周课件（重制版）
│   ├── W01-Introduction-to-Software-Engineering.pptx
│   ├── W02-Software-Process-Models.pptx
│   ├── W03-Agile-Development-and-Scrum.pptx
│   └── ...                       # W04–W16 coming weekly 每周更新
├── 02-teaching-plans/            # Teaching plans & course standard (sanitized) 教案与课标（脱敏版，陆续补充）
└── 03-project/                   # SafeHome team project description & grading rubric 项目说明与评分
```

## SafeHome Project 项目实践

Students work in **5 teams of 5–6** throughout the semester. Requirements and review follow a **two-track model** 双轨需求与评审机制：

| Track 轨道 | Teams 组数 | Requirements 需求来源 | Review 评审 |
|---|---|---|---|
| **Track A — Client-driven 甲方制** | 3 teams | Provided by **Client A** as the client 由甲方 Client A 提出需求 | Dual review: Client A (domain expert) + instructor (technical expert) 甲方（领域专家）与教师（技术专家）共同评审 |
| **Track B — Instructor-driven 教师制** | 2 teams | Provided by the instructor 由教师提供需求 | Sole review by the instructor 教师唯一评审 |

**Review points 评审时点**：requirements gathering (Week 4–5), each modeling phase in class (Week 6–14), final acceptance & defense (Week 16).

See [03-project/SafeHome-项目说明.md](03-project/SafeHome-项目说明.md) for details. 详见项目说明。

## How to Use 使用说明

- **For teachers 教师**：you are free to reuse, adapt, and translate the materials for your own classes (non-commercial). 可自由复用、改编、翻译用于教学（非商业）。
- **For students 学生**：follow the weekly slides; in-class exercises include answers for self-check. 随周学习课件，练习含答案可自查。
- All figures are **original vector drawings** — no copyrighted textbook images are included, so the materials are safe to remix. 全部图表为原创矢量图，不含教材原图，可放心再创作。

## License 许可证

This work is licensed under the **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)**.

本课程资料采用 **知识共享 署名—非商业性使用—相同方式共享 4.0 国际** 许可协议。

[![CC BY-NC-SA 4.0](https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

You are free to share and adapt the material for **non-commercial** purposes with attribution, provided you distribute your contributions under the same license.

## Author 作者

**Ren Zheng 任政** — Software Engineering Lecturer 软件工程专业教师

- Teaching: bilingual (EN/CN) software engineering courses for international students 国际学生双语教学
- GitHub: [klausren](https://github.com/klausren)

---

*Built week by week. Star this repo to follow the course. 逐周更新中，欢迎 Star 关注。*
