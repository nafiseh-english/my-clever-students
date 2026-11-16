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
ALLOWED_STUDENTS = ["Sara", "Ali", "Mohammad", "Setareh", "Nafiseh","Jamil","Bahar","Reza","Darya"]

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
        st.title("📚 Course Syllabus & English Tenses")
        st.markdown("Here are the main grammar topics we will cover in our classes:")
        st.write("---")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.success("""
            ### 🌸 Present Tenses
            - ☀️ **Simple Present**
            - 🏃 **Present Continuous**
            - 🎯 **Present Perfect**
            - ⏳ **Present Perfect Continuous**
            """)
            
        with col2:
            st.info("""
            ### 🦋 Past Tenses
            - 🕰️ **Simple Past**
            - 🎞️ **Past Continuous**
            - 📜 **Past Perfect**
            - 🔄 **Past Perfect Continuous**
            """)
            
        with col3:
            st.warning("""
            ### ✨ Future Tenses
            - 🚀 **Simple Future (will)**
            - 📅 **Future with "be going to"**
            - 🛸 **Future Continuous**
            - 🏆 **Future Perfect**
            - 🌟 **Future Perfect Continuous**
            """)

    elif menu_selection == "Review":
        st.title("📚 Grammar Review & Practice")
        st.markdown("Select a tense from below to review its structure, rules, and examples:")
        
        selected_tense = st.selectbox(
            "Choose a Tense to Review:",
            [
                "Simple Present", 
                "Present Continuous", 
                "Present Perfect", 
                "Simple Past", 
                "Past Continuous", 
                "Simple Future (will)"
            ]
        )
        
        st.write("---")
        
        if selected_tense == "Simple Present":
            st.subheader("☀️ Simple Present Tense")
            st.markdown("**Usage:** Used for habits, daily routines, and general facts.")
            
            col1, col2 = st.columns(2)
            with col1:
                st.success("✅ **Positive Form**\n- I / You / We / They + Verb\n- He / She / It + Verb + **s/es**")
            with col2:
                st.info("❌ **Negative Form**\n- I / You / We / They + **don't** + Verb\n- He / She / It + **doesn't** + Verb")
                
            st.markdown("#### 📝 Examples:")
            st.markdown("- She **wakes up** early every morning.")
            st.markdown("- They **play** tennis on Fridays.")
            
        elif selected_tense == "Present Continuous":
            st.subheader("🏃 Present Continuous Tense")
            st.markdown("**Usage:** Used for actions happening right now, at the moment of speaking.")
            
            st.success("✅ **Formula:** Subject + **am / is / are** + Verb-**ing**")
            
            st.markdown("#### 📝 Examples:")
            st.markdown("- I **am studying** English right now.")
            st.markdown("- Look! It **is raining** outside.")
            
        elif selected_tense == "Present Perfect":
            st.subheader("🎯 Present Perfect Tense")
            st.markdown("**Usage:** Used for actions that happened in the past but have a connection to the present.")
            
            st.success("✅ **Formula:** Subject + **have / has** + **Past Participle (V3)**")
            
            st.markdown("#### 📝 Examples:")
            st.markdown("- I **have visited** a lot of countries.")
            st.markdown("- She **has finished** her homework.")
            
        elif selected_tense == "Simple Past":
            st.subheader("🕰️ Simple Past Tense")
            st.markdown("**Usage:** Used for completed actions in the past at a specific time.")
            
            col1, col2 = st.columns(2)
            with col1:
                st.success("✅ **Positive:** Subject + **Past Verb (V2)**\n- *I went to the park yesterday.*")
            with col2:
                st.info("❌ **Negative:** Subject + **didn't** + Base Verb\n- *I didn't go to the park.*")
                
        elif selected_tense == "Past Continuous":
            st.subheader("🎞️ Past Continuous Tense")
            st.markdown("**Usage:** Used for actions that were ongoing at a specific moment in the past.")
            
            st.success("✅ **Formula:** Subject + **was / were** + Verb-**ing**")
            
            st.markdown("#### 📝 Examples:")
            st.markdown("- I **was watching** TV when you called.")
            st.markdown("- They **were playing** football at 5 PM yesterday.")
            
        elif selected_tense == "Simple Future (will)":
            st.subheader("🚀 Simple Future Tense (will)")
            st.markdown("**Usage:** Used for spontaneous decisions, predictions, or promises about the future.")
            
            st.success("✅ **Formula:** Subject + **will** + Base Verb")
            
            st.markdown("#### 📝 Examples:")
            st.markdown("- I **will help** you with your homework.")
            st.markdown("- It **will rain** tomorrow.")

    elif menu_selection == "Games & Quiz":
        st.title("🎮 Fun Games & Grammar Quiz")
        st.markdown("Choose a game or quiz tab below to test your English skills!")
        
        tab1, tab2, tab3 = st.tabs(["🎯 Grammar Quiz", "🧩 Sentence Unscrambler", "🕵️ Spot the Mistake"])
        
        # --- تب اول: کوییز ---
        with tab1:
            st.subheader("Mixed Tenses Challenge (5 Questions)")
            q1 = st.radio("1. Sara _____ English every day.", ["study", "studies", "studying"], key="q1")
            q2 = st.radio("2. Look! It _____ outside right now.", ["rains", "is raining", "rained"], key="q2")
            q3 = st.radio("3. We _____ to the cinema yesterday.", ["go", "went", "gone"], key="q3")
            q4 = st.radio("4. I _____ already finished my homework.", ["have", "has", "am"], key="q4")
            q5 = st.radio("5. Tomorrow, they _____ visit their grandparents.", ["will", "did", "are"], key="q5")
            
            if st.button("Check My Quiz Score 🏆"):
                score = 0
                if q1 == "studies": score += 1
                if q2 == "is raining": score += 1
                if q3 == "went": score += 1
                if q4 == "have": score += 1
                if q5 == "will": score += 1
                
                if score == 5:
                    st.balloons()
                    st.success(f"🎉 Perfect Score, {st.session_state.student_name}! 5/5! You are a Grammar Master!")
                elif score >= 3:
                    st.info(f"👍 Great job! You got {score}/5. Keep practicing!")
                else:
                    st.error(f"💪 You got {score}/5. Check the Review tab and try again!")

        # --- تب دوم: بازی مرتب کردن جملات ---
        with tab2:
            st.subheader("🧩 Put the words in the correct order!")
            st.info("Scrambled words: **`football / plays / Ali / Fridays / on`**")
            
            user_order = st.text_input("Write the correct sentence (don't forget the period at the end!):", key="scramble1")
            if st.button("Check Sentence ✨"):
                cleaned = user_order.strip().lower().rstrip(".")
                if cleaned == "ali plays football on fridays":
                    st.balloons()
                    st.success("🥳 Spot on! 'Ali plays football on Fridays.' is 100% correct!")
                else:
                    st.warning("🤔 Not quite! Hint: Start with the person's name (Subject + Verb + Object + Time).")

        # --- تب سوم: بازی پیدا کردن اشتباه ---
        with tab3:
            st.subheader("🕵️ Find and fix the grammar mistake!")
            st.error("❌ Incorrect Sentence: **She don't like coffee.**")
            
            fix_choice = st.radio(
                "How should we fix this sentence?",
                [
                    "She doesn't likes coffee.",
                    "She doesn't like coffee.",
                    "She not like coffee."
                ],
                key="spot1"
            )
            
            if st.button("Verify Fix 🔍"):
                if fix_choice == "She doesn't like coffee.":
                    st.balloons()
                    st.success("🌟 Detective Genius! After 'doesn't', we always use the base form of the verb ('like').")
                else:
                    st.error("❌ Oops! Remember: 'doesn't' already has the 's', so the main verb stays simple.")

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
        st.write("Have a question about the topics? Send a direct message:")
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
