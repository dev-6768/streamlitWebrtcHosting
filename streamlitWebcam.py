# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 17:19:16 2023

@author: HP
"""

import streamlit as st
from streamlit_webrtc import webrtc_streamer

st.write("# Hello Mate,")
st.write("This is my first static app created by streamlit, google colab and ngrok.")
st.write("This app uses an underlying library of pyngrok, a python wrapper for ngrok, which provides a secure tunnel for our apps to work publicly on the internet.")
st.write("Now the hassle of html is over and streamlit would become more and more common for developing data science apps and apps which users want.")
st.write("Kudos to the developer team for writing out such an amazing library which provides literally everything in python and harnessing it's power to create something beautiful.")
st.write("Signing off,\nSanidhya Mishra.")

webrtc_streamer(key="sampleKey")