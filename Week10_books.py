import streamlit as st
import random

# Simplified Database of Books
gabriela_books = {
    "Angry": [
        {"title": "Living a Feminist Life", "author": "Sara Ahmed"},
        {"title": "Silent Spring", "author": "Rachel Carson"}
    ],
    "Sporty": [
        {"title": "On Boxing", "author": "Joyce Carol Oates"}
    ],
    "Crying": [
        {"title": "On Earth We're Briefly Gorgeous", "author": "Ocean Vuong"},
        {"title": "The Memory Police", "author": "Yōko Ogawa"}
    ],
    "Relaxed": [
        {"title": "On Love", "author": "Alain de Botton"},
        {"title": "Outliers", "author": "Malcolm Gladwell"}
    ],
    "Old-Fashioned": [
        {"title": "Sense and Sensibility", "author": "Jane Austen"},
        {"title": "Toddler-Hunting & Other Stories", "author": "Take Kōno"}
    ]
}

# Streamlit App
st.title("📚 Gabriela's Book Recommender")
st.write("Choose a mood, and we'll recommend a book!")

# Choose a mood
mood = st.selectbox("What's your current vibe?", list(gabriela_books.keys()))

# Generate recommendation
if st.button("Recommend a Book"):
    book = random.choice(gabriela_books[mood])
    st.success(f"📖 **{book['title']}** by *{book['author']}* is a great match for your **{mood}** vibe!")

# Footer
st.write("Let me know if you like my recommendations, friends!")