/**
 * NPTEL Prep - Practice & Study Mode Controller
 */

const PracticeController = {
  mode: "practice", // "practice" | "study" | "weak"
  questions: [],
  currentIndex: 0,
  currentTopicId: null,
  filter: "all", // "all" | "unattempted" | "marked" | "incorrect"
  
  // DOM Elements
  elements: {},

  init() {
    this.elements = {
      container: document.getElementById("practice-view"),
      topicBadge: document.getElementById("q-topic-badge"),
      diffBadge: document.getElementById("q-diff-badge"),
      counter: document.getElementById("q-counter"),
      bookmarkBtn: document.getElementById("q-bookmark-btn"),
      text: document.getElementById("q-text"),
      optionsList: document.getElementById("options-list"),
      explanationBox: document.getElementById("q-explanation-box"),
      expText: document.getElementById("q-exp-text"),
      expSource: document.getElementById("q-exp-source"),
      checkBtn: document.getElementById("q-check-btn"),
      prevBtn: document.getElementById("q-prev-btn"),
      nextBtn: document.getElementById("q-next-btn"),
      paletteGrid: document.getElementById("palette-grid"),
      filterSelect: document.getElementById("practice-filter-select")
    };

    this.bindEvents();
  },

  bindEvents() {
    if (this.elements.checkBtn) {
      this.elements.checkBtn.addEventListener("click", () => this.handleCheckAnswer());
    }
    if (this.elements.prevBtn) {
      this.elements.prevBtn.addEventListener("click", () => this.prevQuestion());
    }
    if (this.elements.nextBtn) {
      this.elements.nextBtn.addEventListener("click", () => this.nextQuestion());
    }
    if (this.elements.bookmarkBtn) {
      this.elements.bookmarkBtn.addEventListener("click", () => this.toggleBookmark());
    }
    if (this.elements.filterSelect) {
      this.elements.filterSelect.addEventListener("change", (e) => {
        this.filter = e.target.value;
        this.applyFilter();
      });
    }

    // Keyboard navigation
    window.addEventListener("keydown", (e) => {
      // Only process when practice-view is active
      const practiceView = document.getElementById("practice-view");
      if (!practiceView || !practiceView.classList.contains("active")) return;
      if (e.target.tagName === "INPUT" || e.target.tagName === "SELECT") return;

      const key = e.key.toUpperCase();
      if (["A", "B", "C", "D"].includes(key)) {
        this.selectOption(key);
      } else if (["1", "2", "3", "4"].includes(key)) {
        const mapping = { "1": "A", "2": "B", "3": "C", "4": "D" };
        this.selectOption(mapping[key]);
      } else if (e.key === "ArrowRight") {
        this.nextQuestion();
      } else if (e.key === "ArrowLeft") {
        this.prevQuestion();
      } else if (e.key === "Enter") {
        if (this.isAnswerChecked()) {
          this.nextQuestion();
        } else {
          this.handleCheckAnswer();
        }
      }
    });
  },

  startTopic(topicId, mode = "practice") {
    this.mode = mode;
    this.currentTopicId = topicId;
    this.questions = QuestionsRepo.getQuestionsByTopic(topicId);
    this.currentIndex = 0;
    this.filter = "all";
    if (this.elements.filterSelect) this.elements.filterSelect.value = "all";
    
    this.renderQuestion();
    this.renderPalette();
  },

  startCustomQueue(questions, title = "Custom Practice", mode = "practice") {
    this.mode = mode;
    this.currentTopicId = null;
    this.questions = questions;
    this.currentIndex = 0;
    this.filter = "all";
    if (this.elements.filterSelect) this.elements.filterSelect.value = "all";

    this.renderQuestion();
    this.renderPalette();
  },

  startWeakPractice() {
    const weakIds = ProgressManager.getWeakQuestionIds();
    if (weakIds.length === 0) {
      alert("Great job! You currently have no incorrect questions to retry.");
      return;
    }
    const weakQuestions = QuestionsRepo.getQuestionsByIds(weakIds);
    this.startCustomQueue(weakQuestions, "Weak Areas Practice", "practice");
  },

  getCurrentQuestion() {
    return this.questions[this.currentIndex] || null;
  },

  renderQuestion() {
    const q = this.getCurrentQuestion();
    if (!q) {
      this.renderEmptyState();
      return;
    }

    // Save session state
    ProgressManager.saveLastState({
      view: "practice",
      topicId: this.currentTopicId,
      qid: q.id,
      index: this.currentIndex
    });

    // Top badges
    this.elements.topicBadge.textContent = q.topicName;
    this.elements.diffBadge.textContent = q.difficulty || "medium";
    this.elements.diffBadge.className = `q-diff-badge q-diff-${q.difficulty || "medium"}`;
    this.elements.counter.textContent = `Question ${this.currentIndex + 1} of ${this.questions.length}`;

    // Bookmark
    const isBookmarked = ProgressManager.isBookmarked(q.id);
    this.elements.bookmarkBtn.classList.toggle("active", isBookmarked);
    this.elements.bookmarkBtn.innerHTML = isBookmarked ? 
      `★ Marked for Review` : `☆ Mark for Review`;

    // Question text
    this.elements.text.textContent = q.question;

    // Retrieve saved progress for this question
    const progress = ProgressManager.getProgress()[q.id];
    const hasAnswered = !!progress;

    // Render options
    this.elements.optionsList.innerHTML = "";
    ["A", "B", "C", "D"].forEach(key => {
      const optItem = document.createElement("div");
      optItem.className = "option-item";
      optItem.dataset.key = key;

      optItem.innerHTML = `
        <div class="option-key">${key}</div>
        <div class="option-text">${q.options[key]}</div>
      `;

      // If user already answered in practice, or in study mode where state persists:
      if (hasAnswered) {
        if (key === q.correctAnswer) {
          optItem.classList.add("correct");
        } else if (key === progress.selected && !progress.isCorrect) {
          optItem.classList.add("incorrect");
        }
        if (key === progress.selected) {
          optItem.classList.add("selected");
        }
        optItem.classList.add("disabled");
      } else {
        optItem.addEventListener("click", () => this.selectOption(key));
      }

      this.elements.optionsList.appendChild(optItem);
    });

    // Explanation Box
    if (hasAnswered || this.mode === "study") {
      this.showExplanation(q, hasAnswered ? progress.isCorrect : null);
    } else {
      this.hideExplanation();
    }

    // Buttons state
    this.elements.prevBtn.disabled = this.currentIndex === 0;
    this.elements.nextBtn.disabled = this.currentIndex === this.questions.length - 1;

    if (hasAnswered) {
      this.elements.checkBtn.textContent = "Answer Checked";
      this.elements.checkBtn.disabled = true;
    } else {
      this.elements.checkBtn.textContent = "Check Answer";
      this.elements.checkBtn.disabled = !this.getSelectedOption();
    }

    this.updatePaletteActiveState();
  },

  selectOption(key) {
    const q = this.getCurrentQuestion();
    if (!q) return;

    const progress = ProgressManager.getProgress()[q.id];
    // In practice mode, if already submitted, do not allow re-select until explicitly reset
    if (progress && this.mode === "practice") return;

    // Highlight selected option element
    const items = this.elements.optionsList.querySelectorAll(".option-item");
    items.forEach(item => {
      item.classList.toggle("selected", item.dataset.key === key);
    });

    this.elements.checkBtn.disabled = false;

    // In Study mode, selecting an option automatically triggers immediate evaluation!
    if (this.mode === "study" && !progress) {
      this.handleCheckAnswer(key);
    }
  },

  getSelectedOption() {
    const selected = this.elements.optionsList.querySelector(".option-item.selected");
    return selected ? selected.dataset.key : null;
  },

  isAnswerChecked() {
    const q = this.getCurrentQuestion();
    if (!q) return false;
    const progress = ProgressManager.getProgress()[q.id];
    return !!progress;
  },

  handleCheckAnswer(overrideKey = null) {
    const q = this.getCurrentQuestion();
    if (!q) return;

    const selectedKey = overrideKey || this.getSelectedOption();
    if (!selectedKey) {
      alert("Please select an answer option (A, B, C, or D) first.");
      return;
    }

    const isCorrect = (selectedKey === q.correctAnswer);
    ProgressManager.recordAnswer(q.id, selectedKey, isCorrect, q.topicId);

    // Apply classes to options
    const items = this.elements.optionsList.querySelectorAll(".option-item");
    items.forEach(item => {
      item.classList.add("disabled");
      const k = item.dataset.key;
      if (k === q.correctAnswer) {
        item.classList.add("correct");
      } else if (k === selectedKey && !isCorrect) {
        item.classList.add("incorrect");
      }
    });

    this.showExplanation(q, isCorrect);
    this.elements.checkBtn.textContent = "Answer Checked";
    this.elements.checkBtn.disabled = true;

    this.renderPalette();
  },

  showExplanation(q, isCorrect) {
    this.elements.explanationBox.classList.add("show");
    
    let headerText = "Explanation & Concept Analysis:";
    if (isCorrect === true) {
      headerText = "✓ Correct! Concept Analysis:";
    } else if (isCorrect === false) {
      headerText = "✕ Incorrect. Solution & Concept Analysis:";
    }
    
    const expHeader = this.elements.explanationBox.querySelector(".exp-header");
    if (expHeader) expHeader.textContent = headerText;

    this.elements.expText.textContent = q.explanation;

    let sourceInfo = `Source: ${q.sourcePdf || "Lecture Slides"}`;
    if (q.sourcePages && q.sourcePages.length > 0) {
      sourceInfo += ` (Pages: ${q.sourcePages.join(", ")})`;
    }
    this.elements.expSource.textContent = sourceInfo;
  },

  hideExplanation() {
    this.elements.explanationBox.classList.remove("show");
  },

  prevQuestion() {
    if (this.currentIndex > 0) {
      this.currentIndex--;
      this.renderQuestion();
    }
  },

  nextQuestion() {
    if (this.currentIndex < this.questions.length - 1) {
      this.currentIndex++;
      this.renderQuestion();
    }
  },

  jumpToQuestion(index) {
    if (index >= 0 && index < this.questions.length) {
      this.currentIndex = index;
      this.renderQuestion();
    }
  },

  toggleBookmark() {
    const q = this.getCurrentQuestion();
    if (!q) return;
    const isBookmarked = ProgressManager.toggleBookmark(q.id);
    this.elements.bookmarkBtn.classList.toggle("active", isBookmarked);
    this.elements.bookmarkBtn.innerHTML = isBookmarked ? 
      `★ Marked for Review` : `☆ Mark for Review`;
    this.renderPalette();
  },

  renderPalette() {
    if (!this.elements.paletteGrid) return;
    this.elements.paletteGrid.innerHTML = "";

    const progress = ProgressManager.getProgress();
    const bookmarks = ProgressManager.getBookmarks();

    this.questions.forEach((q, idx) => {
      const btn = document.createElement("button");
      btn.className = "palette-btn";
      btn.textContent = idx + 1;
      btn.title = `Question ${idx + 1}: ${q.question.slice(0, 40)}...`;

      if (idx === this.currentIndex) {
        btn.classList.add("active");
      }

      const qProg = progress[q.id];
      if (qProg) {
        if (qProg.isCorrect) {
          btn.classList.add("answered-correct");
        } else {
          btn.classList.add("answered-incorrect");
        }
      }

      if (bookmarks.includes(q.id)) {
        btn.classList.add("marked");
      }

      btn.addEventListener("click", () => this.jumpToQuestion(idx));
      this.elements.paletteGrid.appendChild(btn);
    });
  },

  updatePaletteActiveState() {
    if (!this.elements.paletteGrid) return;
    const btns = this.elements.paletteGrid.querySelectorAll(".palette-btn");
    btns.forEach((btn, idx) => {
      btn.classList.toggle("active", idx === this.currentIndex);
    });
  },

  renderEmptyState() {
    this.elements.text.textContent = "No questions match your current selection.";
    this.elements.optionsList.innerHTML = "";
    this.hideExplanation();
  }
};

window.PracticeController = PracticeController;
