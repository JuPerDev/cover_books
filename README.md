<div align="center">
  <h1>📚 Portlibros</h1>
  <p><i>Generador automático de hojas imprimibles a partir de portadas de libros locales o encontradas en internet.</i></p>

  [![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://en.wikipedia.org/wiki/HTML5)
  [![JavaScript](https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
  [![jsPDF](https://img.shields.io/badge/jsPDF-PDF%20Generation-red.svg?style=for-the-badge)](https://github.com/parallax/jsPDF)
</div>

<br>

## 📖 Descripción del Proyecto

Esta es una aplicación web estática y moderna que funciona directamente en el navegador. Permite subir múltiples imágenes (como portadas de libros, tarjetas o cromos), buscar portadas en internet con Open Library y Google Books, y generar hojas listas para imprimir con una disposición en cuadrícula.

Al no requerir servidor propio ni backend de Python, es gratuita de alojar en GitHub Pages y rápida de usar. Las librerías principales van incluidas en el repositorio para que la generación funcione sin depender de un CDN. Las imágenes locales se procesan en el navegador y no se suben a un servidor de la app; si usas el buscador, se consultan Open Library y Google Books para encontrar y descargar portadas públicas.

Ideal para imprimir colecciones: cada imagen se acomoda automáticamente para aprovechar al máximo el espacio de la hoja. Puedes elegir tamaño de portada, tamaño de hoja, margen, separación, cantidad de copias y formato de descarga.

---

## ✨ Características

- 🔒 **Procesamiento local**: Las imágenes subidas desde tu equipo se procesan localmente en tu navegador.
- ⚡ **Procesamiento instantáneo**: Generación rápida gracias a la librería `jsPDF`.
- 🖼️ **Soporte multi-formato**: Admite imágenes `.jpg`, `.jpeg`, `.png`, y `.webp`.
- 🔎 **Buscador de portadas**: Encuentra portadas mediante Open Library y Google Books, y agrega la mejor versión disponible.
- 📏 **Tamaños configurables**: Elige tamaños predefinidos o personalizados para cada portada.
- 📄 **Hojas configurables**: A4, Carta, Oficio/Legal, A3 o medidas personalizadas.
- 📦 **Descargas flexibles**: Exporta como PDF multipágina, PNG o JPG. Si hay varias hojas en imagen, se descargan en ZIP.
- 📐 **Disposición inteligente**: Calcula dinámicamente columnas y filas según hoja, margen, separación y tamaño de portada.
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
4. Ajusta tamaño de portada, hoja, copias y formato de descarga.
5. Haz clic en **Descargar** y el archivo se generará automáticamente.

---

<div align="center">
  <b>Hecho con ❤️ para organizar y catalogar colecciones de libros.</b>
</div>
