import shutil
import os

def remove():
    # Ruta de la carpeta que deseas eliminar
    carpeta = 'archivos'
    # Verifica si la carpeta existe
    if os.path.exists(carpeta):
        # Elimina la carpeta y su contenido
        shutil.rmtree(carpeta)
        print(f"La carpeta '{carpeta}' ha sido eliminada.")
    else:
        print(f"La carpeta '{carpeta}' no existe.")
        

if __name__ == "__main__":
    remove()
