from library import *
from utils.constants import *
from services.Database import Database

import datetime

st.set_page_config(layout="wide")

st.title("🖋️ Crypto Currency Formulary")
st.markdown("Insert Trade Information Bellow...")

database = Database(worksheets=[
    ("Data", 7)
])

sheet = database.worksheets["Data"].dropna(how="all")


data = st.date_input("Trade date")
time = st.time_input("Trade time", step=60)
coin = st.selectbox("Select coin", options=COINS, index=False)
price = st.number_input("Coin Price", step=0.01, value=None)
income = st.number_input("Value Invested", step=0.01, value=None)

if price == None or income == None:
    amount = 0.0
else:
    amount = income / price


status = st.selectbox("Operation", options=OPS, index=False)

register = st.button("Register")

if register:
    if not data or not time or not coin or not price or not income or not status:
        st.warning("Report All Data.")
    else:
        register_data = pd.DataFrame([{
            "Data": data.strftime("%d-%m-%Y"),
            "Time": time,
            "Coin": coin,
            "Price": price,
            "Income": income,
            "Amount": amount,
            "Status": status
        }])

        updated_df = pd.concat([sheet, register_data], ignore_index=True)

        database.conn.update(worksheet="Data", data=updated_df)

        st.success("Trade Registed with Success!")