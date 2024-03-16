import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

st.title("Crypto Currency")
st.markdown("Hello!")

conn = st.connection("gsheets", type=GSheetsConnection)

data = conn.read(worksheet="Data", usecols=list(range(1)), ttl=5)
data = data.dropna(how="all")

st.dataframe(data)