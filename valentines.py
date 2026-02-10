import streamlit as st
import time

# --- PAGE CONFIG ---
st.set_page_config(page_title="A Special Message ❤️", page_icon="💖", layout="centered")

# --- INITIALIZE SESSION STATE ---
if 'intro_done' not in st.session_state:
    st.session_state.intro_done = False
if 'yes_size' not in st.session_state:
    st.session_state.yes_size = 20
if 'accepted' not in st.session_state:
    st.session_state.accepted = False
if 'no_click_count' not in st.session_state:
    st.session_state.no_click_count = 0

no_messages = [
    "No", "Are you sure?", "Really sure??", "Think again!", 
    "Last chance!", "Surely not?", "You might regret this!", 
    "Give it another thought!", "Are you absolutely sure?", 
    "This could be a mistake!", "Have a heart!"
]

# --- STYLE: Black Background & Deep Button Fix ---
st.markdown(f"""
    <style>
    /* Force the background to black and all text to white */
    .stApp {{
        background-color: #000000 !important;
        color: #ffffff !important;
    }}
    
    /* Ensure headers and text are white on black */
    h1, h2, h3, p, div {{
        color: #ffffff !important;
    }}

    /* TARGET THE YES BUTTON (Column 1) */
    div[data-testid="stColumn"]:nth-of-type(1) button {{
        background-color: #4caf50 !important;
        color: white !important;
        font-size: {st.session_state.yes_size}px !important;
        height: auto !important;
        width: auto !important;
        padding: {st.session_state.yes_size/3}px {st.session_state.yes_size}px !important;
        border-radius: 10px !important;
        border: 2px solid #ffffff !important;
        line-height: 1 !important;
    }}

    /* TARGET THE NO BUTTON (Column 2) */
    div[data-testid="stColumn"]:nth-of-type(2) button {{
        background-color: #f44336 !important;
        color: white !important;
        font-size: 18px !important;
        border-radius: 10px !important;
        border: 1px solid #ffffff !important;
        height: auto !important;
        padding: 10px 20px !important;
    }}
    
    /* Remove default button hover effects that might mess with colors */
    button:hover {{
        border-color: #ffffff !important;
        color: #ffffff !important;
    }}
    </style>
""", unsafe_allow_html=True)

# --- STATE 1: THE INTRO SCREEN ---
if not st.session_state.intro_done:
    st.markdown("""
        <div style="display: flex; justify-content: center; align-items: center; height: 70vh; 
                    font-size: 2.5rem; color: #ff69b4; text-align: center; font-family: 'Arial', sans-serif;">
            Hi beautiful, I want to ask you an important question...
        </div>
    """, unsafe_allow_html=True)
    
    time.sleep(5)
    st.session_state.intro_done = True
    st.rerun()

# --- STATE 2: THE PROPOSAL SCREEN ---
elif not st.session_state.accepted:
    st.title("Hi Beautiful... 🌹")
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHpueG56ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6JmVwPXYxX2ludGVybmFs_by_id&ct=g/c76IJLufpNwSULPk77/giphy.gif")
    st.header("Will you be my Valentine?")

    col1, col2 = st.columns([1, 1])

    with col1:
        if st.button("Yes", key="yes_btn"):
            st.session_state.accepted = True
            st.rerun()

    with col2:
        msg_index = st.session_state.no_click_count % len(no_messages)
        if st.button(no_messages[msg_index], key="no_btn"):
            st.session_state.no_click_count += 1
            st.session_state.yes_size += 35  # Significant growth
            st.rerun()

# --- STATE 3: THE SUCCESS SCREEN ---
else:
    st.balloons()
    st.markdown("<h1 style='text-align: left; color: #4caf50;'>Yay! I knew you'd say yes! 🥰</h1>", unsafe_allow_html=True)
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHpueG56ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/KztT2c4u8mYYUiMKdJ/giphy.gif")
