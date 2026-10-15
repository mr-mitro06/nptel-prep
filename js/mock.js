/**
 * NPTEL Prep - Mock Examination Controller
 */

const MockController = {
  active: false,
  questions: [],
  currentIndex: 0,
  userAnswers: {}, // { [qid]: "A" }
  bookmarks: new Set(),
  startTime: null,
  durationMinutes: 30,
  timeRemainingSeconds: 0,
  timerInterval: null,
  isReviewMode: false,

  // DOM Elements
  elements: {},

  init() {
    this.elements = {
      view: document.getElementById("mock-view"),
      setupSection: document.getElementById("mock-setup-section"),
      examSection: document.getElementById("mock-exam-section"),
      scoreSection: document.getElementById("mock-score-section"),
      
      // Setup controls
      countSelect: document.getElementById("mock-count-select"),
      topicSelect: document.getElementById("mock-topic-select"),
      timeSelect: document.getElementById("mock-time-select"),
      startBtn: document.getElementById("mock-start-btn"),
      
      // Exam screen
      timerDisplay: document.getElementById("mock-timer-display"),
      counter: document.getElementById("mock-q-counter"),
      topicBadge: document.getElementById("mock-q-topic"),
      text: document.getElementById("mock-q-text"),
      optionsList: document.getElementById("mock-options-list"),
      markBtn: document.getElementById("mock-mark-btn"),
      clearBtn: document.getElementById("mock-clear-btn"),
      prevBtn: document.getElementById("mock-prev-btn"),
      nextBtn: document.getElementById("mock-next-btn"),
      submitBtn: document.getElementById("mock-submit-btn"),
      paletteGrid: document.getElementById("mock-palette-grid"),
      
      // Score screen
      scoreVal: document.getElementById("mock-score-val"),
      accuracyVal: document.getElementById("mock-accuracy-val"),
      timeTakenVal: document.getElementById("mock-time-taken-val"),
      reviewQuestionsBtn: document.getElementById("mock-review-btn"),
      retakeBtn: document.getElementById("mock-retake-btn"),
      scoreTopicBreakdown: document.getElementById("mock-topic-breakdown"),
      reviewFilterSelect: document.getElementById("mock-review-filter")
    };

    this.bindEvents();
    this.populateTopicOptions();
  },

  populateTopicOptions() {
    if (!this.elements.topicSelect) return;
    this.elements.topicSelect.innerHTML = `<option value="all">All Topics (Full Syllabus)</option>`;
    QuestionsRepo.getTopics().forEach(t => {
      const opt = document.createElement("option");
      opt.value = t.topicId;
      opt.textContent = t.topicName;
      this.elements.topicSelect.appendChild(opt);
    });
  },

  bindEvents() {
    if (this.elements.startBtn) {
      this.elements.startBtn.addEventListener("click", () => this.startExam());
    }
    if (this.elements.prevBtn) {
      this.elements.prevBtn.addEventListener("click", () => this.prevQuestion());
    }
    if (this.elements.nextBtn) {
      this.elements.nextBtn.addEventListener("click", () => this.nextQuestion());
    }
    if (this.elements.markBtn) {
      this.elements.markBtn.addEventListener("click", () => this.toggleMark());
    }
    if (this.elements.clearBtn) {
      this.elements.clearBtn.addEventListener("click", () => this.clearAnswer());
    }
    if (this.elements.submitBtn) {
      this.elements.submitBtn.addEventListener("click", () => this.confirmSubmit());
    }
    if (this.elements.retakeBtn) {
      this.elements.retakeBtn.addEventListener("click", () => this.showSetup());
    }
    if (this.elements.reviewQuestionsBtn) {
      this.elements.reviewQuestionsBtn.addEventListener("click", () => this.enterReviewMode());
    }
    if (this.elements.reviewFilterSelect) {
      this.elements.reviewFilterSelect.addEventListener("change", () => this.applyReviewFilter());
    }
  },

  showSetup() {
    this.active = false;
    this.isReviewMode = false;
    clearInterval(this.timerInterval);
    this.elements.setupSection.style.display = "block";
    this.elements.examSection.style.display = "none";
    this.elements.scoreSection.style.display = "none";
  },

  startExam() {
    const count = parseInt(this.elements.countSelect.value, 10) || 20;
    const topic = this.elements.topicSelect.value === "all" ? null : this.elements.topicSelect.value;
    const timeLimit = parseInt(this.elements.timeSelect.value, 10); // minutes (0 = untimed)

    this.questions = QuestionsRepo.getRandomSubset(count, topic);
    if (this.questions.length === 0) {
      alert("No questions found for the selected topic filter.");
      return;
    }

    this.active = true;
    this.isReviewMode = false;
    this.currentIndex = 0;
    this.userAnswers = {};
    this.bookmarks = new Set();
    this.startTime = Date.now();
    this.durationMinutes = timeLimit;

    // Timer
    if (timeLimit > 0) {
      this.timeRemainingSeconds = timeLimit * 60;
      this.updateTimerDisplay();
      clearInterval(this.timerInterval);
      this.timerInterval = setInterval(() => this.tickTimer(), 1000);
      this.elements.timerDisplay.style.display = "inline-flex";
    } else {
      clearInterval(this.timerInterval);
      this.elements.timerDisplay.style.display = "none";
    }

    this.elements.setupSection.style.display = "none";
    this.elements.examSection.style.display = "grid";
    this.elements.scoreSection.style.display = "none";

    this.renderQuestion();
    this.renderPalette();
  },

  tickTimer() {
    if (this.timeRemainingSeconds > 0) {
      this.timeRemainingSeconds--;
      this.updateTimerDisplay();
      if (this.timeRemainingSeconds <= 300) { // last 5 minutes warning
        this.elements.timerDisplay.classList.add("warning");
      }
    } else {
      clearInterval(this.timerInterval);
      alert("Time is up! Your mock exam will now be submitted automatically.");
      this.submitExam();
    }
  },

  updateTimerDisplay() {
    const mins = Math.floor(this.timeRemainingSeconds / 60);
    const secs = this.timeRemainingSeconds % 60;
    this.elements.timerDisplay.textContent = `⏱ ${String(mins).padStart(2, "0")}:${String(secs).padStart(2, "0")}`;
  },

  getCurrentQuestion() {
    return this.questions[this.currentIndex] || null;
  },

  renderQuestion() {
    const q = this.getCurrentQuestion();
    if (!q) return;

    this.elements.counter.textContent = `Question ${this.currentIndex + 1} of ${this.questions.length}`;
    this.elements.topicBadge.textContent = q.topicName;
    this.elements.text.textContent = q.question;

    const isMarked = this.bookmarks.has(q.id);
    this.elements.markBtn.classList.toggle("active", isMarked);
    this.elements.markBtn.innerHTML = isMarked ? `★ Marked for Review` : `☆ Mark for Review`;

    const selectedKey = this.userAnswers[q.id];

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

      if (this.isReviewMode) {
        // Reveal answers in review mode
        if (key === q.correctAnswer) {
          optItem.classList.add("correct");
        } else if (key === selectedKey && key !== q.correctAnswer) {
          optItem.classList.add("incorrect");
        }
        if (key === selectedKey) {
          optItem.classList.add("selected");
        }
        optItem.classList.add("disabled");
      } else {
        if (key === selectedKey) {
          optItem.classList.add("selected");
        }
        optItem.addEventListener("click", () => this.selectOption(key));
      }

      this.elements.optionsList.appendChild(optItem);
    });

    // In Review Mode, render the explanation box
    let reviewExpBox = document.getElementById("mock-review-exp");
    if (this.isReviewMode) {
      if (!reviewExpBox) {
        reviewExpBox = document.createElement("div");
        reviewExpBox.id = "mock-review-exp";
        reviewExpBox.className = "explanation-box show";
        this.elements.optionsList.parentNode.insertBefore(reviewExpBox, this.elements.optionsList.nextSibling);
      }
      reviewExpBox.innerHTML = `
        <div class="exp-header">${selectedKey === q.correctAnswer ? '✓ Correct Solution:' : '✕ Correct Solution & Analysis:'}</div>
        <div class="exp-text">${q.explanation}</div>
        <div class="exp-source">Source: ${q.sourcePdf} ${q.sourcePages ? `(Pages ${q.sourcePages.join(", ")})` : ""}</div>
      `;
      reviewExpBox.style.display = "block";
    } else if (reviewExpBox) {
      reviewExpBox.style.display = "none";
    }

    this.elements.prevBtn.disabled = this.currentIndex === 0;
    this.elements.nextBtn.disabled = this.currentIndex === this.questions.length - 1;

    this.updatePaletteActive();
  },

  selectOption(key) {
    if (this.isReviewMode) return;
    const q = this.getCurrentQuestion();
    if (!q) return;

    this.userAnswers[q.id] = key;

    const items = this.elements.optionsList.querySelectorAll(".option-item");
    items.forEach(item => {
      item.classList.toggle("selected", item.dataset.key === key);
    });

    this.renderPalette();
  },

  clearAnswer() {
    if (this.isReviewMode) return;
    const q = this.getCurrentQuestion();
    if (!q) return;

    delete this.userAnswers[q.id];
    const items = this.elements.optionsList.querySelectorAll(".option-item");
    items.forEach(item => item.classList.remove("selected"));

    this.renderPalette();
  },

  toggleMark() {
    const q = this.getCurrentQuestion();
    if (!q) return;

    if (this.bookmarks.has(q.id)) {
      this.bookmarks.delete(q.id);
    } else {
      this.bookmarks.add(q.id);
    }

    const isMarked = this.bookmarks.has(q.id);
    this.elements.markBtn.classList.toggle("active", isMarked);
    this.elements.markBtn.innerHTML = isMarked ? `★ Marked for Review` : `☆ Mark for Review`;

    this.renderPalette();
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

  jumpTo(index) {
    if (index >= 0 && index < this.questions.length) {
      this.currentIndex = index;
      this.renderQuestion();
    }
  },

  renderPalette() {
    if (!this.elements.paletteGrid) return;
    this.elements.paletteGrid.innerHTML = "";

    this.questions.forEach((q, idx) => {
      const btn = document.createElement("button");
      btn.className = "palette-btn";
      btn.textContent = idx + 1;

      if (idx === this.currentIndex) {
        btn.classList.add("active");
      }

      if (this.isReviewMode) {
        const userChoice = this.userAnswers[q.id];
        if (userChoice === q.correctAnswer) {
          btn.classList.add("answered-correct");
        } else if (userChoice) {
          btn.classList.add("answered-incorrect");
        }
      } else {
        if (this.userAnswers[q.id]) {
          btn.classList.add("answered");
        }
        if (this.bookmarks.has(q.id)) {
          btn.classList.add("marked");
        }
      }

      btn.addEventListener("click", () => this.jumpTo(idx));
      this.elements.paletteGrid.appendChild(btn);
    });
  },

  updatePaletteActive() {
    if (!this.elements.paletteGrid) return;
    const btns = this.elements.paletteGrid.querySelectorAll(".palette-btn");
    btns.forEach((btn, idx) => {
      btn.classList.toggle("active", idx === this.currentIndex);
    });
  },

  confirmSubmit() {
    const answeredCount = Object.keys(this.userAnswers).length;
    const totalCount = this.questions.length;
    const unattempted = totalCount - answeredCount;

    let msg = `You have answered ${answeredCount} of ${totalCount} questions.`;
    if (unattempted > 0) {
      msg += `\n${unattempted} questions remain unanswered!`;
    }
    msg += "\n\nAre you sure you want to finish and submit the test?";

    if (confirm(msg)) {
      this.submitExam();
    }
  },

  submitExam() {
    clearInterval(this.timerInterval);
    const durationSeconds = Math.round((Date.now() - this.startTime) / 1000);
    
    let correctCount = 0;
    const topicStats = {};

    this.questions.forEach(q => {
      const chosen = this.userAnswers[q.id];
      const isCorrect = (chosen === q.correctAnswer);
      
      // Update persistent progress
      if (chosen) {
        ProgressManager.recordAnswer(q.id, chosen, isCorrect, q.topicId);
      }

      if (isCorrect) correctCount++;

      if (!topicStats[q.topicName]) {
        topicStats[q.topicName] = { correct: 0, total: 0 };
      }
      topicStats[q.topicName].total++;
      if (isCorrect) topicStats[q.topicName].correct++;
    });

    const total = this.questions.length;
    const accuracy = Math.round((correctCount / total) * 100);

    // Save mock test history
    ProgressManager.recordMockTest({
      score: correctCount,
      total: total,
      accuracy: accuracy,
      durationSeconds: durationSeconds,
      topicCount: Object.keys(topicStats).length
    });

    // Render score card
    this.elements.scoreVal.textContent = `${correctCount} / ${total}`;
    this.elements.accuracyVal.textContent = `${accuracy}%`;

    const mins = Math.floor(durationSeconds / 60);
    const secs = durationSeconds % 60;
    this.elements.timeTakenVal.textContent = `${mins}m ${secs}s`;

    // Render topic breakdown
    if (this.elements.scoreTopicBreakdown) {
      this.elements.scoreTopicBreakdown.innerHTML = "";
      Object.keys(topicStats).forEach(topic => {
        const st = topicStats[topic];
        const pct = Math.round((st.correct / st.total) * 100);
        const row = document.createElement("div");
        row.style.marginBottom = "0.75rem";
        row.innerHTML = `
          <div style="display:flex; justify-content:space-between; font-size:0.85rem; margin-bottom:0.25rem;">
            <span><strong>${topic}</strong></span>
            <span>${st.correct}/${st.total} (${pct}%)</span>
          </div>
          <div class="topic-progress-bar">
            <div class="topic-progress-fill ${pct >= 70 ? 'complete' : ''}" style="width: ${pct}%"></div>
          </div>
        `;
        this.elements.scoreTopicBreakdown.appendChild(row);
      });
    }

    this.elements.setupSection.style.display = "none";
    this.elements.examSection.style.display = "none";
    this.elements.scoreSection.style.display = "block";
  },

  enterReviewMode() {
    this.isReviewMode = true;
    this.currentIndex = 0;
    this.elements.setupSection.style.display = "none";
    this.elements.examSection.style.display = "grid";
    this.elements.scoreSection.style.display = "none";
    this.elements.timerDisplay.textContent = "Review Mode";
    this.elements.timerDisplay.classList.remove("warning");

    this.elements.clearBtn.style.display = "none";
    this.elements.submitBtn.textContent = "Back to Score";
    this.elements.submitBtn.onclick = () => {
      this.elements.examSection.style.display = "none";
      this.elements.scoreSection.style.display = "block";
      this.elements.submitBtn.textContent = "Submit Test";
      this.elements.submitBtn.onclick = () => this.confirmSubmit();
      this.elements.clearBtn.style.display = "inline-flex";
    };

    this.renderQuestion();
    this.renderPalette();
  }
};

window.MockController = MockController;
