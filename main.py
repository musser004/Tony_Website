# Tony website project

from flask import Flask, render_template, flash, redirect
from flask_bootstrap import Bootstrap
from forms import ContactForm
from email_sender import EmailSender
import os
import gunicorn

# Initial Flask setup

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
Bootstrap(app)
email_sender = EmailSender()

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
    return render_template("index.html", form=form)

# Flask run


if __name__ == "__main__":
    app.run(debug=True)