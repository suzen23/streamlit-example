import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.header=('DESESTIMIENTOS ATET')

#cargar el dataframe

excel_file = 'ListDesestimiento.xlsx
sheet_name ='DATA'
df =pd.read_excel(excel_file,
                  sheet_name = sheet_name,
                  usecols='B:D',
                  header=3)





