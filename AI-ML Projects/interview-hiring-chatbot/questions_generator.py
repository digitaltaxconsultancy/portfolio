# questions_generator.py
# Offline / rule-based fallback question generator
# Used when no LLM (e.g., GPT-4 or LLaMA) is available.

import re

# ✅ Predefined question templates for popular tech stacks
TEMPLATES = {
    "python": [
        "Explain the difference between a list and a tuple in Python.",
        "How does Python's garbage collection work?",
        "Describe what a Python decorator does and provide an example use-case.",
        "What is the difference between deep copy and shallow copy?",
        "How does Python manage memory internally?"
    ],
    "django": [
        "How do Django models work? Explain migrations and when to use them.",
        "What are Django signals and when would you use them?",
        "Explain Django's request-response cycle.",
        "How does Django handle static files in production?",
        "What is the purpose of the middleware in Django?"
    ],
    "javascript": [
        "Explain event delegation in JavaScript.",
        "What's the difference between == and === in JS?",
        "How do closures work? Give an example.",
        "What are promises and async/await in JavaScript?",
        "Explain hoisting and how it affects variable scope."
    ],
    "react": [
        "Explain the Virtual DOM and how React updates the UI.",
        "What's the difference between props and state?",
        "Describe hooks and when to use useEffect vs useMemo.",
        "What are controlled and uncontrolled components in React?",
        "Explain React’s reconciliation process."
    ],
    "mysql": [
        "How do you optimize slow SQL queries? Give at least two strategies.",
        "What's the difference between clustered and non-clustered indexes?",
        "Explain ACID properties in databases.",
        "How do you handle database transactions in MySQL?",
        "What are primary and foreign keys?"
    ],
    "flask": [
        "How does Flask handle routing?",
        "What is the purpose of blueprints in Flask?",
        "Explain Flask’s request and response objects.",
        "How does Flask differ from Django?",
        "How do you manage sessions in Flask?"
    ],
    "nodejs": [
        "What is the event loop in Node.js?",
        "How do you handle asynchronous operations in Node.js?",
        "What are streams in Node.js?",
        "What is middleware in Express.js?",
        "How do you handle errors globally in Express?"
    ],
    "default": [
        "Explain a recent project where you used this technology.",
        "What are common challenges when working with this technology?",
        "How do you stay updated with new features in this technology?",
        "What are the main advantages of using this technology?",
        "Describe how you debug or test applications built with this technology."
    ],
}


def normalize_tokens(raw_text):
    tokens = [t.strip().lower() for t in re.split(r"[,\s]+", raw_text) if t.strip()]
    cleaned_tokens = []
    for token in tokens:
        token = re.sub(r"[^a-z0-9\- ]+", "", token)  # ✅ fixed pattern
        cleaned_tokens.append(token)
    return cleaned_tokens
    


def rule_based_questions(raw_tech_stack: str, max_per=5):
    """
    Generate a dictionary of {tech: [questions]} based on given tech stack.
    Works offline — uses predefined templates.
    """
    if not raw_tech_stack:
        return {"General": TEMPLATES["default"][:max_per]}

    tokens = normalize_tokens(raw_tech_stack)
    output = {}

    for t in tokens:
        key = None
        if "python" in t:
            key = "Python"
            output[key] = TEMPLATES["python"][:max_per]
        elif "django" in t:
            key = "Django"
            output[key] = TEMPLATES["django"][:max_per]
        elif "react" in t:
            key = "React"
            output[key] = TEMPLATES["react"][:max_per]
        elif "javascript" in t or t == "js":
            key = "JavaScript"
            output[key] = TEMPLATES["javascript"][:max_per]
        elif "mysql" in t or "mariadb" in t or "postgres" in t or "postgresql" in t:
            key = t.title()
            output[key] = TEMPLATES["mysql"][:max_per]
        elif "flask" in t:
            key = "Flask"
            output[key] = TEMPLATES["flask"][:max_per]
        elif "node" in t or "express" in t:
            key = "Node.js"
            output[key] = TEMPLATES["nodejs"][:max_per]
        else:
            output[t.title()] = TEMPLATES["default"][:max_per]

    return output


# Run a quick demo
if __name__ == "__main__":
    print(rule_based_questions("Python, Django, React, MySQL, Flask, Node.js"))
