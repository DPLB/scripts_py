import os
import shutil

# Directorio que se va a explorar
directorio_origen = "C:\\Users\\diego\\Desktop\\Nueva carpeta"
# Diccionario de palabras clave
palabras_clave = ['DW', 'DS', 'ES', 'EL', 'MA', 'PS', 'CA', 'MD', 'MP', 'SK', 'PR', 'MO', 'DC',
                   'CS', 'MT', 'IN', 'TE', 'ESP', 'BA', 'CC', 'RR', 'MR', 'PO', 'FC', 'NS']

def crear_carpetas_planos(ubicacion, clave):
# Recorre todos los archivos en el directorio
    for archivo in os.listdir(ubicacion):
        # Verifica si el nombre del archivo contiene la clave entregada
        for key in clave:
            if key in archivo.split('-'):
                # Nombre de la carpeta a crear
                split_carpeta = archivo.split("-")[0:5]  
                nombre_carpeta = "-".join(split_carpeta)
                # Verifica si la carpeta no existe antes de crearla
                if not os.path.exists(os.path.join(ubicacion, nombre_carpeta)):
                    # Crea la carpeta
                    os.mkdir(os.path.join(ubicacion, nombre_carpeta))
    
def mover_archivo_pdf(ubicacion):
    # Recorre todos los archivos en el directorio
    for directorio in os.listdir(ubicacion):
        # Comprobar si el elemento es un directorio
        if os.path.isdir(os.path.join(ubicacion, directorio)):
            # Construir la ruta completa del directorio destino
            directorio_destino_raw = os.path.join(ubicacion, directorio)
            split_directorio_destino = directorio_destino_raw.split('\\')
            directorio_destino = split_directorio_destino[5]

        for archivo in os.listdir(ubicacion):
        # Comprobar si el nombre del archivo contiene la cadena "parte del nombre del directorio"
            if directorio_destino in archivo and '.pdf' in archivo.lower():
                # Construir la ruta completa del archivo
                ruta_origen = os.path.join(ubicacion, archivo)
                # Mover el archivo al directorio destino
                shutil.move(ruta_origen, directorio_destino_raw)

crear_carpetas_planos(directorio_origen, palabras_clave)
mover_archivo_pdf(directorio_origen)


    
