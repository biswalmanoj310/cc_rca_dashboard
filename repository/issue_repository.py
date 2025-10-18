# repository/issue_repository.py
from models.issue import Issue
from app import db

class IssueRepository:
    @staticmethod
    def add_issue(data):
        issue = Issue(**data)
        db.session.add(issue)
        db.session.commit()
        return issue

    @staticmethod
    def get_all_issues():
        return Issue.query.all()

    @staticmethod
    def get_issue_by_id(issue_id):
        return Issue.query.get(issue_id)

    @staticmethod
    def delete_issue(issue_id):
        issue = Issue.query.get(issue_id)
        if issue:
            db.session.delete(issue)
            db.session.commit()
            return True
        return False

    @staticmethod
    def search_issues(filters):
        query = Issue.query
        if 'category' in filters:
            query = query.filter_by(category=filters['category'])
        if 'added_by' in filters:
            query = query.filter_by(added_by=filters['added_by'])
        if 'status' in filters:
            query = query.filter_by(status=filters['status'])
        return query.all()
