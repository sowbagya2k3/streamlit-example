import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import mpld3
import streamlit.components.v1 as components
"""
# Welcome to EDA Profiler!
"""

if 'data' in st.session_state:
    df=st.session_state.data
    c=st.container()
    
    src,trg=c.columns(2)
    x=src.selectbox(label="x:axis",options=df.columns)
    y=trg.selectbox(label="y:axis",options=df.columns)
    chart_type=c.selectbox('select chart type',['histogram','pie','scatter'])
    if(chart_type=='histogram'):
        bin=c.slider("select bin",min_value=3,max_value=10)
    if c.button('draw graph'):
        
        
        plt.style.use('ggplot')
        fig=plt.figure()
        if(chart_type=='scatter'):
            plt.scatter(df[x],df[y])
            plt.xlabel(x)
            plt.ylabel(y)
        elif(chart_type=='histogram'):
            
            plt.hist(df[x],bins=bin)
    
        fig_html=mpld3.fig_to_html(fig)
        components.html(fig_html, height=600)
        #st.write(components)