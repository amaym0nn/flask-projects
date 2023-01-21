from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello", methods=["GET", "POST"])
def hello():
    if request.method == "POST":
        name = request.form.get("name")
        surname = request.form.get("surname")
        return render_template("hello.html", name = name, surname = surname)
    else:
        return render_template("hello.html")
    
if __name__ == "__main__":
    app.run(debug = True)