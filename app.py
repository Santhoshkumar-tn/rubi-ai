import streamlit as st
import google.generativeai as genai

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
