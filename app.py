from library import *
from utils.constants import *
from services.Database import Database

database = Database(worksheets=[
    ("Data", 7)
])

sheet = database.worksheets["Data"].dropna(how="all")

st.title("Analysis")

coin = st.multiselect("Select Coin", options=COINS, default="Bitcoin")
print(coin)

st.dataframe(sheet.loc[sheet[['Coin']] == "Bitcoin"])

# line_chart = st.line_chart(sheet.loc[sheet['Coin'] in coin])

