🎓 Sentiment Analysis Using Web Scraping – Aditya University

📌 Project Overview

Sentiment Analysis Using Web Scraping is a Machine Learning project developed to analyze student feedback and comments related to Aditya University.

The main objective of this project is to collect student opinions, preprocess textual data, and classify feedback into three sentiment categories:

- 😊 Positive
- 😐 Neutral
- 😞 Negative

The project uses Natural Language Processing (NLP) techniques and Machine Learning algorithms to understand student opinions about different aspects of the university, such as faculty, infrastructure, hostel facilities, academics, and campus environment.

A web-based application developed using Flask allows users to enter student comments and view the predicted sentiment.

🎯 Project Objectives

- Collect student feedback related to Aditya University using web scraping.
- Perform data preprocessing and cleaning.
- Identify and handle missing values, null values, and duplicate records.
- Apply text preprocessing techniques such as tokenization.
- Convert text into numerical features using TF-IDF.
- Train and evaluate multiple Machine Learning algorithms.
- Compare model performance using evaluation metrics.
- Develop a user-friendly sentiment analysis website.

🛠️ Technologies Used

Technology| Purpose
Python| Programming language
Jupyter Notebook| Model development
Pandas| Data manipulation
NumPy| Numerical operations
Matplotlib| Data visualization
Seaborn| Statistical visualization
BeautifulSoup| Web scraping
Scikit-learn| Machine Learning
NLP| Text preprocessing
Flask| Web application development
HTML & CSS| Website interface

📂 Dataset Description

The dataset contains student feedback and comments related exclusively to Aditya University.

It includes 15 attributes describing student feedback, platform information, student details, and sentiment-related information.

The dataset is used for data cleaning, exploratory data analysis, feature extraction, and sentiment classification.

Dataset preprocessing includes:

- Missing value identification and handling.
- Null value handling.
- Duplicate record detection and removal.
- Data type checking.
- Text cleaning and normalization.

🔄 Project Workflow

1. Data Collection Using Web Scraping
2. Dataset Loading
3. Exploratory Data Analysis (EDA)
4. Data Preprocessing
5. Missing Values and Duplicate Removal
6. Text Cleaning
7. Tokenization
8. TF-IDF Feature Extraction
9. Train-Test Splitting
10. Machine Learning Model Training
11. Ensemble Voting Classification
12. Model Evaluation
13. Data Visualization
14. Sentiment Prediction
15. Flask Web Application Development

🧹 Data Preprocessing

The following preprocessing techniques are performed:

- Checking missing values.
- Handling null values.
- Removing duplicate records.
- Removing unnecessary text and special characters.
- Converting text into lowercase.
- Tokenization.
- Removing unnecessary words where appropriate.
- TF-IDF vectorization.

🤖 Machine Learning Algorithms

Four classification approaches are implemented in this project.

1. Logistic Regression

Logistic Regression is used as a classification algorithm to predict the sentiment of student feedback.

2. Support Vector Machine (SVM)

SVM classifies student comments into sentiment categories by identifying decision boundaries between classes.

3. Random Forest Classifier

Random Forest uses multiple decision trees to perform sentiment classification and combine their predictions.

4. Ensemble Voting Classifier

The Ensemble Voting Classifier combines the predictions of:

- Logistic Regression
- Support Vector Machine
- Random Forest

Hard voting is used to select the final sentiment based on majority voting among the three models.

📊 Model Evaluation

The performance of the trained models is evaluated using the following metrics:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix
- ROC Curve and AUC

The four models are compared to identify their performance on the test dataset.

📈 Data Visualization

The project includes graphical representations such as:

- Missing Values Visualization
- Duplicate Records Analysis
- Box Plot
- Sentiment Distribution Graph
- Confusion Matrices
- ROC Curves
- Precision, Recall and F1-Score Comparison
- Model Accuracy Comparison
- Top 10 Important TF-IDF Features

These visualizations help understand the dataset and compare the performance of different Machine Learning models.

🌐 Web Application

A Flask-based web application is developed for sentiment prediction.

Main functionality:

1. User enters a student comment.
2. The comment is converted into TF-IDF features.
3. The trained Machine Learning model predicts its sentiment.
4. The predicted sentiment is displayed on the website.

The application provides an interactive interface for testing new student comments.

📁 Project Structure

Sentiment_Analysis_Project/
│
├── dataset/
│ └── aditya_university_dataset.csv
│
├── models/
│ ├── logistic_model.pkl
│ ├── svm_model.pkl
│ ├── random_forest_model.pkl
│ └── tfidf_vectorizer.pkl
│
├── templates/
│ └── index.html
│
├── static/
│ └── style.css
│
├── app.py
├── requirements.txt
├── README.md
│
└── Sentiment_Analysis.ipynb

Note: Adjust the filenames and folder structure according to your actual project files.

⚙️ Installation and Setup

Step 1: Clone the Repository

git clone https://github.com/your-username/Sentiment-Analysis-Using-Web-Scraping.git

Step 2: Navigate to Project Folder

cd Sentiment-Analysis-Using-Web-Scraping

Step 3: Install Required Libraries

pip install pandas numpy matplotlib seaborn scikit-learn flask beautifulsoup4 joblib

Step 4: Run Jupyter Notebook

jupyter notebook

Open the "Sentiment_Analysis.ipynb" notebook and execute the cells in order.

Step 5: Run Flask Application

python app.py

Open your browser and visit:

http://127.0.0.1:5000

🔮 Future Enhancements

- Collect feedback from additional university-related sources.
- Improve classification performance using advanced NLP techniques.
- Implement real-time sentiment analysis.
- Add interactive dashboards.
- Include more Machine Learning and Deep Learning algorithms.
- Deploy the application on a cloud platform.

🎓 Conclusion

This project demonstrates how Machine Learning and Natural Language Processing can be used to analyze student feedback related to Aditya University.

By combining web scraping, data preprocessing, TF-IDF feature extraction, and multiple classification algorithms, the system identifies student sentiment and provides useful insights into student opinions.

The Flask-based web application makes sentiment prediction accessible through a simple user interface.

👩‍💻 Project Information

Project Title: Sentiment Analysis Using Web Scraping

Domain: Machine Learning and Natural Language Processing

Programming Language: Python

Application Framework: Flask

Dataset Focus: Aditya University Student Feedback

Algorithms: Logistic Regression, SVM, Random Forest, Ensemble Voting Classifier

Development Environment: Jupyter Notebook

---

⭐ If you find this project useful, consider giving this repository a star!
