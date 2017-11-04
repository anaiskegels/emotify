from flask import Flask, render_template, request
app = Flask("emotify")

@app.route("/", methods=["POST"])
def hello():
    form_data = request.form
    print form_data["email"]
    return render_template ("emotify.html")

app.run(debug=True)
