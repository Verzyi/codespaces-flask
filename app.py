from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def hello_world():
    user = {'first_name': 'Chris',
            'last_name': 'Becker'}
    
    return render_template("home.html", title="Chris Becker", user=user)



