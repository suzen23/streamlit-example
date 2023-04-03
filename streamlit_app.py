from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st 
import numpy as np
#import matplotlib.pyplot as plt

st.header('DESESTIMIENTOS DE ATET')

st.header=('DESESTIMIENTOS ATET')
st.subheader=('des')

#cargar el dataframe
#basepath ="https://github.com/suzen23/streamlit-example"
#archivo1= basepath + "/ListDesestimientoCopia.xlsx"

excel_file = 'ListDesestimiento.xlsx'
sheet_name ='DATA'
df =pd.read_excel(excel_file,
                  sheet_name = sheet_name,
                  usecols='B:D',
                  header=3)


