from flask import Flask, render_template, request
import pickle
import re
import string
import math

app = Flask(__name__)

# Load model
with open("sentiment_model.pkl", "rb") as file:
    model = pickle.load(file)

# Load TF-IDF
with open("tfidf_vectorizer.pkl", "rb") as file:
    tfidf = pickle.load(file)


def preprocess_text(text):

    text = text.lower()

    text = re.sub(r"http\S+|www\S+|https\S+", "", text)

    text = text.translate(
        str.maketrans("", "", string.punctuation)
    )

    text = re.sub(r"\d+", "", text)

    text = re.sub(r"\s+", " ", text).strip()

    return text


def _softmax(scores):
    max_score = max(scores)
    exp_scores = [math.exp(score - max_score) for score in scores]
    total = sum(exp_scores)
    return [score / total for score in exp_scores]


def get_sentiment_percentages(text_vector):
    classes = list(model.classes_)

    if hasattr(model, "predict_proba"):
        probabilities = model.predict_proba(text_vector)[0]
    elif hasattr(model, "decision_function"):
        scores = model.decision_function(text_vector)
        scores = scores[0] if getattr(scores, "ndim", 1) > 1 else scores

        if len(classes) == 2 and not hasattr(scores, "__len__"):
            positive_probability = 1 / (1 + math.exp(-float(scores)))
            probabilities = [1 - positive_probability, positive_probability]
        else:
            probabilities = _softmax([float(score) for score in scores])
    else:
        predicted_class = model.predict(text_vector)[0]
        probabilities = [
            1.0 if sentiment_class == predicted_class else 0.0
            for sentiment_class in classes
        ]

    raw_percentages = {
        str(sentiment_class).lower(): round(float(probability) * 100, 2)
        for sentiment_class, probability in zip(classes, probabilities)
    }

    return {
        "positive": raw_percentages.get("positive", 0),
        "negative": raw_percentages.get("negative", 0),
        "neutral": raw_percentages.get("neutral", 0),
    }


@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None
    percentages = None
    comment = ""

    if request.method == "POST":

        print("POST request received!")

        comment = request.form.get("comment", "")

        print("Comment:", comment)

        if comment.strip():

            cleaned_text = preprocess_text(comment)

            print("Cleaned text:", cleaned_text)

            text_vector = tfidf.transform([cleaned_text])

            prediction = model.predict(text_vector)[0]
            percentages = get_sentiment_percentages(text_vector)

            print("Prediction:", prediction)
            print("Percentages:", percentages)

    return render_template(
        "index.html",
        prediction=prediction,
        percentages=percentages,
        comment=comment
    )


if __name__ == "__main__":
    app.run(debug=True)
