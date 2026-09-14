<div align="center" id="top">

# 📊 CGPA Calculator

**Track your semester grades. Calculate your CGPA. Visualize your progress.**

A clean, modern web app for students to log subjects, credits, and grades — and instantly see their SGPA, overall CGPA, and semester-by-semester trends with real-time visualizations.

[![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-Try_it_now-00C7B7?style=for-the-badge)](https://cgpa-calculator-pgzjdgmdtuxhhuprvppvyt.streamlit.app)
![React](https://img.shields.io/badge/React-18+-61DAFB?style=flat-square&logo=react&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-5+-3178C6?style=flat-square&logo=typescript&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat-square&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Backend-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)
![Status](https://img.shields.io/badge/status-active-brightgreen?style=flat-square)

</div>

---

## 📖 Table of Contents

- [Overview](#-overview)
- [Live Demo](#-live-demo)
- [Features](#-features)
- [How It Works](#️-how-it-works)
- [Architecture](#️-architecture)
- [Tech Stack](#️-tech-stack)
- [Getting Started](#-getting-started)
- [Usage Guide](#-usage-guide)
- [CGPA Calculation Formula](#-cgpa-calculation-formula)
- [Configuration Reference](#-configuration-reference)
- [Performance Tips](#-performance-tips)
- [Project Structure](#-project-structure)
- [Browser Support](#-browser-support)
- [Troubleshooting](#-troubleshooting)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)
- [FAQ](#-faq)
- [Credits & Support](#-credits--support)

---

## 📋 Overview

**CGPA Calculator** is a lightweight, intuitive application designed for students to effortlessly track their academic performance across multiple semesters. Instead of manual spreadsheets and complex calculations, this tool provides:

- ✅ **Real-time SGPA & CGPA calculation** — Results update as you type
- ✅ **Unlimited semester tracking** — Add as many semesters as you need
- ✅ **Visual progress graphs** — See your GPA trends at a glance
- ✅ **No data storage** — Your grades stay with you (local storage)
- ✅ **Mobile-friendly** — Works on phones, tablets, and desktops

Perfect for students tracking their academic journey and for institutions managing student performance data.

---

## 🌐 Live Demo

<div align="center">

### 👉 [**Open CGPA Calculator**](https://cgpa-calculator-pgzjdgmdtuxhhuprvppvyt.streamlit.app)

*Runs live in your browser — no installation required.*

</div>

---

## ✨ Features

<table>
<tr>
<td valign="top" width="50%">

### 🧮 Core Calculations
- **Auto-Calculate SGPA** — Semester GPA computed instantly
- **Live CGPA Updates** — Overall GPA across all semesters
- **Total Credits Counter** — Running total of all credits
- **Grade-to-Points Conversion** — Standard academic grading scale
- **Decimal Precision** — Accurate calculations to 2 decimal places

</td>
<td valign="top" width="50%">

### 📊 Visualization & Tracking
- **Semester Trend Chart** — Visual graph of SGPA progression
- **Unlimited Semesters** — No limits on data entry
- **Subject Breakdown** — Per-subject credits and grades
- **Progress Insights** — See your academic trajectory
- **Responsive UI** — Works on all screen sizes

</td>
</tr>
</table>

---

## 🏗️ How It Works

```
1. Enter Semester      User creates a new semester entry
2. Add Subjects        Log each subject with name, credits, and grade
3. Auto-Calculate      SGPA is computed instantly
4. Track Overall       CGPA updates across all semesters
5. Visualize Progress  Trend chart shows SGPA changes over time
6. Export (Future)     Download results as PDF or CSV
```

---

## 🎯 Architecture

### Core Components

| Component | Description |
|---|---|
| **Frontend Interface** | React + TypeScript UI for grade input and visualization |
| **Grade Validator** | Validates credits, grades, and subject entries |
| **SGPA Calculator** | Computes semester GPA based on credits and grades |
| **CGPA Aggregator** | Calculates overall GPA across all semesters |
| **Visualization Engine** | Renders trend charts and progress graphs |
| **Local Storage** | Persists data in browser (optional) |

### System Integration

| Layer | Technology |
|---|---|
| **Frontend** | React 18+ · TypeScript · Vite · shadcn/ui · Chart.js |
| **UI Components** | Tailwind CSS · React Icons |
| **Backend** | Python · Streamlit (alternative deployment) |
| **Deployment** | Streamlit Cloud / Vercel |
| **Architecture** | Full-stack web application |

---

## 🛠️ Tech Stack

| Category | Technology |
|---|---|
| **Frontend Framework** | React 18+ with TypeScript |
| **Build Tool** | Vite |
| **Styling** | Tailwind CSS |
| **UI Components** | shadcn/ui |
| **Charts & Graphs** | Chart.js / Recharts |
| **Backend** | Python 3.9+ |
| **Server** | Streamlit |
| **Deployment** | Streamlit Cloud, Vercel, or Netlify |

---

## 🚀 Getting Started

### Prerequisites

- **Node.js** ≥ 18 (for the React frontend)
- **Python** ≥ 3.9 (for the Streamlit backend)
- **npm** or **yarn** package manager
- A modern browser (Chrome 90+, Firefox 88+, Safari 14+, or Edge 90+)

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/yourusername/CGPA-Calculator.git
cd CGPA-Calculator
```

**2. Install frontend dependencies**
```bash
cd artifacts/cgpa-calculator
npm install
```

**3. Install backend dependencies**
```bash
cd ../..
pip install -r requirements.txt
```

**4. Launch the application**

**Option A: Run React frontend (development)**
```bash
cd artifacts/cgpa-calculator
npm run dev
```
Opens at **http://localhost:5173/**

**Option B: Run Streamlit backend**
```bash
streamlit run app.py
```
Opens at **http://localhost:8501/**

---

## 📖 Usage Guide

### Adding Your First Semester

| Step | Action |
|---|---|
| 1️⃣ | Click **"+ Add Semester"** button |
| 2️⃣ | Enter semester name (e.g., "Semester 1", "Fall 2024") |
| 3️⃣ | Click **"Add"** to create the semester |

### Entering Subject Grades

| Step | Action |
|---|---|
| 1️⃣ | In your semester, click **"+ Add Subject"** |
| 2️⃣ | Enter **Subject Name** (e.g., "Data Structures", "Calculus") |
| 3️⃣ | Enter **Credits** (numeric value, typically 1-4) |
| 4️⃣ | Select **Grade** from dropdown (A, B, C, D, F, etc.) |
| 5️⃣ | Click **"Add Subject"** |
| 6️⃣ | Your **SGPA** updates automatically |

### Viewing Your Progress

- **Dashboard** — See overall CGPA and total credits at top
- **Semester Cards** — View SGPA for each semester
- **Trend Chart** — Click the graph icon to see your GPA progression
- **Subject Details** — Expand each semester to see individual subjects

### Example Data Entry

```
Semester 1 (Fall 2023):
  • Data Structures (4 credits) → Grade A
  • Calculus I (3 credits) → Grade A
  • Physics (4 credits) → Grade B+
  → SGPA: 3.75

Semester 2 (Spring 2024):
  • Algorithms (4 credits) → Grade A
  • Discrete Math (3 credits) → Grade A
  • Chemistry (4 credits) → Grade A-
  → SGPA: 3.92

Overall CGPA (2 semesters): 3.84
```

---

## 🔢 CGPA Calculation Formula

### Grade Point Scale

| Grade | Points | Grade Range |
|---|---|---|
| A | 4.0 | 90–100 |
| A- | 3.7 | 85–89 |
| B+ | 3.3 | 80–84 |
| B | 3.0 | 75–79 |
| B- | 2.7 | 70–74 |
| C+ | 2.3 | 65–69 |
| C | 2.0 | 60–64 |
| D | 1.0 | Below 60 |
| F | 0.0 | Failed |

### SGPA Formula

```
SGPA = (Σ(Grade Point × Credit) for each subject) / Σ(Credits for semester)
```

**Example:**
```
Subject 1: A (4.0) × 4 credits = 16.0 points
Subject 2: B+ (3.3) × 3 credits = 9.9 points
Total: 25.9 / 7 credits = 3.70 SGPA
```

### CGPA Formula

```
CGPA = (Σ(SGPA × Total Credits of semester)) / Σ(All Credits across semesters)
```

---

## 🔧 Configuration Reference

### Grade Mapping

Customize your institution's grading scale by editing `gradeScale.ts`:

```typescript
const gradeScale = {
  'A': 4.0,
  'A-': 3.7,
  'B+': 3.3,
  'B': 3.0,
  // Add more grades as needed
};
```

### UI Settings

| Setting | Location | Effect |
|---|---|---|
| **Decimal Places** | `config.ts` | Precision of SGPA/CGPA display |
| **Chart Colors** | `theme.ts` | Customize trend graph appearance |
| **Credit Range** | Validation layer | Min/max credits per subject |

---

## ⚡ Performance Tips

| Action | Benefit | When to Use |
|---|---|---|
| Limit to 8 semesters | Faster chart rendering | Large datasets |
| Use short subject names | Cleaner UI | Mobile devices |
| Clear completed semesters | Reduce data volume | End of academic year |
| Use browser cache | Instant reload | Frequent user |

---

## 📁 Project Structure

```bash
CGPA-Calculator/
├── artifacts/
│   ├── cgpa-calculator/          # Frontend React app
│   │   ├── src/
│   │   │   ├── components/       # React components
│   │   │   ├── pages/            # Main pages
│   │   │   ├── utils/            # Calculation logic
│   │   │   └── App.tsx           # Main app component
│   │   ├── public/               # Static assets
│   │   ├── index.html            # Entry HTML
│   │   └── vite.config.ts        # Vite config
│   └── api-server/               # Backend (optional)
├── app.py                        # Streamlit entry point
├── requirements.txt              # Python dependencies
├── package.json                  # Frontend dependencies
├── .gitignore                    # Git ignore file
└── README.md                     # Documentation
```

---

## 🌐 Browser Support

| Browser | Minimum Version | Status |
|---|---|---|
| **Chrome** | 90+ | ✅ Fully Supported |
| **Firefox** | 88+ | ✅ Fully Supported |
| **Safari** | 14+ | ✅ Fully Supported |
| **Edge** | 90+ | ✅ Fully Supported |
| **Mobile Safari** | iOS 14+ | ✅ Fully Supported |
| **Chrome Mobile** | Android 5.0+ | ✅ Fully Supported |

---

## 🐛 Troubleshooting

<details>
<summary><strong>❌ SGPA not calculating correctly</strong></summary>
<br/>

**Solutions:**
- Verify that **grades match** your institution's grading scale
- Check that **all subjects have both credits and grades** entered
- Ensure credits are numeric values (not text)
- Look for **grade validation warnings** in the UI
- Try **refreshing the page** (Ctrl+R or Cmd+R)

**Example of correct entry:**
```
Subject: "Data Structures"
Credits: 4 (numeric, not "4.0" text)
Grade: "A" (from dropdown, not typed)
```

</details>

<details>
<summary><strong>❌ Data not saving</strong></summary>
<br/>

**Solutions:**
- **Enable browser cache** — Check browser settings (Settings → Privacy)
- **Clear browser cache** to force fresh load (Ctrl+Shift+Del)
- **Use a supported browser** — Ensure it's updated to latest version
- **Check local storage** — Browser DevTools → Application → Local Storage
- **Try incognito mode** — Rule out extensions interfering with storage

</details>

<details>
<summary><strong>❌ Trend chart not displaying</strong></summary>
<br/>

**Solutions:**
- Add **at least 2 semesters** to see trend (1 semester = no trend)
- Check that **each semester has at least 1 subject**
- Ensure all subjects have **valid grades** (not blank)
- **Disable ad blockers** — Some block chart rendering libraries
- **Try a different browser** — Check if issue persists

</details>

<details>
<summary><strong>❌ App running slowly</strong></summary>
<br/>

**Solutions:**
- **Reduce semester count** — Delete older/test semesters
- **Clear browser cache** (Ctrl+Shift+Del)
- **Close other tabs** to free up memory
- **Try desktop over mobile** for better performance
- **Check internet connection** speed (visit speedtest.net)

</details>

<details>
<summary><strong>❌ "Export" button not working</strong></summary>
<br/>

**Solutions:**
- This feature is **coming soon** (see Roadmap)
- As a workaround: **Take a screenshot** or **copy data manually**
- Follow issue #12 on GitHub for updates on PDF export feature

</details>

---

## 🗺️ Roadmap

- [ ] **PDF Export** — Download grade sheet as PDF document
- [ ] **CSV Import/Export** — Bulk import grades from Excel/CSV
- [ ] **Dark Mode** — Eye-friendly theme for night studying
- [ ] **What-If Simulator** — Predict GPA with hypothetical grades
- [ ] **Grade Distribution** — Pie chart showing grade breakdown
- [ ] **Multi-User Support** — Save multiple grade profiles
- [ ] **Cloud Sync** — Backup data to cloud (Google Drive, OneDrive)
- [ ] **Mobile App** — iOS and Android native applications
- [ ] **Institutional Integration** — Sync with university portals
- [ ] **AI Insights** — Personalized study recommendations

---

## 🤝 Contributing

Contributions are welcome! Whether you're fixing bugs, improving features, or adding documentation, please help us make this better.

### Steps to Contribute

1. **Fork** the repository on GitHub
2. **Create a feature branch**
   ```bash
   git checkout -b feature/YourFeatureName
   ```
3. **Make your changes** and test thoroughly
4. **Commit with clear messages**
   ```bash
   git commit -m 'Add YourFeatureName - brief description'
   ```
5. **Push to your branch**
   ```bash
   git push origin feature/YourFeatureName
   ```
6. **Open a Pull Request** with clear description of changes

### Areas for Contribution

- 🐛 **Bug fixes** — Found a problem? Help fix it
- ✨ **New features** — Implement items from the Roadmap
- 📖 **Documentation** — Improve README, add examples
- 🎨 **UI/UX Improvements** — Make the app more intuitive
- 🌍 **Localization** — Translate to other languages
- ♿ **Accessibility** — Improve support for screen readers

### Code Style Guidelines

- Use **TypeScript** for type safety
- Follow **Prettier** formatting (`npm run format`)
- Write **clear commit messages** (e.g., "Fix CGPA rounding issue in semester 2")
- Add **comments** for complex logic
- Test changes **locally** before submitting PR

---

## ❓ FAQ

<details>
<summary><strong>Q: Can I use a different grading scale?</strong></summary>

**A:** Yes! Edit the `gradeScale.ts` file in the source code to match your institution's grading system. Then rebuild with `npm run build`.

</details>

<details>
<summary><strong>Q: Is my data saved after I close the browser?</strong></summary>

**A:** By default, data is saved to **browser local storage**, so it persists between sessions. Cloud sync is on the Roadmap for future releases.

</details>

<details>
<summary><strong>Q: Can I import grades from an Excel file?</strong></summary>

**A:** Currently, you need to enter grades manually. CSV import is planned for the next release. Track progress on [GitHub Issues](https://github.com/yourusername/CGPA-Calculator/issues).

</details>

<details>
<summary><strong>Q: How accurate are the CGPA calculations?</strong></summary>

**A:** Calculations follow standard academic formulas and are accurate to 2 decimal places. Double-check with your institution's calculations if you're close to a GPA threshold.

</details>

<details>
<summary><strong>Q: Can I use this for multiple students?</strong></summary>

**A:** Currently, each browser profile has its own data. Multi-user accounts are on the Roadmap. You could use separate browser profiles or incognito windows as a workaround.

</details>

<details>
<summary><strong>Q: What if my institution uses a different CGPA formula?</strong></summary>

**A:** The calculator uses the standard formula: `CGPA = Total Grade Points / Total Credits`. If your institution uses weighted semesters or other formulas, please [open an issue](https://github.com/yourusername/CGPA-Calculator/issues) with details.

</details>

<details>
<summary><strong>Q: Can I deploy this myself?</strong></summary>

**A:** Yes! You can deploy the React frontend to Vercel, Netlify, or any static host, and the Python backend to AWS, Heroku, or any Python-capable server. See [Deployment Guide](#deployment-guide) (coming soon).

</details>

---

## 📱 Deployment Guide

### Deploy Frontend to Vercel

```bash
# Install Vercel CLI
npm install -g vercel

# Deploy from project root
vercel
```

### Deploy Frontend to Netlify

```bash
# Build the project
cd artifacts/cgpa-calculator
npm run build

# Deploy via Netlify CLI or drag-and-drop the dist/ folder
```

### Deploy Backend to Streamlit Cloud

1. Push code to GitHub
2. Visit [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repo and select `app.py`
4. Deploy with one click

---

## 🙏 Credits & Support

<div align="center">

📊

### Built for Students, By Students

*"Know your GPA. Plan your future."*

</div>

<br/>

### Technology Stack

This project is built with:

- **React** — Component-based UI framework
- **TypeScript** — Type-safe JavaScript
- **Vite** — Lightning-fast build tool
- **Tailwind CSS** — Utility-first styling
- **shadcn/ui** — High-quality components
- **Streamlit** — Python app framework
- **Chart.js** — Beautiful data visualizations

### Inspiration & Thanks

Thanks to all students who've tested and provided feedback. Special thanks to contributors who've helped improve this tool.

### Support & Feedback

<div align="center">

📬 **Have a question?** — [Open a GitHub Discussion](https://github.com/yourusername/CGPA-Calculator/discussions)

🐛 **Found a bug?** — [Report it with steps to reproduce](https://github.com/yourusername/CGPA-Calculator/issues)

💡 **Feature idea?** — [Start a discussion or open an issue](https://github.com/yourusername/CGPA-Calculator/issues)

⭐ **Enjoying this?** — A star on GitHub helps others discover it!

</div>

<br/>

**CGPA Calculator** is maintained with ❤️ by the development community.

<div align="center">

<br/>

<sub>Made with ❤️ for students everywhere. If this helped you track your grades, consider giving it a star! ⭐</sub>

<br/>

**Version 1.1.0** · Status: ✅ Active & Maintained

Last Updated: September 2024

<br/>

**[⬆ Back to top](#top)**

</div>
