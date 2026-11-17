import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Student Study Assistant", page_icon="🎓", layout="centered")

st.title("🎓 Student Study Assistant")
st.caption("A simple virtual assistant to help students stay organized and study smarter.")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I'm your Student Study Assistant. Ask me about study tips, time management, exams, or motivation."}
    ]

def get_reply(message: str) -> str:
    text = message.lower().strip()

    if any(word in text for word in ["hello", "hi", "hey"]):
        return "Hello! 😊 How can I help with your studies today?"
    if any(word in text for word in ["time", "date", "today"]):
        now = datetime.now()
        return f"Your device's current date and time is {now.strftime('%A, %d %B %Y, %I:%M %p')}."
    if any(word in text for word in ["study tip", "study tips", "how to study", "focus"]):
        return ("Try the Pomodoro method: study for 25 minutes, then take a 5-minute break. "
                "Keep your phone away, set one clear goal, and revise your notes at the end.")
    if any(word in text for word in ["time management", "schedule", "timetable", "manage time"]):
        return ("Make a short daily timetable. Start with the most important task, divide large topics "
                "into smaller tasks, and add short breaks. Leave some buffer time for revision.")
    if any(word in text for word in ["exam", "test", "prepare", "revision"]):
        return ("For exam preparation, list all topics, study the difficult ones first, practise questions, "
                "and revise using short notes. Get enough sleep the night before the exam.")
    if any(word in text for word in ["motivate", "motivation", "tired", "lazy"]):
        return ("You don't need to finish everything at once. Start with just 10 minutes of focused work. "
                "Small, consistent progress adds up. You can do it! 💪")
    if any(word in text for word in ["python", "programming", "coding"]):
        return ("A good way to learn programming is to practise a little every day. Read a concept, write "
                "a small example, run it, and then change the code to see what happens.")
    if any(word in text for word in ["thank", "thanks"]):
        return "You're welcome! Keep learning and have a productive day. 😊"
    if any(word in text for word in ["bye", "goodbye"]):
        return "Goodbye! Best of luck with your studies. 👋"

    return ("I'm still learning. I can help with study tips, time management, exam preparation, "
            "motivation, programming basics, and the current date/time. Try asking about one of these.")

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Type your question here..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    reply = get_reply(prompt)
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.markdown(reply)

with st.sidebar:
    st.header("About this project")
    st.write("A beginner-friendly, rule-based virtual assistant built with Python and Streamlit.")
    st.subheader("Try asking")
    st.markdown("- Give me study tips\n- How do I manage my time?\n- How should I prepare for exams?\n- Motivate me\n- Help me with Python")
    if st.button("Clear chat"):
        st.session_state.messages = []
        st.rerun()
