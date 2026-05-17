# 1. Instalamos la librería necesaria
!pip install reportlab

from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import A4
import os

def crear_pdf_automatico(nombre_salida):
    ancho_pagina, alto_pagina = A4  # 21cm x 29.7cm
    margen = 1 * cm
    ancho_img = 3 * cm
    alto_img = 4 * cm

    espacio = 0.3 * cm  # 3mm de separación

    # Área útil de la página
    area_ancho = ancho_pagina - 2 * margen
    area_alto = alto_pagina - 2 * margen

    # Calcular columnas y filas para máximo aprovechamiento
    columnas = int((area_ancho + espacio) // (ancho_img + espacio))
    filas = int((area_alto + espacio) // (alto_img + espacio))

    c = canvas.Canvas(nombre_salida, pagesize=A4)

    # Extensiones permitidas
    extensiones = ('.jpg', '.jpeg', '.png', '.webp')

    # 2. Filtramos automáticamente todos los archivos de la carpeta
    imagenes = [f for f in os.listdir('.') if f.lower().endswith(extensiones)]
    imagenes.sort()  # Los ordenamos alfabéticamente

    if not imagenes:
        print("¡Ups! No encontré ninguna imagen en la carpeta. Asegúrate de subirlas primero.")
        return

    print(f"Encontré {len(imagenes)} imágenes. Generando PDF...")
    print(f"Disposición: {columnas} columnas x {filas} filas = {columnas * filas} imágenes por página")

    col_actual = 0
    fila_actual = 0

    for img_path in imagenes:
        for _ in range(2):  # 2 repeticiones por cada imagen
            try:
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

            except Exception as e:
                print(f"No pude procesar {img_path}: {e}")

    c.save()
    print(f"¡Listo! Tu archivo '{nombre_salida}' ha sido creado con éxito.")

# Ejecutamos la función
crear_pdf_automatico("Coleccion_Libros_Auto.pdf")