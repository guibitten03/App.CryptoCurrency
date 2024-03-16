from library import *
from services.Database import Database


st.title("📁 Crypto Trades Registed")
st.markdown("You can see all your trades bellow!")

database = Database(worksheets=[
    ("Data", 7)
])

data = database.worksheets["Data"].dropna(how="all")

edit_data = st.data_editor(data)

database.conn.update(worksheet="Data", data=edit_data)