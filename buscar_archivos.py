import os
import shutil
import re

directorio = "C:\\Users\\diego\\OneDrive\\Trabajo\\5° MOLINO COLLAHUASI\\PLANOS CMDIC"
directorio_destino = "C:\\Users\\diego\\Desktop\\Plnos inst"
planos = []
archivo_txt = 'planos_inst.txt'

def crear_lista(txt, lista):
    # Abrir el archivo de texto en modo lectura
    with open(txt, "r") as archivo:
        # Recorrer cada línea del archivo
        for linea in archivo:
            # Agregar el nombre a la lista
            lista.append(linea.split()[0])

def encontrar_mover(ruta_origen, ruta_destino, lista):
    # Recorre todos los archivos en el directorio y sus subdirectorios
    for root, dirs, files in os.walk(ruta_origen):
        # Busca archivos que coincidan parcialmente con los nombres en la lista
        for nombre_archivo in lista:
            patron = re.compile(nombre_archivo, re.IGNORECASE)
            for archivo_encontrado in files:
                if patron.search(archivo_encontrado):
                    planos_encontrados = os.path.join(root, archivo_encontrado)
                    # Haz algo con el archivo encontrado, por ejemplo, moverlo a otra ubicación
                    shutil.copy(planos_encontrados, ruta_destino)

crear_lista(archivo_txt, planos)
encontrar_mover(directorio, directorio_destino, planos)
