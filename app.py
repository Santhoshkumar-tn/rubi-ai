import streamlit as st
import google.generativeai as genai
import time # Add this at the very top of app.py

if st.button("Generate"):
    try:
        prompt = f"Explain {topic} for {marks} marks..."
        response = model.generate_content(prompt)
        st.markdown(response.text)
    except Exception as e:
        if "429" in str(e):
            st.error("Too many requests! Waiting 10 seconds to retry...")
            time.sleep(10) # Wait 10 seconds
            response = model.generate_content(prompt) # Try again
            st.markdown(response.text)
        else:
            st.error(f"Error: {e}")
# Use your key from Step 1
genai.configure(api_key="AIzaSyDUHLd0AB5mzReHeOfkT3PR7T9T3bu5AOY")
model = genai.GenerativeModel('gemini-2.0-flash')

st.title("RUBI: AI CS Notes")
topic = st.text_input("Enter Topic (e.g. Virtual Memory)")
marks = st.selectbox("Select Marks", [2, 5, 10])

if st.button("Generate"):
    # Prompt engineering ensures the AI follows your 2/5/10 mark rules
    prompt = f"Explain {topic} for {marks} marks. 2 marks = 2 points. 5 marks = 500 words. 10 marks = 1000 words + describe where to draw diagrams."
    response = model.generate_content(prompt)
    st.markdown(response.text)
