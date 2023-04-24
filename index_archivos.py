import os 

directorio = "C:\\Users\\diego\\OneDrive\\Trabajo\\5° MOLINO COLLAHUASI\\PLANOS CMDIC"

def lista_archivos(ruta):
    files_list = []
    for root, dirs, files in os.walk(ruta):
        for file in files:
            files_list.append(file)
    return(files_list)  
        
def crear_txt(lista):
    index_str = "\n".join(lista)
    with open("index_planoscmdic.txt", "w", encoding='utf-8') as archivo:
        archivo.write(index_str)

crear_txt(lista_archivos(directorio))