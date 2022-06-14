from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "flgkjfgohlfghgg"

@app.route("/hello")
def Index():
	flash("What's your name?")
	return render_template("Index.html")

@app.route("/greet", methods=["POST", "GET"])
def greet():
	flash("Hello " + str(request.form['name_input']) + ", nice to see you!")
	return render_template("Index.html")

	