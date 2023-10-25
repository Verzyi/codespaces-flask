
from flask import Blueprint,render_template

# Create a Blueprint for your views
contact = Blueprint('contact', __name__)


@contact.route("/")
def home():
    user = {'first_name': 'Chris',
            'last_name': 'Becker'}
    
    return render_template("home.html", title="Chris Becker", user=user)