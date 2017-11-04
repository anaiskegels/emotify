from flask import Flask, render_template, request
import requests
app = Flask("emotify")

@app.route("/signup")
def email_signup():
    return render_template("sign_up_fml.html")

@app.route("/signup", methods=["POST"])
def sign_up():
    form_data = request.form
    email = form_data["email"]
    response = send_email(email)
    return "Go check your email inbox!"

def send_email(email_to_send_to):
    requests.post(
        "https://api.mailgun.net/v3/sandbox9bb315e881744729a13adf99f9ebee46.mailgun.org/messages",
        auth=("api", "key-cf11104f1ced99b7257fb8c41e5af8ca"),
        data={"from": "Mailgun Sandbox <postmaster@sandbox9bb315e881744729a13adf99f9ebee46.mailgun.org>",
              "to": "Anais Kegels <anais@touchsurgery.com>",
              "subject": "Your mood song picked by Emotify",
              "text": "Hey there! Here is your handpicked song to suit your mood: "})
    return render_template ("sign_up_fml.html")

app.run(debug=True)
