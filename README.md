# Career Guidance Chatbot

A Python-based chatbot that recommends tech careers based on your skills and personality traits.
It uses a **Random Forest Classifier** trained the dataset: [CareerMap – Mapping Tech Roles With Personality & Skills]

Take a look at live Website : https://career-guidance-chatbot-25.streamlit.app/

---

## 📝 Project Structure

```
career/
│
├── CareerMap- Mapping Tech Roles With Personality & Skills.csv # Dataset
├── chatbot.py # Main chatbot script
└── README.md # This file
```

---

## ⚡ Features

- Asks user skill levels (1–7) for technical skills and personality traits.
- Uses a trained Random Forest model to predict the most suitable tech career.
- GUI implemented using **Tkinter** for interactive conversation.
- Handles both numeric and non-numeric dataset columns automatically.

---

## 📦 Requirements

- Python 3.11+
- Libraries: `pandas`, `scikit-learn`, `tkinter`

Install required packages:

```bash
pip install pandas scikit-learn tk
```

Note: Tkinter is usually included with Python.

---

## 🚀 How to Run

Open a terminal or PowerShell in the project folder:

```bash
cd "C:\path\to\career"
```

Run the chatbot:

```bash
python chatbot.py
```

A Tkinter window will appear. The chatbot will ask you to rate your skills (1–7).

Answer all questions. At the end, the chatbot will suggest a suitable career based on your inputs.

---

## 🖥️ Example Interaction

```
Bot: Hi! I'll ask you about your skills.
Bot: Rate your skill level in Database Fundamentals (1-7):
You: 4
Bot: Rate your skill level in Computer Architecture (1-7):
You: 4
Bot: Rate your skill level in Cyber Security (1-7):
You: 5
...
...
...
Bot: ✅ Based on your skills, I suggest you explore a career as: Data Scientist
```

---

## 🔧 Notes

- Ensure that `CareerMap- Mapping Tech Roles With Personality & Skills.csv` is in the same folder as `chatbot.py`.
- Skill ratings must be integers between 1–7. Invalid inputs default to 0.
- You can retrain the model on updated datasets by replacing the CSV file.

---

## 👤 Author

Divya Yelmakanne                                                                                                                                                             
Email: divyayelmakanne@gmail.com                                                                                                                                             
GitHub: https://github.com/divyaYelmakanne                                                                                                                                   

---

## 📄 License

This project is licensed under the MIT License.


