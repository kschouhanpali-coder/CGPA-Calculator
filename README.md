<div align="center">

# 📊 CGPA Calculator 📊

### Track Grades. Calculate GPA. Visualize Success.

![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)
![Version](https://img.shields.io/badge/Version-1.1.0-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)
![Type](https://img.shields.io/badge/Type-GPA%20Tracker-00C7B7?style=for-the-badge)

A clean, fast web app for students to log subjects, credits, and grades, and instantly see their SGPA, overall CGPA, and semester-by-semester trends with clear visualizations.

*The modern GPA tracking tool for ambitious students.*

</div>

---

## 🚀 Live Demo

<div align="center">

### **[▶️ OPEN CGPA CALCULATOR - Live Demo](https://cgpa-calculator-pgzjdgmdtuxhhuprvppvyt.streamlit.app)**

*No installation required. Add your first semester right in your browser!*

</div>

---

## ✨ Features

- ⚡ **Real-Time Calculations** - SGPA and CGPA update as you enter data
- 🎯 **2-Decimal Precision** - Standard academic formulas
- 📚 **Semester Management** - Add semesters, then log subjects with credits and grades
- 🎓 **4.0 Grading Scale** - With customizable grade mappings for your institution
- 📈 **Trend Chart** - See your GPA progress semester by semester
- 📝 **Subject Breakdown** - Expand any semester to review its subjects
- 🔢 **Credits Tracker** - Total credits accumulated at a glance
- ✅ **Input Validation** - Catches invalid credits and missing grades
- 🗑️ **Easy Editing** - Edit or delete entries any time

---

## 🏁 Quick Start

### Use Online
No installation needed! [Launch the live demo](https://cgpa-calculator-pgzjdgmdtuxhhuprvppvyt.streamlit.app)

### Run Locally

**Prerequisites:** Node.js 18+ (React app) and/or Python 3.9+ (Streamlit app)

1. Clone the repository:
```bash
git clone https://github.com/kschouhanpali-coder/CGPA-Calculator.git
cd CGPA-Calculator
```

2. Run the React app:
```bash
cd artifacts/cgpa-calculator
npm install
npm run dev
```

3. Or run the Streamlit app:
```bash
pip install -r requirements.txt
streamlit run app.py
```

4. Open the local URL shown in your terminal in your browser

---

## 🎯 How to Use

1. **Add a Semester** - create a semester such as "Fall 2024" or "Semester 1"
2. **Add Subjects** - enter the subject name, credits, and pick a grade from the dropdown
3. **Watch SGPA Update** - each semester's SGPA is calculated instantly
4. **Track Your CGPA** - the overall CGPA updates across all semesters
5. **View the Trend** - add two or more semesters to see your GPA trend chart

---

## 🔢 Calculation Formulas

| Metric | Formula |
|--------|---------|
| **SGPA** | Σ(Grade Points × Credits) ÷ Σ(Credits) |
| **CGPA** | Σ(SGPA × Semester Credits) ÷ Σ(All Credits) |

### Default Grade Scale (4.0)

| Grade | A | A− | B+ | B | B− | C+ | C | D | F |
|-------|---|----|----|---|----|----|---|---|---|
| **Points** | 4.0 | 3.7 | 3.3 | 3.0 | 2.7 | 2.3 | 2.0 | 1.0 | 0.0 |

> The scale can be changed to match your institution's grading system.

---

## 💻 Technologies Used

- **Frontend:** React 18+, TypeScript, Vite, Tailwind CSS
- **Visualization:** Chart.js, Recharts, Lucide Icons
- **App / Backend:** Python, Streamlit
- **Deployment:** Streamlit Cloud (also works on Vercel and Netlify)

---

## 📝 License

MIT License - Free to use and modify

---

<div align="center">

**[Live Demo](https://cgpa-calculator-pgzjdgmdtuxhhuprvppvyt.streamlit.app) | [GitHub](https://github.com/kschouhanpali-coder/CGPA-Calculator) | [Report Issues](https://github.com/kschouhanpali-coder/CGPA-Calculator/issues)**

*Track grades. Calculate GPA. Visualize success.* 📊

</div>
