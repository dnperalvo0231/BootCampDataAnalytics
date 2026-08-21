import streamlit as st

st.title("BootCamp Data Analytics for Oil & Gas")
st.sidebar.title("Parámetros")

modulos = st.slidebar.selectbox("Seleccione un modulo", ["Introducción a Variables", "Funciones"])
if modulos == "Introducción a Variables":
  pozo = "SPE-001"
  oil_bpd=1250
  water_bpd=350.5
  status=True
  
  st.write(pozo)
  st.write(oil_bpd)
  st.write(water_bpd)
  st.write(status)
elif modulos == "Funciones":
  def calcular_caudal_vogel(caudal_max=1000, presion_yacimiento=3000, presion_fondo=200, decimales=2):
    """
    Calcula el caudal de petroleo mediante la ecuacion de vogel
  
    Parametros:
    Caudal_maximo (float)
    Presion de yacimiento(float)
    presion_fondo (float)
    Decimales (int)
  
    Retorna:
    caudal (float)
    """
    relacion_presion = presion_fondo/presion_yacimiento
    caudal = caudal_max*(1 - 0.2*relacion_presion - 0.8*(relacion_presion**2))
    return (round(caudal, decimales))
  caudal_max = st.numbrer.imput("Ingrese el Caudal Maximo")
