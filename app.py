import pickle
import streamlit as st
import requests
import pandas as pd
import streamlit.components.v1 as com 
import json
from streamlit_lottie import st_lottie
from PIL import Image
from pathlib import Path

st.set_page_config(page_title="Movie_Recommend_page", page_icon=":clapper:", layout="wide")
st.title(":red[MOVIE RECOMMENDATION SYSTEM ]")
st.write("\n\n")
def load_lottieurl(url:str):
    r = requests.get(url)
    if r.status_code != 200:
        return new_func()
    return r.json()

def new_func():
    return None

def load_lottiefile(filepath:str):
    with open(filepath,encoding="utf8") as f:
        data =json.load(f)
    return data

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style.css")

lottie_coding = load_lottiefile("anime2.json")
lottie_coding2 = load_lottiefile("anime.json")

with st.container():
    left_column,right_column=st.columns(2)
    with left_column:
        st.header(":blue[ABOUT THIS PAGE]")
        st.write("##")
        st.write(
    """
    A movie recommendation website is a digital platform designed to assist users in discovering new and exciting films based on their preferences and interests. 
    These websites employ advanced algorithms and user data analysis to generate personalized movie suggestions, taking into account factors such as genre, ratings, and viewing history.
    Users can explore curated lists, read reviews, and receive tailored recommendations that cater to their individual taste
    """
        )
    with right_column:
        st_lottie(lottie_coding, height=400, key="coding")      
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=b9c898bc45906a412d91b4b96ca01e22&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters


st.header('Movie Recommender')
movies_dict= pickle.load(open('movie_list.pkl','rb'))
movies=pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])

# --- HERO SECTION ---
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://kaalaa741@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st_lottie(lottie_coding2, height=300,key="anime")
    
       
