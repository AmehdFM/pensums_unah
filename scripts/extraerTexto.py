import fitz  # PyMuPDF

# Ruta del PDF
pdf_path = "C:\\Users\\Mendez\\Desktop\\proyectos\\Pensums-UNAH\\planes_de_estudio\\Ingeniería-Civil.pdf"

# Archivo de salida
output_path = "texto_completo_extraido.txt"

def extraer_texto_columna_segunda_pagina(pdf_path):
    doc = fitz.open(pdf_path)
    texto_completo = ""

    # Extraer el texto solo de la segunda página (índice 1)
    if len(doc) > 1:  # Verifica si el documento tiene más de una página
        pagina = doc[1]  # La segunda página tiene índice 1
        texto_completo = pagina.get_text("text")
    else:
        print("El documento no tiene suficientes páginas.")

    return texto_completo

# Extraer el texto solo de la segunda página
texto = extraer_texto_columna_segunda_pagina(pdf_path)

# Guardar el texto extraído en un archivo de texto
with open(output_path, 'w', encoding='utf-8') as archivo_salida:
    archivo_salida.write(texto)

# Confirmar que el texto se ha guardado
print(f"El texto de la segunda página ha sido extraído y guardado en {output_path}")
