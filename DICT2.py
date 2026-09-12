import json
import difflib
import streamlit as st

def load_language(name):
    with open(f"DATA/{name}.json", "r", encoding="utf-8") as f:
        return json.load(f)

languages = {
    "yoruba": load_language("yoruba"),
    "hausa": load_language("hausa"),
    "igbo": load_language("igbo"),
    "idoma": load_language("idoma"),
    "kanuri": load_language("kanuri"),
}

# Reverse dictionaries: local language -> English
reverse_languages = {
    lang: {v.lower(): k for k, v in words.items()}
    for lang, words in languages.items()
}

# Session-based usage counter (resets when the app restarts)
if "translation_count" not in st.session_state:
    st.session_state.translation_count = 0

st.set_page_config(page_title="Nigerian Language Translator", page_icon="")

st.title("English → Nigerian Language Translator")
st.write("Translate English words into Yoruba, Igbo, Hausa, Mwaghavul, or Idoma — and back.")

st.divider()

direction = st.radio(
    "Translate direction",
    ["English → Local language", "Local language → English"]
)

language_choice = st.selectbox(
    "Choose a language",
    list(languages.keys())
)

word = st.text_input("Enter a word")

# Pick the correct dictionary for the current direction
if direction == "English → Local language":
    active_dictionary = languages[language_choice]
else:
    active_dictionary = reverse_languages[language_choice]

# Show live suggestions as the user types
if word.strip() != "":
    prefix = word.lower().strip()
    suggestions = [w for w in active_dictionary.keys() if w.startswith(prefix)]

    if suggestions:
        st.caption("Suggestions: " + ", ".join(suggestions[:8]))

# Translate button
if st.button("Translate"):
    if word.strip() == "":
        st.warning("Please enter a word.")
    else:
        word_input = word.lower().strip()

        if word_input in active_dictionary:
            translation = active_dictionary[word_input]
        else:
            close_matches = difflib.get_close_matches(word_input, active_dictionary.keys(), n=1, cutoff=0.7)
            translation = active_dictionary[close_matches[0]] if close_matches else None

        if translation:
            st.session_state.translation_count += 1
            st.success(f"**Translation:** {translation}")
        else:
            st.error("Word not found in the dictionary.")

st.divider()
st.caption(f"Translations this session: {st.session_state.translation_count}")
st.caption("Built using streamlit.")
