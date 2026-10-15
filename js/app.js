/**
 * NPTEL Prep - Main Application Coordinator
 */

document.addEventListener("DOMContentLoaded", async () => {
  // 1. Initialize Theme
  initTheme();

  // 2. Initialize Data Repository
  await QuestionsRepo.init();

  // 3. Initialize Sub-controllers
  PracticeController.init();
  MockController.init();
  RevisionController.init();

  // 4. Setup Routing & Navigation
  initNavigation();

  // 5. Render Views
  renderDashboard();
  renderTopicLibrary();
  renderWeakAreas();
  updateHeaderStats();

  // 6. Listen for Progress Updates to refresh UI metrics
  ProgressManager.onUpdate(() => {
    updateHeaderStats();
    renderDashboard();
    renderTopicLibrary();
    renderWeakAreas();
  });

  // 7. Check for Last Session State to offer "Continue"
  checkLastSession();
});

// Theme Management
function initTheme() {
  const savedTheme = localStorage.getItem("nptel_prep_theme") || "light";
  document.documentElement.setAttribute("data-theme", savedTheme);

  const themeToggleBtn = document.getElementById("theme-toggle-btn");
  if (themeToggleBtn) {
    themeToggleBtn.innerHTML = savedTheme === "dark" ? "☀️" : "🌙";
    themeToggleBtn.title = savedTheme === "dark" ? "Switch to Light Mode" : "Switch to Dark Mode";

    themeToggleBtn.addEventListener("click", () => {
      const current = document.documentElement.getAttribute("data-theme");
      const next = current === "dark" ? "light" : "dark";
      document.documentElement.setAttribute("data-theme", next);
      localStorage.setItem("nptel_prep_theme", next);
      themeToggleBtn.innerHTML = next === "dark" ? "☀️" : "🌙";
      themeToggleBtn.title = next === "dark" ? "Switch to Light Mode" : "Switch to Dark Mode";
    });
  }
}

// Navigation & View Routing
function initNavigation() {
  const navBtns = document.querySelectorAll(".nav-btn");
  navBtns.forEach(btn => {
    btn.addEventListener("click", () => {
      const targetView = btn.dataset.view;
      switchView(targetView);
    });
  });

  // Reset Progress Modal
  const resetBtn = document.getElementById("reset-progress-btn");
  const resetModal = document.getElementById("reset-modal");
  const cancelResetBtn = document.getElementById("cancel-reset-btn");
  const confirmResetBtn = document.getElementById("confirm-reset-btn");

  if (resetBtn && resetModal) {
    resetBtn.addEventListener("click", () => resetModal.classList.add("open"));
    cancelResetBtn.addEventListener("click", () => resetModal.classList.remove("open"));
    confirmResetBtn.addEventListener("click", () => {
      ProgressManager.resetAll();
      resetModal.classList.remove("open");
      alert("All local study progress and history have been reset.");
      renderDashboard();
      renderTopicLibrary();
      renderWeakAreas();
      updateHeaderStats();
    });
  }

  // Brand click -> Dashboard
  const brand = document.querySelector(".brand-section");
  if (brand) {
    brand.addEventListener("click", () => switchView("dashboard-view"));
  }
}

function switchView(viewId) {
  const views = document.querySelectorAll(".view-section");
  views.forEach(v => v.classList.remove("active"));

  const target = document.getElementById(viewId);
  if (target) {
    target.classList.add("active");
  }

  const navBtns = document.querySelectorAll(".nav-btn");
  navBtns.forEach(btn => {
    btn.classList.toggle("active", btn.dataset.view === viewId);
  });

  window.scrollTo({ top: 0, behavior: "smooth" });
}

// Header Stats Bar
function updateHeaderStats() {
  const allQuestions = QuestionsRepo.getAllQuestions();
  const stats = ProgressManager.getOverallStats(allQuestions.length);

  const statAttempted = document.getElementById("header-stat-attempted");
  const statAccuracy = document.getElementById("header-stat-accuracy");
  const statWeak = document.getElementById("header-stat-weak");
  const statFill = document.getElementById("header-progress-fill");

  if (statAttempted) statAttempted.textContent = `${stats.attempted}/${stats.total}`;
  if (statAccuracy) statAccuracy.textContent = `${stats.accuracy}%`;
  if (statWeak) statWeak.textContent = `${stats.incorrect}`;
  if (statFill) statFill.style.width = `${stats.completion}%`;
}

// Dashboard View
function renderDashboard() {
  const allQuestions = QuestionsRepo.getAllQuestions();
  const topics = QuestionsRepo.getTopics();
  const stats = ProgressManager.getOverallStats(allQuestions.length);

  // Metrics
  const elTotalTopics = document.getElementById("dash-total-topics");
  const elTotalQ = document.getElementById("dash-total-q");
  const elAttempted = document.getElementById("dash-attempted");
  const elAccuracy = document.getElementById("dash-accuracy");

  if (elTotalTopics) elTotalTopics.textContent = topics.length;
  if (elTotalQ) elTotalQ.textContent = allQuestions.length;
  if (elAttempted) elAttempted.textContent = stats.attempted;
  if (elAccuracy) elAccuracy.textContent = `${stats.accuracy}%`;

  // Start / Continue Buttons
  const startBtn = document.getElementById("dash-start-btn");
  const continueBtn = document.getElementById("dash-continue-btn");

  if (startBtn) {
    startBtn.onclick = () => {
      // Start practice on first topic or weak area
      if (topics.length > 0) {
        PracticeController.startTopic(topics[0].topicId, "practice");
        switchView("practice-view");
      }
    };
  }

  if (continueBtn) {
    const lastState = ProgressManager.getLastState();
    if (lastState && lastState.topicId) {
      continueBtn.style.display = "inline-flex";
      continueBtn.onclick = () => {
        PracticeController.startTopic(lastState.topicId, "practice");
        if (lastState.index) PracticeController.jumpToQuestion(lastState.index);
        switchView("practice-view");
      };
    } else {
      continueBtn.style.display = "none";
    }
  }

  // Dashboard Topic Cards List
  renderDashboardTopics(topics);
}

function renderDashboardTopics(topics) {
  const container = document.getElementById("dash-topics-list");
  if (!container) return;
  container.innerHTML = "";

  topics.slice(0, 6).forEach(topic => {
    const topicQs = QuestionsRepo.getQuestionsByTopic(topic.topicId);
    const qids = topicQs.map(q => q.id);
    const st = ProgressManager.getTopicStats(topic.topicId, qids);

    const card = document.createElement("div");
    card.className = "topic-card";
    card.innerHTML = `
      <div>
        <div class="topic-card-header">
          <div class="topic-card-title">${topic.topicName}</div>
          <span class="topic-badge">${topic.questionCount} MCQs</span>
        </div>
        <div class="topic-meta">
          <span>${st.accuracy > 0 ? `Accuracy: ${st.accuracy}%` : "Not attempted"}</span>
          <span>•</span>
          <span>${st.attempted}/${st.total} done</span>
        </div>
        <div class="topic-progress-section">
          <div class="topic-progress-text">
            <span>Progress</span>
            <span>${st.completion}%</span>
          </div>
          <div class="topic-progress-bar">
            <div class="topic-progress-fill ${st.completion === 100 ? 'complete' : ''}" style="width: ${st.completion}%"></div>
          </div>
        </div>
      </div>
      <div class="topic-card-actions">
        <button class="btn btn-primary btn-sm" style="flex:1;">Practice</button>
        <button class="btn btn-secondary btn-sm study-btn">Study</button>
      </div>
    `;

    card.querySelector(".btn-primary").addEventListener("click", () => {
      PracticeController.startTopic(topic.topicId, "practice");
      switchView("practice-view");
    });

    card.querySelector(".study-btn").addEventListener("click", () => {
      PracticeController.startTopic(topic.topicId, "study");
      switchView("practice-view");
    });

    container.appendChild(card);
  });
}

// Topic Library View
function renderTopicLibrary() {
  const container = document.getElementById("library-topic-grid");
  const searchInput = document.getElementById("library-search-input");
  if (!container) return;

  const topics = QuestionsRepo.getTopics();

  const drawTopics = (filterText = "") => {
    container.innerHTML = "";
    const clean = filterText.trim().toLowerCase();

    const filtered = topics.filter(t => 
      t.topicName.toLowerCase().includes(clean) ||
      t.sourcePdf.toLowerCase().includes(clean)
    );

    if (filtered.length === 0) {
      container.innerHTML = `<div class="empty-state" style="grid-column: 1/-1;"><p>No topics match your search criteria.</p></div>`;
      return;
    }

    filtered.forEach(topic => {
      const topicQs = QuestionsRepo.getQuestionsByTopic(topic.topicId);
      const qids = topicQs.map(q => q.id);
      const st = ProgressManager.getTopicStats(topic.topicId, qids);

      const card = document.createElement("div");
      card.className = "topic-card";
      card.innerHTML = `
        <div>
          <div class="topic-card-header">
            <div class="topic-card-title">${topic.topicName}</div>
            <span class="topic-badge">${topic.questionCount} MCQs</span>
          </div>
          <div class="topic-meta">
            <span>Source: ${topic.sourcePdf}</span>
          </div>
          <div class="topic-progress-section">
            <div class="topic-progress-text">
              <span>${st.attempted}/${st.total} answered</span>
              <span>${st.accuracy > 0 ? `${st.accuracy}% accuracy` : `${st.completion}% completed`}</span>
            </div>
            <div class="topic-progress-bar">
              <div class="topic-progress-fill ${st.completion === 100 ? 'complete' : ''}" style="width: ${st.completion}%"></div>
            </div>
          </div>
        </div>
        <div class="topic-card-actions">
          <button class="btn btn-primary btn-sm practice-btn" style="flex:1;">Start Practice</button>
          <button class="btn btn-secondary btn-sm study-btn">Study Mode</button>
          <button class="btn btn-outline-primary btn-sm rev-btn" title="Quick Revision">⚡</button>
        </div>
      `;

      card.querySelector(".practice-btn").addEventListener("click", () => {
        PracticeController.startTopic(topic.topicId, "practice");
        switchView("practice-view");
      });

      card.querySelector(".study-btn").addEventListener("click", () => {
        PracticeController.startTopic(topic.topicId, "study");
        switchView("practice-view");
      });

      card.querySelector(".rev-btn").addEventListener("click", () => {
        RevisionController.activeTopicId = topic.topicId;
        RevisionController.renderNav();
        switchView("revision-view");
      });

      container.appendChild(card);
    });
  };

  drawTopics();

  if (searchInput) {
    searchInput.addEventListener("input", (e) => drawTopics(e.target.value));
  }
}

// Weak Areas View
function renderWeakAreas() {
  const container = document.getElementById("weak-questions-container");
  const countBadge = document.getElementById("weak-count-badge");
  const retryBtn = document.getElementById("practice-weak-btn");
  if (!container) return;

  const weakIds = ProgressManager.getWeakQuestionIds();
  if (countBadge) countBadge.textContent = weakIds.length;

  if (weakIds.length === 0) {
    container.innerHTML = `
      <div class="empty-state">
        <div class="empty-state-icon">🎯</div>
        <h3>No Weak Areas Detected!</h3>
        <p>You have not answered any questions incorrectly yet, or you have successfully resolved all prior mistakes.</p>
        <button class="btn btn-primary btn-sm" onclick="switchView('library-view')">Browse Topics</button>
      </div>
    `;
    if (retryBtn) retryBtn.disabled = true;
    return;
  }

  if (retryBtn) {
    retryBtn.disabled = false;
    retryBtn.onclick = () => {
      PracticeController.startWeakPractice();
      switchView("practice-view");
    };
  }

  const weakQs = QuestionsRepo.getQuestionsByIds(weakIds);
  container.innerHTML = "";

  weakQs.forEach((q, idx) => {
    const card = document.createElement("div");
    card.className = "question-card";
    card.style.marginBottom = "1.25rem";
    card.innerHTML = `
      <div class="question-top-bar">
        <div class="q-badge-group">
          <span class="q-topic-badge">${q.topicName}</span>
          <span class="q-diff-badge q-diff-${q.difficulty || 'medium'}">${q.difficulty || 'medium'}</span>
        </div>
        <span class="q-counter">Mistake #${idx + 1}</span>
      </div>
      <div class="question-text" style="font-size:1.05rem;">${q.question}</div>
      <div class="explanation-box show" style="margin-bottom:1rem;">
        <div class="exp-header">Correct Answer: (${q.correctAnswer}) ${q.options[q.correctAnswer]}</div>
        <div class="exp-text">${q.explanation}</div>
      </div>
      <div style="display:flex; justify-content:flex-end;">
        <button class="btn btn-outline-primary btn-sm retry-single-btn">Retry This Question</button>
      </div>
    `;

    card.querySelector(".retry-single-btn").addEventListener("click", () => {
      PracticeController.startCustomQueue([q], "Retry Question", "practice");
      switchView("practice-view");
    });

    container.appendChild(card);
  });
}

function checkLastSession() {
  const lastState = ProgressManager.getLastState();
  if (lastState && lastState.topicId) {
    const continueBtn = document.getElementById("dash-continue-btn");
    if (continueBtn) continueBtn.style.display = "inline-flex";
  }
}

window.switchView = switchView;
