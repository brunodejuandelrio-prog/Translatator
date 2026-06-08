import streamlit as st
import requests
from gtts import gTTS
import io

# Configuración de la página web
st.set_page_config(page_title="Traductor Web Pro", page_icon="🌐", layout="centered")

# Diccionario de idiomas (con su código de traducción y código de voz gTTS)
IDIOMAS = {
    'Español': {'api': 'es', 'voz': 'es'},
    'Inglés': {'api': 'en', 'voz': 'en'},
    'Francés': {'api': 'fr', 'voz': 'fr'},
    'Alemán': {'api': 'de', 'voz': 'de'},
    'Chino': {'api': 'zh', 'voz': 'zh'},
    'Portugués': {'api': 'pt', 'voz': 'pt'}
}

st.title("🌐 Mi Traductor Web Multidioma")
st.write("Escribe o pega un texto, elige el idioma y traduce al instante.")

# Caja de entrada de texto
texto_original = st.text_area("Escribe o pega el texto a traducir:", height=150, placeholder="Escribe o mantén presionado aquí para pegar...")

# Selector de idioma
idioma_seleccionado = st.selectbox("Traducir al idioma:", list(IDIOMAS.keys()))

# Botón de traducir
if st.button("¡Traducir ahora!", type="primary"):
    if not texto_original.strip():
        st.warning("Por favor, escribe o pega algo primero.")
    else:
        codigo_destino = IDIOMAS[idioma_seleccionado]['api']
        codigo_voz = IDIOMAS[idioma_seleccionado]['voz']
        url = f"https://api.mymemory.translated.net/get?q={texto_original}&langpair=autodetect|{codigo_destino}"
        
        with st.spinner("Traduciendo..."):
            try:
                respuesta = requests.get(url)
                datos = respuesta.json()
                texto_traducido = datos['responseData']['translatedText']
                
                # Guardar el resultado en el estado de la app para que no se borre al usar el audio
                st.session_state['resultado'] = texto_traducido
                st.session_state['codigo_voz'] = codigo_voz
                
            except Exception as e:
                st.error("Error de conexión. Inténtalo de nuevo.")

# Si ya hay una traducción hecha, mostramos el resultado y las opciones de audio
if 'resultado' in st.session_state:
    st.success("Resultado:")
    st.info(st.session_state['resultado'])
    
    # --- FUNCIÓN DE ESCUCHAR ---
    st.write("🔊 **Escuchar la pronunciación:**")
    try:
        # Generar el audio usando Google TTS en memoria (sin guardar archivos en el servidor)
        tts = gTTS(text=st.session_state['resultado'], lang=st.session_state['codigo_voz'])
        fp = io.BytesIO()
        tts.write_to_fp(fp)
        fp.seek(0)
        
        # Mostrar el reproductor de audio nativo de la web
        st.audio(fp, format='audio/mp3')
    except Exception as e:
        st.write("No se pudo cargar el reproductor de audio en este momento.")

