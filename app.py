from flask import Flask, render_template, send_file
import os

app = Flask(__name__)

LOG_FILE = "logs.txt"

@app.route("/")
def home():

    logs = []

    new_count = 0
    modified_count = 0
    deleted_count = 0

    if os.path.exists(LOG_FILE):

        with open(LOG_FILE, "r") as file:

            logs = file.readlines()

            logs.reverse()

    for log in logs:

        if "NEW FILE" in log:

            new_count += 1

        elif "MODIFIED" in log:

            modified_count += 1

        elif "DELETED" in log:

            deleted_count += 1

    total_events = (
        new_count +
        modified_count +
        deleted_count
    )

    return render_template(

        "index.html",

        logs=logs,

        total_events=total_events,

        new_count=new_count,

        modified_count=modified_count,

        deleted_count=deleted_count
    )

@app.route("/download")
def download():

    return send_file(
        "logs.txt",
        as_attachment=True
    )

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )