# 🌐 Traductor Web y App para iPad (Multidioma)

¡Bienvenido a **Traductor Pro**! Una aplicación de traducción moderna, rápida y ligera desarrollada íntegramente en **Python**. 

Este proyecto nació como una aplicación nativa para iPad utilizando la suite **Pythonista** (aprovechando los módulos de voz e interfaz de iOS) y ha evolucionado a una **aplicación web global** accesible desde cualquier dispositivo gracias a **Streamlit**.

---

## 🚀 Características Principales

* **⚡ Traducción Inteligente:** Detección automática del idioma de entrada (`autodetect`).
* **🌍 Multidioma:** Soporte instantáneo para Español, Inglés, Francés, Alemán, Chino y Portugués.
* **📱 Doble Versión:**
    * **Versión Web:** Desplegada en la nube y optimizada para móviles y ordenadores.
    * **Versión iPad (Pythonista):** Con funciones nativas como lectura por voz (`speech`) y copiado rápido al portapapeles (`clipboard`).
* **📡 API Confiable:** Conectado con el motor de traducción de MyMemory API.

---

## 🛠️ Tecnologías Utilizadas

* **Python 3**
* **Streamlit** (Para la interfaz web)
* **Requests** (Para la conexión con la API de traducción)
* **Pythonista UI & Speech Modules** (Para la versión nativa de iOS)

---

## 💻 Cómo Ejecutar el Proyecto

### 1. Versión Web (Local)
Si quieres probar la versión web en tu ordenador, clona este repositorio y sigue estos pasos:

```bash
# Clonar el repositorio
git clone [https://github.com/TU_USUARIO/TU_REPOSITORIO.git](https://github.com/TU_USUARIO/TU_REPOSITORIO.git)

# Instalar las dependencias
pip install -r requirements.txt

# Ejecutar la aplicación
streamlit run app.py
