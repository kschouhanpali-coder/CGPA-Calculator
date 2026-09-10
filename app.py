import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(
    page_title="CGPA Calculator",
    page_icon="C",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={},
)

st.markdown(
    """
    <style>
    [data-testid="stHeader"], [data-testid="stToolbar"],
    [data-testid="stDecoration"], footer, [data-testid="stSidebar"] {
        display: none !important;
    }
    .stApp, .main, .block-container {
        padding: 0 !important;
        margin: 0 !important;
        max-width: none !important;
    }
    iframe {
        display: block;
        border: 0 !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


APP_HTML = r"""
<!doctype html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>CGPA Calculator</title>
<style>
:root {
  color-scheme: light;
  --background: hsl(39 38% 95%);
  --foreground: hsl(219 35% 16%);
  --border: hsl(38 22% 84%);
  --input: hsl(39 22% 80%);
  --card: hsl(42 35% 98%);
  --card-border: hsl(38 24% 87%);
  --primary: hsl(220 42% 21%);
  --primary-foreground: hsl(42 35% 98%);
  --secondary: hsl(173 37% 91%);
  --secondary-foreground: hsl(174 43% 22%);
  --muted-foreground: hsl(218 15% 46%);
  --accent: hsl(42 88% 54%);
  --accent-foreground: hsl(220 42% 16%);
  --destructive: hsl(3 63% 49%);
  --font-sans: "Avenir Next", "DM Sans", Arial, sans-serif;
  --font-display: Georgia, "Times New Roman", serif;
  --font-data: "SFMono-Regular", Consolas, "Liberation Mono", monospace;
  --shadow-card: 0 10px 32px rgba(31, 40, 53, 0.07);
  --shadow-lift: 0 14px 28px rgba(31, 40, 53, 0.12);
}

* { box-sizing: border-box; }
html, body { margin: 0; min-width: 320px; background: var(--background); }
body {
  color: var(--foreground);
  font-family: var(--font-sans);
  -webkit-font-smoothing: antialiased;
}
button, input, select { font: inherit; }
button { cursor: pointer; }
button:focus-visible, input:focus-visible, select:focus-visible {
  outline: 3px solid color-mix(in srgb, var(--accent) 42%, transparent);
  outline-offset: 2px;
}

.app-shell {
  min-height: 100vh;
  overflow-x: hidden;
  background:
    linear-gradient(rgba(34, 48, 79, .035) 1px, transparent 1px),
    linear-gradient(90deg, rgba(34, 48, 79, .035) 1px, transparent 1px),
    var(--background);
  background-size: 28px 28px;
}
.page-header, .page-main {
  position: relative;
  width: min(1240px, 100%);
  margin: 0 auto;
  padding-left: 40px;
  padding-right: 40px;
}
.page-header {
  display: flex;
  align-items: center;
  padding-top: 24px;
  padding-bottom: 24px;
}
.brand {
  display: flex;
  align-items: center;
  gap: 12px;
}
.brand-mark {
  display: grid;
  place-items: center;
  width: 40px;
  height: 40px;
  border-radius: 12px;
  background: var(--primary);
  color: var(--accent);
  box-shadow: 4px 4px 0 rgba(244, 181, 27, .45);
}
.brand-mark svg { width: 21px; height: 21px; }
.brand-name {
  color: var(--foreground);
  font-family: var(--font-display);
  font-size: 18px;
  font-weight: 700;
  line-height: 1;
}
.hero {
  padding-top: 56px;
  padding-bottom: 44px;
}
.hero h1 {
  max-width: 680px;
  margin: 0;
  color: var(--primary);
  font-family: var(--font-display);
  font-size: clamp(3.4rem, 7vw, 6.6rem);
  line-height: .9;
  letter-spacing: -.055em;
}
.hero h1 span { color: var(--accent); }

.summary-grid {
  display: grid;
  grid-template-columns: minmax(0, 2fr) minmax(230px, 1fr);
  gap: 16px;
  margin-bottom: 40px;
}
.summary-card {
  min-height: 176px;
  padding: 28px;
  border: 1px solid var(--card-border);
  border-radius: 16px;
  background: var(--card);
  box-shadow: var(--shadow-card);
}
.summary-card.primary {
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  border-color: var(--primary);
  background: var(--primary);
  color: var(--primary-foreground);
}
.eyebrow, .field-label {
  color: var(--muted-foreground);
  font-family: var(--font-data);
  font-size: 10px;
  font-weight: 700;
  letter-spacing: .18em;
  line-height: 1.2;
  text-transform: uppercase;
}
.primary .eyebrow { color: rgba(255, 255, 255, .62); }
.summary-value {
  margin-top: 8px;
  color: var(--primary);
  font-family: var(--font-display);
  font-size: 64px;
  line-height: .95;
  letter-spacing: -.06em;
}
.primary .summary-value { color: var(--accent); }
.summary-side { text-align: right; }
.status-pill {
  display: inline-flex;
  padding: 5px 12px;
  border-radius: 999px;
  background: rgba(255, 255, 255, .12);
  color: rgba(255, 255, 255, .82);
  font-size: 12px;
  font-weight: 700;
}
.status-message {
  max-width: 180px;
  margin: 8px 0 0 auto;
  color: rgba(255, 255, 255, .62);
  font-size: 12px;
  line-height: 1.65;
}
.summary-card:not(.primary) .summary-value { font-size: 52px; }
.summary-note {
  margin-top: 8px;
  color: var(--muted-foreground);
  font-size: 14px;
}

.content-grid {
  display: grid;
  grid-template-columns: minmax(0, 1fr) 300px;
  align-items: start;
  gap: 40px;
}
.records { min-width: 0; }
.section-header {
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  gap: 12px;
  margin-bottom: 20px;
}
.section-header h2, .trend-card h2 {
  margin: 5px 0 0;
  color: var(--primary);
  font-family: var(--font-display);
  font-size: 32px;
  letter-spacing: -.03em;
}
.button-primary, .button-plain {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  border: 0;
  transition: transform .18s ease, box-shadow .18s ease, color .18s ease;
}
.button-primary {
  min-height: 40px;
  padding: 0 16px;
  border-radius: 999px;
  background: var(--accent);
  color: var(--accent-foreground);
  font-size: 14px;
  font-weight: 700;
}
.button-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 16px rgba(244, 181, 27, .3);
}
.button-plain {
  padding: 0;
  background: transparent;
  color: var(--secondary-foreground);
  font-size: 14px;
  font-weight: 700;
}
.button-plain:hover { color: var(--primary); }
.icon { width: 16px; height: 16px; flex: 0 0 auto; }

.semester-card, .trend-card {
  border: 1px solid var(--card-border);
  border-radius: 16px;
  background: var(--card);
  box-shadow: var(--shadow-card);
}
.semester-card {
  overflow: hidden;
  margin-bottom: 20px;
}
.semester-heading {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  padding: 16px 24px;
  border-bottom: 1px solid rgba(229, 225, 215, .85);
  background: rgba(231, 243, 240, .45);
}
.semester-heading-left, .semester-heading-right {
  display: flex;
  align-items: center;
}
.semester-heading-left { min-width: 0; gap: 12px; }
.semester-heading-right { flex: 0 0 auto; gap: 12px; }
.semester-number {
  display: grid;
  place-items: center;
  width: 36px;
  height: 36px;
  flex: 0 0 auto;
  border-radius: 9px;
  background: var(--secondary);
  color: var(--secondary-foreground);
  font-family: var(--font-data);
  font-size: 12px;
  font-weight: 700;
}
.semester-title {
  overflow: hidden;
  color: var(--primary);
  font-family: var(--font-display);
  font-size: 24px;
  letter-spacing: -.03em;
  text-overflow: ellipsis;
  white-space: nowrap;
}
.semester-meta {
  margin-top: 2px;
  color: var(--muted-foreground);
  font-size: 12px;
}
.semester-score { text-align: right; }
.semester-score .field-label { font-size: 9px; }
.semester-score-value {
  color: var(--primary);
  font-family: var(--font-display);
  font-size: 24px;
  line-height: 1;
}
.remove-button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 32px;
  height: 32px;
  border: 0;
  border-radius: 8px;
  background: transparent;
  color: var(--muted-foreground);
}
.remove-button:hover { background: rgba(3, 63, 49, .08); color: var(--destructive); }
.remove-button:disabled { cursor: default; opacity: .25; pointer-events: none; }
.column-labels, .subject-row {
  display: grid;
  grid-template-columns: minmax(0, 1fr) 125px 135px 36px;
  gap: 12px;
}
.column-labels {
  padding: 16px 24px 8px;
  color: var(--muted-foreground);
  font-family: var(--font-data);
  font-size: 10px;
  font-weight: 700;
  letter-spacing: .14em;
  text-transform: uppercase;
}
.subject-list { padding: 0 24px; }
.subject-row {
  align-items: start;
  padding: 16px 0;
  border-bottom: 1px solid rgba(229, 225, 215, .75);
}
.subject-row:last-child { border-bottom: 0; }
.field-input, .field-select {
  width: 100%;
  height: 44px;
  border: 1px solid var(--input);
  border-radius: 9px;
  background: var(--background);
  color: var(--foreground);
  -webkit-text-fill-color: var(--foreground);
  font-size: 14px;
}
.field-input { padding: 0 12px; }
.field-select {
  appearance: none;
  padding: 0 32px 0 12px;
  font-weight: 600;
}
.field-input::placeholder {
  color: var(--muted-foreground);
  opacity: .65;
  -webkit-text-fill-color: var(--muted-foreground);
}
.select-wrap { position: relative; }
.select-wrap .chevron {
  position: absolute;
  top: 14px;
  right: 12px;
  pointer-events: none;
  color: var(--muted-foreground);
}
.field-select option {
  color: var(--foreground);
  background: var(--background);
}
.mobile-label {
  display: none;
  margin-bottom: 6px;
  color: var(--muted-foreground);
  font-family: var(--font-data);
  font-size: 10px;
  font-weight: 700;
  letter-spacing: .14em;
  text-transform: uppercase;
}
.subject-delete { margin-top: 4px; }
.semester-actions {
  padding: 16px 24px;
  border-top: 1px solid rgba(229, 225, 215, .75);
}
.empty-state {
  padding: 56px 24px;
  border: 1px dashed var(--border);
  border-radius: 16px;
  background: rgba(252, 251, 247, .6);
  text-align: center;
}
.empty-state h3 {
  margin: 16px 0 8px;
  color: var(--primary);
  font-family: var(--font-display);
  font-size: 24px;
}
.empty-state p {
  max-width: 320px;
  margin: 0 auto;
  color: var(--muted-foreground);
  font-size: 14px;
  line-height: 1.6;
}

.trend-card {
  position: sticky;
  top: 20px;
  padding: 24px;
}
.trend-header {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
}
.trend-header .icon { color: var(--secondary-foreground); }
.chart-wrap {
  overflow: hidden;
  margin-top: 20px;
  padding: 8px;
  border-radius: 12px;
  background: rgba(231, 243, 240, .45);
}
.chart-wrap svg { display: block; width: 100%; height: auto; }
.trend-footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-top: 16px;
  padding-top: 16px;
  border-top: 1px solid rgba(229, 225, 215, .75);
  color: var(--muted-foreground);
  font-size: 12px;
}
.trend-footer strong {
  color: var(--primary);
  font-family: var(--font-data);
  font-size: 14px;
}
.page-footer {
  position: relative;
  margin-top: 72px;
  padding: 24px 40px;
  border-top: 1px solid rgba(229, 225, 215, .7);
  color: var(--muted-foreground);
  font-size: 12px;
  text-align: center;
}

@media (max-width: 900px) {
  .content-grid { grid-template-columns: 1fr; gap: 28px; }
  .trend-card { position: static; }
}
@media (max-width: 700px) {
  .page-header, .page-main { padding-left: 20px; padding-right: 20px; }
  .hero { padding-top: 36px; padding-bottom: 36px; }
  .summary-grid { grid-template-columns: 1fr; }
  .summary-card.primary { align-items: flex-start; }
  .section-header { align-items: flex-start; }
  .section-header h2 { font-size: 28px; }
  .column-labels { display: none; }
  .subject-list { padding: 0 20px; }
  .subject-row {
    display: grid;
    grid-template-columns: minmax(0, 1fr) 42px;
  }
  .subject-row > label:first-child { grid-column: 1 / -1; }
  .subject-row > label:nth-child(2), .subject-row > .select-wrap { grid-column: 1; }
  .subject-row > .subject-delete { grid-column: 2; grid-row: 2 / span 2; }
  .mobile-label { display: block; }
  .semester-heading, .semester-actions { padding-left: 20px; padding-right: 20px; }
  .page-footer { padding-left: 20px; padding-right: 20px; }
}
@media (max-width: 460px) {
  .summary-card { padding: 22px; }
  .summary-card.primary { display: block; }
  .summary-side { margin-top: 20px; text-align: left; }
  .status-message { margin-left: 0; }
  .semester-heading-right { gap: 4px; }
  .semester-title { font-size: 21px; }
}
</style>
</head>
<body>
<div id="app"></div>
<script>
const GRADE_POINTS = { O: 10, 'A+': 9, A: 8, 'B+': 7, B: 6, 'C+': 5, C: 4, 'D+': 3, D: 2, F: 0 };
const GRADE_OPTIONS = Object.keys(GRADE_POINTS);
let nextId = 2;
let semesters = [{ id: 1, subjects: [{ id: 1, name: '', credits: '', grade: '' }] }];

const icons = {
  cap: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m3 10 9-5 9 5-9 5-9-5Z"/><path d="M7 12.2V16c2.8 2.2 7.2 2.2 10 0v-3.8"/><path d="M21 10v6"/></svg>',
  plus: '<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><path d="M12 5v14M5 12h14"/></svg>',
  x: '<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="m6 6 12 12M18 6 6 18"/></svg>',
  trash: '<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 6h18M8 6V4h8v2M19 6l-1 14H6L5 6M10 11v5M14 11v5"/></svg>',
  chevron: '<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m6 9 6 6 6-6"/></svg>',
  trend: '<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m3 17 6-6 4 4 7-8"/><path d="M14 7h6v6"/></svg>',
  book: '<svg viewBox="0 0 24 24" width="31" height="31" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 5.5A2.5 2.5 0 0 1 6.5 3H20v17H6.5A2.5 2.5 0 0 0 4 22V5.5Z"/><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/></svg>'
};

function escapeHtml(value) {
  return String(value).replace(/[&<>"']/g, (character) => ({
    '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#039;'
  }[character]));
}

function formatScore(value) {
  return Number(value).toFixed(2);
}

function makeSubject() {
  return { id: nextId++, name: '', credits: '', grade: '' };
}

function calculateSemester(semester) {
  const validSubjects = semester.subjects.filter((subject) =>
    subject.name.trim() && Number(subject.credits) > 0 && subject.grade
  );
  const credits = validSubjects.reduce((sum, subject) => sum + Number(subject.credits), 0);
  const weighted = validSubjects.reduce(
    (sum, subject) => sum + Number(subject.credits) * GRADE_POINTS[subject.grade], 0
  );
  return { credits, weighted, sgpa: credits ? weighted / credits : 0, validSubjects };
}

function calculateAll() {
  const semesterStats = semesters.map((semester) => ({
    semester, ...calculateSemester(semester)
  }));
  const totalCredits = semesterStats.reduce((sum, stat) => sum + stat.credits, 0);
  const totalWeighted = semesterStats.reduce((sum, stat) => sum + stat.weighted, 0);
  return { semesterStats, totalCredits, cgpa: totalCredits ? totalWeighted / totalCredits : 0 };
}

function statusFor(cgpa, hasResults) {
  if (!hasResults) return ['Awaiting results', 'Add your first subject to begin.'];
  if (cgpa >= 8) return ['Excellent', 'A strong academic rhythm. Keep going.'];
  if (cgpa >= 6) return ['Good', 'A solid foundation with room to climb.'];
  return ['Needs Improvement', 'Small, steady gains can change the picture.'];
}

function renderTrend(semesterStats) {
  const chartWidth = 260, chartHeight = 150;
  const padding = { top: 16, right: 16, bottom: 28, left: 24 };
  const values = semesterStats.map((item) => item.sgpa);
  const points = values.map((value, index) => {
    const x = values.length === 1
      ? chartWidth / 2
      : padding.left + (index / (values.length - 1)) * (chartWidth - padding.left - padding.right);
    const y = padding.top + (1 - value / 10) * (chartHeight - padding.top - padding.bottom);
    return { x, y, value };
  });
  const line = points.map((point) => `${point.x},${point.y}`).join(' ');
  const area = points.length
    ? `${points[0].x},${chartHeight - padding.bottom} ${line} ${points[points.length - 1].x},${chartHeight - padding.bottom}`
    : '';
  const grid = [0, 5, 10].map((tick) => {
    const y = padding.top + (1 - tick / 10) * (chartHeight - padding.top - padding.bottom);
    return `<line x1="${padding.left}" x2="${chartWidth - padding.right}" y1="${y}" y2="${y}" stroke="rgba(34,48,79,.15)" stroke-dasharray="3 4"/><text x="0" y="${y + 4}" fill="hsl(218 15% 46%)" font-size="9" font-family="monospace">${tick}</text>`;
  }).join('');
  const dots = points.map((point, index) =>
    `<circle cx="${point.x}" cy="${point.y}" r="5" fill="hsl(42 88% 54%)" stroke="hsl(220 42% 21%)" stroke-width="2"/><text x="${point.x}" y="${chartHeight - 8}" text-anchor="middle" fill="hsl(218 15% 46%)" font-size="9" font-family="monospace">S${index + 1}</text>`
  ).join('');
  return `<svg viewBox="0 0 ${chartWidth} ${chartHeight}" role="img" aria-label="Semester SGPA trend chart">
    ${grid}<polygon points="${area}" fill="rgba(244,181,27,.22)"/>
    <polyline points="${line}" fill="none" stroke="hsl(220 42% 21%)" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
    ${dots}
  </svg>`;
}

function semesterMarkup(semester, semesterIndex, stats) {
  const subjects = semester.subjects.map((subject, subjectIndex) => `
    <div class="subject-row">
      <label>
        <span class="mobile-label"><span style="color:var(--accent-foreground)">0${subjectIndex + 1}</span> Subject</span>
        <input class="field-input subject-name" data-semester="${semester.id}" data-subject="${subject.id}" value="${escapeHtml(subject.name)}" placeholder="e.g. Linear Algebra" aria-label="Subject name">
      </label>
      <label>
        <span class="mobile-label">Credits</span>
        <input class="field-input subject-credits" data-semester="${semester.id}" data-subject="${subject.id}" type="number" min="0.5" step="0.5" value="${escapeHtml(subject.credits)}" placeholder="3" aria-label="Credit hours">
      </label>
      <label class="select-wrap">
        <span class="mobile-label">Grade</span>
        <select class="field-select subject-grade" data-semester="${semester.id}" data-subject="${subject.id}" aria-label="Grade">
          <option value="" disabled ${subject.grade ? '' : 'selected'}>Select grade</option>
          ${GRADE_OPTIONS.map((grade) => `<option value="${grade}" ${subject.grade === grade ? 'selected' : ''}>${grade}</option>`).join('')}
        </select>
        <span class="chevron">${icons.chevron}</span>
      </label>
      <button class="remove-button subject-delete" data-action="remove-subject" data-semester="${semester.id}" data-subject="${subject.id}" aria-label="Remove subject">${icons.x}</button>
    </div>
  `).join('');

  return `
    <article class="semester-card">
      <div class="semester-heading">
        <div class="semester-heading-left">
          <div class="semester-number">${semesterIndex + 1}</div>
          <div>
            <div class="semester-title">Semester ${semesterIndex + 1}</div>
            <div class="semester-meta" data-semester-meta="${semester.id}">${stats.validSubjects.length} subjects · ${stats.credits || 0} credits entered</div>
          </div>
        </div>
        <div class="semester-heading-right">
          <div class="semester-score">
            <div class="field-label">SGPA</div>
            <div class="semester-score-value" data-semester-sgpa="${semester.id}">${stats.credits ? formatScore(stats.sgpa) : '—'}</div>
          </div>
          <button class="remove-button" data-action="remove-semester" data-semester="${semester.id}" aria-label="Remove Semester ${semesterIndex + 1}" ${semesters.length === 1 ? 'disabled' : ''}>${icons.trash}</button>
        </div>
      </div>
      <div class="column-labels"><span>Subject</span><span>Credits</span><span>Grade</span><span></span></div>
      <div class="subject-list">${subjects}</div>
      <div class="semester-actions">
        <button class="button-plain" data-action="add-subject" data-semester="${semester.id}">${icons.plus} Add subject</button>
      </div>
    </article>
  `;
}

function render() {
  const stats = calculateAll();
  const [status, statusMessage] = statusFor(stats.cgpa, stats.totalCredits > 0);
  const app = document.getElementById('app');
  app.innerHTML = `
    <div class="app-shell">
      <header class="page-header">
        <div class="brand">
          <div class="brand-mark">${icons.cap}</div>
          <div class="brand-name">CGPA Calculator</div>
        </div>
      </header>
      <main class="page-main">
        <section class="hero"><h1>CGPA<br><span>Calculator</span></h1></section>
        <section class="summary-grid">
          <div class="summary-card primary">
            <div><div class="eyebrow">Overall CGPA</div><div class="summary-value" data-overall>${stats.totalCredits ? formatScore(stats.cgpa) : '—'}</div></div>
            <div class="summary-side"><span class="status-pill" data-status>${status}</span><p class="status-message" data-status-message>${statusMessage}</p></div>
          </div>
          <div class="summary-card">
            <div class="eyebrow">Total credits</div>
            <div class="summary-value" data-total-credits>${stats.totalCredits || '—'}</div>
            <div class="summary-note">${semesters.length} ${semesters.length === 1 ? 'semester' : 'semesters'} tracked</div>
          </div>
        </section>
        <div class="content-grid">
          <section class="records" aria-label="Semester results">
            <div class="section-header">
              <div><div class="eyebrow">Your record</div><h2>Semester results</h2></div>
              <button class="button-primary" data-action="add-semester">${icons.plus}<span>Add semester</span></button>
            </div>
            <div id="semester-list">
              ${semesters.map((semester, index) => semesterMarkup(semester, index, stats.semesterStats[index])).join('')}
            </div>
          </section>
          <aside>
            <section class="trend-card">
              <div class="trend-header">
                <div><div class="eyebrow">At a glance</div><h2>Semester trend</h2></div>
                ${icons.trend}
              </div>
              <div class="chart-wrap" data-chart>${renderTrend(stats.semesterStats)}</div>
              <div class="trend-footer"><span>Latest SGPA</span><strong data-latest>${formatScore(stats.semesterStats.at(-1)?.sgpa || 0)}</strong></div>
            </section>
          </aside>
        </div>
      </main>
      <footer class="page-footer">Built for the semesters that matter.</footer>
    </div>
  `;
  bindEvents();
}

function updateComputed() {
  const stats = calculateAll();
  const [status, statusMessage] = statusFor(stats.cgpa, stats.totalCredits > 0);
  const overall = document.querySelector('[data-overall]');
  const totalCredits = document.querySelector('[data-total-credits]');
  const statusNode = document.querySelector('[data-status]');
  const statusMessageNode = document.querySelector('[data-status-message]');
  if (overall) overall.textContent = stats.totalCredits ? formatScore(stats.cgpa) : '—';
  if (totalCredits) totalCredits.textContent = stats.totalCredits || '—';
  if (statusNode) statusNode.textContent = status;
  if (statusMessageNode) statusMessageNode.textContent = statusMessage;
  stats.semesterStats.forEach((stat) => {
    const meta = document.querySelector(`[data-semester-meta="${stat.semester.id}"]`);
    const sgpa = document.querySelector(`[data-semester-sgpa="${stat.semester.id}"]`);
    if (meta) meta.textContent = `${stat.validSubjects.length} subjects · ${stat.credits || 0} credits entered`;
    if (sgpa) sgpa.textContent = stat.credits ? formatScore(stat.sgpa) : '—';
  });
  const chart = document.querySelector('[data-chart]');
  const latest = document.querySelector('[data-latest]');
  if (chart) chart.innerHTML = renderTrend(stats.semesterStats);
  if (latest) latest.textContent = formatScore(stats.semesterStats.at(-1)?.sgpa || 0);
}

function getSubject(semesterId, subjectId) {
  const semester = semesters.find((item) => item.id === Number(semesterId));
  return semester?.subjects.find((item) => item.id === Number(subjectId));
}

function bindEvents() {
  document.querySelectorAll('input.subject-name').forEach((input) => {
    input.addEventListener('input', (event) => {
      const subject = getSubject(input.dataset.semester, input.dataset.subject);
      if (subject) subject.name = event.target.value;
      updateComputed();
    });
  });
  document.querySelectorAll('input.subject-credits').forEach((input) => {
    input.addEventListener('input', (event) => {
      const subject = getSubject(input.dataset.semester, input.dataset.subject);
      if (subject) subject.credits = event.target.value;
      updateComputed();
    });
  });
  document.querySelectorAll('select.subject-grade').forEach((select) => {
    select.addEventListener('change', (event) => {
      const subject = getSubject(select.dataset.semester, select.dataset.subject);
      if (subject) subject.grade = event.target.value;
      updateComputed();
    });
  });
  document.querySelectorAll('[data-action]').forEach((button) => {
    button.addEventListener('click', () => {
      const action = button.dataset.action;
      if (action === 'add-semester') {
        semesters.push({ id: nextId++, subjects: [makeSubject()] });
      } else if (action === 'remove-semester') {
        semesters = semesters.filter((semester) => semester.id !== Number(button.dataset.semester));
      } else if (action === 'add-subject') {
        const semester = semesters.find((item) => item.id === Number(button.dataset.semester));
        if (semester) semester.subjects.push(makeSubject());
      } else if (action === 'remove-subject') {
        const semester = semesters.find((item) => item.id === Number(button.dataset.semester));
        if (semester) {
          semester.subjects = semester.subjects.filter((subject) => subject.id !== Number(button.dataset.subject));
          if (!semester.subjects.length) semester.subjects.push(makeSubject());
        }
      }
      render();
    });
  });
}

render();
</script>
</body>
</html>
"""

components.html(APP_HTML, height=1700, scrolling=True)