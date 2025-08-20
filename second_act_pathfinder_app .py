
import streamlit as st
import json
from collections import Counter

# Load questions
with open("archetype_quiz_questions.json", "r") as f:
    questions = json.load(f)

st.set_page_config(page_title="Second Act Pathfinder", layout="centered")
st.title("🧭 Second Act Pathfinder")
st.subheader("Discover your Life Minus Work Archetype")

st.markdown("Answer the questions below to reveal your second act identity — and get your personalised lifestyle plan.")

# Store responses
if "responses" not in st.session_state:
    st.session_state.responses = []

def reset_quiz():
    st.session_state.responses = []
    st.session_state.page = 0

# Progress tracker
if "page" not in st.session_state:
    st.session_state.page = 0

# Display questions one at a time
if st.session_state.page < len(questions):
    q = questions[st.session_state.page]
    st.markdown(f"**Q{st.session_state.page + 1}: {q['question']}**")
    for archetype, option in q["options"].items():
        if st.button(option, key=f"{st.session_state.page}-{archetype}"):
            st.session_state.responses.append(archetype)
            st.session_state.page += 1
            st.experimental_rerun()
else:
    result = Counter(st.session_state.responses).most_common(1)[0][0]

    st.success(f"🎉 You're a **{result}**!")
    archetype_links = {
        "Explorer": "Explorer_Lifestyle_Plan.docx",
        "Nurturer": "Nurturer_Lifestyle_Plan.docx",
        "Creator": "Creator_Lifestyle_Plan.docx",
        "Seeker": "Seeker_Lifestyle_Plan.docx",
        "Builder": "Builder_Lifestyle_Plan.docx",
        "Connector": "Connector_Lifestyle_Plan.docx"
    }

    plan_link = archetype_links.get(result, "#")
    st.markdown(f"👇 Download your personalised lifestyle plan:

[📥 Download {result} Plan]({plan_link})")

    st.markdown("---")
    st.button("🔄 Restart", on_click=reset_quiz)
