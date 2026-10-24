# Student Feedback Sentiment Analysis

A Flask web app that classifies student feedback as positive, negative, or neutral using a saved scikit-learn model and TF-IDF vectorizer.

## Run locally

1. Create and activate a Python virtual environment.
2. Install dependencies with `pip install -r requirements.txt`.
3. Run `python app.py` and open `http://127.0.0.1:5000`.

The app loads `sentiment_model.pkl` and `tfidf_vectorizer.pkl` from the project root.

## Deploy to Vercel

Import this GitHub repository in Vercel and deploy it as a Python Flask app. Vercel detects the root-level `app.py` and installs packages from `requirements.txt`.
