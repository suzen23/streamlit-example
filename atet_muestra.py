import pandas as pd
import numpy as np
import plotly.express as px
from PIL import Image

st.header=('DESESTIMIENTOS ATET')
st.subheader=('des')

#cargar el dataframe
#basepath ="https://github.com/suzen23/streamlit-example"
#archivo1= basepath + "/ListDesestimientoCopia.xlsx"

excel_file = 'https://github.com/suzen23/streamlit-example/ListDesestimiento.xlsx'
sheet_name ='DATA'
df =pd.read_excel(excel_file,
                  sheet_name = sheet_name,
                  usecols='B:D',
                  header=3)





