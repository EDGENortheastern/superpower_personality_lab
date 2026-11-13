from pathlib import Path  # Finds files, such as style.css
import streamlit as st  # Creates the web app using Python

st.set_page_config(page_title="Data Science Superpower Lab", page_icon="🦸")
st.html(Path("style.css"))

# Each pair of top strengths gives one hero: (hero name, picture file)
HEROES = {
    "Bravery + Creativity": ("A/B Avenger", "assets/ab_avenger.png"),
    "Creativity + Curiosity": ("Visualisation Visionary", "assets/visualisation_visionary.png"),
    "Creativity + Patience": ("Dashboard Defender", "assets/dashboard_defender.png"),
    "Bravery + Curiosity": ("Hypothesis Hunter", "assets/hypothesis_hunter.png"),
    "Bravery + Patience": ("Validation Vanguard", "assets/validation_vanguard.png"),
    "Curiosity + Patience": ("Pattern Detective", "assets/pattern_detective.png"),
}

st.title("🦸 Data Science Superpower Lab")
st.write("Find your statistics superhero!")

with st.form("quiz"):
    name = st.text_input("What's your name?").title()

    # sliders
    creativity = st.slider("🎨 Creativity", 0, 10, 5)
    bravery = st.slider("⚡ Bravery", 0, 10, 5)
    curiosity = st.slider("🔎 Curiosity", 0, 10, 5)
    patience = st.slider("🧩 Patience", 0, 10, 5)

    # selectbox
    mission = st.selectbox("Which strength do you use most?",
                           ["Creativity", "Bravery", "Curiosity", "Patience"])

    # radio buttons
    style = st.radio("Which strength would your friends pick for you?",
                     ["Creativity", "Bravery", "Curiosity", "Patience"])

    submitted = st.form_submit_button("Reveal my superhero!")

if submitted:

    scores = {
        "Creativity": creativity,
        "Bravery": bravery,
        "Curiosity": curiosity,
        "Patience": patience,
    }
    print(scores)
    # Bonus points from the other two controls
    scores[mission] += 3
    scores[style] += 2
    print(scores)
    # Pick the two highest strengths, put them in A-Z order, and look up the hero
    top_two = sorted(scores, key=scores.get, reverse=True)[:2]
    print(top_two)
    top_two.sort()
    hero_name, picture = HEROES[top_two[0] + " + " + top_two[1]]

    with st.container(key="hero_card"):
        st.subheader(f"🦸 {name or 'Hero'}, you are the {hero_name}!")
        st.image(picture, width=340)
