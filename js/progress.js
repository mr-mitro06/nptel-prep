/**
 * NPTEL Prep - Progress and State Persistence Manager
 * Uses browser localStorage for complete client-side persistence.
 */

const STORAGE_KEYS = {
  PROGRESS: "nptel_prep_progress",
  BOOKMARKS: "nptel_prep_bookmarks",
  MOCK_HISTORY: "nptel_prep_mock_history",
  THEME: "nptel_prep_theme",
  LAST_STATE: "nptel_prep_last_state"
};

const ProgressManager = {
  // Load raw progress dictionary: { [qid]: { answered: true, selected: "A", isCorrect: true, attempts: 1, lastAttempt: timestamp } }
  getProgress() {
    try {
      const data = localStorage.getItem(STORAGE_KEYS.PROGRESS);
      return data ? JSON.parse(data) : {};
    } catch (e) {
      console.error("Error reading progress from localStorage", e);
      return {};
    }
  },

  saveProgress(progress) {
    try {
      localStorage.setItem(STORAGE_KEYS.PROGRESS, JSON.stringify(progress));
    } catch (e) {
      console.error("Error saving progress to localStorage", e);
    }
  },

  // Record an answer attempt for a specific question
  recordAnswer(qid, selectedOption, isCorrect, topicId) {
    const progress = this.getProgress();
    const existing = progress[qid] || { attempts: 0 };
    progress[qid] = {
      answered: true,
      selected: selectedOption,
      isCorrect: isCorrect,
      attempts: (existing.attempts || 0) + 1,
      lastAttempt: Date.now(),
      topicId: topicId
    };
    this.saveProgress(progress);
    this.notifyUpdate();
  },

  // Bookmarks / Mark for Review
  getBookmarks() {
    try {
      const data = localStorage.getItem(STORAGE_KEYS.BOOKMARKS);
      return data ? JSON.parse(data) : [];
    } catch (e) {
      return [];
    }
  },

  isBookmarked(qid) {
    const bookmarks = this.getBookmarks();
    return bookmarks.includes(qid);
  },

  toggleBookmark(qid) {
    let bookmarks = this.getBookmarks();
    if (bookmarks.includes(qid)) {
      bookmarks = bookmarks.filter(id => id !== qid);
    } else {
      bookmarks.push(qid);
    }
    try {
      localStorage.setItem(STORAGE_KEYS.BOOKMARKS, JSON.stringify(bookmarks));
    } catch (e) {
      console.error("Error updating bookmarks", e);
    }
    this.notifyUpdate();
    return bookmarks.includes(qid);
  },

  // Mock Test History
  getMockHistory() {
    try {
      const data = localStorage.getItem(STORAGE_KEYS.MOCK_HISTORY);
      return data ? JSON.parse(data) : [];
    } catch (e) {
      return [];
    }
  },

  recordMockTest(result) {
    const history = this.getMockHistory();
    history.unshift({
      id: Date.now(),
      date: new Date().toISOString(),
      score: result.score,
      total: result.total,
      accuracy: result.accuracy,
      durationSeconds: result.durationSeconds,
      topicCount: result.topicCount
    });
    // Keep last 50 tests
    const trimmed = history.slice(0, 50);
    try {
      localStorage.setItem(STORAGE_KEYS.MOCK_HISTORY, JSON.stringify(trimmed));
    } catch (e) {
      console.error("Error saving mock history", e);
    }
    this.notifyUpdate();
  },

  // Overall Statistics
  getOverallStats(totalAvailableQuestions = 400) {
    const progress = this.getProgress();
    const answeredKeys = Object.keys(progress);
    const attemptedCount = answeredKeys.length;
    
    let correctCount = 0;
    let incorrectCount = 0;
    
    answeredKeys.forEach(qid => {
      if (progress[qid].isCorrect) {
        correctCount++;
      } else {
        incorrectCount++;
      }
    });

    const accuracy = attemptedCount > 0 ? Math.round((correctCount / attemptedCount) * 100) : 0;
    const completion = totalAvailableQuestions > 0 ? Math.round((attemptedCount / totalAvailableQuestions) * 100) : 0;
    const bookmarks = this.getBookmarks();

    return {
      total: totalAvailableQuestions,
      attempted: attemptedCount,
      correct: correctCount,
      incorrect: incorrectCount,
      accuracy: accuracy,
      completion: completion,
      bookmarksCount: bookmarks.length
    };
  },

  // Topic-wise Statistics
  getTopicStats(topicId, topicQuestionIds = []) {
    const progress = this.getProgress();
    let attempted = 0;
    let correct = 0;

    topicQuestionIds.forEach(qid => {
      if (progress[qid]) {
        attempted++;
        if (progress[qid].isCorrect) {
          correct++;
        }
      }
    });

    const total = topicQuestionIds.length;
    const accuracy = attempted > 0 ? Math.round((correct / attempted) * 100) : 0;
    const completion = total > 0 ? Math.round((attempted / total) * 100) : 0;

    return {
      total,
      attempted,
      correct,
      accuracy,
      completion
    };
  },

  // Weak questions (answered incorrectly on last attempt)
  getWeakQuestionIds() {
    const progress = this.getProgress();
    return Object.keys(progress).filter(qid => !progress[qid].isCorrect);
  },

  // Last Session State
  saveLastState(state) {
    try {
      localStorage.setItem(STORAGE_KEYS.LAST_STATE, JSON.stringify(state));
    } catch (e) {}
  },

  getLastState() {
    try {
      const s = localStorage.getItem(STORAGE_KEYS.LAST_STATE);
      return s ? JSON.parse(s) : null;
    } catch (e) {
      return null;
    }
  },

  // Reset All Progress
  resetAll() {
    try {
      localStorage.removeItem(STORAGE_KEYS.PROGRESS);
      localStorage.removeItem(STORAGE_KEYS.BOOKMARKS);
      localStorage.removeItem(STORAGE_KEYS.MOCK_HISTORY);
      localStorage.removeItem(STORAGE_KEYS.LAST_STATE);
      this.notifyUpdate();
      return true;
    } catch (e) {
      return false;
    }
  },

  // Listeners
  listeners: [],
  onUpdate(callback) {
    this.listeners.push(callback);
  },
  notifyUpdate() {
    this.listeners.forEach(cb => {
      try { cb(); } catch (e) { console.error(e); }
    });
  }
};

window.ProgressManager = ProgressManager;
