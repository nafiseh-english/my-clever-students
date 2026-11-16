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

# --- بانک سوالات دوگانه (Set A و Set B) برای تمام ۱۳ ساختار ---
QUIZ_BANK = {
    "Simple Present": {
        "A": [
            {"q": "1. Sara _____ English every day.", "opts": ["study", "studies", "studying"], "ans": "studies"},
            {"q": "2. Ali and Reza _____ football on Fridays.", "opts": ["plays", "play", "playing"], "ans": "play"},
            {"q": "3. _____ she like ice cream?", "opts": ["Do", "Does", "Is"], "ans": "Does"},
            {"q": "4. They _____ live in Tehran.", "opts": ["doesn't", "don't", "aren't"], "ans": "don't"},
        ],
        "B": [
            {"q": "1. The sun _____ in the east.", "opts": ["rise", "rises", "rising"], "ans": "rises"},
            {"q": "2. My father _____ to work by car.", "opts": ["go", "goes", "going"], "ans": "goes"},
            {"q": "3. _____ you drink coffee in the morning?", "opts": ["Do", "Does", "Are"], "ans": "Do"},
            {"q": "4. Bahar _____ watch TV at night.", "opts": ["don't", "doesn't", "isn't"], "ans": "doesn't"},
        ]
    },
    "Present Continuous": {
        "A": [
            {"q": "1. Look! It _____ outside right now.", "opts": ["rains", "is raining", "rained"], "ans": "is raining"},
            {"q": "2. I _____ studying for my exam at the moment.", "opts": ["am", "is", "are"], "ans": "am"},
            {"q": "3. What _____ Darya and Setareh doing now?", "opts": ["is", "do", "are"], "ans": "are"},
            {"q": "4. Listen! Someone _____ at the door.", "opts": ["knocks", "is knocking", "knocked"], "ans": "is knocking"},
        ],
        "B": [
            {"q": "1. Be quiet! The baby _____.", "opts": ["sleeps", "is sleeping", "slept"], "ans": "is sleeping"},
            {"q": "2. We _____ watching a movie right now.", "opts": ["are", "is", "do"], "ans": "are"},
            {"q": "3. Why _____ Jamil running so fast?", "opts": ["are", "does", "is"], "ans": "is"},
            {"q": "4. They _____ playing video games at the moment.", "opts": ["aren't", "don't", "isn't"], "ans": "aren't"},
        ]
    },
    "Present Perfect": {
        "A": [
            {"q": "1. I _____ already finished my homework.", "opts": ["have", "has", "am"], "ans": "have"},
            {"q": "2. Nafiseh _____ visited Paris twice.", "opts": ["have", "has", "is"], "ans": "has"},
            {"q": "3. Have you ever _____ sushi?", "opts": ["eat", "ate", "eaten"], "ans": "eaten"},
            {"q": "4. We _____ lived here since 2020.", "opts": ["have", "has", "did"], "ans": "have"},
        ],
        "B": [
            {"q": "1. Mohammad _____ just arrived home.", "opts": ["have", "has", "was"], "ans": "has"},
            {"q": "2. They _____ never seen snow before.", "opts": ["has", "have", "are"], "ans": "have"},
            {"q": "3. Has Ali _____ his keys yet?", "opts": ["find", "found", "finding"], "ans": "found"},
            {"q": "4. She has worked here _____ five years.", "opts": ["since", "for", "ago"], "ans": "for"},
        ]
    },
    "Present Perfect Continuous": {
        "A": [
            {"q": "1. I have _____ studying English for two hours.", "opts": ["be", "been", "being"], "ans": "been"},
            {"q": "2. It _____ been raining since morning.", "opts": ["have", "has", "is"], "ans": "has"},
            {"q": "3. How long have you been _____ here?", "opts": ["wait", "waited", "waiting"], "ans": "waiting"},
            {"q": "4. They _____ been playing tennis all afternoon.", "opts": ["have", "has", "are"], "ans": "have"},
        ],
        "B": [
            {"q": "1. Sara has been _____ on this project for weeks.", "opts": ["work", "worked", "working"], "ans": "working"},
            {"q": "2. We _____ been living in this city since 2018.", "opts": ["have", "has", "were"], "ans": "have"},
            {"q": "3. Why are your eyes red? Have you been _____?", "opts": ["cry", "crying", "cried"], "ans": "crying"},
            {"q": "4. Reza _____ been feeling well lately.", "opts": ["haven't", "hasn't", "isn't"], "ans": "hasn't"},
        ]
    },
    "Simple Past": {
        "A": [
            {"q": "1. We _____ to the cinema yesterday.", "opts": ["go", "went", "gone"], "ans": "went"},
            {"q": "2. Did you _____ Sara at school?", "opts": ["see", "saw", "seen"], "ans": "see"},
            {"q": "3. Reza _____ play football last weekend.", "opts": ["don't", "doesn't", "didn't"], "ans": "didn't"},
            {"q": "4. They _____ very happy at the party.", "opts": ["was", "were", "are"], "ans": "were"},
        ],
        "B": [
            {"q": "1. I _____ a great book last night.", "opts": ["read", "reads", "reading"], "ans": "read"},
            {"q": "2. Where _____ Bahar go on vacation?", "opts": ["do", "does", "did"], "ans": "did"},
            {"q": "3. She _____ buy that dress yesterday.", "opts": ["didn't", "wasn't", "doesn't"], "ans": "didn't"},
            {"q": "4. He _____ born in 2010.", "opts": ["were", "was", "is"], "ans": "was"},
        ]
    },
    "Past Continuous": {
        "A": [
            {"q": "1. I _____ watching TV when you called.", "opts": ["was", "were", "am"], "ans": "was"},
            {"q": "2. They _____ playing football at 5 PM yesterday.", "opts": ["was", "were", "are"], "ans": "were"},
            {"q": "3. What _____ you doing when it started to rain?", "opts": ["was", "were", "did"], "ans": "were"},
            {"q": "4. Setareh _____ sleeping at midnight.", "opts": ["wasn't", "weren't", "didn't"], "ans": "wasn't"},
        ],
        "B": [
            {"q": "1. While Ali _____ driving, he saw an accident.", "opts": ["was", "were", "is"], "ans": "was"},
            {"q": "2. We _____ studying English all evening.", "opts": ["was", "were", "have"], "ans": "were"},
            {"q": "3. _____ Darya cooking dinner at 7 PM?", "opts": ["Was", "Were", "Did"], "ans": "Was"},
            {"q": "4. The kids _____ making noise while I was working.", "opts": ["was", "were", "are"], "ans": "were"},
        ]
    },
    "Past Perfect": {
        "A": [
            {"q": "1. When I arrived, the train had already _____.", "opts": ["leave", "left", "leaving"], "ans": "left"},
            {"q": "2. She _____ never seen a bear before she went to Canada.", "opts": ["has", "had", "was"], "ans": "had"},
            {"q": "3. After they had _____ dinner, they went for a walk.", "opts": ["eat", "ate", "eaten"], "ans": "eaten"},
            {"q": "4. He failed the test because he _____ studied.", "opts": ["hadn't", "hasn't", "didn't"], "ans": "hadn't"},
        ],
        "B": [
            {"q": "1. By the time we got to the theater, the movie _____ started.", "opts": ["has", "had", "was"], "ans": "had"},
            {"q": "2. I realized I had _____ my wallet at home.", "opts": ["forget", "forgot", "forgotten"], "ans": "forgotten"},
            {"q": "3. Had Jamil _____ his work before 6 PM?", "opts": ["finish", "finished", "finishing"], "ans": "finished"},
            {"q": "4. They were tired because they _____ walked all day.", "opts": ["have", "had", "were"], "ans": "had"},
        ]
    },
    "Past Perfect Continuous": {
        "A": [
            {"q": "1. We had been _____ for an hour before the bus came.", "opts": ["wait", "waited", "waiting"], "ans": "waiting"},
            {"q": "2. She was tired because she _____ been running.", "opts": ["has", "had", "was"], "ans": "had"},
            {"q": "3. How long had you _____ studying before you took the test?", "opts": ["be", "been", "being"], "ans": "been"},
            {"q": "4. They had been _____ in London for ten years before moving.", "opts": ["live", "lived", "living"], "ans": "living"},
        ],
        "B": [
            {"q": "1. The ground was wet because it had been _____.", "opts": ["rain", "rained", "raining"], "ans": "raining"},
            {"q": "2. Ali _____ been working there for five years before he quit.", "opts": ["has", "had", "was"], "ans": "had"},
            {"q": "3. I had been _____ to call you all morning.", "opts": ["try", "tried", "trying"], "ans": "trying"},
            {"q": "4. He hadn't been _____ well for weeks.", "opts": ["feel", "felt", "feeling"], "ans": "feeling"},
        ]
    },
    "Simple Future (will)": {
        "A": [
            {"q": "1. Tomorrow, they _____ visit their grandparents.", "opts": ["will", "did", "are"], "ans": "will"},
            {"q": "2. I promise I _____ help you with your project.", "opts": ["will", "am", "was"], "ans": "will"},
            {"q": "3. It _____ rain tomorrow, look at the forecast.", "opts": ["will", "does", "did"], "ans": "will"},
            {"q": "4. She _____ be late for the meeting.", "opts": ["won't", "didn't", "isn't"], "ans": "won't"},
        ],
        "B": [
            {"q": "1. I think Jamil _____ pass the exam easily.", "opts": ["will", "is", "was"], "ans": "will"},
            {"q": "2. _____ you open the window, please?", "opts": ["Will", "Do", "Are"], "ans": "Will"},
            {"q": "3. We _____ travel to Shiraz next month.", "opts": ["will", "did", "were"], "ans": "will"},
            {"q": "4. Don't worry, I _____ tell anyone your secret.", "opts": ["won't", "don't", "didn't"], "ans": "won't"},
        ]
    },
    "Future with 'be going to'": {
        "A": [
            {"q": "1. Look at those dark clouds! It is _____ to rain.", "opts": ["go", "going", "will"], "ans": "going"},
            {"q": "2. I _____ going to buy a new laptop next week.", "opts": ["am", "is", "are"], "ans": "am"},
            {"q": "3. What _____ Nafiseh going to do after graduation?", "opts": ["am", "is", "are"], "ans": "is"},
            {"q": "4. We are going to _____ a party on Friday.", "opts": ["have", "has", "having"], "ans": "have"},
        ],
        "B": [
            {"q": "1. They _____ going to travel to Spain this summer.", "opts": ["am", "is", "are"], "ans": "are"},
            {"q": "2. Sara is going to _____ medicine at university.", "opts": ["study", "studies", "studying"], "ans": "study"},
            {"q": "3. Be careful! You are _____ to drop that glass!", "opts": ["go", "going", "went"], "ans": "going"},
            {"q": "4. He _____ going to watch TV tonight.", "opts": ["isn't", "aren't", "doesn't"], "ans": "isn't"},
        ]
    },
    "Future Continuous": {
        "A": [
            {"q": "1. This time tomorrow, I will be _____ on the beach.", "opts": ["relax", "relaxed", "relaxing"], "ans": "relaxing"},
            {"q": "2. At 8 PM tonight, we _____ be watching the match.", "opts": ["will", "are", "have"], "ans": "will"},
            {"q": "3. Don't call her at 9; she will _____ sleeping.", "opts": ["be", "been", "being"], "ans": "be"},
            {"q": "4. Will you be _____ the car tomorrow morning?", "opts": ["use", "used", "using"], "ans": "using"},
        ],
        "B": [
            {"q": "1. Next week, Darya will be _____ in New York.", "opts": ["work", "worked", "working"], "ans": "working"},
            {"q": "2. They _____ be studying for finals all weekend.", "opts": ["will", "are", "did"], "ans": "will"},
            {"q": "3. What will you _____ doing at this time next year?", "opts": ["be", "been", "is"], "ans": "be"},
            {"q": "4. I won't be _____ at the office tomorrow.", "opts": ["stay", "stayed", "staying"], "ans": "staying"},
        ]
    },
    "Future Perfect": {
        "A": [
            {"q": "1. By next year, I will have _____ from university.", "opts": ["graduate", "graduated", "graduating"], "ans": "graduated"},
            {"q": "2. She _____ have finished the report by 5 PM.", "opts": ["will", "is", "has"], "ans": "will"},
            {"q": "3. By the time you arrive, we will _____ eaten dinner.", "opts": ["has", "have", "had"], "ans": "have"},
            {"q": "4. Will they have _____ the house before winter?", "opts": ["build", "built", "building"], "ans": "built"},
        ],
        "B": [
            {"q": "1. By 2030, scientists will have _____ a cure.", "opts": ["find", "found", "finding"], "ans": "found"},
            {"q": "2. Mohammad _____ have saved enough money by June.", "opts": ["will", "does", "is"], "ans": "will"},
            {"q": "3. I will have _____ three books by the end of the month.", "opts": ["read", "reads", "reading"], "ans": "read"},
            {"q": "4. The train _____ have left by the time we get there.", "opts": ["will", "is", "was"], "ans": "will"},
        ]
    },
    "Future Perfect Continuous": {
        "A": [
            {"q": "1. By next month, I will have been _____ here for 5 years.", "opts": ["work", "worked", "working"], "ans": "working"},
            {"q": "2. At 6 PM, she will have _____ driving for four hours.", "opts": ["be", "been", "being"], "ans": "been"},
            {"q": "3. How long will you _____ been studying English by June?", "opts": ["has", "have", "had"], "ans": "have"},
            {"q": "4. They _____ have been living together for a decade next year.", "opts": ["will", "are", "have"], "ans": "will"},
        ],
        "B": [
            {"q": "1. By midnight, we will have been _____ for 12 hours.", "opts": ["travel", "traveled", "traveling"], "ans": "traveling"},
            {"q": "2. Next week, Bahar will have _____ teaching for 10 years.", "opts": ["be", "been", "being"], "ans": "been"},
            {"q": "3. He will _____ been waiting for two hours by the time she arrives.", "opts": ["has", "have", "had"], "ans": "have"},
            {"q": "4. By 2028, I _____ have been playing the piano for 15 years.", "opts": ["will", "am", "was"], "ans": "will"},
        ]
    }
}

# --- مدیریت وضعیت و پیشرفت دانش‌آموز (Session State) ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "unlocked_index" not in st.session_state:
    st.session_state.unlocked_index = 0
if "quiz_variant" not in st.session_state:
    st.session_state.quiz_variant = {tense: "A" for tense in TENSE_LEVELS}
if "scores" not in st.session_state:
    st.session_state.scores = {}

# --- صفحه ورود ---
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
        st.caption(f"Current Level: **{TENSE_LEVELS[st.session_state.unlocked_index]}**")
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
        st.markdown("Select any of the 13 structures below to review its formula, usage, and examples:")
        
        selected_tense = st.selectbox("Choose a Structure to Review:", TENSE_LEVELS)
        st.write("---")
        
        if selected_tense == "Simple Present":
            st.subheader("☀️ Simple Present Tense")
            st.markdown("**Usage:** Habits, daily routines, and general facts.")
            col1, col2 = st.columns(2)
            with col1:
                st.success("✅ **Positive:** I/You/We/They + Verb | He/She/It + Verb + **s/es**")
            with col2:
                st.info("❌ **Negative:** don't / doesn't + Base Verb")
            st.markdown("#### 📝 Examples:\n- She **wakes up** early every morning.\n- They **play** tennis on Fridays.")
            
        elif selected_tense == "Present Continuous":
            st.subheader("🏃 Present Continuous Tense")
            st.markdown("**Usage:** Actions happening right now, at the moment of speaking.")
            st.success("✅ **Formula:** Subject + **am / is / are** + Verb-**ing**")
            st.markdown("#### 📝 Examples:\n- I **am studying** English right now.\n- Look! It **is raining** outside.")
            
        elif selected_tense == "Present Perfect":
            st.subheader("🎯 Present Perfect Tense")
            st.markdown("**Usage:** Past actions with a result or connection to the present.")
            st.success("✅ **Formula:** Subject + **have / has** + **Past Participle (V3)**")
            st.markdown("#### 📝 Examples:\n- I **have visited** Paris twice.\n- She **has finished** her homework.")

        elif selected_tense == "Present Perfect Continuous":
            st.subheader("⏳ Present Perfect Continuous Tense")
            st.markdown("**Usage:** Actions that started in the past and are still continuing now.")
            st.success("✅ **Formula:** Subject + **have / has + been** + Verb-**ing**")
            st.markdown("#### 📝 Examples:\n- I **have been studying** English for two hours.\n- It **has been raining** since morning.")
            
        elif selected_tense == "Simple Past":
            st.subheader("🕰️ Simple Past Tense")
            st.markdown("**Usage:** Completed actions at a specific time in the past.")
            col1, col2 = st.columns(2)
            with col1:
                st.success("✅ **Positive:** Subject + **Past Verb (V2)**")
            with col2:
                st.info("❌ **Negative:** Subject + **didn't** + Base Verb")
            st.markdown("#### 📝 Examples:\n- We **went** to the cinema yesterday.\n- He **didn't play** football last weekend.")
                
        elif selected_tense == "Past Continuous":
            st.subheader("🎞️ Past Continuous Tense")
            st.markdown("**Usage:** Actions that were in progress at a specific moment in the past.")
            st.success("✅ **Formula:** Subject + **was / were** + Verb-**ing**")
            st.markdown("#### 📝 Examples:\n- I **was watching** TV when you called.\n- They **were playing** football at 5 PM.")

        elif selected_tense == "Past Perfect":
            st.subheader("📜 Past Perfect Tense")
            st.markdown("**Usage:** An action that happened before another action in the past.")
            st.success("✅ **Formula:** Subject + **had** + **Past Participle (V3)**")
            st.markdown("#### 📝 Examples:\n- When I arrived, the train **had already left**.\n- She **had eaten** dinner before we got home.")

        elif selected_tense == "Past Perfect Continuous":
            st.subheader("🔄 Past Perfect Continuous Tense")
            st.markdown("**Usage:** Ongoing past action that continued up until another past moment.")
            st.success("✅ **Formula:** Subject + **had + been** + Verb-**ing**")
            st.markdown("#### 📝 Examples:\n- We **had been waiting** for an hour before the bus came.\n- She was tired because she **had been running**.")
            
        elif selected_tense == "Simple Future (will)":
            st.subheader("🚀 Simple Future Tense (will)")
            st.markdown("**Usage:** Spontaneous decisions, promises, and general predictions.")
            st.success("✅ **Formula:** Subject + **will** + Base Verb")
            st.markdown("#### 📝 Examples:\n- I **will help** you with your homework.\n- It **will rain** tomorrow.")

        elif selected_tense == "Future with 'be going to'":
            st.subheader("📅 Future with 'be going to'")
            st.markdown("**Usage:** Planned future intentions and predictions based on present evidence.")
            st.success("✅ **Formula:** Subject + **am / is / are + going to** + Base Verb")
            st.markdown("#### 📝 Examples:\n- I **am going to buy** a new laptop next week.\n- Look at the clouds! It **is going to rain**.")

        elif selected_tense == "Future Continuous":
            st.subheader("🛸 Future Continuous Tense")
            st.markdown("**Usage:** Actions that will be in progress at a specific time in the future.")
            st.success("✅ **Formula:** Subject + **will + be** + Verb-**ing**")
            st.markdown("#### 📝 Examples:\n- This time tomorrow, I **will be relaxing** on the beach.\n- At 8 PM tonight, we **will be watching** the match.")

        elif selected_tense == "Future Perfect":
            st.subheader("🏆 Future Perfect Tense")
            st.markdown("**Usage:** Actions that will be completed before a specific time in the future.")
            st.success("✅ **Formula:** Subject + **will + have** + **Past Participle (V3)**")
            st.markdown("#### 📝 Examples:\n- By next year, I **will have graduated** from university.\n- She **will have finished** the report by 5 PM.")

        elif selected_tense == "Future Perfect Continuous":
            st.subheader("🌟 Future Perfect Continuous Tense")
            st.markdown("**Usage:** Emphasizes the duration of an action up to a certain point in the future.")
            st.success("✅ **Formula:** Subject + **will + have + been** + Verb-**ing**")
            st.markdown("#### 📝 Examples:\n- By next month, I **will have been working** here for 5 years.\n- At 6 PM, she **will have been driving** for four hours.")

    elif menu_selection == "Games & Quiz":
        st.title("🎮 Mastery Quests & Grammar Challenges")
        st.info("📌 **Rule:** Score **75% or higher** on each structure to unlock the next level! If you score below 75%, review the lesson and generate a **new quiz version**.")
        
        tab1, tab2, tab3 = st.tabs(["🏆 13-Level Mastery Quizzes", "🧩 Sentence Unscrambler", "🕵️ Spot the Mistake"])
        
        # --- تب اول: کوییزهای مرحله‌ای برای تمام ۱۳ ساختار ---
        with tab1:
            st.subheader("🗺️ Your 13-Level Learning Path")
            
            # نمایش مراحل در ردیف‌های 4 تایی برای زیبایی بیشتر
            for row_start in range(0, len(TENSE_LEVELS), 4):
                row_items = TENSE_LEVELS[row_start:row_start + 4]
                cols = st.columns(len(row_items))
                for i, tense in enumerate(row_items):
                    idx = row_start + i
                    with cols[i]:
                        if idx <= st.session_state.unlocked_index:
                            score_txt = f" ({st.session_state.scores[tense]}%)" if tense in st.session_state.scores else ""
                            st.success(f"🔓 **Level {idx+1}**\n\n{tense}{score_txt}")
                        else:
                            st.error(f"🔒 **Level {idx+1}**\n\n{tense}")
            
            st.write("---")
            
            available_tenses = TENSE_LEVELS[:st.session_state.unlocked_index + 1]
            chosen_quiz_tense = st.selectbox("Select an unlocked level to take its quiz:", available_tenses)
            
            current_variant = st.session_state.quiz_variant[chosen_quiz_tense]
            questions = QUIZ_BANK[chosen_quiz_tense][current_variant]
            
            st.markdown(f"### 📝 {chosen_quiz_tense} Quiz — **Version {current_variant}**")
            
            user_answers = []
            for i, item in enumerate(questions):
                ans = st.radio(item["q"], item["opts"], key=f"{chosen_quiz_tense}_{current_variant}_q{i}")
                user_answers.append(ans)
            
            if st.button("Submit Quiz 🎯"):
                correct_count = sum(1 for i, item in enumerate(questions) if user_answers[i] == item["ans"])
                percentage = int((correct_count / len(questions)) * 100)
                st.session_state.scores[chosen_quiz_tense] = percentage
                
                st.write("---")
                if percentage >= 75:
                    st.balloons()
                    st.success(f"🎉 Awesome job, {st.session_state.student_name}! You scored **{percentage}%** ({correct_count}/4)!")
                    
                    current_idx = TENSE_LEVELS.index(chosen_quiz_tense)
                    if current_idx == st.session_state.unlocked_index and current_idx + 1 < len(TENSE_LEVELS):
                        st.session_state.unlocked_index += 1
                        next_tense = TENSE_LEVELS[st.session_state.unlocked_index]
                        st.info(f"🔓 **NEW LEVEL UNLOCKED:** You can now study and take the quiz for **{next_tense}**!")
                        if st.button(f"Continue to {next_tense} 🚀"):
                            st.rerun()
                    elif current_idx + 1 == len(TENSE_LEVELS):
                        st.success("🏆 **GRAND MASTER!** You have mastered ALL 13 English grammar structures!")
                else:
                    st.error(f"📉 You scored **{percentage}%** ({correct_count}/4). You need at least **75%** to unlock the next level.")
                    st.warning("💡 Go back to the **Review** tab, study the rules carefully, and click below to try a **new quiz with different questions**!")
                    
            if chosen_quiz_tense in st.session_state.scores and st.session_state.scores[chosen_quiz_tense] < 75:
                if st.button("🔄 Generate New Quiz Questions (Retake)"):
                    st.session_state.quiz_variant[chosen_quiz_tense] = "B" if current_variant == "A" else "A"
                    st.rerun()

        # --- تب دوم: بازی مرتب کردن جملات ---
        with tab2:
            st.subheader("🧩 Put the words in the correct order!")
            st.info("Scrambled words: **`football / plays / Ali / Fridays / on`**")
            
            user_order = st.text_input("Write the correct sentence:", key="scramble1")
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
        st.write(f"Official Grammar Report Card for **{st.session_state.student_name}**:")
        st.write("---")
        
        if not st.session_state.scores:
            st.info("No quizzes taken yet! Go to **Games & Quiz** to start Level 1 (Simple Present).")
        else:
            for tense in TENSE_LEVELS:
                if tense in st.session_state.scores:
                    sc = st.session_state.scores[tense]
                    status = "✅ Passed" if sc >= 75 else "❌ Needs Review (< 75%)"
                    st.markdown(f"- **{tense}:** **{sc}%** — {status}")
                else:
                    st.markdown(f"- **{tense}:** *Not attempted yet*")

    elif menu_selection == "Activity Level":
        st.title("📈 Activity Level")
        progress_percent = int(((st.session_state.unlocked_index + 1) / len(TENSE_LEVELS)) * 100)
        st.write("Your current course progression:")
        st.progress(progress_percent)
        st.write(f"You have unlocked **{st.session_state.unlocked_index + 1} out of {len(TENSE_LEVELS)}** grammar levels ({progress_percent}%).")

    elif menu_selection == "Total Activities":
        st.title("🏆 Total Activities")
        st.write("Summary of your achievements:")
        passed_count = sum(1 for sc in st.session_state.scores.values() if sc >= 75)
        col1, col2 = st.columns(2)
        col1.metric(label="Levels Passed (75%+)", value=f"{passed_count} / {len(TENSE_LEVELS)}")
        col2.metric(label="Quizzes Attempted", value=str(len(st.session_state.scores)))

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
