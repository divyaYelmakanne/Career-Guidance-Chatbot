import tkinter as tk
from tkinter import scrolledtext
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# -------------------------
# Load Dataset
# -------------------------
df = pd.read_csv("CareerMap- Mapping Tech Roles With Personality & Skills.csv")

# Encode target (career roles)
le = LabelEncoder()
df["Role"] = le.fit_transform(df["Role"])  # Assuming target column is "Role"

# Encode non-numeric features (if any)
for col in df.columns:
    if df[col].dtype == "object" and col != "Role":
        df[col] = LabelEncoder().fit_transform(df[col])

# Features (drop role column)
X = df.drop("Role", axis=1)
y = df["Role"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# -------------------------
# Chatbot logic
# -------------------------
questions = list(X.columns)   # Each skill/personality trait will be a question
answers = []
current_q = 0

def chatbot_response(user_input=""):
    global current_q, answers
    
    # Save previous answer if available
    if user_input != "":
        try:
            answers.append(int(user_input))
        except:
            answers.append(0)  # Default if not valid number

    # Ask next question
    if current_q < len(questions):
        bot_msg = f"Rate your skill level in {questions[current_q]} (1-7):"
        current_q += 1
        return bot_msg
    else:
        # All answers collected → Predict career
        if len(answers) == len(questions):
            user_features = pd.DataFrame([answers], columns=questions)
            prediction = model.predict(user_features)[0]
            career = le.inverse_transform([prediction])[0]
            return f"✅ Based on your skills, I suggest you explore a career as: **{career}**"
        else:
            return "⚠️ Not enough data collected!"

# -------------------------
# Tkinter GUI
# -------------------------
def send():
    user_input = entry.get()
    chat_window.insert(tk.END, "You: " + user_input + "\n")
    
    bot_reply = chatbot_response(user_input)
    chat_window.insert(tk.END, "Bot: " + bot_reply + "\n")
    
    entry.delete(0, tk.END)

# GUI Setup
root = tk.Tk()
root.title("Career Guidance Chatbot")

chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20)
chat_window.pack(padx=10, pady=10)

entry = tk.Entry(root, width=40)
entry.pack(padx=10, pady=5, side=tk.LEFT)

send_button = tk.Button(root, text="Send", command=send)
send_button.pack(padx=5, pady=5, side=tk.LEFT)

# Start conversation
chat_window.insert(tk.END, "Bot: Hi! I’ll ask you about your skills.\n")
chat_window.insert(tk.END, chatbot_response() + "\n")

root.mainloop()
