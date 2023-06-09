import os 
import re

directorio_principal = "C:\\Users\\diego\\Desktop\\instru"
planos_directorio = [file for root, dirs, files in os.walk(directorio_principal) for file in files]

def encontrar_repetidos(lista):
    lista_archivos = []
    dicc_archivos = {}
    lista_planos = []
    for archivo in lista:
        lista_archivos.append(re.split(r'\[|\]', archivo))
    for plano in lista_archivos:
        if len(plano) < 2:
            plano.append("sr")
        if plano[0] not in dicc_archivos:
            dicc_archivos[plano[0]] = plano[1]
        else:
            if plano[1] > dicc_archivos[plano[0]]:
                dicc_archivos[plano[0]] = plano[1]
        for clave, valor in dicc_archivos.items():
            if valor != "sr":
                lista_planos.append(clave + "[" + valor + '].pdf')
            else:
                lista_planos.append(clave)
    return(lista_planos)

def borrar_repetidos(planos, permitidos, ruta):
    lista_borrar = [plano for plano in planos if plano not in permitidos]
    for plano_borrar in lista_borrar:
        os.remove(os.path.join(ruta, os.path.join("-".join(plano_borrar.split('-')[0:5]), plano_borrar)))
        

print(borrar_repetidos(planos_directorio, encontrar_repetidos(planos_directorio), directorio_principal))