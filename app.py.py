import nltk_download 
import nltk
import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import re
import joblib
from nltk.tokenize import word_tokenize

# Make sure nltk resources are available
nltk_packages = ['punkt', 'stopwords', 'wordnet']
for pkg in nltk_packages:
    try:
        nltk.data.find(f'tokenizers/{pkg}') if pkg == 'punkt' else nltk.data.find(f'corpora/{pkg}')
    except LookupError:
        nltk.download(pkg)

# Load model and vectorizer
model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

ps = PorterStemmer()

def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    text = nltk.word_tokenize(text)
    text = [ps.stem(word) for word in text if word not in stopwords.words('english')]
    return " ".join(text)

# Streamlit UI
st.title("📩 SMS Spam Classifier")
input_sms = st.text_area("Enter your message:")

if st.button("Predict"):
    transformed = preprocess(input_sms)
    vector_input = vectorizer.transform([transformed])
    prediction = model.predict(vector_input)[0]
    
    if prediction == 1:
        st.error("This is a SPAM message!")
    else:
        st.success("This is NOT a spam message.")
