from library import *
from services.Database import Database
from services.Style import Style

st.set_page_config(layout="wide")

st.title("📁 Crypto Trades Registed")
st.markdown("You can see all your trades bellow!")

style = Style("assets/style.css")

database = Database(worksheets=[
    ("Data", 7)
])

data = database.worksheets["Data"].dropna(how="all")

edit_data = st.data_editor(data,hide_index=True)

database.conn.update(worksheet="Data", data=edit_data)