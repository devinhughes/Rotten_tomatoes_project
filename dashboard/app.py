# Dependencies
from flask import Flask, render_template

# Set up Flask
app = Flask(__name__)

# Home page route
@app.route("/")
def index():
    return render_template("index.html")

# Results page route
@app.route("/results")
def results():
    return render_template("results.html")

if __name__ == "__main__":
    app.run()