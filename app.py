import streamlit as st

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Home - LS", page_icon=":love_letter:", layout="wide")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Welcome, we're Life Scentence! :wave:")
    st.title("A healthcare company at your service!")
    st.write("Get your healthcare here and get updated when anything changes.")
    st.write("[Learn More](https://trollface.dk/)")

# --- WHAT WE DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What we do")
        st.write("##")
        st.write(
            """
            We make sure you get the best healthcare anyone can provide and help you with all of your questions.        
            """
        )
