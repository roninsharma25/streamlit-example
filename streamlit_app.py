from collections import namedtuple
import altair as alt
import math
import pandas as pd
import numpy as np
import streamlit as st
import graphviz as graphviz
import os

st.title('SYSEN 5160: HW #1')
st.header('Ronin Sharma (rrs234)')
st.write('This is an example graph visualization showing the sequence of some ECE, CS, and INFO classes based on prerequisites.')

st.graphviz_chart('''
    digraph {
        ECE_2300 -> ECE_3420
        ECE_3420 -> ECE_4750
        ECE_3420 -> ECE_5725
        CS_1110 -> CS_2110
        CS_1110 -> ECE_2300
        CS_2110 -> CS_3110
        INFO_1300 -> INFO_2300
        INFO_2300 -> INFO_3300
    }
''')

"""
This is an example bar chart.
"""

data = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
        ]

chart_data = pd.DataFrame(
     data,
     columns=['Group 1', 'Group 2', 'Group 3'])

st.bar_chart(chart_data)

"""
Example Selectbox
"""

option = st.selectbox(
     'How would you like to be contacted?',
     ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)

"""
Example Button
"""

if st.button("Button"):
    st.write("Button Clicked")
else:
    st.write("Button Not Clicked")

"""
Example JSON:
"""
st.json({1: 2, 3: 4, 'field1': 'value1'})


"""
Example Dataframe:
"""

df = pd.DataFrame([[1,2,3], [4,5,6]], columns = ['Column 1', 'Column 2', 'Column 3'])
st.dataframe(df)

"""
Example Image:
"""

st.image(np.full((250, 250, 3), 120))

"""
Example Video:
"""

videoFile = 'example.mp4'
videoData = open(videoFile, 'rb').read()

st.video(videoData)

"""
Example Info Box:
"""
st.info("This application is for SYSEN 5160 HW #1")

"""
Example Success Box:
"""
st.success("This application works!")

