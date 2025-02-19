
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
```
### 2. Install Required Packages:
Make sure you have Python installed. Then install the necessary Python libraries:
```bash
pip install -r requirements.txt
```
(Alternatively, install packages manually: `pandas`, `numpy`, `scikit-learn`, `nltk`, `streamlit`, `pickle`, and `requests`.)

### 3. Kaggle API Setup:
- Install the Kaggle API client:
  ```bash
  pip install kaggle
  ```
- Place your `kaggle.json` (downloadable from your Kaggle account) in the project root or follow the commands in the notebook to configure the credentials.

### 4. Download the Dataset:
The Jupyter Notebook (`movie-recommend.ipynb`) includes commands to download and extract the dataset from Kaggle.

## Usage

### Running the Data Processing Notebook

1. Open the Jupyter Notebook `movie-recommend.ipynb`.
2. Run the cells sequentially to:
   - Download and extract the dataset.
   - Process and clean the data.
   - Build the similarity matrix and generate the movie dictionary.
   - Save the processed data as pickle files (`movies_dict.pkl` and `similarity.pkl`)

### Running the Streamlit Web App

1. Ensure that `movies_dict.pkl` and `similarity.pkl` are present in the project folder (generated from the notebook).
2. Set your TMDB API key as an environment variable:
   ```bash
   export TMDB_API_KEY=your_tmdb_api_key_here
   ```
   (Alternatively, update the key directly in `app.py` if you prefer.)
3. Run the app:
   ```bash
   streamlit run app.py
   ```
4. The app will open in your default web browser. Use the dropdown to select a movie and click the "Recommend" button to see the recommendations along with movie posters.

## How It Works

- **Data Processing**: The notebook cleans and preprocesses the dataset, extracting features like genres, keywords, cast, and crew. It then creates a combined "tags" field for each movie.
  
- **Vectorization & Similarity**: The text data is transformed into numerical vectors using CountVectorizer, and cosine similarity is computed to find similar movies.
  
- **Recommendation**: Given a movie title, the system finds the most similar movies based on the computed similarity scores.
  
- **Web Interface**: The Streamlit app allows users to interact with the recommender system, showing movie titles and posters by fetching them from the TMDB API.


## Environment Variables

- **TMDB_API_KEY** : Required for fetching movie posters from the TMDB API. Set this variable in your environment before running the Streamlit app.

## Dependencies
- Python 3.x
- Kaggle API
- Pandas
- NumPy
- Scikit-learn
- NLTK
- Streamlit
- Requests
- Pickle (standard library)


## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
- Kaggle for providing the dataset.
- TMDB for the movie poster API.
- Open-source libraries and communities that made this project possible.


**For any questions or issues, please open an issue on the repository or contact `bjasnav@gmail.com`.**



