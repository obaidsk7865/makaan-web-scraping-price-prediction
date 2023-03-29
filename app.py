import streamlit as st
import pickle
import pandas as pd
import sklearn
import numpy as np

#import the model

pipe = pickle.load(open('model.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))


st.title("Makaan Predicton")



bhk = st.selectbox("BHK",df['no_bhk'].unique())


construction_status = st.selectbox("cons_stats" ,['Under Construction','Ready to move','New','Resale'])

status = 0
if construction_status == 'Under Construction':
    status = 3
elif construction_status == 'Ready to move':
    status = 1
elif construction_status == 'New':
    status = 0
elif construction_status == 'Resale':
    status = 2

squarefeet = st.number_input('select area  in Squarefeet')
if st.button('Predict Price'):
    #query
    input = pd.DataFrame([[bhk,squarefeet,status]], columns=['no_bhk','area','cons_stats'])

    # query = query.reshape(1,12)
    st.success("The predicted price is " + str(int(pipe.predict(input)[0])))