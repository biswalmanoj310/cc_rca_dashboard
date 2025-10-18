from datetime import datetime
from extensions import db

class Issue(db.Model):
    __tablename__ = "issues"

    id = db.Column(db.Integer, primary_key=True)
    issue_date = db.Column(db.Date, nullable=False)
    issue_description = db.Column(db.Text, nullable=False)
    solution = db.Column(db.Text)
    root_cause = db.Column(db.Text)
    activity_type = db.Column(db.String(100))
    category = db.Column(db.String(100))
    action_items = db.Column(db.Text)
    status = db.Column(db.String(50), default="Open")
    added_by = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    @property
    def formatted_date(self):
        return self.issue_date.strftime('%b %d, %Y') if self.issue_date else ''
