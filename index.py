from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home_page.html")

@app.route("/result")
def result_page():
    return render_template("result_page.html")
    
if __name__ == "__main__":
    app.run(debug=True)