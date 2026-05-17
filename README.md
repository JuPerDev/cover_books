<div align="center">
  <h1>📚 Cover Books to PDF Generator</h1>
  <p><i>Generador automático de PDFs en formato de cuadrícula a partir de portadas de libros.</i></p>

  [![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
  [![Flask](https://img.shields.io/badge/Flask-Web%20Framework-lightgrey.svg)](https://flask.palletsprojects.com/)
  [![ReportLab](https://img.shields.io/badge/ReportLab-PDF%20Generation-red.svg)](https://docs.reportlab.com/)
</div>

<br>

## 📖 Descripción del Proyecto

Esta es una aplicación web intuitiva construida con **Python** y **Flask**. Permite a los usuarios subir múltiples imágenes (como portadas de libros, tarjetas, o cromos) y automáticamente genera un documento PDF optimizado en tamaño A4 con una disposición en cuadrícula.

Ideal para imprimir colecciones: cada imagen se acomoda automáticamente para aprovechar al máximo el espacio de la hoja (con dimensiones de 3x4 cm por imagen y separaciones de 3mm) y además **duplica cada portada** según las especificaciones.

---

## ✨ Características

- 🖼️ **Soporte multi-formato**: Admite imágenes `.jpg`, `.jpeg`, `.png`, y `.webp`.
- ⚡ **Procesamiento rápido**: Generación del PDF casi instantánea gracias a la librería `reportlab`.
- 📏 **Disposición inteligente**: Calcula dinámicamente columnas y filas para ajustarse perfectamente al papel A4.
- 🧹 **Limpieza automática**: Usa directorios temporales que se borran automáticamente, manteniendo el servidor limpio.
- 🎨 **Interfaz amigable**: Interfaz web simple y directa para subir los archivos de manera sencilla.

---

## 🛠️ Requisitos Previos

Asegúrate de tener instalado en tu sistema:
- [Python 3.8+](https://www.python.org/downloads/)
- `pip` (Administrador de paquetes de Python)

---

## 🚀 Instalación y Configuración

Sigue estos pasos para ejecutar el proyecto en tu máquina local:

### 1. Clonar el repositorio
```bash
git clone https://github.com/JuPerDev/cover_books.git
cd cover_books
```

### 2. Crear y activar un entorno virtual (Recomendado)
Para mantener las dependencias aisladas del resto de tu sistema:

**En Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**En macOS y Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar las dependencias
Instala los paquetes necesarios definidos en `requirements.txt`:
```bash
pip install -r requirements.txt
```

---

## 💻 Uso de la Aplicación

1. Una vez activado el entorno virtual y con las dependencias instaladas, arranca el servidor:
   ```bash
   python app.py
   ```
2. Abre tu navegador web favorito y dirígete a:
   👉 **`http://localhost:8080`**
3. Selecciona las imágenes de tus portadas.
4. Haz clic en el botón de **Generar PDF** y la descarga del archivo `Coleccion_Libros_Auto.pdf` comenzará de forma automática.

---

## 📁 Estructura del Proyecto

```text
cover_books/
│
├── app.py                 # Código principal del servidor (Flask)
├── requirements.txt       # Dependencias necesarias
├── BASE.MD                # Script base original de consola (referencia)
├── .gitignore             # Archivos excluidos de git
├── templates/
│   └── index.html         # Interfaz web
└── README.md              # Documentación del proyecto
```

---

<div align="center">
  <b>Hecho con ❤️ para organizar y catalogar colecciones de libros.</b>
</div>
