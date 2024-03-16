from library import *
from services.Database import Database


st.title("Crypto Currency")
st.markdown("Hello!")

database = Database(worksheets=[
    ("Data", 7)
])

data = database.worksheets["Data"].dropna(how="all")

st.dataframe(data)