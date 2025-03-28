import streamlit as st
import pickle
import pandas as pd
import requests

import os
API_KEY = os.getenv("TMDB_API_KEY")

# Function to fetch the movie poster from TMDB API
def fetch_poster(movie_id):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=0a132b2f4eb1ea9764bff6f8c0494b8a&language=en-US')
    data = response.json()
    return "http://image.tmdb.org/t/p/w500/" + data['poster_path']

# Load the movie data and similarity matrix
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

# Function to recommend similar movies
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []   
    recommended_movies_poster = [] 

    for i in movies_list:
        movie_id = movies.iloc[i[0]]['movie_id']  
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id)) 

    return recommended_movies, recommended_movies_poster

# Streamlit app UI
st.title('Movie Recommender System')

# Dropdown for selecting a movie
selected_movie_name = st.selectbox(
    'What do you want to Watch?',
    movies['title'].values
)

# Recommend button to get recommendations
if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)

    # Creating columns to display the recommended movies
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])
