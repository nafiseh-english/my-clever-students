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

# --- سیستم ذخیره دائمی پیشرفت دانش‌آموزان (جلوگیری از ریست شدن با رفرش) ---
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

# --- بانک جامع ۲۰ سوالی برای هر ۱۳ ساختار (۱۰ سوال Version A + ۱۰ سوال Version B) ---
# انواع سوال: "mc" (چهارگزینه‌ای), "fill" (جای خالی), "order" (جمله‌سازی), "tf" (True/False)
RAW_QUESTIONS = {
    "Simple Present": {
        "A": [
            {"type": "mc", "q": "1. Sara _____ English every day.", "opts": ["study", "studies", "studying"], "ans": "studies"},
            {"type": "mc", "q": "2. Ali and Reza _____ football on Fridays.", "opts": ["plays", "play", "playing"], "ans": "play"},
            {"type": "mc", "q": "3. _____ she like ice cream?", "opts": ["Do", "Does", "Is"], "ans": "Does"},
            {"type": "fill", "q": "4. Fill in the blank: He _____ (go) to school by bus every morning.", "ans": "goes"},
            {"type": "fill", "q": "5. Fill in the blank: They _____ (not / live) in Shiraz.", "ans": "don't live"},
            {"type": "fill", "q": "6. Fill in the blank: Water _____ (boil) at 100 degrees Celsius.", "ans": "boils"},
            {"type": "order", "q": "7. Make a correct sentence: `always / early / wakes up / Bahar`", "ans": "bahar always wakes up early"},
            {"type": "order", "q": "8. Make a correct sentence: `coffee / drink / you / do / ?`", "ans": "do you drink coffee"},
            {"type": "tf", "q": "9. True or False: 'She don't like spicy food.' is grammatically correct.", "ans": "False"},
            {"type": "tf", "q": "10. True or False: We add '-s' or '-es' to verbs for He/She/It in positive sentences.", "ans": "True"},
        ],
        "B": [
            {"type": "mc", "q": "1. The sun _____ in the east.", "opts": ["rise", "rises", "rising"], "ans": "rises"},
            {"type": "mc", "q": "2. My father _____ to work by car.", "opts": ["go", "goes", "going"], "ans": "goes"},
            {"type": "mc", "q": "3. _____ you drink tea in the morning?", "opts": ["Do", "Does", "Are"], "ans": "Do"},
            {"type": "fill", "q": "4. Fill in the blank: Darya _____ (watch) TV every evening.", "ans": "watches"},
            {"type": "fill", "q": "5. Fill in the blank: Jamil _____ (not / play) video games on weekdays.", "ans": "doesn't play"},
            {"type": "fill", "q": "6. Fill in the blank: Cats _____ (like) milk.", "ans": "like"},
            {"type": "order", "q": "7. Make a correct sentence: `on / tennis / play / Fridays / we`", "ans": "we play tennis on fridays"},
            {"type": "order", "q": "8. Make a correct sentence: `does / live / where / Setareh / ?`", "ans": "where does setareh live"},
            {"type": "tf", "q": "9. True or False: 'Does he plays football?' is correct.", "ans": "False"},
            {"type": "tf", "q": "10. True or False: Simple Present is used for daily habits and general truths.", "ans": "True"},
        ]
    },
    "Present Continuous": {
        "A": [
            {"type": "mc", "q": "1. Look! It _____ outside right now.", "opts": ["rains", "is raining", "rained"], "ans": "is raining"},
            {"type": "mc", "q": "2. I _____ studying for my exam at the moment.", "opts": ["am", "is", "are"], "ans": "am"},
            {"type": "mc", "q": "3. What _____ Darya and Setareh doing now?", "opts": ["is", "do", "are"], "ans": "are"},
            {"type": "fill", "q": "4. Fill in the blank: Listen! Someone _____ (knock) at the door.", "ans": "is knocking"},
            {"type": "fill", "q": "5. Fill in the blank: They _____ (not / watch) TV right now.", "ans": "aren't watching"},
            {"type": "fill", "q": "6. Fill in the blank: Reza _____ (write) an email at the moment.", "ans": "is writing"},
            {"type": "order", "q": "7. Make a correct sentence: `now / reading / a book / am / I`", "ans": "i am reading a book now"},
            {"type": "order", "q": "8. Make a correct sentence: `are / going / where / you / ?`", "ans": "where are you going"},
            {"type": "tf", "q": "9. True or False: 'She is cook dinner now.' is correct.", "ans": "False"},
            {"type": "tf", "q": "10. True or False: Present Continuous uses 'am/is/are + verb-ing'.", "ans": "True"},
        ],
        "B": [
            {"type": "mc", "q": "1. Be quiet! The baby _____.", "opts": ["sleeps", "is sleeping", "slept"], "ans": "is sleeping"},
            {"type": "mc", "q": "2. We _____ watching a movie right now.", "opts": ["are", "is", "do"], "ans": "are"},
            {"type": "mc", "q": "3. Why _____ Jamil running so fast?", "opts": ["are", "does", "is"], "ans": "is"},
            {"type": "fill", "q": "4. Fill in the blank: Nafiseh _____ (cook) pasta at the moment.", "ans": "is cooking"},
            {"type": "fill", "q": "5. Fill in the blank: I _____ (not / sleep) right now.", "ans": "am not sleeping"},
            {"type": "fill", "q": "6. Fill in the blank: Look! The birds _____ (fly) south.", "ans": "are flying"},
            {"type": "order", "q": "7. Make a correct sentence: `playing / in the park / are / the kids`", "ans": "the kids are playing in the park"},
            {"type": "order", "q": "8. Make a correct sentence: `is / raining / it / today / ?`", "ans": "is it raining today"},
            {"type": "tf", "q": "9. True or False: 'They are swiming in the pool.' has correct spelling.", "ans": "False"},
            {"type": "tf", "q": "10. True or False: Words like 'now' and 'at the moment' are common with Present Continuous.", "ans": "True"},
        ]
    },
    "Present Perfect": {
        "A": [
            {"type": "mc", "q": "1. I _____ already finished my homework.", "opts": ["have", "has", "am"], "ans": "have"},
            {"type": "mc", "q": "2. Nafiseh _____ visited Paris twice.", "opts": ["have", "has", "is"], "ans": "has"},
            {"type": "mc", "q": "3. Have you ever _____ sushi?", "opts": ["eat", "ate", "eaten"], "ans": "eaten"},
            {"type": "fill", "q": "4. Fill in the blank: We _____ (live) here since 2020.", "ans": "have lived"},
            {"type": "fill", "q": "5. Fill in the blank: Ali _____ (not / see) that movie yet.", "ans": "hasn't seen"},
            {"type": "fill", "q": "6. Fill in the blank: She has _____ (write) three books so far.", "ans": "written"},
            {"type": "order", "q": "7. Make a correct sentence: `just / has / arrived / Mohammad`", "ans": "mohammad has just arrived"},
            {"type": "order", "q": "8. Make a correct sentence: `ever / you / been / to London / have / ?`", "ans": "have you ever been to london"},
            {"type": "tf", "q": "9. True or False: 'She have gone to the market.' is grammatically correct.", "ans": "False"},
            {"type": "tf", "q": "10. True or False: Present Perfect uses 'have/has + Past Participle (V3)'.", "ans": "True"},
        ],
        "B": [
            {"type": "mc", "q": "1. Mohammad _____ just arrived home.", "opts": ["have", "has", "was"], "ans": "has"},
            {"type": "mc", "q": "2. They _____ never seen snow before.", "opts": ["has", "have", "are"], "ans": "have"},
            {"type": "mc", "q": "3. She has worked here _____ five years.", "opts": ["since", "for", "ago"], "ans": "for"},
            {"type": "fill", "q": "4. Fill in the blank: Has Sara _____ (find) her keys yet?", "ans": "found"},
            {"type": "fill", "q": "5. Fill in the blank: I _____ (know) Bahar for ten years.", "ans": "have known"},
            {"type": "fill", "q": "6. Fill in the blank: They _____ (not / finish) the project yet.", "ans": "haven't finished"},
            {"type": "order", "q": "7. Make a correct sentence: `already / eaten / have / lunch / we`", "ans": "we have already eaten lunch"},
            {"type": "order", "q": "8. Make a correct sentence: `has / broken / Reza / his leg`", "ans": "reza has broken his leg"},
            {"type": "tf", "q": "9. True or False: We use 'since' with a period of time like 'since five years'.", "ans": "False"},
            {"type": "tf", "q": "10. True or False: 'Yet' is usually used at the end of negative and question sentences.", "ans": "True"},
        ]
    },
    "Present Perfect Continuous": {
        "A": [
            {"type": "mc", "q": "1. I have _____ studying English for two hours.", "opts": ["be", "been", "being"], "ans": "been"},
            {"type": "mc", "q": "2. It _____ been raining since morning.", "opts": ["have", "has", "is"], "ans": "has"},
            {"type": "mc", "q": "3. How long have you been _____ here?", "opts": ["wait", "waited", "waiting"], "ans": "waiting"},
            {"type": "fill", "q": "4. Fill in the blank: They _____ (play) tennis all afternoon.", "ans": "have been playing"},
            {"type": "fill", "q": "5. Fill in the blank: Darya _____ (work) here since 2022.", "ans": "has been working"},
            {"type": "fill", "q": "6. Fill in the blank: Why are your hands dirty? Have you been _____ (garden)?", "ans": "gardening"},
            {"type": "order", "q": "7. Make a correct sentence: `for / has / sleeping / hours / been / he / three`", "ans": "he has been sleeping for three hours"},
            {"type": "order", "q": "8. Make a correct sentence: `been / what / doing / have / you / ?`", "ans": "what have you been doing"},
            {"type": "tf", "q": "9. True or False: 'She has been work here for a year.' is correct.", "ans": "False"},
            {"type": "tf", "q": "10. True or False: This tense emphasizes the duration of an ongoing action from past to now.", "ans": "True"},
        ],
        "B": [
            {"type": "mc", "q": "1. Sara has been _____ on this project for weeks.", "opts": ["work", "worked", "working"], "ans": "working"},
            {"type": "mc", "q": "2. We _____ been living in this city since 2018.", "opts": ["have", "has", "were"], "ans": "have"},
            {"type": "mc", "q": "3. Reza _____ been feeling well lately.", "opts": ["haven't", "hasn't", "isn't"], "ans": "hasn't"},
            {"type": "fill", "q": "4. Fill in the blank: Setareh _____ (learn) French for six months.", "ans": "has been learning"},
            {"type": "fill", "q": "5. Fill in the blank: I _____ (wait) for the bus since 8 AM.", "ans": "have been waiting"},
            {"type": "fill", "q": "6. Fill in the blank: How long has Jamil been _____ (drive)?", "ans": "driving"},
            {"type": "order", "q": "7. Make a correct sentence: `all / raining / has / been / it / day`", "ans": "it has been raining all day"},
            {"type": "order", "q": "8. Make a correct sentence: `have / studying / how long / been / you / ?`", "ans": "how long have you been studying"},
            {"type": "tf", "q": "9. True or False: 'They have being running for an hour.' is correct.", "ans": "False"},
            {"type": "tf", "q": "10. True or False: The formula is 'have/has + been + verb-ing'.", "ans": "True"},
        ]
    },
    "Simple Past": {
        "A": [
            {"type": "mc", "q": "1. We _____ to the cinema yesterday.", "opts": ["go", "went", "gone"], "ans": "went"},
            {"type": "mc", "q": "2. Did you _____ Sara at school?", "opts": ["see", "saw", "seen"], "ans": "see"},
            {"type": "mc", "q": "3. They _____ very happy at the party.", "opts": ["was", "were", "are"], "ans": "were"},
            {"type": "fill", "q": "4. Fill in the blank: Reza _____ (not / play) football last weekend.", "ans": "didn't play"},
            {"type": "fill", "q": "5. Fill in the blank: She _____ (buy) a new dress two days ago.", "ans": "bought"},
            {"type": "fill", "q": "6. Fill in the blank: I _____ (visit) my grandparents last summer.", "ans": "visited"},
            {"type": "order", "q": "7. Make a correct sentence: `yesterday / finished / homework / his / Ali`", "ans": "ali finished his homework yesterday"},
            {"type": "order", "q": "8. Make a correct sentence: `go / did / where / you / last night / ?`", "ans": "where did you go last night"},
            {"type": "tf", "q": "9. True or False: 'Did she went to the party?' is grammatically correct.", "ans": "False"},
            {"type": "tf", "q": "10. True or False: After 'didn't', we always use the base form of the verb.", "ans": "True"},
        ],
        "B": [
            {"type": "mc", "q": "1. Where _____ Bahar go on vacation?", "opts": ["do", "does", "did"], "ans": "did"},
            {"type": "mc", "q": "2. He _____ born in 2010.", "opts": ["were", "was", "is"], "ans": "was"},
            {"type": "mc", "q": "3. Nafiseh _____ a delicious cake yesterday.", "opts": ["make", "made", "making"], "ans": "made"},
            {"type": "fill", "q": "4. Fill in the blank: They _____ (not / arrive) on time.", "ans": "didn't arrive"},
            {"type": "fill", "q": "5. Fill in the blank: We _____ (see) a great film last night.", "ans": "saw"},
            {"type": "fill", "q": "6. Fill in the blank: Mohammad _____ (study) hard for the test.", "ans": "studied"},
            {"type": "order", "q": "7. Make a correct sentence: `at home / was / yesterday / Darya`", "ans": "darya was at home yesterday"},
            {"type": "order", "q": "8. Make a correct sentence: `call / you / did / why / me / ?`", "ans": "why did you call me"},
            {"type": "tf", "q": "9. True or False: 'We was at the park.' is correct.", "ans": "False"},
            {"type": "tf", "q": "10. True or False: Simple Past is used for completed actions in the past.", "ans": "True"},
        ]
    },
    "Past Continuous": {
        "A": [
            {"type": "mc", "q": "1. I _____ watching TV when you called.", "opts": ["was", "were", "am"], "ans": "was"},
            {"type": "mc", "q": "2. They _____ playing football at 5 PM yesterday.", "opts": ["was", "were", "are"], "ans": "were"},
            {"type": "mc", "q": "3. Setareh _____ sleeping at midnight.", "opts": ["wasn't", "weren't", "didn't"], "ans": "wasn't"},
            {"type": "fill", "q": "4. Fill in the blank: What _____ (you / do) at 8 PM last night?", "ans": "were you doing"},
            {"type": "fill", "q": "5. Fill in the blank: While Sara _____ (cook), the phone rang.", "ans": "was cooking"},
            {"type": "fill", "q": "6. Fill in the blank: It _____ (rain) heavily all evening.", "ans": "was raining"},
            {"type": "order", "q": "7. Make a correct sentence: `reading / was / a book / Jamil / at 9 PM`", "ans": "jamil was reading a book at 9 pm"},
            {"type": "order", "q": "8. Make a correct sentence: `were / laughing / why / they / ?`", "ans": "why were they laughing"},
            {"type": "tf", "q": "9. True or False: 'They was driving too fast.' is correct.", "ans": "False"},
            {"type": "tf", "q": "10. True or False: Past Continuous uses 'was/were + verb-ing'.", "ans": "True"},
        ],
        "B": [
            {"type": "mc", "q": "1. While Ali _____ driving, he saw an accident.", "opts": ["was", "were", "is"], "ans": "was"},
            {"type": "mc", "q": "2. _____ Darya cooking dinner at 7 PM?", "opts": ["Was", "Were", "Did"], "ans": "Was"},
            {"type": "mc", "q": "3. The kids _____ making noise while I was working.", "opts": ["was", "were", "are"], "ans": "were"},
            {"type": "fill", "q": "4. Fill in the blank: We _____ (not / listen) when the teacher spoke.", "ans": "weren't listening"},
            {"type": "fill", "q": "5. Fill in the blank: Reza _____ (study) when I arrived.", "ans": "was studying"},
            {"type": "fill", "q": "6. Fill in the blank: You _____ (sleep) at 10 AM yesterday.", "ans": "were sleeping"},
            {"type": "order", "q": "7. Make a correct sentence: `walking / in the park / were / we`", "ans": "we were walking in the park"},
            {"type": "order", "q": "8. Make a correct sentence: `was / doing / what / Bahar / ?`", "ans": "what was bahar doing"},
            {"type": "tf", "q": "9. True or False: 'I were waiting for you.' is grammatically correct.", "ans": "False"},
            {"type": "tf", "q": "10. True or False: Past Continuous often describes a background action interrupted by Simple Past.", "ans": "True"},
        ]
    },
    "Past Perfect": {
        "A": [
            {"type": "mc", "q": "1. When I arrived, the train had already _____.", "opts": ["leave", "left", "leaving"], "ans": "left"},
            {"type": "mc", "q": "2. She _____ never seen a bear before she went to Canada.", "opts": ["has", "had", "was"], "ans": "had"},
            {"type": "mc", "q": "3. He failed the test because he _____ studied.", "opts": ["hadn't", "hasn't", "didn't"], "ans": "hadn't"},
            {"type": "fill", "q": "4. Fill in the blank: After they had _____ (eat) dinner, they left.", "ans": "eaten"},
            {"type": "fill", "q": "5. Fill in the blank: Nafiseh _____ (finish) her work before 5 PM.", "ans": "had finished"},
            {"type": "fill", "q": "6. Fill in the blank: I realized I had _____ (lose) my wallet.", "ans": "lost"},
            {"type": "order", "q": "7. Make a correct sentence: `had / the movie / started / already`", "ans": "the movie had already started"},
            {"type": "order", "q": "8. Make a correct sentence: `before / had / met / you / him / ?`", "ans": "had you met him before"},
            {"type": "tf", "q": "9. True or False: 'She had went home before I called.' is correct.", "ans": "False"},
            {"type": "tf", "q": "10. True or False: Past Perfect shows an action completed before another past action.", "ans": "True"},
        ],
        "B": [
            {"type": "mc", "q": "1. By the time we got there, the show _____ started.", "opts": ["has", "had", "was"], "ans": "had"},
            {"type": "mc", "q": "2. I realized I had _____ my keys at home.", "opts": ["forget", "forgot", "forgotten"], "ans": "forgotten"},
            {"type": "mc", "q": "3. They were tired because they _____ walked all day.", "opts": ["have", "had", "were"], "ans": "had"},
            {"type": "fill", "q": "4. Fill in the blank: Had Jamil _____ (clean) his room before guests came?", "ans": "cleaned"},
            {"type": "fill", "q": "5. Fill in the blank: Sara _____ (never / fly) in a plane before 2021.", "ans": "had never flown"},
            {"type": "fill", "q": "6. Fill in the blank: When I woke up, my brother had _____ (go) to school.", "ans": "gone"},
            {"type": "order", "q": "7. Make a correct sentence: `had / cooked / dinner / Mohammad / before 8`", "ans": "mohammad had cooked dinner before 8"},
            {"type": "order", "q": "8. Make a correct sentence: `why / left / had / early / they / ?`", "ans": "why had they left early"},
            {"type": "tf", "q": "9. True or False: Past Perfect uses 'had + Past Participle (V3)' for all subjects.", "ans": "True"},
            {"type": "tf", "q": "10. True or False: 'They have arrived before the storm started.' is correct.", "ans": "False"},
        ]
    },
    "Past Perfect Continuous": {
        "A": [
            {"type": "mc", "q": "1. We had been _____ for an hour before the bus came.", "opts": ["wait", "waited", "waiting"], "ans": "waiting"},
            {"type": "mc", "q": "2. She was tired because she _____ been running.", "opts": ["has", "had", "was"], "ans": "had"},
            {"type": "mc", "q": "3. How long had you _____ studying before the test?", "opts": ["be", "been", "being"], "ans": "been"},
            {"type": "fill", "q": "4. Fill in the blank: They _____ (live) in London for 10 years before moving.", "ans": "had been living"},
            {"type": "fill", "q": "5. Fill in the blank: Ali _____ (work) all day, so he was exhausted.", "ans": "had been working"},
            {"type": "fill", "q": "6. Fill in the blank: It had been _____ (snow) all night.", "ans": "snowing"},
            {"type": "order", "q": "7. Make a correct sentence: `had / crying / been / she / for hours`", "ans": "she had been crying for hours"},
            {"type": "order", "q": "8. Make a correct sentence: `been / waiting / how long / had / you / ?`", "ans": "how long had you been waiting"},
            {"type": "tf", "q": "9. True or False: 'He had been sleep for ten hours.' is correct.", "ans": "False"},
            {"type": "tf", "q": "10. True or False: The formula is 'had + been + verb-ing'.", "ans": "True"},
        ],
        "B": [
            {"type": "mc", "q": "1. The ground was wet because it had been _____.", "opts": ["rain", "rained", "raining"], "ans": "raining"},
            {"type": "mc", "q": "2. Ali _____ been working there for five years before he quit.", "opts": ["has", "had", "was"], "ans": "had"},
            {"type": "mc", "q": "3. He hadn't been _____ well for weeks.", "opts": ["feel", "felt", "feeling"], "ans": "feeling"},
            {"type": "fill", "q": "4. Fill in the blank: I _____ (try) to call you all morning.", "ans": "had been trying"},
            {"type": "fill", "q": "5. Fill in the blank: Darya _____ (practice) piano for two hours before dinner.", "ans": "had been practicing"},
            {"type": "fill", "q": "6. Fill in the blank: Had they been _____ (argue) before you arrived?", "ans": "arguing"},
            {"type": "order", "q": "7. Make a correct sentence: `driving / had / been / Reza / since morning`", "ans": "reza had been driving since morning"},
            {"type": "order", "q": "8. Make a correct sentence: `had / studying / Setareh / been / English`", "ans": "setareh had been studying english"},
            {"type": "tf", "q": "9. True or False: 'We has been waiting for an hour.' is correct.", "ans": "False"},
            {"type": "tf", "q": "10. True or False: Past Perfect Continuous shows duration before a past event.", "ans": "True"},
        ]
    },
    "Simple Future (will)": {
        "A": [
            {"type": "mc", "q": "1. Tomorrow, they _____ visit their grandparents.", "opts": ["will", "did", "are"], "ans": "will"},
            {"type": "mc", "q": "2. I promise I _____ help you with your project.", "opts": ["will", "am", "was"], "ans": "will"},
            {"type": "mc", "q": "3. She _____ be late for the meeting.", "opts": ["won't", "didn't", "isn't"], "ans": "won't"},
            {"type": "fill", "q": "4. Fill in the blank: I think it _____ (rain) tomorrow.", "ans": "will rain"},
            {"type": "fill", "q": "5. Fill in the blank: Don't worry, Jamil _____ (not / forget) your birthday.", "ans": "won't forget"},
            {"type": "fill", "q": "6. Fill in the blank: _____ (you / open) the window, please?", "ans": "Will you open"},
            {"type": "order", "q": "7. Make a correct sentence: `call / will / tonight / I / you`", "ans": "i will call you tonight"},
            {"type": "order", "q": "8. Make a correct sentence: `will / when / arrive / Sara / ?`", "ans": "when will sara arrive"},
            {"type": "tf", "q": "9. True or False: 'She will goes to Tehran tomorrow.' is correct.", "ans": "False"},
            {"type": "tf", "q": "10. True or False: After 'will', we always use the base form of the verb.", "ans": "True"},
        ],
        "B": [
            {"type": "mc", "q": "1. I think Jamil _____ pass the exam easily.", "opts": ["will", "is", "was"], "ans": "will"},
            {"type": "mc", "q": "2. _____ you help me carry these bags?", "opts": ["Will", "Do", "Are"], "ans": "Will"},
            {"type": "mc", "q": "3. Don't worry, I _____ tell anyone your secret.", "opts": ["won't", "don't", "didn't"], "ans": "won't"},
            {"type": "fill", "q": "4. Fill in the blank: We _____ (travel) to Shiraz next month.", "ans": "will travel"},
            {"type": "fill", "q": "5. Fill in the blank: Bahar _____ (be) 20 years old next year.", "ans": "will be"},
            {"type": "fill", "q": "6. Fill in the blank: They _____ (not / come) to the party tonight.", "ans": "won't come"},
            {"type": "order", "q": "7. Make a correct sentence: `will / win / our team / the match`", "ans": "our team will win the match"},
            {"type": "order", "q": "8. Make a correct sentence: `you / will / marry / me / ?`", "ans": "will you marry me"},
            {"type": "tf", "q": "9. True or False: 'Won't' is the short form of 'will not'.", "ans": "True"},
            {"type": "tf", "q": "10. True or False: 'He wills help us.' is grammatically correct.", "ans": "False"},
        ]
    },
    "Future with 'be going to'": {
        "A": [
            {"type": "mc", "q": "1. Look at those dark clouds! It is _____ to rain.", "opts": ["go", "going", "will"], "ans": "going"},
            {"type": "mc", "q": "2. I _____ going to buy a new laptop next week.", "opts": ["am", "is", "are"], "ans": "am"},
            {"type": "mc", "q": "3. What _____ Nafiseh going to do after graduation?", "opts": ["am", "is", "are"], "ans": "is"},
            {"type": "fill", "q": "4. Fill in the blank: We _____ (have) a party on Friday.", "ans": "are going to have"},
            {"type": "fill", "q": "5. Fill in the blank: Ali _____ (not / buy) that expensive car.", "ans": "isn't going to buy"},
            {"type": "fill", "q": "6. Fill in the blank: Are you going to _____ (visit) your aunt?", "ans": "visit"},
            {"type": "order", "q": "7. Make a correct sentence: `going to / am / study / tonight / I`", "ans": "i am going to study tonight"},
            {"type": "order", "q": "8. Make a correct sentence: `is / going to / what / Reza / cook / ?`", "ans": "what is reza going to cook"},
            {"type": "tf", "q": "9. True or False: 'They is going to travel soon.' is correct.", "ans": "False"},
            {"type": "tf", "q": "10. True or False: We use 'be going to' for planned future actions and evidence-based predictions.", "ans": "True"},
        ],
        "B": [
            {"type": "mc", "q": "1. They _____ going to travel to Spain this summer.", "opts": ["am", "is", "are"], "ans": "are"},
            {"type": "mc", "q": "2. Sara is going to _____ medicine at university.", "opts": ["study", "studies", "studying"], "ans": "study"},
            {"type": "mc", "q": "3. He _____ going to watch TV tonight.", "opts": ["isn't", "aren't", "doesn't"], "ans": "isn't"},
            {"type": "fill", "q": "4. Fill in the blank: Be careful! You _____ (drop) that glass!", "ans": "are going to drop"},
            {"type": "fill", "q": "5. Fill in the blank: Darya _____ (learn) Spanish next year.", "ans": "is going to learn"},
            {"type": "fill", "q": "6. Fill in the blank: We _____ (not / stay) at a hotel.", "ans": "aren't going to stay"},
            {"type": "order", "q": "7. Make a correct sentence: `going to / is / rain / it`", "ans": "it is going to rain"},
            {"type": "order", "q": "8. Make a correct sentence: `are / going to / when / leave / you / ?`", "ans": "when are you going to leave"},
            {"type": "tf", "q": "9. True or False: 'She going to call me.' is missing the verb 'is'.", "ans": "True"},
            {"type": "tf", "q": "10. True or False: 'I am going to bought a phone.' is correct.", "ans": "False"},
        ]
    },
    "Future Continuous": {
        "A": [
            {"type": "mc", "q": "1. This time tomorrow, I will be _____ on the beach.", "opts": ["relax", "relaxed", "relaxing"], "ans": "relaxing"},
            {"type": "mc", "q": "2. At 8 PM tonight, we _____ be watching the match.", "opts": ["will", "are", "have"], "ans": "will"},
            {"type": "mc", "q": "3. Don't call her at 9; she will _____ sleeping.", "opts": ["be", "been", "being"], "ans": "be"},
            {"type": "fill", "q": "4. Fill in the blank: Will you be _____ (use) the car tomorrow morning?", "ans": "using"},
            {"type": "fill", "q": "5. Fill in the blank: Mohammad _____ (fly) to Istanbul at this time tomorrow.", "ans": "will be flying"},
            {"type": "fill", "q": "6. Fill in the blank: They _____ (not / work) on Sunday afternoon.", "ans": "won't be working"},
            {"type": "order", "q": "7. Make a correct sentence: `will / studying / be / at 10 PM / Setareh`", "ans": "setareh will be studying at 10 pm"},
            {"type": "order", "q": "8. Make a correct sentence: `be / doing / what / will / tomorrow / you / ?`", "ans": "what will you be doing tomorrow"},
            {"type": "tf", "q": "9. True or False: 'I will being working tomorrow.' is correct.", "ans": "False"},
            {"type": "tf", "q": "10. True or False: Future Continuous uses 'will + be + verb-ing'.", "ans": "True"},
        ],
        "B": [
            {"type": "mc", "q": "1. Next week, Darya will be _____ in New York.", "opts": ["work", "worked", "working"], "ans": "working"},
            {"type": "mc", "q": "2. They _____ be studying for finals all weekend.", "opts": ["will", "are", "did"], "ans": "will"},
            {"type": "mc", "q": "3. What will you _____ doing at this time next year?", "opts": ["be", "been", "is"], "ans": "be"},
            {"type": "fill", "q": "4. Fill in the blank: I _____ (not / stay) at the office tomorrow.", "ans": "won't be staying"},
            {"type": "fill", "q": "5. Fill in the blank: At noon, Bahar _____ (have) lunch with her boss.", "ans": "will be having"},
            {"type": "fill", "q": "6. Fill in the blank: We will be _____ (wait) for you at the airport.", "ans": "waiting"},
            {"type": "order", "q": "7. Make a correct sentence: `sleeping / will / be / the baby / at midnight`", "ans": "the baby will be sleeping at midnight"},
            {"type": "order", "q": "8. Make a correct sentence: `will / attending / Jamil / be / the conference / ?`", "ans": "will jamil be attending the conference"},
            {"type": "tf", "q": "9. True or False: 'She will be cook dinner at 7.' is correct.", "ans": "False"},
            {"type": "tf", "q": "10. True or False: Future Continuous describes an action in progress at a specific future time.", "ans": "True"},
        ]
    },
    "Future Perfect": {
        "A": [
            {"type": "mc", "q": "1. By next year, I will have _____ from university.", "opts": ["graduate", "graduated", "graduating"], "ans": "graduated"},
            {"type": "mc", "q": "2. She _____ have finished the report by 5 PM.", "opts": ["will", "is", "has"], "ans": "will"},
            {"type": "mc", "q": "3. By the time you arrive, we will _____ eaten dinner.", "opts": ["has", "have", "had"], "ans": "have"},
            {"type": "fill", "q": "4. Fill in the blank: Will they have _____ (build) the house before winter?", "ans": "built"},
            {"type": "fill", "q": "5. Fill in the blank: Ali _____ (complete) the course by June.", "ans": "will have completed"},
            {"type": "fill", "q": "6. Fill in the blank: I _____ (not / finish) reading this book by tonight.", "ans": "won't have finished"},
            {"type": "order", "q": "7. Make a correct sentence: `will / left / have / the train / by 6 PM`", "ans": "the train will have left by 6 pm"},
            {"type": "order", "q": "8. Make a correct sentence: `have / saved / how much / will / you / ?`", "ans": "how much will you have saved"},
            {"type": "tf", "q": "9. True or False: 'She will has arrived by noon.' is correct.", "ans": "False"},
            {"type": "tf", "q": "10. True or False: Future Perfect uses 'will + have + Past Participle (V3)'.", "ans": "True"},
        ],
        "B": [
            {"type": "mc", "q": "1. By 2030, scientists will have _____ a cure.", "opts": ["find", "found", "finding"], "ans": "found"},
            {"type": "mc", "q": "2. Mohammad _____ have saved enough money by June.", "opts": ["will", "does", "is"], "ans": "will"},
            {"type": "mc", "q": "3. The train _____ have left by the time we get there.", "opts": ["will", "is", "was"], "ans": "will"},
            {"type": "fill", "q": "4. Fill in the blank: I will have _____ (read) three books by the end of the month.", "ans": "read"},
            {"type": "fill", "q": "5. Fill in the blank: Nafiseh _____ (write) ten articles by Friday.", "ans": "will have written"},
            {"type": "fill", "q": "6. Fill in the blank: By 10 PM, the kids will have _____ (fall) asleep.", "ans": "fallen"},
            {"type": "order", "q": "7. Make a correct sentence: `by tomorrow / repaired / will / have / Reza / the car`", "ans": "reza will have repaired the car by tomorrow"},
            {"type": "order", "q": "8. Make a correct sentence: `finished / will / you / have / by 8 / ?`", "ans": "will you have finished by 8"},
            {"type": "tf", "q": "9. True or False: 'By' is a very common preposition used with Future Perfect.", "ans": "True"},
            {"type": "tf", "q": "10. True or False: 'We will have went home by then.' is correct.", "ans": "False"},
        ]
    },
    "Future Perfect Continuous": {
        "A": [
            {"type": "mc", "q": "1. By next month, I will have been _____ here for 5 years.", "opts": ["work", "worked", "working"], "ans": "working"},
            {"type": "mc", "q": "2. At 6 PM, she will have _____ driving for four hours.", "opts": ["be", "been", "being"], "ans": "been"},
            {"type": "mc", "q": "3. How long will you _____ been studying English by June?", "opts": ["has", "have", "had"], "ans": "have"},
            {"type": "fill", "q": "4. Fill in the blank: They _____ (live) together for a decade next year.", "ans": "will have been living"},
            {"type": "fill", "q": "5. Fill in the blank: By noon, Darya _____ (study) for five hours.", "ans": "will have been studying"},
            {"type": "fill", "q": "6. Fill in the blank: In July, we will have been _____ (travel) for six months.", "ans": "traveling"},
            {"type": "order", "q": "7. Make a correct sentence: `will / waiting / have / been / I / for two hours`", "ans": "i will have been waiting for two hours"},
            {"type": "order", "q": "8. Make a correct sentence: `been / working / how long / will / Sara / have / ?`", "ans": "how long will sara have been working"},
            {"type": "tf", "q": "9. True or False: 'He will has been sleeping for 8 hours.' is correct.", "ans": "False"},
            {"type": "tf", "q": "10. True or False: The formula is 'will + have + been + verb-ing'.", "ans": "True"},
        ],
        "B": [
            {"type": "mc", "q": "1. By midnight, we will have been _____ for 12 hours.", "opts": ["travel", "traveled", "traveling"], "ans": "traveling"},
            {"type": "mc", "q": "2. Next week, Bahar will have _____ teaching for 10 years.", "opts": ["be", "been", "being"], "ans": "been"},
            {"type": "mc", "q": "3. By 2028, I _____ have been playing the piano for 15 years.", "opts": ["will", "am", "was"], "ans": "will"},
            {"type": "fill", "q": "4. Fill in the blank: He will _____ (wait) for two hours by the time she arrives.", "ans": "have been waiting"},
            {"type": "fill", "q": "5. Fill in the blank: By 5 PM, Jamil _____ (run) for three hours.", "ans": "will have been running"},
            {"type": "fill", "q": "6. Fill in the blank: Next year, they will have been _____ (build) this bridge for 4 years.", "ans": "building"},
            {"type": "order", "q": "7. Make a correct sentence: `for / will / teaching / have / been / Setareh / ten years`", "ans": "setareh will have been teaching for ten years"},
            {"type": "order", "q": "8. Make a correct sentence: `will / been / living / where / you / have / ?`", "ans": "where will you have been living"},
            {"type": "tf", "q": "9. True or False: 'They will have be working all day.' is correct.", "ans": "False"},
            {"type": "tf", "q": "10. True or False: Future Perfect Continuous emphasizes the duration of an action up to a future point.", "ans": "True"},
        ]
    }
}

# --- مدیریت وضعیت و پیشرفت دانش‌آموز (Session State) ---
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
            
            # بارگذاری پیشرفت ذخیره‌شده این دانش‌آموز از فایل
            all_data = load_all_progress()
            student_data = all_data.get(clean_name, {})
            st.session_state.unlocked_index = student_data.get("unlocked_index", 0)
            st.session_state.scores = student_data.get("scores", {})
            st.session_state.quiz_variant = student_data.get("quiz_variant", {t: "A" for t in TENSE_LEVELS})
            
            # اطمینان از اینکه همه زمان‌ها کلید A/B دارند
            for t in TENSE_LEVELS:
                if t not in st.session_state.quiz_variant:
                    st.session_state.quiz_variant[t] = "A"
                    
            st.rerun()
        else:
            st.error("Access denied! Your name is not in the authorized list.")
            
else:
    # همگام‌سازی مداوم با فایل ذخیره تا با رفرش یا تغییر تب داده‌ها از بین نروند
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
        
        # پیش‌فرض روی آخرین سطح بازشده دانش‌آموز قرار می‌گیرد
        selected_tense = st.selectbox(
            "Choose a Structure to Review:",
            TENSE_LEVELS,
            index=st.session_state.unlocked_index
        )
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
        st.title("🎮 Mastery Quests & Comprehensive Quizzes")
        st.info("📌 **Rule:** Each quiz has **10 mixed questions** (Multiple Choice, Fill-in-the-blank, Sentence Building, and True/False). Score **75% or higher** to unlock the next level! Your progress is automatically saved.")
        
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
        
        # به طور پیش‌فرض روی جدیدترین مرحله‌ای که باز شده قرار می‌گیرد تا به عقب برنگردد
        available_tenses = TENSE_LEVELS[:st.session_state.unlocked_index + 1]
        chosen_quiz_tense = st.selectbox(
            "Select an unlocked level (defaults to your current active level):",
            available_tenses,
            index=len(available_tenses) - 1
        )
        
        current_variant = st.session_state.quiz_variant.get(chosen_quiz_tense, "A")
        questions = RAW_QUESTIONS[chosen_quiz_tense][current_variant]
        
        st.markdown(f"### 📝 {chosen_quiz_tense} Comprehensive Test — **Set {current_variant}** (10 Questions)")
        
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
            for i, item in enumerate(questions):
                u_ans = str(user_answers[i]).strip().lower().rstrip(".?!")
                c_ans = str(item["ans"]).strip().lower().rstrip(".?!")
                if u_ans == c_ans:
                    correct_count += 1
                    
            percentage = int((correct_count / len(questions)) * 100)
            st.session_state.scores[chosen_quiz_tense] = percentage
            
            current_idx = TENSE_LEVELS.index(chosen_quiz_tense)
            if percentage >= 75:
                if current_idx == st.session_state.unlocked_index and current_idx + 1 < len(TENSE_LEVELS):
                    st.session_state.unlocked_index += 1
                
                # ذخیره دائمی پیشرفت در فایل
                save_student_progress(
                    st.session_state.student_name,
                    st.session_state.unlocked_index,
                    st.session_state.scores,
                    st.session_state.quiz_variant
                )
                
                st.balloons()
                st.success(f"🎉 Congratulations {st.session_state.student_name}! You scored **{percentage}%** ({correct_count}/10)!")
                
                if st.session_state.unlocked_index > current_idx:
                    next_tense = TENSE_LEVELS[st.session_state.unlocked_index]
                    st.info(f"🔓 **NEXT LEVEL UNLOCKED:** **{next_tense}** is now open and saved to your profile!")
                    if st.button(f"Proceed to {next_tense} 🚀"):
                        st.rerun()
                elif current_idx + 1 == len(TENSE_LEVELS):
                    st.success("🏆 **GRAND MASTER!** You have completed and passed ALL 13 English grammar structures!")
            else:
                # ذخیره نمره پایین‌تر برای ثبت سابقه
                save_student_progress(
                    st.session_state.student_name,
                    st.session_state.unlocked_index,
                    st.session_state.scores,
                    st.session_state.quiz_variant
                )
                st.error(f"📉 You scored **{percentage}%** ({correct_count}/10). You need at least **75%** to unlock the next level.")
                st.warning("💡 Review the rules in the **Review** tab, then click the button below to take a **completely different set of 10 questions**!")
                
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
        passed_count = sum(1 for sc in st.session_state.scores.values() if sc >= 75)
        progress_percent = int((passed_count / len(TENSE_LEVELS)) * 100)
        st.write("Your overall course completion:")
        st.progress(progress_percent)
        st.write(f"You have mastered **{passed_count} out of {len(TENSE_LEVELS)}** grammar structures ({progress_percent}%).")

    elif menu_selection == "Total Activities":
        st.title("🏆 Total Activities")
        st.write("Summary of your saved achievements:")
        passed_count = sum(1 for sc in st.session_state.scores.values() if sc >= 75)
        col1, col2 = st.columns(2)
        col1.metric(label="Structures Mastered (75%+)", value=f"{passed_count} / {len(TENSE_LEVELS)}")
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
