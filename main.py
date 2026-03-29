import streamlit as st
from api_handler import generate_fake_news
from utils import get_category_emoji, get_random_place, get_random_person

# --- Page Configuration ---
st.set_page_config(
    page_title="Breaking Bakwaas - Fake News Generator",
    page_icon="📰",
    layout="centered"
)

# --- Initialize Session State for History ---
if "news_history" not in st.session_state:
    st.session_state.news_history = []

# --- Sidebar UI ---
with st.sidebar:
    st.title("⚙️ Settings & Controls")
    st.markdown("Welcome to **Breaking Bakwaas**!")
    
    st.divider()
    
    # Mode Selection
    mode = st.radio("Choose Mode:", ["Auto Generate", "Custom Input"])
    
    st.divider()
    if st.button("🗑️ Clear History"):
        st.session_state.news_history = []
        st.rerun()

# --- Main UI ---
st.title("📰 Breaking Bakwaas")
st.subheader("Your #1 source for completely unreliable, hilarious news.")

# Inputs based on mode
custom_prompt = ""
if mode == "Auto Generate":
    col1, col2 = st.columns(2)
    with col1:
        place = st.text_input("Place", placeholder="e.g., Pune, Mars, Your Kitchen")
    with col2:
        person = st.text_input("Person Name", placeholder="e.g., Rahul, Batman, My Boss")
else:
    place = ""
    person = ""
    custom_prompt = st.text_area("What is the news about?", placeholder="e.g., A dog who learned to code in Python...")

# Common Inputs
col3, col4 = st.columns(2)
with col3:
    news_type = st.selectbox("News Type", ["Politics", "Sports", "Entertainment", "Technology", "Funny", "Breaking News"])
with col4:
    tone = st.selectbox("Tone", ["Funny", "Sarcastic", "Dramatic", "Absurd"])

# --- Generation Logic ---
if st.button("🚀 Generate Fake News!", use_container_width=True, type="primary"):
    
    # Auto-fill missing data if in Auto Generate mode
    if mode == "Auto Generate":
        final_place = place if place else get_random_place()
        final_person = person if person else get_random_person()
    else:
        final_place = "Unknown"
        final_person = "Unknown"
        if not custom_prompt:
            st.warning("Please enter some details in the Custom Input box!")
            st.stop()
            
    with st.spinner("Cooking up some fresh bakwaas..."):
        headline, content = generate_fake_news(
            mode=mode,
            place=final_place,
            person=final_person,
            news_type=news_type,
            tone=tone,
            custom_prompt=custom_prompt
        )
        
        emoji = get_category_emoji(news_type)
        formatted_headline = f"{emoji} {headline}"
        
        # Save to history
        st.session_state.news_history.insert(0, {"headline": formatted_headline, "content": content})

# --- Display Latest Output ---
if st.session_state.news_history:
    st.divider()
    latest_news = st.session_state.news_history[0]
    
    # Display the news
    st.markdown(f"## **{latest_news['headline']}**")
    st.write(latest_news['content'])
    
    st.divider()
    
    # Actions (Download & Copy)
    text_to_download = f"{latest_news['headline']}\n\n{latest_news['content']}"
    
    st.download_button(
        label="📥 Download as Text",
        data=text_to_download,
        file_name="breaking_bakwaas.txt",
        mime="text/plain"
    )

# --- Display History ---
if len(st.session_state.news_history) > 1:
    st.markdown("### 🕒 Previous Headlines")
    for i, past_news in enumerate(st.session_state.news_history[1:6]): # Show last 5
        with st.expander(past_news['headline']):
            st.write(past_news['content'])