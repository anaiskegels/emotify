from flask import Flask, render_template, request
app = Flask("emotify")

@app.route("/")
def hello():
    return "Emotify: Listen to your Emotions"

@app.route("/<emotion>")
    return render_template ("emotify.html", name = emotion.title() )

@app.route("/signup", methods=["POST"])
def sign_up():
    form_data = request.form
    print form_data["email"]
    return "All OK"

app.run(debug=True)
