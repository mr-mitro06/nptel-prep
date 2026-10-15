# NPTEL Prep — Interactive Examination Preparation Platform

An interactive, distraction-free, topic-wise MCQ study and revision platform built for students preparing for the **NPTEL Software Testing Examination** (Prof. Meenakshi D'Souza, IIIT Bangalore / Ammann & Offutt curriculum).

The platform transforms 20 comprehensive lecture slide PDFs into a structured question bank of **400 high-yield, mathematically rigorous practice MCQs**, complete with detailed concept breakdowns, formula citations, and exact slide references.

---

## 🌟 Key Features

* **400 Grounded MCQs**: Exactly 20 topic-specific, lecture-grounded practice questions per lecture module across all 20 PDF decks.
* **Instant Explanations & Citations**: Every question includes a four-option format, verified single correct answer, in-depth explanation of why the answer is correct, and citation to the source lecture PDF and slide numbers.
* **Practice Mode**: Test your knowledge one question at a time with instant feedback, answer verification, bookmarking ("Mark for Review"), and a visual question palette.
* **Study Mode**: Accelerated flashcard-style learning mode for rapid revision of question rationales and concept analysis.
* **Simulated Mock Examination**: Full exam simulation with configurable question count (10, 20, 30, 50), optional countdown timer, randomized questions, answer masking until submission, comprehensive score breakdown, and question-by-question review.
* **Weak Areas & Mistake Tracker**: Automatically tracks questions answered incorrectly across all practice and mock sessions. Allows direct re-testing, clearing resolved questions once mastered.
* **Quick Revision Cheat Sheets**: Structured topic-by-topic summary notes containing essential definitions, key formulas/metrics, concept comparisons, common misconceptions, and high-yield exam facts with instant keyword search.
* **100% Offline & Private**: Zero server dependencies. Runs directly in any modern browser via `file://` or static web servers. All study progress and test histories persist securely in `localStorage`.
* **Sleek Minimalist Design**: Modern, distraction-free interface with typography tailored for readability, subtle elevations, smooth animations, and a one-click Dark Mode toggle.

---

## 📚 Course Modules & Topic Breakdown

| # | Topic Name | Source PDF | Questions |
|---|------------|------------|:---------:|
| 1 | Input Space Partitioning (ISP) | `ISP-full-slides.pdf` | 20 |
| 2 | Graph Structural Coverage Criteria | `graphs-structural-coverage.pdf` | 20 |
| 3 | Graph Structural Coverage Algorithms | `graphs-structural-coverage-algorithms.pdf` | 20 |
| 4 | Graph Coverage - Data Flow | `graphs-data-flow.pdf` | 20 |
| 5 | Graph Coverage from Source Code | `graphs-source-code.pdf` | 20 |
| 6 | Graph Coverage - Source Code Data Flow | `graphs-source-code-data-flow.pdf` | 20 |
| 7 | Graph Coverage from Specifications | `graphs-specification.pdf` | 20 |
| 8 | Logic Coverage Criteria (ACC, GACC, CACC, RACC) | `logic-coverage-criteria.pdf` | 20 |
| 9 | Logic Coverage Algorithms | `logic-coverage-algorithms.pdf` | 20 |
| 10 | Logic Coverage from Source Code (Part 1) | `logic-source-code1.pdf` | 20 |
| 11 | Logic Coverage from Source Code (Part 2) | `logic-source-code2.pdf` | 20 |
| 12 | Mutation Testing Principles & Practice | `mutation-testing-source-code.pdf` | 20 |
| 13 | Mutation Operators for Source Code | `mutation-operators-source-code.pdf` | 20 |
| 14 | Mutation Testing for Integration | `mutation-for-integration.pdf` | 20 |
| 15 | Regression Testing (Selection & Prioritization) | `regression-testing.pdf` | 20 |
| 16 | Object-Oriented Testing | `OO-testing.pdf` | 20 |
| 17 | Web Applications Testing | `web-apps-testing.pdf` | 20 |
| 18 | Mobile Applications Testing | `mobile-apps-testing.pdf` | 20 |
| 19 | Non-Functional Testing (Performance & Security) | `non-functional-testing.pdf` | 20 |
| 20 | Comprehensive Testing Exercises & Case Studies | `exer-student.pdf` | 20 |
| **Total** | **20 Course Modules** | **20 PDF Files** | **400 MCQs** |

---

## 🚀 Getting Started

### Method 1: Instant Browser Launch (Zero Setup)
Simply double-click `index.html` or open it directly in any modern browser (Chrome, Edge, Firefox, Safari). The application bundles offline data fallbacks (`js/data.js`), functioning immediately without a local server.

### Method 2: Local HTTP Server (Recommended)
You can launch a lightweight local HTTP server using Python:

```bash
# In the repository root:
python -m http.server 8080
```

Open your browser and navigate to:
```
http://localhost:8080/index.html
```

---

## 🛠️ Project Structure

```
nptelex/
├── index.html                   # Main semantic HTML5 single-page application
├── css/
│   └── style.css                # Minimal, modern CSS design system & dark mode
├── js/
│   ├── app.js                   # Application coordinator and routing
│   ├── data.js                  # Bundled offline data fallback
│   ├── mock.js                  # Mock examination controller & timer
│   ├── practice.js              # Practice and Study mode controller
│   ├── progress.js              # LocalStorage persistence & metrics
│   ├── questions.js             # Question bank repository and filters
│   └── revision.js              # Quick revision cheat sheet controller
├── data/
│   ├── topics.json              # Master topic metadata index
│   ├── all_questions.json       # Consolidated question bank (400 MCQs)
│   ├── revision.json            # Topic definitions, formulas & comparisons
│   └── questions/               # Individual topic JSON files
│       ├── isp-full-slides.json
│       ├── graphs-structural-coverage.json
│       └── ... (20 files)
├── scripts/
│   ├── extract_all_pdfs.py      # PDF text extractor via pypdf
│   ├── build_all_data.py        # Question bank assembler & strict validator
│   ├── generate_revision_notes.py # Quick revision compiler
│   ├── generate_js_data.py      # Offline bundle generator
│   └── question_data/           # Modular question bank sources (Parts 1-4)
├── Lecture Materials/           # Original course lecture slide decks
├── README.md                    # Project documentation
├── .gitignore                   # Git exclusion rules
└── LICENSE                      # MIT License
```

---

## 📋 Question Data Schema

Every question in the question bank adheres to this validated schema:

```json
{
  "id": "isp-001",
  "topicId": "isp-full-slides",
  "topicName": "Input Space Partitioning (ISP)",
  "sourcePdf": "ISP-full-slides.pdf",
  "question": "In Input Space Partitioning (ISP), which two fundamental properties must every valid partition of an input domain satisfy?",
  "options": {
    "A": "Minimality and Determinism",
    "B": "Pairwise disjointness and Completeness",
    "C": "Subsumption and Linear independence",
    "D": "Commutativity and Associativity"
  },
  "correctAnswer": "B",
  "explanation": "A partition of set S is defined as a set of subsets {S1, S2, ..., Sn} such that the subsets are mutually pairwise disjoint (Si ∩ Sj = ∅ for i ≠ j) and together cover the entire domain completely (∪ Si = S).",
  "difficulty": "easy",
  "sourcePages": [2, 5]
}
```

---

## 🚢 Publishing to GitHub Pages

To publish the platform to GitHub Pages:

1. **Create a new repository** on GitHub (e.g. `nptel-prep`).
2. **Add remote and push**:
   ```bash
   git remote add origin https://github.com/<your-username>/nptel-prep.git
   git branch -M main
   git push -u origin main
   ```
3. **Enable GitHub Pages**:
   - Go to your repository settings on GitHub (`Settings` → `Pages`).
   - Under **Build and deployment** > **Source**, choose **Deploy from a branch**.
   - Select branch `main` and folder `/ (root)`.
   - Click **Save**.
4. Your site will be live at `https://<your-username>.github.io/nptel-prep/` within minutes!

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
Practice questions are original academic practice questions grounded in NPTEL course slide materials.
