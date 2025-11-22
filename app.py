import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv
from duckduckgo_search import DDGS

# 1. Load Environment Variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("API Key nahi mili! .env file check kar.")
else:
    genai.configure(api_key=api_key)

st.set_page_config(page_title="HealthBuddy", page_icon="🩺")

# 2. Session State (Memory)
if "history" not in st.session_state:
    st.session_state.history = []

# 3. Tool Function
def medical_search_tool(term):
    try:
        results = DDGS().text(f"what is {term} medical definition simple", max_results=1)
        if results:
            return results[0]['body']
        return "No definition found."
    except:
        return "Search failed."

# 4. Main Agent Logic
def run_agent(user_text):
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    # Step A: Find terms
    prompt1 = f"Extract 3 complex medical terms from this text: {user_text}. Return ONLY terms comma separated."
    res1 = model.generate_content(prompt1)
    terms = res1.text.split(',')
    
    # Step B: Use Tool
    tool_data = {}
    for t in terms:
        t = t.strip()
        tool_data[t] = medical_search_tool(t)
        
    # Step C: Translate
    prompt2 = f"Rewrite this medical report in simple English using these definitions: {tool_data}. Original: {user_text}"
    res2 = model.generate_content(prompt2)
    return res2.text

# 5. UI Layout
st.title("🩺 HealthBuddy Agent")
user_input = st.text_area("Medical Report yaha paste kar:")

if st.button("Translate"):
    if user_input:
        with st.spinner("Agent kaam kar raha hai..."):
            output = run_agent(user_input)
            st.success("Simplified Report:")
            st.write(output)
    else:
        st.warning("Kuch likh to sahi pehle!")