import streamlit as st
from datetime import datetime
import os
from helpers import is_end_message, format_candidate_summary,save_candidate_data
from questions_generator import rule_based_questions
from prompt_utils import generate_llm_response


# --------------------------- #
# Streamlit Page Configuration
# --------------------------- #
st.set_page_config(
    page_title="Hiring Assistant chatbot🤖",
    page_icon="💬",
    layout="wide"
)

# --------------------------- #
# App Initialization
# --------------------------- #
if "messages" not in st.session_state:
    st.session_state.messages = []
if "candidate" not in st.session_state:
    st.session_state.candidate = {}
if "chat_active" not in st.session_state:
    st.session_state.chat_active = False
if "questions_asked" not in st.session_state:
    st.session_state.questions_asked = False

# --------------------------- #
# Greeting Message
# --------------------------- #
def chatbot_greeting():
    greeting = (
        "👋 Hello there! I'm your Hiring Assistant Chatbot.\n\n"
        "I’ll ask you a few questions to get to know you better and test your technical skills. "
        "You can type 'exit', 'bye', or 'quit' anytime to end the chat.\n\nShall we start?"
    )
    st.session_state.messages.append({"role": "assistant", "content": greeting})
    return greeting

# --------------------------- #
# Collect Candidate Info
# --------------------------- #
def collect_candidate_info():
    st.subheader("🧾 Candidate Information")

    with st.form("candidate_form"):
        name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        phone = st.text_input("Phone Number")
        experience = st.number_input("Years of Experience", min_value=0, step=1)
        position = st.text_input("Desired Position(s)")
        location = st.text_input("Current Location")
        tech_stack = st.text_area("Tech Stack (Languages, Frameworks, Databases, Tools)")

        submitted = st.form_submit_button("Start Chat")
        if submitted:
            if not name or not email or not phone or not tech_stack:
                st.warning("⚠️ Please fill all required fields.")
            else:
                st.session_state.candidate = {
                    "name": name,
                    "email": email,
                    "phone": phone,
                    "experience": experience,
                    "position": position,
                    "location": location,
                    "tech_stack": tech_stack
                }
                st.session_state.chat_active = True
                chatbot_greeting()
                st.rerun()

               # st.experimental_rerun()

# --------------------------- #
# Chatbot Conversation Logic
# --------------------------- #
def chat_interface():
    st.subheader("💬 Chat with Assistant Chatbot")

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).markdown(msg["content"])

    user_input = st.chat_input("Type your message...")

    if user_input:
        # Store user input
        st.session_state.messages.append({"role": "user", "content": user_input})

        # Check for conversation end
        if is_end_message(user_input):
            candidate_name = st.session_state.get("candidate", {}).get("name", "Candidate")
            farewell = f"🤖 Thank you, {candidate_name}! 🙏 Our HR team will review your responses and get back to you soon. 👋"

            # Save the assistant's farewell message
            st.session_state.messages.append({
                "role": "assistant",
                "content": farewell
            })

            save_candidate_data(st.session_state.candidate)

            # Mark chat as inactive
            st.session_state.chat_active = False

            # Immediately update the UI
            st.rerun()
            return

        # First Technical Questions
        if not st.session_state.questions_asked:
            tech_stack = st.session_state.candidate.get("tech_stack", "")

            tech_questions = rule_based_questions(tech_stack)
            questions = [q for qs in tech_questions.values() for q in qs]  # flatten dictionary

          #  questions = rule_based_questions(tech_stack)
            response = "Here are a few questions based on your skills:\n\n"
            for i, q in enumerate(questions, 1):
                response += f"**{i}. {q}**\n\n"
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.session_state.questions_asked = True

        else:
            # Use LLM for follow-up responses
            last_msgs = [m["content"] for m in st.session_state.messages[-5:]]
            context = "\n".join(last_msgs)
            reply = generate_llm_response(context, user_input)
            st.session_state.messages.append({"role": "assistant", "content": reply})

       # st.experimental_rerun()
        st.rerun()


# --------------------------- #
# Sidebar with Candidate Summary
# --------------------------- #
with st.sidebar:
    st.header("📋 Candidate Summary")
    if st.session_state.candidate:
        st.markdown(format_candidate_summary(st.session_state.candidate))
    else:
        st.info("Please fill candidate details to begin.")

# --------------------------- #
# Main Section
# --------------------------- #
st.title("Hiring Assistant Chatbot 🤖")

if not st.session_state.chat_active:
    collect_candidate_info()
else:
    chat_interface()

# --------------------------- #
# Save Chat Log Option
# --------------------------- #
if st.session_state.messages:
    if st.button("💾 Export Chat Log"):
        filename = f"chatlog_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            for msg in st.session_state.messages:
                f.write(f"{msg['role'].upper()}: {msg['content']}\n\n")
        st.success(f"Chat saved as {filename}")
