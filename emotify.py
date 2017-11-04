from flask import Flask, render_template, request
app = Flask("emotify")

@app.route("/")
def welcome():
    return render_template ("emotify.html")

@app.route("/", methods=["POST"])
def sign_up():
    form_data = request.form
    print form_data["email"]
    return "Go check your inbox!"

app.run(debug=True)
