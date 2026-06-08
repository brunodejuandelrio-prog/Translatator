import streamlit as st
import requests

# Configuración de la página web
st.set_page_config(page_title="Traductor Web Pro", page_icon="🌐", layout="centered")

# Diccionario de idiomas
IDIOMAS = {
    'Español': 'es',
    'Inglés': 'en',
    'Francés': 'fr',
    'Alemán': 'de',
    'Chino': 'zh',
    'Portugués': 'pt'
}

st.title("🌐 Mi Traductor Web Multidioma")
st.write("Escribe un texto, elige el idioma y traduce al instante.")

# Caja de entrada de texto
texto_original = st.text_area("Escribe el texto a traducir:", height=150)

# Selector de idioma (Menú desplegable o botones)
idioma_seleccionado = st.selectbox("Traducir al idioma:", list(IDIOMAS.keys()))

# Botón de traducir
if st.button("¡Traducir ahora!", type="primary"):
    if not texto_original.strip():
        st.warning("Por favor, escribe algo primero.")
    else:
        codigo_destino = IDIOMAS[idioma_seleccionado]
        url = f"https://api.mymemory.translated.net/get?q={texto_original}&langpair=autodetect|{codigo_destino}"
        
        with st.spinner("Traduciendo..."):
            try:
                respuesta = requests.get(url)
                datos = respuesta.json()
                texto_traducido = datos['responseData']['translatedText']
                
                # Mostrar el resultado en una caja destacada
                st.success("Resultado:")
                st.info(texto_traducido)
                
            except Exception as e:
                st.error("Error de conexión. Inténtalo de nuevo.")
