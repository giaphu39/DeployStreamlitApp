import streamlit as st
import pickle
import sklearn
import numpy as np
pickled_model = pickle.load(open('model.pickle', 'rb'))
st.title('Revenue Prediction')
x = st.number_input('Input Temperature')
x = np.array(x).reshape(-1, 1)
if st.button('Predict'):
  st.text('Revenue Prediction')
  y_pred = pickled_model.predict(x)
  st.success(*y_pred)
