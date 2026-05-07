import streamlit as st
import google.generativeai as genai
import time

# Use the Secrets you set up in Streamlit Cloud
genai.configure(api_key=st.secrets["AIzaSyDUHLd0AB5mzReHeOfkT3PR7T9T3bu5AOY"])

# Use the Flash model - it's faster and has higher limits in 2026
model = genai.GenerativeModel('gemini-2.0-flash')

st.title("RUBI: AI CS Notes")
topic = st.text_input("Enter Topic (e.g., Virtual Memory)")
marks = st.selectbox("Select Marks", [2, 5, 10])

# ONLY ONE BUTTON HERE
if st.button("Generate"):
    if topic:
        try:
            with st.spinner("RUBI is thinking..."):
                prompt = f"Explain {topic} for {marks} marks. 2 marks = 2 points. 5 marks = 500 words. 10 marks = 1000 words + describe where to draw diagrams."
                response = model.generate_content(prompt)
                st.markdown(response.text)
        except Exception as e:
            if "429" in str(e):
                st.error("Google's free limit reached. Waiting 10 seconds to retry...")
                time.sleep(10)
                # Second attempt
                response = model.generate_content(prompt)
                st.markdown(response.text)
            else:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a topic first!")
