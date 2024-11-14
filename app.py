import pickle

import pandas as pd
import streamlit as st


def recommend(movie):
    movies_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movies_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movie_names = []
    for i in movies_list:
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names

movies_dict = pickle.load(open("model/movies.pkl",'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('model/similarity.pkl','rb'))

st.title("Movie Recommender System")

selected_movie_name = st.selectbox(
    "Similar to which of the following movie: ",
    movies['title'].values
)

if st.button('Show Recommendation'):
    recommended_movie_names= recommend(selected_movie_name)
    for i in recommended_movie_names:
        st.write(i)




