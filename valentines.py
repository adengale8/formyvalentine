import streamlit as st
import time

# --- PAGE CONFIG ---
st.set_page_config(page_title="A Special Message ❤️", page_icon="💖")

# --- INITIALIZE SESSION STATE ---
if 'intro_done' not in st.session_state:
    st.session_state.intro_done = False

if 'yes_size' not in st.session_state:
    st.session_state.yes_size = 20

if 'accepted' not in st.session_state:
    st.session_state.accepted = False

# --- STATE 1: THE INTRO SCREEN ---
if not st.session_state.intro_done:
    # Centering the text using HTML
    st.markdown("""
        <style>
        .intro-text {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 80vh;
            font-size: 3rem;
            color: #d63384;
            text-align: center;
            font-family: 'Arial', sans-serif;
        }
        </style>
        <div class="intro-text">
            Hi beautiful, I want to ask you an important question...
        </div>
    """, unsafe_allow_html=True)
    
    # Wait for 5 seconds
    time.sleep(5)
    
    # Set the state to done and refresh the page
    st.session_state.intro_done = True
    st.rerun()

# --- STATE 2: THE PROPOSAL SCREEN ---
elif not st.session_state.accepted:
    st.title("Hi Beautiful... 🌹")
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHpueG56ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/c76IJLufpNwSULPk77/giphy.gif")
    st.header("Will you be my Valentine?")

    # CSS for the Growing Button
    st.markdown(f"""
        <style>
        div[data-testid="column"]:nth-of-type(1) button {{
            font-size: {st.session_state.yes_size}px !important;
            height: auto !important;
            width: auto !important;
            padding: {st.session_state.yes_size/2}px {st.session_state.yes_size}px !important;
            background-color: #4caf50 !important;
            color: white !important;
            transition: all 0.2s ease;
        }}
        div[data-testid="column"]:nth-of-type(2) button {{
            background-color: #f44336 !important;
            color: white !important;
        }}
        </style>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])

    with col1:
        if st.button("Yes", key="yes_btn"):
            st.session_state.accepted = True
            st.rerun()

    with col2:
        if st.button("No", key="no_btn"):
            st.session_state.yes_size += 20  # Make 'Yes' bigger
            st.rerun()  # Rerun to apply new CSS size

# --- STATE 3: THE SUCCESS SCREEN ---
else:
    st.balloons()
    st.success("Yay! I knew you'd say yes! 🥰")
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHpueG56ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/KztT2c4u8mYYUiMKdJ/giphy.gif")