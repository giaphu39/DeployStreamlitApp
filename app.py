import streamlit as st
import pickle
import sklearn
pickled_model = pickle.load(open('model.pkl', 'rb'))
st.title('Revenue Prediction')
a = st.number_input('Input Temperature')
if st.button('Predict'):
  st.text('Revenue Prediction')
  y_pred = model.predict(x)
  st.success(y_pred)
