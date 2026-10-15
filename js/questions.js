/**
 * NPTEL Prep - Question and Data Bank Repository
 */

const QuestionsRepo = {
  topics: [],
  questions: [],
  revision: [],
  initialized: false,

  async init() {
    if (this.initialized) return;

    // First attempt to read bundled offline data
    if (window.NPTEL_DATA) {
      this.topics = window.NPTEL_DATA.topics || [];
      this.questions = window.NPTEL_DATA.questions || [];
      this.revision = window.NPTEL_DATA.revision || [];
      this.initialized = true;
      console.log(`QuestionsRepo initialized from bundled data: ${this.topics.length} topics, ${this.questions.length} questions.`);
      return;
    }

    // Fallback to fetch for server-hosted environments
    try {
      const [topicsRes, questionsRes, revisionRes] = await Promise.all([
        fetch("data/topics.json"),
        fetch("data/all_questions.json"),
        fetch("data/revision.json")
      ]);
      this.topics = await topicsRes.json();
      this.questions = await questionsRes.json();
      this.revision = await revisionRes.json();
      this.initialized = true;
      console.log(`QuestionsRepo initialized from JSON fetch: ${this.topics.length} topics, ${this.questions.length} questions.`);
    } catch (err) {
      console.warn("Fetch failed, checking for local fallback", err);
    }
  },

  getTopics() {
    return this.topics;
  },

  getTopicById(topicId) {
    return this.topics.find(t => t.topicId === topicId) || null;
  },

  getAllQuestions() {
    return this.questions;
  },

  getQuestionsByTopic(topicId) {
    return this.questions.filter(q => q.topicId === topicId);
  },

  getQuestionById(qid) {
    return this.questions.find(q => q.id === qid) || null;
  },

  getQuestionsByIds(ids = []) {
    const idSet = new Set(ids);
    return this.questions.filter(q => idSet.has(q.id));
  },

  getAllRevision() {
    return this.revision;
  },

  getRevisionForTopic(topicId) {
    return this.revision.find(r => r.topicId === topicId) || null;
  },

  searchQuestions(query = "") {
    const clean = query.trim().toLowerCase();
    if (!clean) return this.questions;
    return this.questions.filter(q => 
      q.question.toLowerCase().includes(clean) ||
      q.topicName.toLowerCase().includes(clean) ||
      q.explanation.toLowerCase().includes(clean) ||
      Object.values(q.options).some(opt => opt.toLowerCase().includes(clean))
    );
  },

  getRandomSubset(count = 20, topicFilter = null) {
    let pool = topicFilter ? this.getQuestionsByTopic(topicFilter) : [...this.questions];
    // Fisher-Yates shuffle
    for (let i = pool.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [pool[i], pool[j]] = [pool[j], pool[i]];
    }
    return pool.slice(0, Math.min(count, pool.length));
  }
};

window.QuestionsRepo = QuestionsRepo;
