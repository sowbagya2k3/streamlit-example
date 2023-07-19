import streamlit as st
import pandas as pd
from streamlit_pandas_profiling import st_profile_report
st.header("pandas profile")
if 'data' in st.session_state:
   pr = st.session_state.data.profile_report()
   st.dataframe(st.session_state.data)
   st_profile_report(pr)