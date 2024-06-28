# -*- coding: utf-8 -*-

import Utility
import tkinter.dialog
import tkinter.messagebox
from TemaStructure import MyTemaStructureClass
from JsonManagement import MyJsonManagementClass
import tkinter
from tkinter import ttk
from tkinter import simpledialog
import random

class MyApplication:
    def __init__(self):
        # Crear la ventana principal
        self.window = tkinter.Tk() 
        self.window.title("Temas") 
        self.window.option_add("*Font", "Helvetica 12") # Establecer la fuente de la ventana
        self.window.geometry("1000x800")

        # Crear los objetos de las clases MyTemaStructureClass y MyJsonManagementClass
        self.tema = MyTemaStructureClass() # Objeto de la clase MyTemaStructureClass
        self.json_manager = MyJsonManagementClass() # Objeto de la clase MyJsonManagementClass

        # Crear el entry para el título del tema, su label y el botón para obtener un título aleatorio
        self.title_cb_lable = tkinter.Label(self.window, text="Título del tema")
        self.title_cb_lable.grid(row=0, column=0, padx=10)

        self.title_cb = ttk.Combobox(self.window)
        self.title_cb.grid(row=1, column=0, padx=10)
        self.title_cb.config(state="readonly")
        self.title_cb.bind("<<ComboboxSelected>>", self.on_combobox_selected_title)
        self.refresh_cb_title()

        self.get_random_title_button = tkinter.Button(self.window, text="Obtener un título aleatorio", command=self.set_random_title)
        self.get_random_title_button.grid(row=1, column=1)

        self.create_new_title_button = tkinter.Button(self.window, text="Crear un nuevo título", command=self.create_new_title)
        self.create_new_title_button.grid(row=1, column=2)

        self.delete_title_button = tkinter.Button(self.window, text="Eliminar título", command=self.delete_title)
        self.delete_title_button.grid(row=1, column=3)

        # Crear el entry para el subtítulo, su label y el botón para obtener un subtítulo aleatorio
        self.subtitle_cb_label = tkinter.Label(self.window, text="Subtítulo")
        self.subtitle_cb_label.grid(row=2, column=0, padx=10)

        self.subtitle_cb = ttk.Combobox(self.window, width=30)
        self.subtitle_cb.grid(row=3, column=0, padx=10)
        self.subtitle_cb.config(state="readonly")

        self.get_random_subtitle_button = tkinter.Button(self.window, text="Obtener un subtítulo aleatorio", command=self.set_random_subtitle)
        self.get_random_subtitle_button.grid(row=3, column=1)

        self.add_new_subtitle_button = tkinter.Button(self.window, text="Agregar un nuevo subtítulo", command=self.add_new_subtitle)
        self.add_new_subtitle_button.grid(row=3, column=2)

        self.delete_subtitle_button = tkinter.Button(self.window, text="Eliminar subtítulo", command=self.delete_subtitle)
        self.delete_subtitle_button.grid(row=3, column=3)

        # Crear el entry para el texto del subtítulo y su label
        self.text_Entry_label = tkinter.Label(self.window, text="Texto")
        self.text_Entry_label.grid(row=4, column=0, padx=10)

        self.text_Entry = tkinter.Text(self.window, width=50, height=30)
        self.text_Entry.grid(row=5, column=0, padx=10)
        self.text_Entry.config(state="disabled")

        self.show_text_button = tkinter.Button(self.window, text="Mostrar texto", command=self.refresh_text_Entry)
        self.show_text_button.grid(row=5, column=1)

        self.modify_text_button = tkinter.Button(self.window, text="Modificar texto", command=self.modify_text)
        self.modify_text_button.grid(row=5, column=2)

        # Botón para guardar los cambios
        self.save_changes_button = tkinter.Button(self.window, text="Guardar cambios", command=self.save_changes)
        self.save_changes_button.grid(row=6, column=0)

    def on_combobox_selected_title(self, event) -> None:
        """
        Evento que se ejecuta cuando se selecciona un título del combobox
        """
        # Establecer el tema seleccionado
        self.set_tema()

    def set_random_title(self) -> None:
        """
        Selecciona un título aleatorio del combobox y lo muestra en la interfaz
        """
        # Tomar los títulos del combobox
        titles = self.title_cb['values']
        # Si no hay títulos disponibles, mostrar un mensaje de error
        if len(titles) == 0:
            tkinter.messagebox.showerror("Error", "No hay temas disponibles")
            return
        # Seleccionar un título aleatorio y mostrarlo en la interfaz
        random_title = random.choice(titles)
        self.title_cb.set(random_title)
        self.set_tema()
        
    def set_random_subtitle(self) -> None:
        """
        Selecciona un subtítulo aleatorio del combobox y lo muestra en la interfaz
        """
        # Tomar los subtítulos del combobox
        subtitles = self.subtitle_cb['values']
        # Si no hay subtítulos disponibles, mostrar un mensaje de error
        if len(subtitles) == 0:
            tkinter.messagebox.showerror("Error", "No hay subtítulos disponibles")
            return
        # Seleccionar un subtítulo aleatorio y mostrarlo en la interfaz
        random_subtitle = random.choice(subtitles)
        self.subtitle_cb.set(random_subtitle)
        
    def create_new_title(self) -> None:
        """
        Crea un nuevo título y lo añade a la lista de títulos
        """
        # Tomar el título ingresado por el usuario
        title = self.get_input_prompt("Ingrese el nuevo título")
        # Si el título ingresado por el usuario no es válido, mostrar un mensaje de error
        if Utility.is_string_not_valid(title, "El título no puede estar vacío"): return
        # Si el título ya existe, mostrar un mensaje de error
        if self.json_manager.get_theme(title) != None:
            tkinter.messagebox.showerror("Error", "El título ya existe")
            return
        # Crear un nuevo título y refrescar el combobox de los títulos
        self.tema.title = title
        self.tema.content = []
        self.title_cb.set(title)
        self.are_changes = True

    def add_new_subtitle(self) -> None:
        """
        Añade un nuevo subtítulo al tema seleccionado
        """
        # Guardar los cambios realizados en el texto del subtítulo
        self.tema.update_subtitle_content(self.subtitle_cb.get(), self.text_Entry.get("1.0", tkinter.END))
        # Tomar el subtítulo ingresado por el usuario
        subtitle = self.get_input_prompt("Ingrese el subtítulo")
        # Si el subtítulo ingresado por el usuario no es válido, mostrar un mensaje de error
        if Utility.is_string_not_valid(subtitle, "El subtítulo no puede estar vacío"): return
        # Si el subtítulo ya existe, mostrar un mensaje de error
        if subtitle in self.subtitle_cb['values']:
            tkinter.messagebox.showerror("Error", "El subtítulo ya existe")
            return
        # Añadir el subtítulo al tema y refrescar el combobox de los subtítulos
        self.tema.add_subtitle(subtitle, "")
        self.subtitle_cb.set(subtitle)
        self.subtitle_cb.focus()
        self.refresh_cb_subtitle()
        self.refresh_text_Entry()

    def modify_text(self) -> None:
        """
        Cambia el estado del text_Entry a normal para poder modificar el texto
        """
        # Cambiar el estado del text_Entry a normal y poner el foco en el text_Entry
        self.text_Entry.config(state="normal")
        self.text_Entry.focus()

    def save_changes(self) -> None:
        """
        Guarda los cambios realizados en el texto del subtítulo, los subtítulos y los títulos
        """
        # Si no se ha seleccionado un título, mostrar un mensaje de error
        if Utility.is_string_not_valid(self.tema.title, "No se ha seleccionado o agregado un título"): return
        # Si no se ha seleccionado o agregado un subtítulo, mostrar un mensaje de error
        if self.tema.content == []:
            tkinter.messagebox.showerror("Error", "No se ha seleccionado o agregado un subtítulo")
            return
        # Guardar los cambios realizados en el texto del subtítulo
        subtitle = self.subtitle_cb.get()
        text = self.text_Entry.get("1.0", tkinter.END)
        self.tema.update_subtitle_content(subtitle, text)
        # Guardar los cambios realizados en los subtítulos
        if self.json_manager.update_theme_content(self.tema.title, self.tema.content) == False:
            self.json_manager.add_theme(self.tema.title, self.tema.content)
        # Mostrar un mensaje de éxito y refrescar el combobox de los títulos
        self.refresh_cb_title()
        self.refresh_cb_subtitle()
        self.text_Entry.config(state="disabled")
        tkinter.messagebox.showinfo("Información", "Cambios guardados con éxito")
        self.refresh_cb_title()
    
    def delete_title(self) -> None:
        """
        Elimina el título seleccionado
        """
        # Tomar el título seleccionado
        title = self.title_cb.get()
        # Si no se ha seleccionado un título, mostrar un mensaje de error y confirmar si se quiere eliminar el título
        if Utility.is_string_not_valid_and_confirm_delete_cancel(title, "No se ha seleccionado un título", "¿Está seguro de que desea eliminar el título?"): return
        # Eliminar el título seleccionado
        self.json_manager.delete_theme(title)
        # Refrescar el combobox de los títulos y mostrar un mensaje de éxito
        self.refresh_cb_title()
        self.title_cb.set("")
        self.subtitle_cb.set("")
        Utility.delete_text_content(self.text_Entry)
        self.refresh_cb_subtitle()
        tkinter.messagebox.showinfo("Información", "Tema eliminado con éxito")

    def delete_subtitle(self) -> None:
        """
        Elimina el subtítulo seleccionado
        """
        # Tomar el subtítulo seleccionado
        subtitle = self.subtitle_cb.get()
        # Si no se ha seleccionado un subtítulo, mostrar un mensaje de error
        if Utility.is_string_not_valid_and_confirm_delete_cancel(subtitle, "No se ha seleccionado un subtítulo", "¿Está seguro de que desea eliminar el subtítulo?"): return
        # Eliminar el subtítulo seleccionado
        self.tema.delete_subtitle(subtitle)
        # Refrescar el combobox de los subtítulos y mostrar un mensaje de éxito
        self.refresh_cb_subtitle()
        self.subtitle_cb.set("")
        Utility.delete_text_content(self.text_Entry)
        tkinter.messagebox.showinfo("Información", "Subtítulo eliminado con éxito")

    def get_input_prompt(self, prompt) -> str:
        """
        Muestra un prompt para obtener un input del usuario
        """
        # Mostrar un prompt para obtener un input del usuario
        return simpledialog.askstring("Input", prompt)

    def refresh_cb_title(self) -> None:
        """
        Refresca el combobox de los títulos
        """
        # Obtener los títulos de los temas
        self.title_cb['values'] = self.json_manager.get_all_titles()

    def refresh_cb_subtitle(self) -> None:
        """
        Refresca el combobox de los subtítulos
        """
        # Obtener los subtítulos del tema seleccionado
        self.subtitle_cb['values'] = [content["subtitle"] for content in self.tema.content]
    
    def refresh_text_Entry(self) -> None:
        """
        Refresca el text_Entry con el contenido del subtítulo seleccionado
        """
        # Obtener el contenido del subtítulo seleccionado
        subtitle = self.subtitle_cb.get()
        text = self.tema.get_text(subtitle)
        # Eliminar el contenido actual del text_Entry y añadir el nuevo contenido
        Utility.delete_text_content(self.text_Entry)
        self.text_Entry.config(state="normal")
        self.text_Entry.insert(tkinter.END, text)
        self.text_Entry.config(state="disabled")

    def set_tema(self) -> None:
        """
        Establece el tema seleccionado en la interfaz
        """
        # Obtener el tema seleccionado
        title = self.title_cb.get()
        theme = self.json_manager.get_theme(title)
        # Si no se ha encontrado el tema, mostrar un mensaje de error
        if theme == None:
            tkinter.messagebox.showerror("Error", "No se ha encontrado el tema")
            return
        # Establecer el tema en la interfaz
        self.tema.title = theme["title"]
        self.tema.content = theme["content"]
        # Refrescar el combobox de los subtítulos y poner el foco en el combobox de los subtítulos
        self.refresh_cb_subtitle()
        self.subtitle_cb.focus()

if "__main__" == __name__:
    app = MyApplication()
    app.window.mainloop()
    
