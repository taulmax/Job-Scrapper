from flask import Flask, render_template, request, send_file
from scrapper import get_jobs
from exporter import save_to_file

app = Flask("M2racle Remote Scrapper")
db = {}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/search")
def search():
    user_job = request.args.get("lang").lower()

    existing_jobs = db.get(user_job)

    if existing_jobs:
        jobs = db[user_job]
    else:
        jobs = get_jobs(user_job)
        db[user_job] = jobs

    if jobs:
        jobs_len = len(jobs)
    else:
        return render_template("nosearch.html", user_job=user_job)

    return render_template("search.html", user_job=user_job, jobs=jobs, jobs_len=jobs_len)


@app.route("/export")
def export():
    user_job = request.args.get("lang").lower()
    jobs = db.get(user_job)
    save_to_file(jobs)
    return send_file("jobs.csv", mimetype="text/csv", attachment_filename=f"{user_job}.csv", as_attachment=True)


app.run("127.0.0.1")
