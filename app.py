import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="My Clever Students",
    page_icon="🎓",
    layout="centered"
)

# Custom CSS for Soft Blue Theme Styling
st.markdown("""
    <style>
    .main {
        background-color: #f0f4f8;
    }
    .stButton>button {
        background-color: #3b82f6;
        color: white;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        border: none;
    }
    .stButton>button:hover {
        background-color: #2563eb;
        color: white;
    }
    h1, h2, h3 {
        color: #1e3a8a;
    }
    </style>
""", unsafe_allow_html=True)

# App Header with Emoji and Colors
st.title("🌟 My Clever Students - Educational Portal")
st.markdown("### Welcome to your interactive English learning hub! 🚀")
st.write("---")

# Creating Tabs for Navigation
tab1, tab2, tab3 = st.tabs(["📚 Class Review", "📝 Homework", "📤 Submit Answer"])

with tab1:
    st.header("Class Review")
    st.write("Review the topics covered in our latest class sessions:")
    st.checkbox("I have reviewed vocabulary list 1.")
    st.checkbox("I have practiced the reading text.")

with tab2:
    st.header("Homework Assignments")
    st.write("Complete the exercises assigned for this week:")
    st.checkbox("I have completed exercise page 12 in the workbook.")
    st.checkbox("I have practiced the listening file.")

with tab3:
    st.header("Submit Your Answer")
    st.write("Write your answers or notes here to send:")
    student_name = st.text_input("Full Name:")
    student_answer = st.text_area("Write your answer here...")

    if st.button("Submit Answer"):
        if student_name:
            st.success(
                f"Thank you, {student_name}! Your answer has been successfully submitted. 🎉"
            )
        else:
            st.warning("Please enter your name first.")
