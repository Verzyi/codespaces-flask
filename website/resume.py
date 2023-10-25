
from flask import Blueprint,render_template

# Create a Blueprint for your views
resume = Blueprint('resume', __name__)



@resume.route("/resume")
def myResume():
    user = {'first_name': 'Chris',
            'last_name': 'Becker'}

    return render_template("/resume/resume.html", title="Chris Becker", user=user)


