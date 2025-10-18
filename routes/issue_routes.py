from flask import Blueprint, render_template, request, redirect, url_for, flash
from datetime import datetime
from extensions import db
from models.issue import Issue

bp = Blueprint("issues", __name__)

@bp.route("/")
def index_redirect():
    return redirect(url_for("issues.dashboard"))

@bp.route("/dashboard")
def dashboard():
    issues = Issue.query.all()
    return render_template("dashboard.html", issues=issues)

@bp.route("/add", methods=["GET", "POST"])
def add_issue():
    if request.method == "POST":
        issue = Issue(
            issue_date=datetime.strptime(request.form["issue_date"], "%Y-%m-%d"),
            issue_description=request.form["issue_description"],
            solution=request.form.get("solution"),
            root_cause=request.form.get("root_cause"),
            activity_type=request.form.get("activity_type"),
            category=request.form.get("category"),
            action_items=request.form.get("action_items"),
            status=request.form.get("status"),
            added_by=request.form.get("added_by"),
        )
        db.session.add(issue)
        db.session.commit()
        flash("✅ Issue added successfully!")
        return redirect(url_for("issues.dashboard"))
    return render_template("add_issue.html")


@bp.route("/edit/<int:issue_id>", methods=["GET", "POST"])
def edit_issue(issue_id):
    issue = Issue.query.get_or_404(issue_id)

    if request.method == "POST":
        issue.issue_date = datetime.strptime(request.form["issue_date"], "%Y-%m-%d")
        issue.issue_description = request.form["issue_description"]
        issue.solution = request.form.get("solution")
        issue.root_cause = request.form.get("root_cause")
        issue.activity_type = request.form.get("activity_type")
        issue.category = request.form.get("category")
        issue.action_items = request.form.get("action_items")
        issue.status = request.form.get("status")
        issue.added_by = request.form.get("added_by")

        db.session.commit()
        flash(f"✅ Issue #{issue_id} updated successfully!")
        return redirect(url_for("issues.dashboard"))

    return render_template("edit_issue.html", issue=issue)




@bp.route("/delete/<int:issue_id>")
def delete_issue(issue_id):
    issue = Issue.query.get(issue_id)
    if issue:
        db.session.delete(issue)
        db.session.commit()
        flash(f"Issue #{issue_id} deleted successfully.")
    else:
        flash("⚠️ Issue not found.")
    return redirect(url_for("issues.dashboard"))

@bp.route("/statistics")
def statistics():
    issues = Issue.query.all()
    user_stats = {}
    category_stats = {}

    for issue in issues:
        user_stats[issue.added_by] = user_stats.get(issue.added_by, 0) + 1
        category_stats[issue.category] = category_stats.get(issue.category, 0) + 1

    stats = {"users": user_stats, "categories": category_stats}
    return render_template("statistics.html", stats=stats)

@bp.route("/search", methods=["GET"])
def search():
    query = Issue.query
    added_by = request.args.get("added_by")
    category = request.args.get("category")
    status = request.args.get("status")

    if added_by:
        query = query.filter(Issue.added_by.ilike(f"%{added_by}%"))
    if category:
        query = query.filter(Issue.category.ilike(f"%{category}%"))
    if status:
        query = query.filter(Issue.status == status)

    issues = query.all()
    flash(f"Showing {len(issues)} result(s) for your search.")
    return render_template("dashboard.html", issues=issues)
