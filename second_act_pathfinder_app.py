
import streamlit as st

st.set_page_config(page_title="Second Act Pathfinder", page_icon="🌟")

st.title("🌟 What’s Your Ideal Life After Work?")
st.subheader("Take this 2-minute quiz to discover your Second Act Path.")

st.markdown("---")

# Define quiz questions and options
questions = [
    {
        "question": "What sounds like the perfect morning?",
        "options": {
            "Grabbing my backpack and hitting a trail ☀️": "Explorer",
            "Volunteering at a community garden 🌱": "Nurturer",
            "Journaling with a cup of tea and music 🎨": "Creator",
            "Meeting a friend for coffee and conversation ☕": "Connector",
        }
    },
    {
        "question": "What excites you most right now?",
        "options": {
            "Planning a trip to somewhere I’ve never been 🌍": "Explorer",
            "Helping others feel seen, heard, and supported 👐": "Nurturer",
            "Learning a new skill or picking up an old hobby ✏️": "Creator",
            "Joining a group or starting a club 🤝": "Connector",
        }
    },
    {
        "question": "Which quote speaks to you most?",
        "options": {
            "“Life begins at the end of your comfort zone.”": "Explorer",
            "“The meaning of life is to give life meaning.”": "Nurturer",
            "“Creativity is intelligence having fun.”": "Creator",
            "“Connection is why we’re here.”": "Connector",
        }
    },
    {
        "question": "What do you miss (or want more of) post-career?",
        "options": {
            "Spontaneity and new experiences": "Explorer",
            "Purpose and making a difference": "Nurturer",
            "Time for reflection and creating": "Creator",
            "Laughter and social connection": "Connector",
        }
    },
    {
        "question": "Pick a dream day headline:",
        "options": {
            "“Traveled somewhere new and got lost in the best way”": "Explorer",
            "“Made someone else’s day brighter”": "Nurturer",
            "“Created something I’m proud of”": "Creator",
            "“Was surrounded by my people”": "Connector",
        }
    },
]

# Create dictionary to store results
scores = {"Explorer": 0, "Nurturer": 0, "Creator": 0, "Connector": 0}

# Collect user input
for idx, q in enumerate(questions):
    st.write(f"**Q{idx+1}: {q['question']}**")
    choice = st.radio("", list(q["options"].keys()), key=idx)
    scores[q["options"][choice]] += 1
    st.markdown("---")

# Show results
if st.button("Show My Path"):
    result = max(scores, key=scores.get)
    st.success(f"🌟 Your Second Act Archetype is: **{result}**")

    descriptions = {
        "Explorer": "You crave movement, adventure, and novelty. Whether it’s travel, exploration, or bold new experiences, your second act is about freedom with purpose.",
        "Nurturer": "You find joy in giving, supporting, and making an impact. Your next chapter is about legacy through compassion and helping others thrive.",
        "Creator": "You thrive when expressing yourself. Your path forward is about curiosity, introspection, and crafting something beautiful and meaningful.",
        "Connector": "You come alive through people. Relationships, shared experiences, and community are your soul food in this new chapter."
    }

    st.markdown(f"**About You:** {descriptions[result]}")
    st.markdown("👉 [Join the Life Minus Work Community](https://lifeminuswork.com)")

