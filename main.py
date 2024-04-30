import random
import os

# Obtener la lista de archivos en la carpeta "Temas/"
files_list = os.listdir("Temas/")
file_random = "Temas/" + files_list[random.randint(0, len(files_list) - 1)]

# Caracter de salto de línea
line_break = "\n"

# Identificadores para diferentes tipos de contenido
identifier_title = "TITULO:\n"
identifier_theme = "TEMA:\n"
identifier_paragraph = "PARRAFO:\n"
identifier_enumeration = "ENUMERACION:\n"
identifiers = [identifier_title, identifier_theme, identifier_paragraph, identifier_enumeration]

# Variables para almacenar los datos
title = ""
theme_content = {}

# Leer el archivo seleccionado
with open(file_random, 'r', encoding='utf-8') as file:
    for line in file:
        if line in identifiers:
            last_identifier = line

        if last_identifier == identifier_title and line != identifier_title and line != line_break:
            title = line
        elif last_identifier == identifier_theme and line != identifier_theme and line != line_break:
            theme_content[line] = ""
        elif last_identifier == identifier_paragraph and line != identifier_theme:
            last_key = list(theme_content.keys())[-1]
            theme_content[last_key] = theme_content[last_key] + line


while True:
    # Seleccionar un tema aleatorio
    keys_list = list(theme_content.keys())
    random_key_index = random.randint(0, len(keys_list) - 1)
    key_selected = keys_list[random_key_index]
    os.system("cls")
    print("Titulo: ", title)
    print("Tema: ", key_selected)
    input("Presiona cualquier tecla para mostrar el resto")
    os.system("cls")
    print("Titulo: ", title)
    print("Tema: ", key_selected)
    print(theme_content[key_selected])
    input("Presiona cualquier tecla para un siguiente tema:")
