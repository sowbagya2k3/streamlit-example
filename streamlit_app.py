from collections import namedtuple
import altair as alt
import math
import pandas as pd
import pandas_profiling
import streamlit as st
from streamlit_pandas_profiling import st_profile_report

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""
df=None
def load_data():
    global df
    import streamlit as st
    option=st.sidebar.selectbox("Select source data type",['csv','json','xml','xlsx'])
    
    if(option=='csv'):
        uploaded_file=st.sidebar.file_uploader("upload csv file", type="csv")
        if uploaded_file is not None:
            df=pd.read_csv(uploaded_file)
            st.write("total number of rows",df.size)
            #st.dataframe(df.describe())
          
    elif(option=='json'):
        uploaded_file=st.sidebar.file_uploader("upload json file", type="json")
    elif(option=='xlsx'):
        uploaded_file=st.sidebar.file_uploader("upload json file", type="json")
    elif(option=='xml'):
        uploaded_file=st.sidebar.file_uploader("upload json file", type="xml")
    else:
        st.sidebar.text('Please select an option to upload')
    if df is not None:
        selected_col=st.multiselect(label="select colums to import",options=df.columns)
        dropna=st.checkbox("Drop NA")
        dropDuplicate=st.checkbox("Drop Duplicates")
        if st.button("load"):
            df=df[selected_col]
            if dropna:
                df=df.dropna()
            if dropDuplicate:
                df=df.drop_duplicates()
            st.dataframe(df)
           # if 'data' not in st.session_state:
            st.session_state.data=df
         

    


#uploaded_file=st.sidebar.file_uploader("upload xls file", type="csv")
#df=pd.read_excel('C:/Users/91934/Downloads/data1.xls', sheet_name=1)
#st.dataframe(df)
#pf=df.profile_report()
#st_profile_report(pf)
#if uploaded_file is not None:
 #   df=pd.read_csv(uploaded_file)
  #  st.dataframe(df)
   # st.write(df.describe())
if 'data' in st.session_state:
    st.dataframe(st.session_state.data)

load_data()    

   


