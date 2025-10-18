from flask import Flask, redirect, url_for
from extensions import db
from config import Config
from routes.issue_routes import bp as issue_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    from models.issue import Issue
    db.create_all()

app.register_blueprint(issue_bp, url_prefix="/cc_rca")

@app.route("/")
def root_redirect():
    return redirect(url_for("issues.dashboard"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
