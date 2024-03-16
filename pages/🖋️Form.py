from library import *

st.title("Crypto Currency")
st.markdown("Hello!")

conn = st.connection("gsheets", type=GSheetsConnection)

data = conn.read(worksheet="Data", usecols=list(range(7)), ttl=5)
data = data.dropna(how="all")

st.dataframe(data)