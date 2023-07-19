import streamlit as st

st.header("sowbagya")

st.sidebar.header("my Menu")
x=st.sidebar.slider("My Ranfe",min_value=0,max_value=100)
st.text(x)