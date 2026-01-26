# 🛡️ Debug Arena

### Real-Time Competitive Debugging Platform

**Debug Arena** is a secure, real-time competitive debugging platform built for live coding events and hackathons. It challenges participants to identify and fix logical and syntactical bugs in Python code under strict proctoring conditions.

Designed for **on-site competitive events at SNS College of Technology**, the platform combines automated evaluation, anti-cheat enforcement, and real-time scoring to ensure fairness, speed, and engagement.

---

## 🎯 Project Objective

To simulate a **high-pressure competitive coding environment** where teams must debug faulty code efficiently while adhering to strict security and integrity rules—mirroring real-world technical interviews and contests.

---

## 🚀 Key Features

### ⚙️ Automated Evaluation Engine

* Executes submitted Python code in a controlled environment
* Compares output against predefined expected results
* Supports multi-level progressive difficulty

### 🔐 Proctoring & Anti-Cheat System (`proctor.js`)

* Mandatory fullscreen enforcement
* Detects tab switching, window blur, and focus loss
* Automatically disqualifies teams after **3 violations**

### 🏆 Real-Time Leaderboard

* Live score updates across all teams
* Scoring based on:

  * Completion time
  * Level difficulty
  * Hint usage penalties

### 🧠 Intelligent Hint System (Oracle)

* Secure modal-based hints
* Logical guidance instead of direct answers
* Score penalties applied per hint usage

### 🛠️ Admin Controls

* Manual team reset and session management
* CLI-based administrative overrides
* Level locking and progression control

### 🎨 Modern UI/UX

* Dark-themed competitive dashboard
* Responsive layout optimized for large screens
* Developer-focused design for reduced distraction

---

## 🛠️ Tech Stack

### Backend

* **Python**
* **Flask**
* **SQLAlchemy**

### Frontend

* **HTML / Jinja Templates**
* **Tailwind CSS**
* **JavaScript**
* **CodeMirror** (In-browser IDE)

### Database

* **SQLite** (Development)
* **PostgreSQL** (Production-ready)

---

## 🏗️ System Architecture Overview

```text
Client Browser
     │
     ▼
Proctor.js (Security Layer)
     │
     ▼
Flask Middleware (Gatekeeper)
     │
     ├── Authentication & Session Control
     ├── Level Access Validation
     ├── Violation Tracking
     │
     ▼
Evaluation Engine
     │
     ▼
Leaderboard & Scoring System
```

### Core Modules

1. **Authentication Layer** – Secure team-based login system
2. **Gatekeeper Middleware** – Blocks users after violation threshold
3. **Arena (IDE)** – Interactive debugging interface
4. **Oracle** – Controlled hint delivery with penalties

---

## 🏁 Getting Started (Local Setup)

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Priyadharshan-19/DebugArena.git
cd DebugArena
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Application

```bash
python app.py
```

The app will be available at:

```
http://127.0.0.1:5000
```

---

## 🧪 Challenge Design

* Levels are structured from **basic syntax errors** to **complex logical flaws**
* Each level includes:

  * Buggy source code
  * Expected output
  * Optional hints with penalties
* Designed to scale from **beginner to advanced debugging skills**

> *(Level 1–8 challenge documentation can be added here)*

---

## 🎓 Academic & Event Use

This project is purpose-built for:

* Inter-college coding competitions
* Technical symposiums
* Debugging rounds in hackathons
* Internal assessments and lab evaluations

---

## 👨‍💻 Developer

**Priyadharshan M**
2nd Year – Computer Science & Engineering @
SNS College of Technology

---

## 📌 License

This project is intended for academic and educational use.
Commercial usage requires explicit permission.

