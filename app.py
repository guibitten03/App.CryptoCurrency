from library import *
from utils.constants import *
from services.Database import Database

st.set_page_config(layout="wide")

database = Database(worksheets=[
    ("Data", 7)
])

sheet = database.worksheets["Data"].dropna(how="all")

st.title("Analysis")

coin = st.selectbox("Select Coin", options=COINS, index=False)

line_filtered_df = sheet[(sheet['Coin'] == coin) & (sheet['Status'] == "Buy")]
mean_price = line_filtered_df['Income'].sum() / line_filtered_df['Amount'].sum()

line_filtered_df['Mean Price'] = [mean_price for x in range(line_filtered_df.shape[0])]

c1, c2 = st.columns(2, gap="small")

with c1:
    line_chart = st.line_chart(line_filtered_df, x="Data", y=["Price", "Mean Price"])

bar_filtered_df = sheet[(sheet['Coin'] == coin)]
bar_filtered_df = bar_filtered_df.groupby(by="Status")['Income'].sum()

with c2:
    bar_chart = st.bar_chart(bar_filtered_df)

