<div align="center">

# 🎓 Software Engineering I · 软件工程 I

**A bilingual, project-driven open course for international students**
**面向国际学生的双语 · 项目驱动开源课程**

[![Course](https://img.shields.io/badge/course-16%20weeks%20%7C%2032%20hours-4E29FF)]()
[![Language](https://img.shields.io/badge/language-English%20%2B%20中文注释-2EA043)]()
[![Progress](https://img.shields.io/badge/slides%20released-4%2F16-blue)]()
[![Update](https://img.shields.io/badge/update-weekly-FF6905?labelColor=555)]()
[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/license-CC%20BY--NC--SA%204.0-lightgrey.svg)](./LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-8957E5.svg)](https://github.com/klausren/software-engineering-course/pulls)

[Course Overview 课程简介](#-course-overview-课程简介) · [Syllabus 教学大纲](#-weekly-syllabus-教学大纲) · [SafeHome Project 项目实践](#-safehome-project-项目实践) · [Adoption 采用登记](#-course-adoption-课程采用登记) · [Author 作者](#-author-作者)

</div>

---

A complete, bilingual (English-primary with Chinese annotations) open course for **Software Engineering I** — a 16-week, 32-hour undergraduate course for international students, taught with a project-driven approach built around the **SafeHome** home-security system case.

面向国际学生的《软件工程 I》开源课程：16 周 / 32 学时，英文主讲、中文注释，以 SafeHome 智能家居安全系统项目贯穿全学期。

> **Course status 课程状态**：Teaching in progress (Semester 2026-2027-1). Slides are rebuilt weekly and published progressively — **W01–W04 released, W05–W16 in production.**
> 课程进行中（2026-2027-1 学期）。课件按周重制并陆续发布——**已发布 W01–W04，W05–W16 制作中。**

> 📚 **Companion textbook 配套教材**：An open English textbook covering the full 64-hour SE I + SE II sequence (running case: CareLink) is being written alongside this course — [klausren/oose-textbook](https://github.com/klausren/oose-textbook).
> 配套英文教材（覆盖 SE I + II 共 64 学时，贯穿案例 CareLink）正在随课程同步编写——[klausren/oose-textbook](https://github.com/klausren/oose-textbook)。

## 📖 Course Overview 课程简介

| Item 项目 | Detail 内容 |
|---|---|
| Course 课程 | Software Engineering I 软件工程 I |
| Credits / Hours 学分 / 学时 | 2 credits / 32 hours (Theory 24 + Practice 8) |
| Duration 周期 | 16 weeks, 2 hours per week |
| Language 语言 | English with Chinese annotations 英文主讲、中文注释 |
| Textbook 参考教材 | R. S. Pressman, *Software Engineering: A Practitioner's Approach* (9th ed.) |
| Project 项目 | SafeHome — a home security system built by student teams all semester |

**Highlights 教学特色**

- 🔧 **Project-driven 项目驱动** — One semester-long team project (SafeHome); every modeling technique learned in class is immediately applied to the project. 每周所学建模技术即刻应用于团队项目。
- 🌏 **Bilingual 双语** — English-primary slides with concise Chinese annotations to help international students master technical terms. 英文主讲，中文注释辅助术语理解。
- ✍️ **Hands-on 每课练习** — Each week includes 2–3 in-class exercises with answers. 每周 2–3 个课堂练习（含答案）。
- 🎨 **Original figures 原创图表** — All diagrams are original vector drawings (no copyrighted textbook images), so the materials are safe to remix. 全部图表为原创矢量图，不含教材原图。

## 📅 Weekly Syllabus 教学大纲

| Week 周 | Topic 主题 | Slides 课件 |
|:---:|---|---|
| 01 | Introduction to Software Engineering 软件工程导论 | ✅ [W01](01-slides/W01-Introduction-to-Software-Engineering.pptx) · 44 pages |
| 02 | Software Process Models 软件开发过程模型 | ✅ [W02](01-slides/W02-Software-Process-Models.pptx) · 41 pages |
| 03 | Agile Development & Scrum 敏捷开发与 Scrum | ✅ [W03](01-slides/W03-Agile-Development-and-Scrum.pptx) · 42 pages |
| 04 | Requirements Inception & Elicitation 需求启始与获取 | ✅ [W04](01-slides/W04-Requirements-Inception-and-Elicitation.pptx) · 43 pages |
| 05 | Requirements Gathering & Practice I 需求收集实践 | 🚧 in production 制作中 |
| 06 | Requirements Modeling: Business Process 业务流程建模 | 🚧 in production 制作中 |
| 07 | Requirements Modeling: Use Case 用例建模 | 🚧 in production 制作中 |
| 08 | Requirements Modeling: Use Case Specification 用例描述 | 🚧 in production 制作中 |
| 09 | Requirements Modeling: Domain Model 领域模型 | 🚧 in production 制作中 |
| 10 | Domain Model (Cont.) 领域模型实践 | 🚧 in production 制作中 |
| 11 | Behavior-Based Modeling 行为建模 | 🚧 in production 制作中 |
| 12 | Behavior-Based Modeling (Cont.) 行为建模实践 | 🚧 in production 制作中 |
| 13 | Class-Based Modeling 类建模 | 🚧 in production 制作中 |
| 14 | Class-Based Modeling (Cont.) 类建模实践 | 🚧 in production 制作中 |
| 15 | User Interface Design 用户界面设计 | 🚧 in production 制作中 |
| 16 | Architectural Design & Final Defense 架构设计与项目验收答辩 | 🚧 in production 制作中 |

## 🔐 SafeHome Project 项目实践

Students work in **5 teams of 5–6** throughout the semester. Requirements and review follow a **two-track model** 双轨需求与评审机制：

| Track 轨道 | Teams 组数 | Requirements 需求来源 | Review 评审 |
|---|:---:|---|---|
| **Track A — Client-driven 甲方制** | 3 | Provided by **Client A** as the client 由甲方 Client A 提出需求 | Dual review: Client A (domain expert) + instructor (technical expert) 甲方（领域专家）与教师（技术专家）共同评审 |
| **Track B — Instructor-driven 教师制** | 2 | Provided by the instructor 由教师提供需求 | Sole review by the instructor 教师唯一评审 |

**Review points 评审时点**：requirements gathering (Week 4–5) → modeling phase reviews in class (Week 6–14) → final acceptance & defense (Week 16).

See [03-project/SafeHome-项目说明.md](03-project/SafeHome-项目说明.md) for details. 详见项目说明。

## 📂 Repository Structure 目录结构

```
.
├── README.md                     # This file 本说明
├── LICENSE                       # CC BY-NC-SA 4.0
├── 01-slides/                    # Weekly lecture slides (rebuild version) 每周课件（重制版）
│   ├── W01-Introduction-to-Software-Engineering.pptx
│   ├── W02-Software-Process-Models.pptx
│   ├── W03-Agile-Development-and-Scrum.pptx
│   ├── W04-Requirements-Inception-and-Elicitation.pptx
│   └── ...                       # W05–W16 coming weekly 每周更新
├── 02-teaching-plans/            # Teaching plans & course standard (sanitized) 教案与课标（脱敏版，陆续补充）
├── 03-project/                   # SafeHome team project description 项目说明
└── assets/                       # Images used in README 说明用图片
```

## 🚀 How to Use 使用说明

- **For teachers 教师** — You are free to reuse, adapt, and translate the materials for your own classes (non-commercial). 可自由复用、改编、翻译用于教学（非商业）。
- **For students 学生** — Follow the weekly slides; in-class exercises include answers for self-check. 随周学习课件，练习含答案可自查。
- **For self-learners 自学者** — Each deck is self-contained: concepts → diagrams → exercises. Recommended pace: one deck per week. 每份课件自成体系，建议每周一份。

## 🏫 Course Adoption 课程采用登记

If you use these slides — in whole or in part — in your own course, please **register your adoption**. A public adoption record sustains the project, helps other teachers find classroom-proven materials, and builds evidence for the future print edition.
如果您在本校课程中使用（全部或部分）本课件，欢迎登记。公开的采用记录既能帮助项目持续迭代，也能让更多同行找到经过课堂验证的素材，同时为将来的出版积累依据。

**How to register 如何登记**：open an issue with the **Course adoption** template — takes about one minute. 提交一个「课程采用登记」issue（已有现成模板，一分钟搞定）：
👉 [登记 / Register here](https://github.com/klausren/software-engineering-course/issues/new?template=course-adoption.md)

**Adopters 采用记录**

| Institution 学校 | Course 课程 | Term 学期 | Scope 使用范围 |
|---|---|---|---|
| Dalian Neusoft University of Information 大连东软信息学院 | Software Engineering I 软件工程 I | 2026–2027–1 | Full course 全部课件 |
| *Yours? 你的课程？* | | | |

## 💬 Feedback & Contribution 反馈与贡献

Found a typo, a broken link, or a factual error? Open an [issue](https://github.com/klausren/software-engineering-course/issues) or submit a pull request — corrections from practitioners and educators are especially welcome.

发现错别字、失效链接或内容错误？欢迎提 [issue](https://github.com/klausren/software-engineering-course/issues) 或直接发 Pull Request，特别欢迎一线教师与从业者的修正。

## 📄 License 许可证

This work is licensed under the **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)**.

本课程资料采用 **知识共享 署名—非商业性使用—相同方式共享 4.0 国际** 许可协议。

[![CC BY-NC-SA 4.0](https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

You are free to share and adapt the material for **non-commercial** purposes with attribution, provided you distribute your contributions under the same license.

## 👤 Author 作者

**Ren Zheng 任政** — Software Engineering Lecturer 软件工程专业教师

- 🎓 Teaching: bilingual (EN/CN) software engineering courses for international students 国际学生双语教学
- 💻 GitHub: [klausren](https://github.com/klausren)
- 📕 Xiaohongshu 小红书: **改卷子的任老师** (ID: `63808230340`) — teaching notes & study tips on Software Engineering. 分享软件工程教学笔记与学习干货，欢迎关注！

<img src="assets/xiaohongshu-card.jpg" alt="改卷子的任老师 Xiaohongshu" width="320"/>

---

<div align="center">

**⭐ Star this repo to follow the course · 点个 Star 追更本课程 ⭐**

*Built week by week, published every week. 逐周制作，每周发布。*

</div>
