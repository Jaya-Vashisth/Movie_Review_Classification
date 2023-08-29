# Movie Review Classification Project

## Table of Contents

- [Overview](#overview)
- [Usage](#usage)
- [Preprocessing](#preprocessing)
- [NLP Pipeline](#nlp-pipeline)
- [Model Training](#model-training)
- [Evaluation](#evaluation)
- [Future Work](#future-work)

## Overview

This project focuses on classifying movie reviews as either "negative" or "positive" using machine learning techniques. The dataset consists of 40,000 movie reviews labeled with their corresponding classes. The goal is to build a classification model that accurately predicts the sentiment of each review.

## Usage

1. Load the dataset: The dataset containing movie reviews and their corresponding classes ("negative" or "positive") is provided in the `data` directory.
2. Preprocessing: Class balancing and duplicate reviews are removed to ensure data quality and some other tasks.
3. Word Cloud: A word cloud is generated to visualize the most frequent words in the dataset.
4. NLP Pipeline: The text data goes through tokenization, stopword removal, and stemming to prepare it for vectorization.
5. Vectorization: The text data is transformed into numerical features using **Count Vectorization** and **TF-IDF Vectorization**.
6. Model Training: A Multinomial Naive Bayes model is trained on both vectorized datasets.
7. Evaluation: Model performance is assessed using a confusion matrix, classification report, accuracy metrics, and roc curve.

## NLP Pipeline

The following preprocessing tasks are performed:

1. Lowercasing, HTML Tag Removal, Special Character Removal, Handling Contractions, Handling Numerical Data, Handling Emojis and Special Symbols, Handling URLs 
2. Tokenization: Splitting the text into individual words or tokens.
3. Removing Stopwords: Stopwords are common words that don't contribute much to the meaning. Removing them can reduce noise and improve efficiency.
4. Stemming and Lemmatization: Stemming reduces words to their root form (e.g., "running" to "run")

The NLP pipeline consists of the following steps:

1. Tokenization: Splitting the text into individual words or tokens.
2. Stopword Removal: Filtering out common words that don't carry significant meaning.
3. Stemming: Reducing words to their root form to normalize the text.

## Model Training

- The Multinomial Naive Bayes classifier is trained on  the Count Vectorized and TF-IDF Vectorized datasets.
- The accuracy achieved on the Count Vectorized dataset is approximately 85%, and on the TF-IDF Vectorized dataset, it's nearly 86%.

## Evaluation

Model performance is evaluated using the following metrics:

- Confusion Matrix: Provides a detailed breakdown of the model's predictions.
- Classification Report: Presents precision, recall, F1-score, and support for both classes.
- Accuracy: The overall accuracy of the model's predictions.

## Future Work

In the future, we plan to explore the following:

- Experiment with various classification models (e.g., Random Forest, Support Vector Machines) to improve accuracy.
- Fine-tune hyperparameters to optimize model performance.
- Implement techniques such as cross-validation for more robust evaluation.
- Explore text preprocessing techniques and feature engineering to enhance model results.

---
