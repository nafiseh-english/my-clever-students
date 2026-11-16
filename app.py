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

# --- بخش مدیریت ورود (Authentication) ---
ALLOWED_STUDENTS = ["Jamil", "Nafiseh"]

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.title("🔒 Student Login Portal")
    st.markdown("Please enter your name in English to access the portal:")
    
    entered_name = st.text_input("Your Name", label_visibility="collapsed")
    
    if st.button("Login"):
        if entered_name.strip().title() in ALLOWED_STUDENTS:
            st.session_state.logged_in = True
            st.session_state.student_name = entered_name.strip().title()
            st.rerun()
        else:
            st.error("Access denied! Your name is not in the authorized list.")
            
else:
    # --- محتوای اصلی سایت ---
    st.title(f"🌟 Welcome, {st.session_state.student_name}! - Educational Portal")
    st.markdown("### Welcome to your interactive English learning hub! 🚀")
    st.write("---")

    # Creating Tabs for Navigation (اضافه شدن تب آزمون Quiz)
    tab1, tab2, tab3, tab4 = st.tabs(["📚 Class Review", "📝 Homework & Upload", "📤 Submit Answer", "🎯 Mini Quiz"])

    # --- تب اول: خلاصه جلسه پیش (Class Review) ---
    with tab1:
        st.header("Class Review & Summary")
        st.write("Review the topics, vocabulary, and grammar covered in our latest session:")
        
        st.info("💡 **Key Vocabulary of the Week:**\n- Adventure, Curious, Explore, Brilliant")
        st.success("📌 **Grammar Point:** Past Simple Tense (Regular & Irregular verbs)")
        
        st.markdown("---")
        st.write("Check your review progress:")
        st.checkbox("I have reviewed the vocabulary list.")
        st.checkbox("I have studied the grammar notes.")

    # --- تب دوم: تکالیف و بارگذاری فایل (Homework & Upload) ---
    with tab2:
        st.header("Homework Assignments & File Upload")
        st.write("Download or view this week's assignments, and upload your completed files (PDF, Images, etc.):")
        
        st.markdown("📄 **Assignment Task:** Write a short paragraph about your last weekend using past tense.")
        
        # امکان بارگذاری فایل توسط دانش‌آموز
        uploaded_file = st.file_uploader("Upload your homework file (PDF, Word, Image):", type=["pdf", "png", "jpg", "docx"])
        
        if uploaded_file is not None:
            st.success(f"File '{uploaded_file.name}' successfully uploaded! Great job, {st.session_state.student_name}. 🎉")

    # --- تب سوم: ارسال پاسخ متنی (Submit Answer) ---
    with tab3:
        st.header("Submit Your Answer")
        st.write("Write your answers or notes here to send:")
        st.info(f"Submitting as: **{st.session_state.student_name}**")
        student_answer = st.text_area("Write your answer here...")

        if st.button("Submit Answer Text"):
            if student_answer:
                st.success(
                    f"Thank you, {st.session_state.student_name}! Your answer has been successfully submitted. 🎉"
                )
            else:
                st.warning("Please write your answer first.")

    # --- تب چهارم: آزمون کوچک (Mini Quiz) ---
    with tab4:
        st.header("Class Mini Quiz")
        st.write("Test your knowledge based on today's lesson:")
        
        q1 = st.radio("1. What is the past form of the verb 'Go'?", ["Goed", "Went", "Gone", "Going"])
        
        if st.button("Submit Quiz"):
            if q1 == "Went":
                st.success("🌟 Excellent! Your answer is correct (Went).")
            else:
                st.error("❌ Incorrect. Try again! (Hint: It's an irregular verb).")
                
    # دکمه خروج
    st.write("---")
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()
