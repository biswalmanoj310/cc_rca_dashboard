# services/issue_service.py
from repository.issue_repository import IssueRepository
from collections import Counter

class IssueService:
    @staticmethod
    def add_new_issue(data):
        return IssueRepository.add_issue(data)

    @staticmethod
    def delete_issue(issue_id):
        return IssueRepository.delete_issue(issue_id)

    @staticmethod
    def get_dashboard_data():
        return IssueRepository.get_all_issues()

    @staticmethod
    def get_statistics():
        issues = IssueRepository.get_all_issues()
        user_stats = Counter([i.added_by for i in issues])
        category_stats = Counter([i.category for i in issues])
        return {'users': user_stats, 'categories': category_stats}

    @staticmethod
    def search(filters):
        return IssueRepository.search_issues(filters)
