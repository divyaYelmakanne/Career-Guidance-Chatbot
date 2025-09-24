# chatbot.py (Streamlit Version)
import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# -------------------------
# Load & Preprocess Dataset
# -------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("CareerMap- Mapping Tech Roles With Personality & Skills.csv")

    # Encode target (career roles)
    le = LabelEncoder()
    df["Role"] = le.fit_transform(df["Role"])  # Assuming target column is "Role"

    # Encode non-numeric features (if any)
    for col in df.columns:
        if df[col].dtype == "object" and col != "Role":
            df[col] = LabelEncoder().fit_transform(df[col])

    return df, le

@st.cache_resource
def train_model(df):
    X = df.drop("Role", axis=1)
    y = df["Role"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    return model, list(X.columns)

# Load
df, le = load_data()
model, questions = train_model(df)

# -------------------------
# Streamlit UI Setup
# -------------------------
st.set_page_config(page_title="Career Guidance Chatbot", layout="centered")
st.title("💼 Career Guidance Chatbot")

# Session state
if "answers" not in st.session_state:
    st.session_state.answers = []
if "current_q" not in st.session_state:
    st.session_state.current_q = 0
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# -------------------------
# Chatbot Logic
# -------------------------
def chatbot_response(user_input=""):
    if user_input != "":
        try:
            st.session_state.answers.append(int(user_input))
        except:
            st.session_state.answers.append(0)  # Default if invalid

    # Ask next question
    if st.session_state.current_q < len(questions):
        bot_msg = f"Rate your skill level in **{questions[st.session_state.current_q]}** (1-7):"
        st.session_state.current_q += 1
        return bot_msg
    else:
        # All answers collected → Predict career
        if len(st.session_state.answers) == len(questions):
            user_features = pd.DataFrame([st.session_state.answers], columns=questions)
            prediction = model.predict(user_features)[0]
            career = le.inverse_transform([prediction])[0]
            return f"✅ Based on your skills, I suggest you explore a career as: **{career}**"
        else:
            return "⚠️ Not enough data collected!"

# -------------------------
# Display Chat History
# -------------------------
for chat in st.session_state.chat_history:
    st.markdown(chat)

# Input box
user_input = st.text_input("Your answer (1-7):", key="input")

if st.button("Send") and user_input:
    chat_output = f"**You:** {user_input}\n\n"
    bot_reply = chatbot_response(user_input)
    chat_output += f"**Bot:** {bot_reply}\n\n"

    st.session_state.chat_history.append(chat_output)
    st.session_state.input = ""  # clear input
    st.rerun()

# Start conversation if first run
if st.session_state.current_q == 0 and not st.session_state.chat_history:
    welcome_msg = "Bot: Hi! I’ll ask you about your skills.\n"
    first_q = chatbot_response()
    st.session_state.chat_history.append(f"**Bot:** {first_q}\n\n")
    st.rerun()
