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
ALLOWED_STUDENTS = ["Nafiseh","Jamil","Bahar","Reza","Ali"]

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
    # --- منوی کناری (Sidebar) ---
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

    # --- محتوای صفحات ---
    if menu_selection == "Class Topics":
        st.title("🌟 Lesson 1: Simple Present Tense")
        st.markdown("### Talking about Daily Routines & Habits ⏰")
        
        st.info("""
        **When do we use Simple Present?**
        - For daily routines (e.g., *I wake up at 7 AM.*)
        - For general facts (e.g., *The sun rises in the east.*)
        """)
        
        col1, col2 = st.columns(2)
        with col1:
            st.success("✅ **I / You / We / They + Verb**\n- I **play** football.\n- They **study** English.")
        with col2:
            st.warning("⭐ **He / She / It + Verb + s/es**\n- She **plays** football.\n- He **watches** TV.")
            
        st.write("---")
        st.markdown("#### 🎯 Your Self-Check (Did you learn it?):")
        
        # سوال اول با فیدبک تعاملی
        check1 = st.radio(
            "Did you fully understand when to add 's' or 'es' for He/She/It?", 
            ["Select an option...", "Yes", "No"],
            key="check1"
        )
        
        if check1 == "Yes":
            st.success("😁 Brilliant! High five! 🥳 You've mastered this rule.")
        elif check1 == "No":
            st.warning("🔍 No worries at all! Let's take a closer look: remember we add 's' or 'es' only for third-person singular (He, She, It) in positive sentences. You can review the boxes above!")

        st.write("")
        
        # سوال دوم با فیدبک تعاملی
        check2 = st.radio(
            "Did you write 3 sentences about your daily routine?", 
            ["Select an option...", "Yes", "No"],
            key="check2"
        )
        
        if check2 == "Yes":
            st.success("🌟 Awesome! You are super active and doing a great job! 🎉")
        elif check2 == "No":
            st.warning("💪 Let's try writing just one sentence about what you do every morning (e.g., *I wake up at 8 o'clock.*). You can do it!")

    elif menu_selection == "Review":
        st.title("📚 Quick Review: Simple Present")
        st.write("Review the key vocabulary and frequency adverbs from our lesson:")
        
        st.markdown("""
        | Vocabulary (Daily Routines) | Example Sentence |
        | :--- | :--- |
        | **Wake up** | Sara **wakes up** early every day. |
        | **Brush teeth** | Ali **brushes** his teeth twice a day. |
        | **Go to school** | We **go** to school by bus. |
        | **Do homework** | Setareh **does** her homework in the afternoon. |
        """)
        
        st.info("💡 **Frequency Adverbs:** Always (100%) > Usually (80%) > Sometimes (50%) > Never (0%)")

    elif menu_selection == "Games & Quiz":
        st.title("🎯 Simple Present Challenge!")
        st.write("Answer these 3 questions to test your grammar skills:")
        
        q1 = st.radio("1. Sara _____ English every day.", ["study", "studies", "studying"])
        q2 = st.radio("2. Ali and Mohammad _____ football on Fridays.", ["plays", "play", "playing"])
        q3 = st.radio("3. _____ she like ice cream?", ["Do", "Does", "Is"])
        
        if st.button("Check My Score 🏆"):
            score = 0
            if q1 == "studies":
                score += 1
            if q2 == "play":
                score += 1
            if q3 == "Does":
                score += 1
                
            if score == 3:
                st.balloons()
                st.success(f"🎉 Amazing job, {st.session_state.student_name}! You got 3/3!")
            elif score == 2:
                st.info(f"👍 Good job! You got 2/3. Review the 'He/She/It' rule once more!")
            else:
                st.error(f"💪 You got {score}/3. Don't worry, check the Class Topics tab and try again!")

    elif menu_selection == "Grades per Lesson":
        st.title("📊 Grades per Lesson")
        st.write("Check your scores and feedback for each completed lesson:")
        st.markdown("- **Lesson 1 (Simple Present):** ⭐⭐⭐⭐⭐ (5/5)")

    elif menu_selection == "Activity Level":
        st.title("📈 Activity Level")
        st.write("Your current participation and activity status:")
        st.progress(80)
        st.write("You are doing great! 80% of this week's Simple Present tasks completed.")

    elif menu_selection == "Total Activities":
        st.title("🏆 Total Activities")
        st.write("Summary of all tasks and homework you have completed so far:")
        col1, col2 = st.columns(2)
        col1.metric(label="Completed Lessons", value="1")
        col2.metric(label="Quizzes Passed", value="1")

    elif menu_selection == "Contact Teacher":
        st.title("👩‍🏫 Contact Teacher")
        st.write("Have a question about Simple Present? Send a direct message:")
        teacher_msg = st.text_area("Your message to the teacher:")
        if st.button("Send Message"):
            if teacher_msg:
                st.success("Your message has been sent to the teacher successfully! ✉️")
            else:
                st.warning("Please write a message first.")

    elif menu_selection == "Ideas & Suggestions":
        st.title("💡 Ideas & Suggestions")
        st.write("What topic or game should we add next?")
        idea_msg = st.text_area("Write your suggestion here...")
        if st.button("Submit Idea"):
            if idea_msg:
                st.success("Thank you! Your suggestion was sent. 🚀")
            else:
                st.warning("Please write your idea first.")
