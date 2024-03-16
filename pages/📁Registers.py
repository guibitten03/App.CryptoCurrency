from library import *
from services.Database import Database


st.title("Crypto Trades Registed")
st.markdown("You can see all your trades bellow!")

database = Database(worksheets=[
    ("Data", 7)
])

data = database.worksheets["Data"].dropna(how="all")

st.dataframe(data)