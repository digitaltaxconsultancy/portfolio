import os
import openai
from dotenv import load_dotenv

# ---------------------- #
# Load environment variables
# ---------------------- #
load_dotenv()

# You can use either OpenAI GPT or any HuggingFace LLaMA model endpoint
openai.api_key = os.getenv("OPENAI_API_KEY")

# ---------------------- #
# Generate LLM Response
# ---------------------- #
def generate_llm_response(context, user_input):
    """
    Uses OpenAI GPT (or other LLM) to generate an interview-style chatbot reply
    based on recent conversation context and candidate message.
    """
    try:
        prompt = f"""
        You are an AI . 
        You are friendly, professional, and only talk about interview-related topics.

        Conversation so far:
        {context}

        Candidate says: "{user_input}"

        Respond helpfully and stay on topic. If the input is unclear, politely ask for clarification.
        """

        # ---------------- #
        # GPT API (Chat Model)
        # ---------------- #
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or "gpt-4" if available
            messages=[
                {"role": "system", "content": "You are a helpful and intelligent Interview Chatbot."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=200,
            temperature=0.7
        )

        reply = response["choices"][0]["message"]["content"].strip()
        return reply

    except Exception as e:
        print(f"⚠️ Error with LLM: {e}")
        # ---------------- #
        # Fallback message
        # ---------------- #
        return (
            "I'm sorry, I couldn’t process that right now 🤖. "
            "Could you please rephrase or try again?"
        )
