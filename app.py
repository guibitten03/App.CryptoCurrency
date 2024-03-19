from library import *
from utils.constants import *
from services.Database import Database

database = Database(worksheets=[
    ("Data", 7)
])

sheet = database.worksheets["Data"].dropna(how="all")

st.title("Analysis")

coins = st.multiselect("Select Coin", options=COINS, default="Bitcoin")

st.dataframe(sheet.loc[sheet[['Coin']] in coins.values])

# line_chart = st.line_chart(sheet.loc[sheet['Coin'] in coin])

