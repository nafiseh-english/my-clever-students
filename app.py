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
# لیست اسامی مجاز به انگلیسی (می‌توانید اسامی دلخواه خود را اینجا اضافه کنید)
ALLOWED_STUDENTS = ["Jamil","Nafiseh"]

# بررسی اینکه آیا کاربر قبلاً وارد شده است یا خیر
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.title("🔒 Student Login Portal")
    st.markdown("Please enter your name in English to access the portal:")
    
    # کادر ورود نام (بدون نمایش متن بالای کادر)
    entered_name = st.text_input("Your Name", label_visibility="collapsed")
    
    if st.button("Login"):
        # بررسی اینکه آیا نام وارد شده در لیست مجاز هست یا خیر
        if entered_name.strip().title() in ALLOWED_STUDENTS:
            st.session_state.logged_in = True
            st.session_state.student_name = entered_name.strip().title()
            st.rerun()
        else:
            st.error("Access denied! Your name is not in the authorized list.")
            
else:
    # --- محتوای اصلی سایت (فقط بعد از ورود موفق نمایش داده می‌شود) ---
    st.title(f"🌟 Welcome, {st.session_state.student_name}! - Educational Portal")
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
        st.info(f"Submitting as: **{st.session_state.student_name}**")
        student_answer = st.text_area("Write your answer here...")

        if st.button("Submit Answer"):
            if student_answer:
                st.success(
                    f"Thank you, {st.session_state.student_name}! Your answer has been successfully submitted. 🎉"
                )
            else:
                st.warning("Please write your answer first.")
                
    # دکمه خروج (برای تست یا تغییر کاربر)
    st.write("---")
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()
