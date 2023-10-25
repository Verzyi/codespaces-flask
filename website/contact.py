
from flask import Blueprint,render_template

# Create a Blueprint for your views
contact = Blueprint('contact', __name__)


@contact.route("/contact-info")
def home():
    user = {'first_name': 'Chris',
            'last_name': 'Becker'}
    
    return render_template("contact/contact-info.html", title="Chris Becker", user=user)