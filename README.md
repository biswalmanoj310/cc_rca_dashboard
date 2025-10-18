# 🧠 CC-RCA Dashboard  
**Root Cause Analysis & Corrective Action Tracker**

[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0-green.svg)](https://flask.palletsprojects.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-blue.svg)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED.svg?logo=docker)](https://hub.docker.com/r/biswalmanoj310/cc_rca_dashboard)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub Repo stars](https://img.shields.io/github/stars/biswalmanoj310/cc_rca_dashboard?style=social)](https://github.com/biswalmanoj310/cc_rca_dashboard/stargazers)

A full-stack Flask + PostgreSQL web application to track software issues, perform RCA (Root Cause Analysis), and record corrective actions — complete with analytics, search, and a responsive dashboard UI.

---

## 🚀 Features

- 📋 RCA Dashboard showing all issues in tabular format  
- ➕ Add / ✏️ Edit / ❌ Delete issues  
- 🔍 Quick & Advanced Search by Category, Date, User, etc.  
- 📊 Statistics page showing:
  - Issues by Category  
  - Issues by User (`added_by`)  
  - Status distribution charts  
- 🗓️ Uses PostgreSQL for persistence  
- 🧱 Docker-based setup — one command deployment  
- 🧰 Easily extensible Flask / SQLAlchemy backend  

---

## 🏗️ Architecture Overview

| Component | Description |
|------------|-------------|
| **Flask App** | Web frontend + REST backend |
| **PostgreSQL** | Relational DB storing all issues |
| **SQLAlchemy ORM** | Database abstraction layer |
| **Docker Compose** | Orchestrates Flask + Postgres services |
| **Bootstrap / JS** | For responsive UI in templates |

---

## 📁 Folder Structure

cc_rca_dashboard/
├── app.py
├── config.py
├── extensions.py
├── models/
│ └── issue.py
├── routes/
│ └── issue_routes.py
├── templates/
│ ├── dashboard.html
│ ├── add_issue.html
│ └── statistics.html
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── pg_data_dump.sql

yaml
Copy code

---

## ⚙️ Local Setup (Without Docker)

### 1️⃣ Create and activate virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
2️⃣ Install dependencies
bash
Copy code
pip install -r requirements.txt
3️⃣ Run Flask
bash
Copy code
python app.py
Visit 👉 http://127.0.0.1:5000/cc_rca/dashboard

🐳 Docker Setup (Recommended)
1️⃣ Clone the repo
bash
Copy code
git clone https://github.com/biswalmanoj310/cc_rca_dashboard.git
cd cc_rca_dashboard
2️⃣ Build and start containers
bash
Copy code
docker compose up --build
✅ Flask runs at: http://127.0.0.1:5050/cc_rca/dashboard
✅ PostgreSQL runs at: localhost:5432

3️⃣ Stop containers
bash
Copy code
docker compose down
🧠 Database Notes
First-time setup automatically initializes PostgreSQL with sample data from:

pgsql
Copy code
pg_data_dump.sql
Your live DB is stored in a Docker volume named pgdata.

To export updated data later:

bash
Copy code
docker exec -t cc_rca_db pg_dump -U cc_rca_user cc_rca_db > pg_data_dump.sql
🧰 Environment Variables
Variable	Default	Description
POSTGRES_USER	cc_rca_user	DB username
POSTGRES_PASSWORD	cc_rca_pass	DB password
POSTGRES_DB	cc_rca_db	Database name
FLASK_ENV	production	Flask environment
DATABASE_URL	(set by Docker)	DB connection string

You can override these in a .env file for security.

🧪 Testing the Application
After running docker compose up, open your browser and verify:

http://127.0.0.1:5050/cc_rca/dashboard → shows all issues

http://127.0.0.1:5050/cc_rca/add → add new issue

http://127.0.0.1:5050/cc_rca/statistics → statistics charts

☁️ Deploying from Docker Hub
You can also run directly from the published Docker image:

bash
Copy code
docker run -d -p 5050:5000 biswalmanoj310/cc_rca_dashboard:demo
Then open 👉 http://127.0.0.1:5050/cc_rca/dashboard

💾 Backing up and Restoring Data
Backup:

bash
Copy code
docker exec -t cc_rca_db pg_dump -U cc_rca_user cc_rca_db > backup.sql
Restore:

bash
Copy code
cat backup.sql | docker exec -i cc_rca_db psql -U cc_rca_user -d cc_rca_db
📜 License

MIT License © 2025 Manoj Kumar Biswal

💡 Author
Manoj Kumar Biswal
🧑‍💻 DevOps Engineer • Toastmasters Leader • RCA Automation Architect
📧 mbiswal@juniper.net
🌐 https://github.com/biswalmanoj310

🏁 Quick Start Summary
Command	Description
docker compose up --build	Run app + PostgreSQL
docker compose down	Stop containers
pg_dump	Backup data
docker push biswalmanoj310/cc_rca_dashboard:demo	Publish image

⭐ If you find this useful, please give it a star on GitHub!

yaml
Copy code

---

## ✅ **What to do next**

1. Save this in your project root as: