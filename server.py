"""
SwarmForgeAI demo server — public landing + login-gated app surface.
Run: python server.py
"""
import os
from pathlib import Path

from dotenv import load_dotenv
from flask import Flask, redirect, render_template_string, request, session, url_for, abort, send_file

load_dotenv()

app = Flask(__name__)

if not os.getenv("FLASK_SECRET"):
    raise ValueError("FLASK_SECRET environment variable is required.")
if not os.getenv("APP_USERNAME") or not os.getenv("APP_PASSWORD"):
    raise ValueError("APP_USERNAME and APP_PASSWORD environment variables are required.")

app.secret_key = os.getenv("FLASK_SECRET")
app.permanent_session_lifetime = 60 * 60 * 8
app.config.update(
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE="Lax",
)

USERNAME = os.getenv("APP_USERNAME")
PASSWORD = os.getenv("APP_PASSWORD")
BASE_DIR = Path(__file__).parent

LOGIN_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>SwarmForgeAI — Sign In</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    font-family: 'Inter', sans-serif;
    min-height: 100vh;
    background: radial-gradient(circle at top, #172554 0%, #020617 58%, #020617 100%);
    color: #e2e8f0;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 24px;
  }
  .card {
    width: 100%;
    max-width: 420px;
    background: rgba(15, 23, 42, 0.92);
    border: 1px solid rgba(148, 163, 184, 0.18);
    border-radius: 20px;
    padding: 32px;
    box-shadow: 0 24px 60px rgba(0, 0, 0, 0.42);
  }
  .eyebrow { color: #93c5fd; font-size: 12px; letter-spacing: 0.18em; text-transform: uppercase; margin-bottom: 10px; }
  h1 { font-size: 28px; margin-bottom: 10px; }
  p { color: #94a3b8; line-height: 1.6; margin-bottom: 24px; }
  label { display: block; margin-bottom: 8px; font-size: 14px; color: #cbd5e1; }
  input {
    width: 100%;
    padding: 12px 14px;
    border-radius: 12px;
    border: 1px solid rgba(148, 163, 184, 0.18);
    background: rgba(15, 23, 42, 0.92);
    color: #e2e8f0;
    font-size: 15px;
    margin-bottom: 16px;
  }
  input:focus { outline: none; border-color: #60a5fa; }
  button {
    width: 100%;
    border: none;
    border-radius: 12px;
    background: linear-gradient(135deg, #38bdf8, #2563eb);
    color: white;
    padding: 13px 16px;
    font-size: 15px;
    font-weight: 700;
    cursor: pointer;
  }
  button:hover { filter: brightness(1.06); }
  .error {
    margin-bottom: 16px;
    padding: 12px 14px;
    border-radius: 12px;
    background: rgba(127, 29, 29, 0.35);
    border: 1px solid rgba(248, 113, 113, 0.35);
    color: #fecaca;
    font-size: 14px;
  }
  .back { display: inline-block; margin-top: 18px; color: #93c5fd; text-decoration: none; font-size: 14px; }
</style>
</head>
<body>
  <div class="card">
    <div class="eyebrow">SimpliCoreAI</div>
    <h1>SwarmForgeAI Login</h1>
    <p>Sign in to access the protected hospitality operator demo. Public visitors should start on the main landing page.</p>
    {% if error %}<div class="error">{{ error }}</div>{% endif %}
    <form method="post">
      <label>Username</label>
      <input type="text" name="username" autocomplete="username" autofocus>
      <label>Password</label>
      <input type="password" name="password" autocomplete="current-password">
      <button type="submit">Enter demo</button>
    </form>
    <a class="back" href="/">← Back to SwarmForgeAI</a>
  </div>
</body>
</html>
"""


def login_required(f):
    def wrapped(*args, **kwargs):
        if not session.get("logged_in"):
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    wrapped.__name__ = f.__name__
    return wrapped


@app.route("/")
def index():
    landing_path = BASE_DIR / "public" / "index.html"
    if not landing_path.exists():
        abort(404)
    return landing_path.read_text()


@app.route("/home")
def home():
    return redirect(url_for("index"), code=302)


@app.route("/login", methods=["GET", "POST"])
def login():
    if session.get("logged_in"):
        return redirect(url_for("app_demo"), code=303)

    error = None
    if request.method == "POST":
        if request.form.get("username") == USERNAME and request.form.get("password") == PASSWORD:
            session.permanent = True
            session["logged_in"] = True
            return redirect(url_for("app_demo"), code=303)
        error = "Invalid username or password."
    return render_template_string(LOGIN_HTML, error=error)


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"), code=303)


@app.route("/support")
@login_required
def support_center():
    support_path = BASE_DIR / "protected" / "support.html"
    if not support_path.exists():
        abort(404)
    return support_path.read_text(encoding="utf-8")


@app.route("/support-logo")
@login_required
def support_logo():
    logo_path = BASE_DIR / "protected" / "assets" / "swarmforge-logo.jpg"
    if not logo_path.exists():
        abort(404)
    return send_file(logo_path, mimetype="image/jpeg", conditional=True)


@app.route("/app")
@login_required
def app_demo():
    app_path = BASE_DIR / "protected" / "hotel-demo.html"
    if not app_path.exists():
        abort(404)
    return app_path.read_text()


@app.route("/demo/")
def legacy_demo_slash_redirect():
    return redirect(url_for("app_demo"), code=302)


@app.route("/demo")
def legacy_demo_redirect():
    return redirect(url_for("app_demo"), code=302)


BLOG_PAGES = {
    "index": "index.html",
    "agent-booking-channel": "agent-booking-channel.html",
    "trust-layer": "trust-layer.html",
    "ai-desk": "ai-desk.html",
}

SUITE_PAGES = {
    "morning-brief": "morning-brief.html",
    "approvals-desk": "approvals-desk.html",
    "weekly-opportunities": "weekly-opportunities.html",
    "owner-view": "owner-view.html",
}


def blog_html(slug):
    filename = BLOG_PAGES.get(slug)
    if not filename:
        abort(404)
    path = BASE_DIR / "public" / "blog" / filename
    if not path.is_file():
        abort(404)
    return path.read_text(encoding="utf-8")


@app.route("/blog")
def blog_index_redirect():
    return redirect("/blog/", code=302)


@app.route("/blog/")
def blog_index():
    return blog_html("index")


@app.route("/blog/<page>")
def blog_page(page):
    slug = page[:-5] if page.endswith(".html") else page
    return blog_html(slug)


def suite_html(slug):
    filename = SUITE_PAGES.get(slug)
    if not filename:
        abort(404)
    path = BASE_DIR / "public" / "suite" / filename
    if not path.is_file():
        abort(404)
    return path.read_text(encoding="utf-8")


@app.route("/suite")
def suite_index_redirect():
    return redirect("/#suite", code=302)


@app.route("/suite/<page>")
def suite_page(page):
    slug = page[:-5] if page.endswith(".html") else page
    return suite_html(slug)


if __name__ == "__main__":
    port = int(os.getenv("PORT", "8877"))
    print(f"SwarmForgeAI server starting on http://0.0.0.0:{port}")
    app.run(host="0.0.0.0", port=port, debug=False)
