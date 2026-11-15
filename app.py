import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="My Clever Students",
    page_icon="🎓",
    layout="centered"
)

# Custom CSS for colorful styling
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stButton>button {
        background-color: #4f46e5;
        color: white;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        border: none;
    }
    .stButton>button:hover {
        background-color: #4338ca;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# App Header with Emoji and Colors
st.title("🌟 Student Homework & Feedback Portal")
st.markdown("### Welcome to your interactive English learning & assignment hub! 🚀")
st.write("---")

# Sidebar with colorful styling
st.sidebar.header("📌 Navigation")
menu = st.sidebar.selectbox(
    "Choose a section:",
    ["🏠 Home", "📤 Submit Homework", "💬 View Feedback"]
)

if menu == "🏠 Home":
    st.info("👋 **Welcome Dear Student / Teacher!** Use the sidebar to navigate through the platform.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.success("✨ **For Students:** Submit your writing and audio assignments easily.")
    with col2:
        st.warning("👩‍🏫 **For Teachers:** Review homework and provide helpful feedback.")

elif menu == "📤 Submit Homework":
    st.subheader("📤 Submit Your Homework")
    st.write("Here you can upload your English assignments.")
    
    student_name = st.text_input("Your Name:")
    homework_title = st.selectbox("Select Homework:", ["Assignment 1: Essay Writing", "Assignment 2: Speaking Practice", "Assignment 3: Vocabulary"])
    uploaded_file = st.file_uploader("Upload your file (Text, PDF, Audio):", type=["txt", "pdf", "mp3", "wav"])
    
    if st.button("Submit Assignment"):
        if student_name:
            st.success(f"🎉 Great job {student_name}! Your homework has been submitted successfully.")
        else:
            st.error("⚠️ Please enter your name before submitting.")

elif menu == "💬 View Feedback":
    st.subheader("💬 Teacher's Feedback")
    st.write("Check your scores and feedback from your teacher here.")
    st.info("No feedback available yet. Submit an assignment first!")