# Dependencies
from flask import Flask, render_template, request

# Set up Flask
app = Flask(__name__)

# Home page route
@app.route("/")
def index():
    return render_template("index.html")

# Results page route
@app.route("/results", methods=['POST'])
def results():
    form_data = request.form
    genres = request.form.getlist("genres")
    return render_template("results.html", form_data=form_data, genres=genres)

if __name__ == "__main__":
    app.run()