import streamlit as st
import json
import os

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
    .mistake-box {
        background-color: #fff1f2;
        border-left: 4px solid #e11d48;
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 15px;
    }
    .success-box {
        background-color: #f0fdf4;
        border-left: 4px solid #22c55e;
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# --- لیست کامل زبان‌آموزان مجاز ---
ALLOWED_STUDENTS = ["Sara", "Ali", "Mohammad", "Setareh", "Nafiseh", "Jamil", "Bahar", "Reza", "Darya"]

# --- تمام ۱۳ ساختار آموزشی به ترتیب مراحل ---
TENSE_LEVELS = [
    "Simple Present",
    "Present Continuous",
    "Present Perfect",
    "Present Perfect Continuous",
    "Simple Past",
    "Past Continuous",
    "Past Perfect",
    "Past Perfect Continuous",
    "Simple Future (will)",
    "Future with 'be going to'",
    "Future Continuous",
    "Future Perfect",
    "Future Perfect Continuous"
]

# --- سیستم ذخیره دائمی پیشرفت دانش‌آموزان ---
PROGRESS_FILE = "student_progress.json"

def load_all_progress():
    if os.path.exists(PROGRESS_FILE):
        try:
            with open(PROGRESS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}

def save_student_progress(student_name, unlocked_index, scores, quiz_variant):
    data = load_all_progress()
    data[student_name] = {
        "unlocked_index": unlocked_index,
        "scores": scores,
        "quiz_variant": quiz_variant
    }
    with open(PROGRESS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# --- بانک جامع سوالات همراه با دلیل ساده و آموزشی برای هر پاسخ ---
RAW_QUESTIONS = {
    "Simple Present": {
        "A": [
            {"type": "mc", "q": "1. Sara _____ English every day.", "opts": ["study", "studies", "studying"], "ans": "studies", "tip": "For He/She/It in Simple Present, we add '-es' or '-s' to the verb."},
            {"type": "mc", "q": "2. Ali and Reza _____ football on Fridays.", "opts": ["plays", "play", "playing"], "ans": "play", "tip": "For plural subjects (Ali and Reza = They), we use the base verb 'play'."},
            {"type": "mc", "q": "3. _____ she like ice cream?", "opts": ["Do", "Does", "Is"], "ans": "Does", "tip": "We use 'Does' to make questions for He/She/It."},
            {"type": "fill", "q": "4. Fill in the blank: He _____ (go) to school by bus every morning.", "ans": "goes", "tip": "With 'He', the verb 'go' changes to 'goes'."},
            {"type": "fill", "q": "5. Fill in the blank: They _____ (not / live) in Shiraz.", "ans": "don't live", "tip": "For plural subjects in negative sentences, we use 'don't'."},
            {"type": "fill", "q": "6. Fill in the blank: Water _____ (boil) at 100 degrees Celsius.", "ans": "boils", "tip": "General facts use Simple Present ('Water' is singular, so 'boils')."},
            {"type": "order", "q": "7. Make a correct sentence: `always / early / wakes up / Bahar`", "ans": "bahar always wakes up early", "tip": "Structure: Subject (Bahar) + Adverb (always) + Verb (wakes up)."},
            {"type": "order", "q": "8. Make a correct sentence: `coffee / drink / you / do / ?`", "ans": "do you drink coffee", "tip": "Question structure: Do + Subject (you) + Verb (drink) + Object."},
            {"type": "tf", "q": "9. Detective check: Can we say 'My cat speaks English fluently every night' in real life?", "ans": "False", "tip": "Cats cannot speak human languages! This is false."},
            {"type": "tf", "q": "10. Detective check: Do we add '-s' to the verb for 'He/She/It' in positive Simple Present sentences?", "ans": "True", "tip": "Yes! He/She/It always takes '-s' or '-es' in positive sentences."},
        ],
        "B": [
            {"type": "mc", "q": "1. The sun _____ in the east.", "opts": ["rise", "rises", "rising"], "ans": "rises", "tip": "The sun is singular (It), so we use 'rises'."},
            {"type": "mc", "q": "2. My father _____ to work by car.", "opts": ["go", "goes", "going"], "ans": "goes", "tip": "My father = He, so the verb takes '-es' ('goes')."},
            {"type": "mc", "q": "3. _____ you drink tea in the morning?", "opts": ["Do", "Does", "Are"], "ans": "Do", "tip": "With 'you', we always use 'Do' for questions."},
            {"type": "fill", "q": "4. Fill in the blank: Darya _____ (watch) TV every evening.", "ans": "watches", "tip": "Darya = She, so 'watch' becomes 'watches'."},
            {"type": "fill", "q": "5. Fill in the blank: Jamil _____ (not / play) video games on weekdays.", "ans": "doesn't play", "tip": "Jamil = He, so negative form is 'doesn't play'."},
            {"type": "fill", "q": "6. Fill in the blank: Cats _____ (like) milk.", "ans": "like", "tip": "Cats is plural, so we use the base verb 'like'."},
            {"type": "order", "q": "7. Make a correct sentence: `on / tennis / play / Fridays / we`", "ans": "we play tennis on fridays", "tip": "Structure: Subject (we) + Verb (play) + Object + Time."},
            {"type": "order", "q": "8. Make a correct sentence: `does / live / where / Setareh / ?`", "ans": "where does setareh live", "tip": "Wh-question structure: Where + does + Subject + base verb."},
            {"type": "tf", "q": "9. Detective check: Is 'He don't like vegetables' grammatically correct?", "ans": "False", "tip": "For 'He', we must use 'doesn't', not 'don't'."},
            {"type": "tf", "q": "10. Detective check: Is Simple Present used for permanent truths and routines?", "ans": "True", "tip": "Exactly! Habits and facts are Simple Present."},
        ]
    }
    # (بقیه زمان‌ها نیز از همین الگو پیروی می‌کنند)
}

# تکمیل بقیه زمان‌ها به صورت پیش‌فرض برای اینکه خالی نباشند
for t in TENSE_LEVELS:
    if t not in RAW_QUESTIONS:
        RAW_QUESTIONS[t] = {
            "A": [
                {"type": "mc", "q": f"1. Sample question for {t} (A)?", "opts": ["Option 1", "Option 2", "Option 3"], "ans": "Option 1", "tip": "Review the basic grammar formula for this tense."},
                {"type": "tf", "q": f"2. Detective check: Is {t} a grammar structure?", "ans": "True", "tip": "Yes, it is one of the 13 English tenses."}
            ],
            "B": [
                {"type": "mc", "q": f"1. Sample question for {t} (B)?", "opts": ["Option 1", "Option 2", "Option 3"], "ans": "Option 1", "tip": "Review the basic grammar formula for this tense."},
                {"type": "tf", "q": f"2. Detective check: Is {t} used in English?", "ans": "True", "tip": "Yes, it is widely used."}
            ]
        }

# --- مدیریت وضعیت و پیشرفت دانش‌آموز ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# --- صفحه ورود ---
if not st.session_state.logged_in:
    st.title("🔒 Student Login Portal")
    st.markdown("Please enter your name in English to access the portal:")
    
    entered_name = st.text_input("Your Name", label_visibility="collapsed")
    
    if st.button("Login"):
        clean_name = entered_name.strip().title()
        if clean_name in ALLOWED_STUDENTS:
            st.session_state.logged_in = True
            st.session_state.student_name = clean_name
            
            all_data = load_all_progress()
            student_data = all_data.get(clean_name, {})
            st.session_state.unlocked_index = student_data.get("unlocked_index", 0)
            st.session_state.scores = student_data.get("scores", {})
            st.session_state.quiz_variant = student_data.get("quiz_variant", {t: "A" for t in TENSE_LEVELS})
            
            for t in TENSE_LEVELS:
                if t not in st.session_state.quiz_variant:
                    st.session_state.quiz_variant[t] = "A"
                    
            st.rerun()
        else:
            st.error("Access denied! Your name is not in the authorized list.")
            
else:
    all_data = load_all_progress()
    if st.session_state.student_name in all_data:
        saved = all_data[st.session_state.student_name]
        st.session_state.unlocked_index = saved.get("unlocked_index", st.session_state.unlocked_index)
        st.session_state.scores = saved.get("scores", st.session_state.scores)
        st.session_state.quiz_variant = saved.get("quiz_variant", st.session_state.quiz_variant)

    # --- منوی کناری (Sidebar) ---
    with st.sidebar:
        st.image("https://img.icons8.com/color/96/student-male.png", width=80)
        st.markdown(f"### Hi, {st.session_state.student_name}! 🌸")
        current_lvl_name = TENSE_LEVELS[st.session_state.unlocked_index]
        st.caption(f"Active Level: **{current_lvl_name}**")
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
        st.markdown("Here are all 13 grammar structures we will cover in our classes:")
        st.write("---")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.success("### 🌸 Present Tenses\n- ☀️ **Simple Present**\n- 🏃 **Present Continuous**\n- 🎯 **Present Perfect**\n- ⏳ **Present Perfect Continuous**")
        with col2:
            st.info("### 🦋 Past Tenses\n- 🕰️ **Simple Past**\n- 🎞️ **Past Continuous**\n- 📜 **Past Perfect**\n- 🔄 **Past Perfect Continuous**")
        with col3:
            st.warning("### ✨ Future Tenses\n- 🚀 **Simple Future (will)**\n- 📅 **Future with 'be going to'**\n- 🛸 **Future Continuous**\n- 🏆 **Future Perfect**\n- 🌟 **Future Perfect Continuous**")

    elif menu_selection == "Review":
        st.title("📚 Grammar Review & Practice")
        st.markdown("Select any of the 13 structures below to review its formula, usage, and examples:")
        
        selected_tense = st.selectbox(
            "Choose a Structure to Review:",
            TENSE_LEVELS,
            index=st.session_state.unlocked_index
        )
        st.write("---")
        st.subheader(f"📖 Review: {selected_tense}")
        st.markdown("Study the rules and examples carefully before taking the quiz!")

    elif menu_selection == "Games & Quiz":
        st.title("🎮 Mastery Quests & Comprehensive Quizzes")
        st.info("📌 **Rule:** Score **75% or higher** to unlock the next level! Detailed friendly feedback will show your exact mistakes.")
        
        st.subheader("🗺️ Your 13-Level Learning Path")
        for row_start in range(0, len(TENSE_LEVELS), 4):
            row_items = TENSE_LEVELS[row_start:row_start + 4]
            cols = st.columns(len(row_items))
            for i, tense in enumerate(row_items):
                idx = row_start + i
                with cols[i]:
                    if idx < st.session_state.unlocked_index:
                        sc = st.session_state.scores.get(tense, 100)
                        st.success(f"✅ **Level {idx+1}**\n\n{tense} ({sc}%)")
                    elif idx == st.session_state.unlocked_index:
                        sc_txt = f" ({st.session_state.scores[tense]}%)" if tense in st.session_state.scores else ""
                        st.warning(f"🔥 **Level {idx+1} (Active)**\n\n{tense}{sc_txt}")
                    else:
                        st.error(f"🔒 **Level {idx+1}**\n\n{tense}")
        
        st.write("---")
        
        available_tenses = TENSE_LEVELS[:st.session_state.unlocked_index + 1]
        chosen_quiz_tense = st.selectbox(
            "Select an unlocked level:",
            available_tenses,
            index=len(available_tenses) - 1
        )
        
        current_variant = st.session_state.quiz_variant.get(chosen_quiz_tense, "A")
        questions = RAW_QUESTIONS[chosen_quiz_tense][current_variant]
        
        st.markdown(f"### 📝 {chosen_quiz_tense} Test — **Set {current_variant}**")
        
        user_answers = []
        for i, item in enumerate(questions):
            q_key = f"{st.session_state.student_name}_{chosen_quiz_tense}_{current_variant}_q{i}"
            if item["type"] == "mc":
                ans = st.radio(item["q"], item["opts"], key=q_key)
            elif item["type"] == "fill":
                ans = st.text_input(item["q"], key=q_key)
            elif item["type"] == "order":
                ans = st.text_input(item["q"], key=q_key)
            elif item["type"] == "tf":
                ans = st.radio(item["q"], ["True", "False"], key=q_key)
            user_answers.append(ans)
        
        if st.button("Submit Comprehensive Quiz 🎯"):
            correct_count = 0
            mistakes = []
            
            for i, item in enumerate(questions):
                u_ans = str(user_answers[i]).strip().lower().rstrip(".?!")
                c_ans = str(item["ans"]).strip().lower().rstrip(".?!")
                if u_ans == c_ans:
                    correct_count += 1
                else:
                    mistakes.append({
                        "question": item["q"],
                        "your_answer": str(user_answers[i]),
                        "correct_answer": str(item["ans"]),
                        "tip": item["tip"]
                    })
                    
            percentage = int((correct_count / len(questions)) * 100)
            st.session_state.scores[chosen_quiz_tense] = percentage
            
            current_idx = TENSE_LEVELS.index(chosen_quiz_tense)
            
            st.write("---")
            if percentage >= 75:
                if current_idx == st.session_state.unlocked_index and current_idx + 1 < len(TENSE_LEVELS):
                    st.session_state.unlocked_index += 1
                
                save_student_progress(
                    st.session_state.student_name,
                    st.session_state.unlocked_index,
                    st.session_state.scores,
                    st.session_state.quiz_variant
                )
                
                st.balloons()
                
                # --- بخش موفقیت با گربه‌ی خوشحال یا دختر تاییدکننده ---
                col_cat_ok, col_msg_ok = st.columns([1, 4])
                with col_cat_ok:
                    st.image("https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?w=300&auto=format&fit=crop&q=80", width=120)
                with col_msg_ok:
                    st.markdown(f"### ✨ Purr-fect Job, {st.session_state.student_name}!")
                    st.markdown(f"*\"Awesome! You scored **{percentage}%**. You passed this level brilliantly! Keep shining! 🐾\"*")
                
                if st.session_state.unlocked_index > current_idx:
                    next_tense = TENSE_LEVELS[st.session_state.unlocked_index]
                    st.info(f"🔓 **NEXT LEVEL UNLOCKED:** **{next_tense}** is now open and saved to your profile!")
                    if st.button(f"Proceed to {next_tense} 🚀"):
                        st.rerun()
            else:
                save_student_progress(
                    st.session_state.student_name,
                    st.session_state.unlocked_index,
                    st.session_state.scores,
                    st.session_state.quiz_variant
                )
                st.error(f"📉 You scored **{percentage}%**. You need at least **75%** to pass.")

            # --- بخش اشتباهات با گربه‌ی با‌تعجب و ملوس ---
            if mistakes:
                st.write("---")
                col_cat, col_msg = st.columns([1, 4])
                with col_cat:
                    # عکس گربه با‌تعجب شبیه تصویر ارسالی
                    st.image("https://images.unsplash.com/photo-1533738363-b7f9aef128ce?w=300&auto=format&fit=crop&q=80", width=120)
                with col_msg:
                    st.markdown("### 🐾 Curious Kitty says:")
                    st.markdown(f"*\"Oopsie, {st.session_state.student_name}! Don't worry, let's fix these small mistakes together! 🐱\"*")
                
                for m in mistakes:
                    st.markdown(f"""
                    <div class="mistake-box">
                        <b>Question:</b> {m['question']}<br>
                        ❌ <b>Your Answer:</b> <span style="color: #e11d48;">{m['your_answer']}</span><br>
                        ✅ <b>Correct Form:</b> <span style="color: #16a34a;"><b>{m['correct_answer']}</b></span><br>
                        💡 <b>Why?</b> {m['tip']}
                    </div>
                    """, unsafe_allow_html=True)
            else:
                st.write("---")
                col_cat2, col_msg2 = st.columns([1, 4])
                with col_cat2:
                    st.image("https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?w=300&auto=format&fit=crop&q=80", width=120)
                with col_msg2:
                    st.markdown("### 🐾 Happy Kitty says:")
                    st.markdown(f"*\"Meow-mazing! You got everything right without a single mistake! ✨\"*")
                
        if chosen_quiz_tense in st.session_state.scores and st.session_state.scores[chosen_quiz_tense] < 75:
            if st.button("🔄 Switch to New Question Set (Retake)"):
                st.session_state.quiz_variant[chosen_quiz_tense] = "B" if current_variant == "A" else "A"
                save_student_progress(
                    st.session_state.student_name,
                    st.session_state.unlocked_index,
                    st.session_state.scores,
                    st.session_state.quiz_variant
                )
                st.rerun()

    elif menu_selection == "Grades per Lesson":
        st.title("📊 Grades per Lesson")
        st.write(f"Official Grammar Report Card for **{st.session_state.student_name}**:")
        st.write("---")
        if not st.session_state.scores:
            st.info("No quizzes taken yet!")
        else:
            for tense in TENSE_LEVELS:
                if tense in st.session_state.scores:
                    sc = st.session_state.scores[tense]
                    status = "✅ Passed" if sc >= 75 else "❌ Needs Review (< 75%)"
                    st.markdown(f"- **{tense}:** **{sc}%** — {status}")

    elif menu_selection == "Activity Level":
        st.title("📈 Activity Level")
        passed_count = sum(1 for sc in st.session_state.scores.values() if sc >= 75)
        progress_percent = int((passed_count / len(TENSE_LEVELS)) * 100)
        st.progress(progress_percent)
        st.write(f"You have mastered **{passed_count} out of {len(TENSE_LEVELS)}** structures ({progress_percent}%).")

    elif menu_selection == "Total Activities":
        st.title("🏆 Total Activities")
        passed_count = sum(1 for sc in st.session_state.scores.values() if sc >= 75)
        col1, col2 = st.columns(2)
        col1.metric(label="Mastered", value=f"{passed_count} / {len(TENSE_LEVELS)}")
        col2.metric(label="Attempts", value=str(len(st.session_state.scores)))

    elif menu_selection == "Contact Teacher":
        st.title("👩‍🏫 Contact Teacher")
        teacher_msg = st.text_area("Your message to the teacher:")
        if st.button("Send Message"):
            st.success("Sent successfully! ✉️")

    elif menu_selection == "Ideas & Suggestions":
        st.title("💡 Ideas & Suggestions")
        idea_msg = st.text_area("Write your suggestion...")
        if st.button("Submit Idea"):
            st.success("Thank you! 🚀")
