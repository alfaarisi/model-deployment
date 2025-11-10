from flask import Flask, render_template, request, jsonify
from utils import make_prediction


app = Flask(__name__)

@app.route("/") # creates the url or the name of the page
def home():
    
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    news = request.form.get('content')
    predictions = make_prediction(news)
    

    return render_template("index.html", predictions = predictions, news=news )

@app.route("/api/predict", methods=["POST"])
def predict_api():
    data = request.get_json(force=True) # get data posted as a json
    news = data["content"]
    predictions = make_prediction(news)
    return jsonify({'predictions': predictions, 'news': news})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True) # debug=True so our updates can reflect
