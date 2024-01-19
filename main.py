# Tony website project

from flask import Flask, render_template, flash, redirect
from flask_bootstrap import Bootstrap
from forms import ContactForm
from email_sender import EmailSender
import os
from event_manager import EventManager
import gunicorn

# Initial Flask setup

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
Bootstrap(app)
email_sender = EmailSender()
event_manager = EventManager()

# Data pulled in from Google Sheets via Sheety API will populate "Events" tab

sheet_data = event_manager.get_event_data()

# Index page setup


@app.route("/", methods=["GET", "POST"])
def index():
    form = ContactForm()

    # Contact form setup

    if form.validate_on_submit():
        flash("Message successfully sent!")
        email_sender.send_email(name=form.name.data,
                                phone=form.phone.data,
                                contact_email=form.email.data,
                                message=form.message.data
                                )
        form.name.data = ""
        form.email.data = ""
        form.phone.data = ""
        form.message.data = ""
        redirect("index.html#contact")
    # else:
    #     return render_template("index.html", form=form, section="contact")
    return render_template("index.html", form=form, events=sheet_data)

# Flask run


if __name__ == "__main__":
    app.run(debug=True)
