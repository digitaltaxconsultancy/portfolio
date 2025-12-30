
Then open your browser and visit:
👉 http://localhost:8501

------------------------------------------------------------

## 🚀 Usage Guide

1. Launch the chatbot using Streamlit.
2. The chatbot greets the user:
   “👋 Hello there! I'm your Hiring Assistant Chatbot.”
3. Enter candidate information (name, role, experience, etc.).
4. The chatbot dynamically generates follow-up questions based on responses.
5. Once the conversation ends, a summary or candidate profile is displayed.

💬 The assistant can also handle technical or behavioral questions during interviews.

------------------------------------------------------------

## 🧠 Technical Details

**Frontend:** Streamlit  
**Backend:** Python  
**AI Model:** OpenAI GPT-based model (e.g., GPT-4 or GPT-3.5-turbo)  
**Environment Variables:** `.env` for API key storage  

### Libraries Used
- streamlit – UI framework
- openai – API integration for GPT models
- dotenv – for managing environment variables
- json / os – for data handling

### Architecture Overview
- The chatbot logic is implemented in Python using a modular design.
- Streamlit handles UI state management (`st.session_state`).
- OpenAI API processes candidate interactions and generates intelligent responses.

------------------------------------------------------------

## ✍️ Prompt Design

Prompt engineering plays a crucial role in this chatbot. The prompts are designed to:
- Collect structured information (e.g., “Please tell me your name and years of experience.”)
- Ask clarifying or follow-up questions
- Identify technical roles and generate relevant interview questions
- End the conversation politely with a confirmation or summary message

**Example Prompt Logic:**
“You are an HR hiring assistant. Greet the candidate, ask for their basic information, and then move on to job-related questions based on their experience.”

------------------------------------------------------------

## 🧩 Challenges & Solutions

**1️⃣ Challenge:** Maintaining conversation flow and session context  
**✅ Solution:** Used `st.session_state` in Streamlit to preserve message history across interactions.

**2️⃣ Challenge:** Avoiding repetitive or irrelevant responses from the model  
**✅ Solution:** Implemented structured prompt templates with system and user role separation.

**3️⃣ Challenge:** Handling candidate exit or chat end logic  
**✅ Solution:** Added a function `is_end_message()` to detect farewell keywords and gracefully end sessions.

**4️⃣ Challenge:** API key and rate limit issues  
**✅ Solution:** Used `.env` configuration for secure key storage and added retry handling for API timeouts.

------------------------------------------------------------

## 👨‍💻 Author

**Developed by:** Anita Navale  
**Role:** Full Stack Developer & AI Enthusiast  
**Tagline:** Education for Everyone, Everywhere 🌍

------------------------------------------------------------

