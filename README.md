<div align="center">
  <h1>📚 Cover Books to PDF Generator</h1>
  <p><i>Generador automático de PDFs en formato de cuadrícula a partir de portadas de libros.</i></p>

  [![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://en.wikipedia.org/wiki/HTML5)
  [![JavaScript](https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
  [![jsPDF](https://img.shields.io/badge/jsPDF-PDF%20Generation-red.svg?style=for-the-badge)](https://github.com/parallax/jsPDF)
</div>

<br>

## 📖 Descripción del Proyecto

Esta es una aplicación web estática y moderna que funciona **completamente en tu navegador**. Permite a los usuarios subir múltiples imágenes (como portadas de libros, tarjetas o cromos) y automáticamente genera un documento PDF optimizado en tamaño A4 con una disposición en cuadrícula.

Al no requerir ningún servidor o backend de Python, es **100% gratuita de alojar en GitHub Pages**, mucho más rápida y completamente privada, ya que los archivos nunca abandonan tu dispositivo.

Ideal para imprimir colecciones: cada imagen se acomoda automáticamente para aprovechar al máximo el espacio de la hoja (con dimensiones de 3x4 cm por imagen y separaciones de 3mm) y además **duplica cada portada** automáticamente.

---

## ✨ Características

- 🔒 **100% Privacidad**: Las imágenes se procesan localmente en tu navegador. No se sube nada a ningún servidor.
- ⚡ **Procesamiento instantáneo**: Generación rápida gracias a la librería `jsPDF`.
- 🖼️ **Soporte multi-formato**: Admite imágenes `.jpg`, `.jpeg`, `.png`, y `.webp`.
- 📏 **Disposición inteligente**: Calcula dinámicamente columnas y filas para ajustarse perfectamente al papel A4.
- 🎨 **Interfaz amigable**: Interfaz web intuitiva con soporte "Arrastrar y Soltar" (Drag and Drop).

---

## 🚀 Despliegue en GitHub Pages

Al ser un sitio web puramente estático, puedes tenerlo en línea gratis en segundos:

1. Ve a los **Settings** (Configuración) de este repositorio en GitHub.
2. Navega a la sección **Pages** (Páginas) en el menú lateral izquierdo.
3. En **Source** (Fuente), selecciona la rama `main` y la carpeta `/ (root)`.
4. Haz clic en **Save** (Guardar).
5. En unos minutos, tu aplicación estará disponible en vivo a través del enlace proporcionado por GitHub (por ejemplo, `https://JuPerDev.github.io/cover_books/`).

---

## 💻 Uso Local

Si prefieres usarlo sin internet en tu computadora:

1. Clona el repositorio o descarga los archivos.
   ```bash
   git clone https://github.com/JuPerDev/cover_books.git
   ```
2. Simplemente abre el archivo `index.html` en tu navegador web favorito (Chrome, Firefox, Safari, Edge, etc.) haciendo doble clic sobre él.
3. Selecciona o arrastra tus portadas.
4. Haz clic en **Generar PDF** y el archivo `Coleccion_Libros_Auto.pdf` se descargará automáticamente.

---

<div align="center">
  <b>Hecho con ❤️ para organizar y catalogar colecciones de libros.</b>
</div>
