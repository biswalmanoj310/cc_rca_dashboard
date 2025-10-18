"""
migrate_sqlite_to_postgres.py
---------------------------------
This script migrates all data from your existing SQLite database (issues.db)
to your PostgreSQL database (running in Docker).

Requirements:
- Your models.issue.Issue class must already be defined
- PostgreSQL must be running and reachable
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.issue import Issue
import os

# ---- Configuration ----
SQLITE_DB_PATH = os.path.join(os.path.dirname(__file__), "issues.db")
SQLITE_URI = f"sqlite:///{SQLITE_DB_PATH}"

POSTGRES_URI = "postgresql+psycopg2://cc_rca_user:cc_rca_pass@localhost:5432/cc_rca_db"
# ⚠️ If running from inside Docker, change localhost → db
# POSTGRES_URI = "postgresql+psycopg2://cc_rca_user:cc_rca_pass@db:5432/cc_rca_db"

# ---- Create database engines ----
sqlite_engine = create_engine(SQLITE_URI)
postgres_engine = create_engine(POSTGRES_URI)

# ---- Create sessions ----
SQLiteSession = sessionmaker(bind=sqlite_engine)
PostgresSession = sessionmaker(bind=postgres_engine)

sqlite_session = SQLiteSession()
postgres_session = PostgresSession()

print("🔍 Reading data from SQLite...")

try:
    issues = sqlite_session.query(Issue).all()
    print(f"✅ Found {len(issues)} issues in SQLite.")
except Exception as e:
    print(f"❌ Error reading from SQLite: {e}")
    sqlite_session.close()
    postgres_session.close()
    exit(1)

print("🚀 Migrating data to PostgreSQL...")

count = 0
for issue in issues:
    new_issue = Issue(
        issue_date=issue.issue_date,
        issue_description=issue.issue_description,
        solution=issue.solution,
        root_cause=issue.root_cause,
        activity_type=issue.activity_type,
        category=issue.category,
        action_items=issue.action_items,
        status=issue.status,
        added_by=issue.added_by,
    )
    postgres_session.add(new_issue)
    count += 1

try:
    postgres_session.commit()
    print(f"✅ Successfully migrated {count} issues to PostgreSQL.")
except Exception as e:
    print(f"❌ Error committing to PostgreSQL: {e}")
    postgres_session.rollback()
finally:
    sqlite_session.close()
    postgres_session.close()

print("🎉 Migration complete!")
