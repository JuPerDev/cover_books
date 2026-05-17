from flask import Flask, render_template, request, send_file
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import A4
import os
import tempfile
import shutil

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generar', methods=['POST'])
def generar_pdf():
    if 'imagenes' not in request.files:
        return "No se subieron imágenes", 400

    archivos = request.files.getlist('imagenes')
    archivos = [f for f in archivos if f.filename and f.filename.lower().endswith(('.jpg', '.jpeg', '.png', '.webp'))]

    if not archivos:
        return "No se encontraron imágenes válidas", 400

    # Crear carpeta temporal para las imágenes
    tmp_dir = tempfile.mkdtemp()
    pdf_path = os.path.join(tmp_dir, "Coleccion_Libros_Auto.pdf")

    # Guardar imágenes temporalmente
    rutas_imagenes = []
    for f in archivos:
        ruta = os.path.join(tmp_dir, f.filename)
        f.save(ruta)
        rutas_imagenes.append(ruta)

    rutas_imagenes.sort()

    # Generar PDF
    ancho_pagina, alto_pagina = A4
    margen = 1 * cm
    ancho_img = 3 * cm
    alto_img = 4 * cm
    espacio = 0.3 * cm  # 3mm de separación

    area_ancho = ancho_pagina - 2 * margen
    area_alto = alto_pagina - 2 * margen

    columnas = int((area_ancho + espacio) // (ancho_img + espacio))
    filas = int((area_alto + espacio) // (alto_img + espacio))

    c = canvas.Canvas(pdf_path, pagesize=A4)

    col_actual = 0
    fila_actual = 0

    for img_path in rutas_imagenes:
        for _ in range(2):
            x = margen + col_actual * (ancho_img + espacio)
            y = alto_pagina - margen - (fila_actual + 1) * alto_img - fila_actual * espacio

            c.drawImage(img_path, x, y, width=ancho_img, height=alto_img,
                        preserveAspectRatio=False)

            col_actual += 1
            if col_actual >= columnas:
                col_actual = 0
                fila_actual += 1

            if fila_actual >= filas:
                c.showPage()
                col_actual = 0
                fila_actual = 0

    c.save()

    response = send_file(pdf_path, as_attachment=True, download_name="Coleccion_Libros_Auto.pdf")
    shutil.rmtree(tmp_dir, ignore_errors=True)
    return response

if __name__ == '__main__':
    print("Servidor corriendo en http://localhost:8080")
    app.run(debug=True, port=8080)
