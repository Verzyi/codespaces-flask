from flask import Blueprint,render_template

# Create a Blueprint for your views
projects = Blueprint('projects', __name__)


@projects.route("/projects")
def home():
    user = {'first_name': 'Chris',
            'last_name': 'Becker'}
    
    return render_template("home.html", title="Chris Becker", user=user)