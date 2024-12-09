import streamlit as st
import random

# Updated Database of books for each "Gabriela" with moods narrowed to 5
gabriela_moods = {
    "Like getting angry": [
        {"title": "Living a Feminist Life", "author": "Sara Ahmed", "mood": "motivational", "length": "medium"},
        {"title": "Borderlands/La Frontera: The New Mestiza", "author": "Gloria E. Anzaldúa", "mood": "thought-provoking", "length": "long"},
        {"title": "Silent Spring", "author": "Rachel Carson", "mood": "informative", "length": "medium"}
    ],
    "Like watching sports": [
        {"title": "On Boxing", "author": "Joyce Carol Oates", "mood": "motivational", "length": "short"}
    ],
    "Like crying": [
        {"title": "On Earth We're Briefly Gorgeous", "author": "Ocean Vuong", "mood": "introspective", "length": "medium"},
        {"title": "The Memory Police", "author": "Yōko Ogawa", "mood": "thought-provoking", "length": "medium"},
        {"title": "Una canción de Bob Dylan en la agenda de mi madre", "author": "Sergio Galarza", "mood": "nostalgic", "length": "short"},
        {"title": "La personalidad de los pelícanos", "author": "Sergio Galarza", "mood": "introspective", "length": "short"},
        {"title": "El Último Vuelo del Flamenco", "author": "Mia Couto", "mood": "motivational", "length": "medium"},
        {"title": "Del cielo a casa", "author": "Hebe Uhart", "mood": "introspective", "length": "medium"},
        {"title": "What We Talk About When We Talk About Love", "author": "Raymond Carver", "mood": "thought-provoking", "length": "short"},
        {"title": "Loco afán: Crónicas del sidario", "author": "Pedro Lemebel", "mood": "motivational", "length": "medium"}
    ],
    "Like listening and not reading": [
        {"title": "On Love", "author": "Alain de Botton", "mood": "informative", "length": "short"},
        {"title": "Outliers", "author": "Malcolm Gladwell", "mood": "informative", "length": "medium"},
        {"title": "Grit", "author": "Angela Duckworth", "mood": "motivational", "length": "long"}
    ],
    "Very old fashioned": [
        {"title": "Toddler-Hunting & Other Stories", "author": "Take Kōno", "mood": "introspective", "length": "short"},
        {"title": "En diciembre llegaban las brisas", "author": "Marvel Moreno", "mood": "introspective", "length": "medium"},
        {"title": "Sense and Sensibility", "author": "Jane Austen", "mood": "motivational", "length": "long"}
    ],
    "Like sticking to real-life": [
        {"title": "Tell Me How It Ends: An Essay in Forty Questions", "author": "Valeria Luiselli", "mood": "thought-provoking", "length": "short"},
        {"title": "Dispatches", "author": "Michael Herr", "mood": "informative", "length": "medium"},
        {"title": "Noticia de un secuestro", "author": "Gabriel García Márquez", "mood": "thought-provoking", "length": "long"}
    ]
}

# Streamlit App
st.title("📚 Gabriela's Personalized Book Recommender")
st.write("Find the perfect book based on your current vibe!")

# Step 1: Choose a mood
version = st.selectbox("How are you feeling today?", options=list(gabriela_moods.keys()))

# Step 2: Choose mood
if version:
    st.write(f"You're channeling **{version}** today.")
    mood = st.radio("How are you feeling?", options=["nostalgic", "introspective", "motivational", "informative", "thought-provoking"])

    # Step 3: Choose length
    length = st.selectbox("How long would you like the book to be?", options=["short", "medium", "long"])

    # Step 4: Generate recommendation
    if st.button("Recommend a Book"):
        # Filter books by selected criteria
        recommendations = [
            book for book in gabriela_moods[version]
            if book["mood"] == mood and book["length"] == length
        ]

        # Provide recommendation or fallback message
        if recommendations:
            book = random.choice(recommendations)
            st.success(f"📖 **{book['title']}** by *{book['author']}* matches your '{mood}' mood and '{length}' preference as {version}!")
        else:
            st.warning(f"Sorry, no books match your mood '{mood}' and length '{length}' for {version}. Try different criteria!")

# Footer
st.write("Enjoy your personalized reading adventure!")