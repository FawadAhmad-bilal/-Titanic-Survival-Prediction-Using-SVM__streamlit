import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
import pickle



# ---- PAGE CONFIG ----
st.set_page_config(
    page_title="Titanic Survival Prediction",
    page_icon="🚢",
    layout="centered"
)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/RMS_Titanic_3.jpg/1280px-RMS_Titanic_3.jpg", 
              use_container_width=True)
# give title to it and the describtion
st.title("🚢TITANIC SURVIVAL USING SVC")
st.write("fill the following detail and know about survival")
st.divider()# draw a line after it

with st.sidebar:
    st.header("📊 Model Info")
    st.metric("**Accuracy Score**",  "82%")
    st.write("---")
    st.write("**Algorithm:** Support Vector (classification)")
    st.write("**Scaler:** Standard Scaler")
    st.write("**Test size🧪:** 20%")
    st.write("**Random state:** 42")
    
    st.write("---")
@st.cache_resource
def load_model():
    model  = pickle.load(open("model.pkl", "rb"))#the model i train we it load here 
    scaler = pickle.load(open("scaler.pkl", "rb"))
    return model, scaler

model, scaler = load_model()
col1,col2=st.columns(2)
# taking inputs from the user 

# divide the feature into columns for better view
with col1:
    pclass= st.selectbox("🎫Ticket Class :",[1,2,3])
    sex = st.selectbox("👤Gender :",["male","female"])
    age = st.slider("🎂Age :",10,100,30 )
    sibsp = st.number_input("👫Siblings/Spouse Count", 0, 8, 0)
with col2:
    parch = st.number_input("👨‍👩‍👦Parents/Children Count", 0, 6, 0)
    fare  = st.number_input("💰Fare Amount", 0.0, 500.0, 50.0)
    embarked= st.selectbox("⚓embarked from :",["S - Southampton","C - Cherbourg","Q - Queenstown"])

# now i will do encoding
if st.button("🔍 Predict My Survival :", use_container_width=True):
                               


    #  encoding sex
    if sex =="male":
        sex_encoded=1
    else:
       sex_encoded=0


    # encoding embarded

    if embarked == "S - Southampton":
        embarked_encoded=0
    elif embarked== "C - Cherbourg":
        embarked_encoded=1
    else:
        embarked_encoded=2

    input_values=np.array([[pclass,sex_encoded,age,sibsp,parch,fare,embarked_encoded]])

    input_scaled=scaler.transform(input_values)

    prediction = model.predict(input_scaled)

    if prediction[0] == 1:
        st.success("✅ Mubarak Ho! Aap Survive Kar Lete!")
        st.balloons()
        st.metric(label="Survival Status", value="SURVIVED 🎉")
        st.divider()

    else:
         st.error("❌ Afsos! Aap Survive Nahi Karte!")
         st.metric(label="Survival Status", value="DID NOT SURVIVE 😢")
