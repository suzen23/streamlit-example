import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.header=('DESESTIMIENTOS ATET')

basepath ="https://github.com/suzen23/streamlit-example"
archivo1= basepath + "/ListDesestimiento.xlsx"


dfind = pd.read_excel(archivo1, sheet_name="LISTADO")
dexo = pd.read_excel(archivo1, sheet_name="Motivo")

dfind.head()
dfind.info()

print(dfind)
