from pdf2docx import Converter
import os
import subprocess

ARCHIVOS_CONVERTIDOS = 'Convertidos'
libreoffice_path = '/usr/bin/libreoffice'
def convert_to_docx(entradas, nombre, carpeta_salida):
    carpeta = os.path.join(carpeta_salida, ARCHIVOS_CONVERTIDOS)
    os.makedirs(carpeta, exist_ok=True)
    docx_file = os.path.join(carpeta, nombre.replace('.pdf', '.docx'))
    cv = Converter(entradas)
    cv.convert(docx_file)
    cv.close()
    return docx_file


def convert_to_pdf_w(entradas, carpeta_salida):
    # Para convertir un solo archivo .docx a .pdf
    while True:
        nombre = input("Introduce el nombre del archivo pdf: ").strip()
        if nombre:
            break
        print("El nombre no puede estar vacio") 
    ruta_archivo_pdf = os.path.join(carpeta_salida, f"{nombre}.pdf")
    convert(entradas, ruta_archivo_pdf)
    print(f"¡Archivo '{entradas}' convertido a '{ruta_archivo_pdf}'!")

def convert_to_pdf(entrada, salida):
     # Convertir el archivo .docx a .pdf
    try:
        pdf= os.path.join(salida, ARCHIVOS_CONVERTIDOS)
        os.makedirs(pdf, exist_ok=True)
        print(pdf)
        subprocess.run([libreoffice_path, '--headless', '--convert-to', 'pdf', entrada, '--outdir', pdf])
        
        if os.path.exists(pdf):
            """devuelve la ruta del archivo pdf
            uniendo la carpeta de salida con el nombre del archivo docx y
            canbiando la extension a pdf"""
            return os.path.join(pdf, os.path.splitext(os.path.basename(entrada))[0] + '.pdf')
        else:
            raise FileNotFoundError(f"No se pudo generar el archivo PDF para {entrada}")
    except Exception as e:
        return f"Error al convertir el archivo: {e}"
    
# Función para convertir doc/docx a PDF en Linux
def convertir_ppt_to_pdf_linux(ppt_path, pdf_path):
    subprocess.run([libreoffice_path, '--headless', '--convert-to', 'pdf', ppt_path,'--outdir', os.path.dirname(pdf_path)])
