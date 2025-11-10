import joblib

from joblib import dump, load

cv = joblib.load("models/cv.joblib")
topic_clas = joblib.load("models/topic_clas.joblib")

    
def make_prediction(news):   
    tokenized_news = cv.transform([news])
    predictions = topic_clas.predict(tokenized_news)
    predictions = predictions[0]
    return predictions