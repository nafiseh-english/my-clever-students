import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="My Clever Students",
    page_icon="🎓",
    layout="centered"
)

# Custom CSS for Soft Pink Theme Styling
st.markdown("""
    <style>
    .stApp {
        background-color: #fdf2f8;
    }
    .stButton>button {
        background-color: #db2777;
        color: white;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        border: none;
    }
    .stButton>button:hover {
        background-color: #be185d;
        color: white;
    }
    h1, h2, h3 {
        color: #9d174d;
    }
    /* Style for active tab */
    [data-baseweb="tab-highlight"] {
        background-color: #db2777 !important;
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
