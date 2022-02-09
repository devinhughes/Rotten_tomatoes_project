# Dependencies
from flask import Flask, render_template, request
import predicting

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
    prediction = predicting.predict(form_data)
    return render_template("results.html", form_data=form_data, genres=genres, prediction=prediction)

if __name__ == "__main__":
    app.run()