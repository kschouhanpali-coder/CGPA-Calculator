<div align="center">

# 🎓 CGPA Calculator

### Track your semester grades. Calculate your CGPA. Visualize your progress.

A clean, modern web app for students to log subjects, credits, and grades — and instantly see their SGPA, overall CGPA, and semester-by-semester trend.

[![Live Demo](https://img.shields.io/badge/demo-live-brightgreen?style=for-the-badge&logo=streamlit&logoColor=white)](https://cgpa-calculator-pgzjdgmdtuxhhuprvppvyt.streamlit.app)
[![Made with React](https://img.shields.io/badge/frontend-React%20%2B%20TypeScript-61DAFB?style=for-the-badge&logo=react&logoColor=white)](#)
[![Made with Python](https://img.shields.io/badge/backend-Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](#)

**[🚀 View Live Demo](https://cgpa-calculator-pgzjdgmdtuxhhuprvppvyt.streamlit.app)** &nbsp;·&nbsp; **[📖 Documentation](#-how-it-works)** &nbsp;·&nbsp; **[🐛 Report a Bug](../../issues)**

</div>

---

## 🔍 At a Glance

<div align="center">

| Overall CGPA | Total Credits | Semester Tracking | Trend Insights |
|:---:|:---:|:---:|:---:|
| Auto-calculated | Live running total | Unlimited semesters | Visual SGPA graph |

</div>

---

## ✨ Features

| | |
|---|---|
| 📊 **Overall CGPA** | Automatically calculated across all tracked semesters |
| 📚 **Semester-wise SGPA** | Subject-level breakdown of credits and grades |
| ➕ **Add Unlimited Semesters** | Simple, guided flow for entering results |
| 🧮 **Live Total Credits** | See your cumulative credit count at a glance |
| 📈 **Semester Trend Chart** | Visualize how your SGPA changes over time |
| ⚡ **Instant Calculations** | No manual math — results update as you type |

---

## 🛠️ Tech Stack

<div align="center">

| Layer | Technology |
|---|---|
| **Frontend** | React · TypeScript · Vite · shadcn/ui |
| **Backend / Logic** | Python · Streamlit |
| **Deployment** | Streamlit Cloud |

</div>

> Update this table if your actual stack differs from the above.

---

## 🚀 Getting Started

### Prerequisites

- **Node.js** ≥ 18 (for the frontend)
- **Python** ≥ 3.9 (for the Streamlit app)

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/CGPA-Calculator.git
cd CGPA-Calculator

# 2. Install frontend dependencies
npm install

# 3. Install backend dependencies
pip install -r requirements.txt
```

### Running Locally

```bash
# Run the frontend
npm run dev

# Run the Streamlit app
streamlit run app.py
```

The frontend will be available at `http://localhost:3000`, and the Streamlit app will open automatically in your browser.

---

## 📁 Project Structure

```
CGPA-Calculator/
├── artifacts/
│   ├── api-server/          # Backend API (TypeScript)
│   └── cgpa-calculator/     # Frontend app (React + Vite)
├── app.py                   # Streamlit entry point
├── requirements.txt         # Python dependencies
└── README.md
```

---

## 📖 How It Works

1. Click **"+ Add semester"** to start a new semester entry
2. For each subject, enter the **name**, **credits**, and **grade**
3. Your **SGPA** for that semester is calculated automatically
4. Your **overall CGPA** and **semester trend chart** update in real time as you add more semesters

---

## 🗺️ Roadmap

- [ ] Export results as PDF
- [ ] Dark mode
- [ ] Grade prediction / "what-if" simulator
- [ ] Multi-user accounts with saved history

> Feel free to open an issue if you'd like to suggest a feature!

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the project
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request
