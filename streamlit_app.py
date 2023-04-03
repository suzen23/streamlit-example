from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st 
import numpy as np
#import matplotlib.pyplot as plt

st.header('DESESTIMIENTOS DE ATET')

st.subheader('holas')

excel_file = 'ListDesestimiento.xlsx'
sheet_name ='DATA'

df =pd.read_excel(excel_file,
                  sheet_name = sheet_name,
                  usecols='B:D',
                  header=3)


