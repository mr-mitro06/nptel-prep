/**
 * NPTEL Prep - Quick Revision Section Controller
 */

const RevisionController = {
  activeTopicId: null,
  elements: {},

  init() {
    this.elements = {
      nav: document.getElementById("revision-topics-nav"),
      content: document.getElementById("revision-content-area"),
      searchInput: document.getElementById("revision-search-input")
    };

    this.bindEvents();
    this.renderNav();
  },

  bindEvents() {
    if (this.elements.searchInput) {
      this.elements.searchInput.addEventListener("input", (e) => {
        this.filterContent(e.target.value);
      });
    }
  },

  renderNav() {
    if (!this.elements.nav) return;
    this.elements.nav.innerHTML = "";

    const topics = QuestionsRepo.getTopics();
    if (topics.length === 0) return;

    if (!this.activeTopicId) {
      this.activeTopicId = topics[0].topicId;
    }

    topics.forEach((t) => {
      const btn = document.createElement("button");
      btn.className = `rev-nav-item ${t.topicId === this.activeTopicId ? 'active' : ''}`;
      btn.textContent = t.topicName;
      btn.dataset.topicId = t.topicId;

      btn.addEventListener("click", () => {
        this.activeTopicId = t.topicId;
        const items = this.elements.nav.querySelectorAll(".rev-nav-item");
        items.forEach(i => i.classList.toggle("active", i.dataset.topicId === t.topicId));
        this.renderTopicContent(t.topicId);
      });

      this.elements.nav.appendChild(btn);
    });

    this.renderTopicContent(this.activeTopicId);
  },

  renderTopicContent(topicId) {
    if (!this.elements.content) return;
    const revData = QuestionsRepo.getRevisionForTopic(topicId);
    if (!revData) {
      this.elements.content.innerHTML = `<div class="empty-state"><p>No revision notes available for this topic.</p></div>`;
      return;
    }

    let html = `
      <div style="margin-bottom: 1.5rem;">
        <span class="topic-badge" style="font-size:0.8rem; margin-bottom:0.4rem; display:inline-block;">Topic Cheat Sheet</span>
        <h2 style="font-size: 1.4rem; font-weight: 800; color: var(--text-primary); letter-spacing:-0.02em;">${revData.topicName}</h2>
        <div style="font-size: 0.8rem; color: var(--text-muted); font-family: var(--font-mono); margin-top:0.25rem;">Source: ${revData.sourcePdf}</div>
      </div>
    `;

    // 1. Key Definitions
    if (revData.keyDefinitions && revData.keyDefinitions.length > 0) {
      html += `
        <div class="rev-section-block">
          <div class="rev-block-title">📌 Essential Definitions</div>
          ${revData.keyDefinitions.map(d => `
            <div class="rev-item-card">
              <div class="rev-item-term">${d.term}</div>
              <div class="rev-item-def">${d.definition}</div>
            </div>
          `).join("")}
        </div>
      `;
    }

    // 2. Formulas & Metrics
    if (revData.formulas && revData.formulas.length > 0) {
      html += `
        <div class="rev-section-block">
          <div class="rev-block-title">📐 Key Formulas & Metrics</div>
          ${revData.formulas.map(f => `
            <div class="rev-item-card">
              <div class="rev-item-term">${f.name}</div>
              <code class="rev-formula-code">${f.formula}</code>
              <div class="rev-item-def" style="margin-top:0.35rem;">${f.note}</div>
            </div>
          `).join("")}
        </div>
      `;
    }

    // 3. Concept Comparisons
    if (revData.comparisons && revData.comparisons.length > 0) {
      html += `
        <div class="rev-section-block">
          <div class="rev-block-title">⚖️ Concept Comparisons</div>
          ${revData.comparisons.map(c => `
            <div class="rev-item-card">
              <div class="rev-item-term">${c.conceptA} vs ${c.conceptB}</div>
              <div class="rev-item-def">${c.distinction}</div>
            </div>
          `).join("")}
        </div>
      `;
    }

    // 4. Common Misconceptions
    if (revData.commonMisconceptions && revData.commonMisconceptions.length > 0) {
      html += `
        <div class="rev-section-block">
          <div class="rev-block-title">⚠️ Common Misconceptions & Pitfalls</div>
          ${revData.commonMisconceptions.map(m => `
            <div class="rev-item-card" style="border-left: 3px solid var(--warning);">
              <div class="rev-item-def" style="color:var(--text-primary);">${m}</div>
            </div>
          `).join("")}
        </div>
      `;
    }

    // 5. High-Yield Exam Facts
    if (revData.highYieldFacts && revData.highYieldFacts.length > 0) {
      html += `
        <div class="rev-section-block">
          <div class="rev-block-title">💡 High-Yield Exam Facts</div>
          ${revData.highYieldFacts.map(fact => `
            <div class="rev-item-card" style="border-left: 3px solid var(--success);">
              <div class="rev-item-def" style="color:var(--text-primary); font-weight:500;">✓ ${fact}</div>
            </div>
          `).join("")}
        </div>
      `;
    }

    this.elements.content.innerHTML = html;
  },

  filterContent(query) {
    const clean = query.trim().toLowerCase();
    if (!clean) {
      this.renderTopicContent(this.activeTopicId);
      return;
    }

    const allRev = QuestionsRepo.getAllRevision();
    const matched = [];

    allRev.forEach(r => {
      const matchDefs = (r.keyDefinitions || []).filter(d => d.term.toLowerCase().includes(clean) || d.definition.toLowerCase().includes(clean));
      const matchForms = (r.formulas || []).filter(f => f.name.toLowerCase().includes(clean) || f.formula.toLowerCase().includes(clean) || f.note.toLowerCase().includes(clean));
      const matchComps = (r.comparisons || []).filter(c => c.conceptA.toLowerCase().includes(clean) || c.conceptB.toLowerCase().includes(clean) || c.distinction.toLowerCase().includes(clean));
      const matchFacts = (r.highYieldFacts || []).filter(fact => fact.toLowerCase().includes(clean));

      if (matchDefs.length || matchForms.length || matchComps.length || matchFacts.length || r.topicName.toLowerCase().includes(clean)) {
        matched.push({
          topicName: r.topicName,
          sourcePdf: r.sourcePdf,
          defs: matchDefs,
          forms: matchForms,
          comps: matchComps,
          facts: matchFacts
        });
      }
    });

    if (matched.length === 0) {
      this.elements.content.innerHTML = `<div class="empty-state"><p>No revision items matched "${query}".</p></div>`;
      return;
    }

    let html = `<h3 style="font-size:1.1rem; margin-bottom:1rem; color:var(--text-primary);">Search Results for "${query}" (${matched.length} topics)</h3>`;
    matched.forEach(m => {
      html += `
        <div style="margin-bottom: 2rem; border-bottom: 1px solid var(--border-light); padding-bottom: 1.5rem;">
          <h4 style="color:var(--primary); font-size:1.05rem; margin-bottom:0.75rem;">${m.topicName}</h4>
          ${m.defs.map(d => `<div class="rev-item-card"><div class="rev-item-term">${d.term}</div><div class="rev-item-def">${d.definition}</div></div>`).join("")}
          ${m.forms.map(f => `<div class="rev-item-card"><div class="rev-item-term">${f.name}</div><code class="rev-formula-code">${f.formula}</code><div class="rev-item-def">${f.note}</div></div>`).join("")}
          ${m.comps.map(c => `<div class="rev-item-card"><div class="rev-item-term">${c.conceptA} vs ${c.conceptB}</div><div class="rev-item-def">${c.distinction}</div></div>`).join("")}
          ${m.facts.map(fact => `<div class="rev-item-card" style="border-left: 3px solid var(--success);"><div class="rev-item-def">✓ ${fact}</div></div>`).join("")}
        </div>
      `;
    });

    this.elements.content.innerHTML = html;
  }
};

window.RevisionController = RevisionController;
