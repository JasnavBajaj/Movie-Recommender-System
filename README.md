# Movie Recommender System

This project is a content-based movie recommendation system built using Python. It leverages movie metadata (including genres, keywords, cast, and crew) from the [TMDB Movie Metadata dataset](https://www.kaggle.com/tmdb/tmdb-movie-metadata) on Kaggle, and provides movie recommendations based on textual similarity. The project includes a Jupyter Notebook for data processing and model building (`movie-recommend.ipynb`) and a Streamlit web app (`app.py`) for an interactive user interface.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Environment Variables](#environment-variables)
- [Dependencies](#dependencies)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Overview

The Movie Recommender System:
- Downloads and extracts the TMDB Movie Metadata dataset using the Kaggle API.
- Processes and cleans the data (merging movie details and credits, handling missing values, and extracting useful features).
- Creates a 'tags' column that combines key textual information (overview, genres, keywords, cast, crew) and preprocesses it using stemming.
- Converts the tags into a numerical feature vector using a Count Vectorizer.
- Computes cosine similarity between movies to determine which movies are similar.
- Provides movie recommendations through a function in the notebook and an interactive Streamlit web app that also fetches movie posters via the TMDB API.

## Features

- **Data Acquisition**: Automated download and extraction of the TMDB movie dataset from Kaggle.
- **Data Processing**: Merges movie and credits data, handles missing values, and creates a comprehensive tags field.
- **NLP Processing**: Applies tokenization and stemming to improve text matching.
- **Similarity Computation**: Uses cosine similarity to find similar movies.
- **Interactive Web App**: Built with Streamlit, allowing users to select a movie and view recommendations along with movie posters.

## Dataset

- **Source**: [TMDB Movie Metadata Dataset on Kaggle](https://www.kaggle.com/tmdb/tmdb-movie-metadata)
- **Files Used**: `tmdb_5000_movies.csv` and `tmdb_5000_credits.csv`

## Installation

### 1. Clone the Repository
Clone this repository to your local machine using the following commands:
```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name

### 2. Install Required Packages:
Make sure have Python installed. Then install the necessary Python Libraries:
```bash
pip install -r requirements.txt

(Alernatively, install packages manually: `pandas`,`numpy`, `scikit-learn`, `nltk`, `streamlit`, `pickle`, and `requests`)
