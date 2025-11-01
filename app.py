from flask import Flask, render_template, request, jsonify
import joblib
from joblib import dump, load

cv = joblib.load("models/cv.joblib")
topic_clas = joblib.load("models/topic_clas.joblib")
app = Flask(__name__)

@app.route("/") # creates the url or the name of the page
def home():
    
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        news = request.form.get('content')
    tokenized_news = cv.transform([news])
    predictions = topic_clas.predict(tokenized_news)
    predictions = predictions[0]

    return render_template("index.html", predictions = predictions, news=news )

@app.route("/api/predict", methods=["POST"])
def predict_api():
    data = request.get_json(force=True) # get data posted as a json
    news = data["content"]
    tokenized_news = cv.transform([news]) # X
    predictions = topic_clas.predict(tokenized_news)
    predictions = predictions[0]
    return jsonify({'predictions': predictions, 'news': news})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True) # debug=True so our updates can reflect
