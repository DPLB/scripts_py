import os
import shutil

# Directorio que se va a explorar
directorio_origen = "C:\\Users\\diego\\OneDrive\\Trabajo\\5° MOLINO COLLAHUASI\\PLANOS CMDIC"
directorio_destino = "C:\\Users\\diego\\Desktop\\instru"
# Diccionario de palabras clave
codigo_clave = ['46', '48']
    
def copiar_carpeta(ubicacion, destino, clave):
    # Recorre todos los directorios en el directorio
    for directorio in os.listdir(ubicacion):
            for key in clave:
                if key in directorio.split('-'):                   
                    # Construir la ruta completa del directorio origen
                    ruta_origen = os.path.join(ubicacion, directorio)
                    ruta_destino = os.path.join(destino, directorio)
                    # copiar el directorio al directorio destino
                    shutil.copytree(ruta_origen, ruta_destino)

copiar_carpeta(directorio_origen, directorio_destino, codigo_clave)


    
