import os
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # Suppress TensorFlow warnings

import pyttsx3
import streamlit as st
import nltk
from transformers import pipeline
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Ensure NLTK data is downloaded
# nltk.download('punkt')
# nltk.download('stopwords')

chatbot = pipeline("text-generation", model="distilgpt2")

def speak(text):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')   # Get current speaking rate
    engine.setProperty('rate', rate-50)
    engine.say(text)
    engine.runAndWait()

def healthcare_chatbot(user_text):
    if "symptoms" in user_text:
        return "Please provide more details about your symptoms"
    elif "diagnosis" in user_text:
        return "Please provide more details about your diagnosis"
    elif "treatment" in user_text:
        return "It is important to take treatment regularly"
    else:
        response = chatbot(user_text, max_length=250, num_return_sequences=1)
        return response[0]['generated_text']

def main():
    st.title("Health Care Chatbot")
    user_input = st.text_input("How can I assist you today?")
    if st.button("Submit"):
        if user_input:
            st.write("User: ", user_input)
            with st.spinner("Processing your query, Please wait..."):
                response = healthcare_chatbot(user_input)
            st.write("HealthCare assistant: ", response)
            speak(response)
        else:
            st.write("Please enter a valid query.")

if __name__ == "__main__":
 main()