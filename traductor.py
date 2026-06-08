import ui
import requests
import speech
import clipboard

# Diccionario con códigos de idioma y sus variantes de voz para iOS
IDIOMAS = {
    'Español': {'codigo': 'es', 'voz': 'es-ES'},
    'Inglés': {'codigo': 'en', 'voz': 'en-US'},
    'Francés': {'codigo': 'fr', 'voz': 'fr-FR'},
    'Alemán': {'codigo': 'de', 'voz': 'de-DE'},
    'Chino': {'codigo': 'zh', 'voz': 'zh-CN'},
    'Portugués': {'codigo': 'pt', 'voz': 'pt-PT'}
}

def traducir_texto(sender):
    texto_original = sender.superview['texto_entrada'].text
    if not texto_original or texto_original.strip() == "":
        sender.superview['texto_salida'].text = "Por favor, escribe algo primero."
        return
    
    sender.superview['texto_salida'].text = "Traduciendo..."
    
    selector = sender.superview['selector_idioma']
    idioma_nombre = selector.segments[selector.selected_index]
    codigo_destino = IDIOMAS[idioma_nombre]['codigo']
    
    url = f"https://api.mymemory.translated.net/get?q={texto_original}&langpair=autodetect|{codigo_destino}"
    
    try:
        respuesta = requests.get(url)
        datos = respuesta.json()
        texto_traducido = datos['responseData']['translatedText']
        sender.superview['texto_salida'].text = texto_traducido
    except Exception as e:
        sender.superview['texto_salida'].text = "Error de conexión. Inténtalo de nuevo."

def escuchar_texto(sender):
    # Obtener el texto traducido actual
    texto_traducido = sender.superview['texto_salida'].text
    if not texto_traducido or texto_traducido in ["", "Traduciendo...", "Por favor, escribe algo primero.", "Error de conexión. Inténtalo de nuevo."]:
        return
    
    # Detectar el idioma seleccionado para usar la pronunciación correcta
    selector = sender.superview['selector_idioma']
    idioma_nombre = selector.segments[selector.selected_index]
    codigo_voz = IDIOMAS[idioma_nombre]['voz']
    
    # Detener cualquier lectura previa y hablar
    speech.stop()
    speech.say(texto_traducido, codigo_voz, 0.5) # 0.5 es la velocidad

def copiar_texto(sender):
    texto_traducido = sender.superview['texto_salida'].text
    if texto_traducido and texto_traducido not in ["Traduciendo...", "Por favor, escribe algo primero."]:
        clipboard.set(texto_traducido)
        # Un pequeño truco visual: cambiamos temporalmente el título del botón para avisar
        titulo_original = sender.title
        sender.title = "¡Copiado! ✅"
        def restaurar(): sender.title = titulo_original
        ui.delay(restaurar, 1.5)

# --- Configuración de la Interfaz Gráfica (UI) ---
vista = ui.View()
vista.name = 'Traductor Pro iPad'
vista.background_color = '#f4f6f9'
vista.width = 400
vista.height = 580

# Caja de entrada de texto
lbl1 = ui.Label(text="Escribe el texto a traducir:", frame=(20, 20, 360, 20))
lbl1.font = ('<system-bold>', 14)
vista.add_subview(lbl1)

entrada = ui.TextView(name='texto_entrada', frame=(20, 45, 360, 110))
entrada.border_width = 1
entrada.border_color = '#d1d1d6'
entrada.corner_radius = 8
entrada.font = ('<system>', 15)
vista.add_subview(entrada)

# Selector de Idiomas
lbl2 = ui.Label(text="Traducir al idioma:", frame=(20, 170, 360, 20))
lbl2.font = ('<system-bold>', 14)
vista.add_subview(lbl2)

selector = ui.SegmentedControl(name='selector_idioma', frame=(20, 195, 360, 40))
selector.segments = list(IDIOMAS.keys())
selector.selected_index = 1
vista.add_subview(selector)

# Botón Traducir
boton = ui.Button(title='¡Traducir ahora!', frame=(20, 255, 360, 45))
boton.background_color = '#34c759'
boton.tint_color = 'white'
boton.font = ('<system-bold>', 16)
boton.corner_radius = 10
boton.action = traducir_texto
vista.add_subview(boton)

# Caja de salida de texto
salida = ui.TextView(name='texto_salida', frame=(20, 315, 360, 150))
salida.border_width = 1
salida.border_color = '#d1d1d6'
salida.corner_radius = 8
salida.editable = False
salida.font = ('<system>', 15)
salida.background_color = '#fafafa'
vista.add_subview(salida)

# --- NUEVOS BOTONES (Escuchar y Copiar) ---
# Botón Escuchar (Altavoz)
btn_escuchar = ui.Button(title=' 🔊 Escuchar', frame=(20, 480, 170, 45))
btn_escuchar.background_color = '#007af0'
btn_escuchar.tint_color = 'white'
btn_escuchar.font = ('<system-bold>', 15)
btn_escuchar.corner_radius = 8
btn_escuchar.action = escuchar_texto
vista.add_subview(btn_escuchar)

# Botón Copiar
btn_copiar = ui.Button(title=' 📋 Copiar Texto', frame=(210, 480, 170, 45))
btn_copiar.background_color = '#5856d6' # Color morado iOS
btn_copiar.tint_color = 'white'
btn_copiar.font = ('<system-bold>', 15)
btn_copiar.corner_radius = 8
btn_copiar.action = copiar_texto
vista.add_subview(btn_copiar)

# Presentar en el iPad
vista.present('sheet')
