import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="My Clever Students",
    page_icon="🎓",
    layout="wide"
)

# Custom CSS for Soft Pink Theme Styling & Sidebar
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
    section[data-testid="stSidebar"] {
        background-color: #fce7f3;
    }
    </style>
""", unsafe_allow_html=True)

# --- بخش مدیریت ورود (Authentication) ---
ALLOWED_STUDENTS = ["Sara", "Ali", "Mohammad", "Setareh"]

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
    # --- منوی کناری (Sidebar) مطابق طرح شما ---
    with st.sidebar:
        st.image("https://img.icons8.com/color/96/student-male.png", width=80)
        st.markdown(f"### Hi, {st.session_state.student_name}! 🌸")
        st.write("---")
        
        st.markdown("### 📚 Learning Hub")
        menu_selection = st.radio(
            "Navigation",
            [
                "Class Topics", 
                "Review", 
                "Games & Quiz", 
                "Grades per Lesson", 
                "Activity Level", 
                "Total Activities",
                "Contact Teacher",
                "Ideas & Suggestions"
            ],
            label_visibility="collapsed"
        )
        
        st.write("---")
        if st.button("Logout"):
            st.session_state.logged_in = False
            st.rerun()

    # --- محتوای اصلی صفحات بر اساس انتخاب منوی کناری ---
    if menu_selection == "Class Topics":
        st.title("🌟 Class Topics")
        st.markdown("Here you can find all the main topics covered in our English classes.")
        st.info("📌 Current Topic: Unit 3 - Adventures and Exploration")
        st.checkbox("Completed reading part")
        st.checkbox("Watched the session video")

    elif menu_selection == "Review":
        st.title("📚 Class Review & Summary")
        st.write("Review the key vocabulary and grammar from our latest session:")
        st.success("💡 **Key Vocabulary:** Adventure, Curious, Explore, Brilliant")
        st.info("📌 **Grammar Point:** Past Simple Tense")

    elif menu_selection == "Games & Quiz":
        st.title("🎯 Games & Mini Quiz")
        st.write("Test your knowledge and practice English with fun quizzes:")
        q1 = st.radio("What is the past form of 'Go'?", ["Goed", "Went", "Gone", "Going"])
        if st.button("Submit Quiz"):
            if q1 == "Went":
                st.success("🌟 Excellent! Correct answer.")
            else:
                st.error("❌ Incorrect. Try again!")

    elif menu_selection == "Grades per Lesson":
        st.title("📊 Grades per Lesson")
        st.write("Check your scores and feedback for each completed lesson:")
        st.markdown("- Lesson 1: ⭐⭐⭐⭐⭐ (5/5)")
        st.markdown("- Lesson 2: ⭐⭐⭐⭐☆ (4/5)")

    elif menu_selection == "Activity Level":
        st.title("📈 Activity Level")
        st.write("Your current participation and activity status:")
        st.progress(75)
        st.write("You are doing great! 75% of weekly goals completed.")

    elif menu_selection == "Total Activities":
        st.title("🏆 Total Activities")
        st.write("Summary of all tasks and homework you have completed so far:")
        st.metric(label="Completed Assignments", value="12")
        st.metric(label="Quizzes Passed", value="4")

    elif menu_selection == "Contact Teacher":
        st.title("👩‍🏫 Contact Teacher")
        st.write("Have a question? Send a direct message to your teacher:")
        teacher_msg = st.text_area("Your message to the teacher:")
        if st.button("Send Message"):
            if teacher_msg:
                st.success("Your message has been sent to the teacher successfully! ✉️")
            else:
                st.warning("Please write a message first.")

    elif menu_selection == "Ideas & Suggestions":
        st.title("💡 Ideas & Suggestions")
        st.write("We would love to hear your ideas for improving the class or portal:")
        idea_msg = st.text_area("Write your suggestion here...")
        if st.button("Submit Idea"):
            if idea_msg:
                st.success("Thank you! Your suggestion was sent. 🚀")
            else:
                st.warning("Please write your idea first.")
