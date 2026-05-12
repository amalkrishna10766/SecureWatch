from flask import Flask, render_template, request, redirect

app = Flask(__name__)

USERNAME = "admin"
PASSWORD = "secure123"

@app.route('/', methods=['GET', 'POST'])
def login():

    error = ""

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        if username == USERNAME and password == PASSWORD:

            return redirect("http://127.0.0.1:5000")

        else:

            error = "Invalid Credentials"

    return render_template(
        'login.html',
        error=error
    )

if __name__ == '__main__':

    app.run(
        host="0.0.0.0",
        port=3000,
        debug=True
    )