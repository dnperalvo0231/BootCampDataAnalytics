import streamlit as st

st.title("BootCamp Data Analytics for Oil & Gas")

pozo = "SPE-001"
oil_bpd=1250
water_bpd=350.5
status=True

st.write(pozo)
st.write(oil_bpd)
st.write(water_bpd)
st.write(status)

st.sidebar.title("Parámetros")
