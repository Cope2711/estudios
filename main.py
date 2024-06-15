import tkinter.messagebox
from TemaStructure import MyTemaStructureClass
from JsonManagement import MyJsonManagementClass
from Autocomplete import MyAutocompleteClass
import tkinter
import random

class MyApplication:
    def __init__(self):
        # Crear la ventana principal
        self.window = tkinter.Tk()
        self.window.title("Temas")
        self.window.geometry("800x800")

        # Crear los objetos de las clases MyTemaStructureClass y MyJsonManagementClass
        self.tema = MyTemaStructureClass()
        self.json_manager = MyJsonManagementClass()

        # Crear el entry para el título del tema, su label y el botón para obtener un título aleatorio
        self.title_Entry_label = tkinter.Label(self.window, text="Título del tema")
        self.title_Entry_label.grid(row=0, column=0, padx=10)

        self.title_Entry = tkinter.Entry(self.window)
        self.title_Entry.grid(row=1, column=0, padx=10)
        
        MyAutocompleteClass(self.title_Entry, self.get_all_titles())

        self.get_random_title_button = tkinter.Button(self.window, text="Obtener un título aleatorio", command=self.get_random_title)
        self.get_random_title_button.grid(row=1, column=1)

        # Crear el entry para el subtítulo, su label y el botón para obtener un subtítulo aleatorio
        self.subtitle_Entry_label = tkinter.Label(self.window, text="Subtítulo")
        self.subtitle_Entry_label.grid(row=2, column=0, padx=10)

        self.subtitle_Entry = tkinter.Entry(self.window, width=30)
        self.subtitle_Entry.grid(row=3, column=0, padx=10)

        self.get_random_subtitle_button = tkinter.Button(self.window, text="Obtener un subtítulo aleatorio", command=self.get_random_subtitle_button)
        self.get_random_subtitle_button.grid(row=3, column=1)

        # Crear el entry para el texto del subtítulo y su label
        self.text_Entry_label = tkinter.Label(self.window, text="Texto")
        self.text_Entry_label.grid(row=4, column=0, padx=10)

        self.text_Entry = tkinter.Text(self.window, width=50, height=30)
        self.text_Entry.grid(row=5, column=0, padx=10)

        self.show_text_button = tkinter.Button(self.window, text="Mostrar texto", command=self.show_text)
        self.show_text_button.grid(row=5, column=1)

    def get_random_title(self):
        # Obtener todos los temas
        themes = self.json_manager.get_all_themes()
        # Obtener la cantidad de temas
        len_themes = len(themes)
        # Si no hay temas, mostrar un mensaje de error
        if len_themes == 0: 
            tkinter.messagebox.showerror("Error", "No hay temas en el archivo") 
            return
        # Obtener un tema aleatorio
        random_theme = themes[random.randint(0, len_themes - 1)]
        # Asignar el título del tema aleatorio al objeto de la clase MyTemaStructureClass
        self.tema.title = random_theme["title"]
        # Asignar el título del tema aleatorio al entry
        self.title_Entry.delete(0, tkinter.END) 
        self.title_Entry.insert(0, self.tema.title)

    def get_random_subtitle_button(self):
        # Si no hay un tema seleccionado, mostrar un mensaje de error
        if self.title_Entry.get() == "":
            tkinter.messagebox.showerror("Error", "No hay un tema seleccionado")
            return
        # Asignar el título y el content del tema por si se introdujo a mano o si cambió
        theme = self.json_manager.get_theme(self.title_Entry.get())
        self.tema.title = theme["title"]
        self.tema.content = theme["content"]
        # Obtener los subtítulos del tema seleccionado
        subtitles = self.tema.get_subtitles()
        # Obtener la cantidad de subtítulos
        len_subtitles = len(subtitles)
        # Si no hay subtítulos, mostrar un mensaje de error
        if len_subtitles == 0:
            tkinter.messagebox.showerror("Error", "No hay subtítulos en el tema seleccionado")
            return
        # Obtener un subtítulo aleatorio
        random_subtitle = subtitles[random.randint(0, len_subtitles - 1)]
        # Asignar el subtítulo aleatorio al entry
        self.subtitle_Entry.delete(0, tkinter.END)
        self.subtitle_Entry.insert(0, random_subtitle)

    def show_text(self):
        # Si no hay un tema seleccionado, mostrar un mensaje de error
        if self.tema.title == "":
            tkinter.messagebox.showerror("Error", "No hay un tema seleccionado")
            return
        # Si no hay un subtítulo seleccionado, mostrar un mensaje de error
        if self.subtitle_Entry.get() == "":
            tkinter.messagebox.showerror("Error", "No hay un subtítulo seleccionado")
            return
        # Obtener el texto del subtítulo seleccionado
        text = self.tema.get_text(self.subtitle_Entry.get())
        # Si no hay texto, mostrar un mensaje de error
        if text == None:
            tkinter.messagebox.showerror("Error", "No hay texto en el subtítulo seleccionado")
            return
        # Mostrar el texto en el entry
        self.text_Entry.delete(1.0, tkinter.END)
        self.text_Entry.insert(tkinter.END, text)

    def get_all_titles(self):
        return [theme["title"] for theme in self.json_manager.get_all_themes()]

if "__main__" == __name__:
    app = MyApplication()
    app.window.mainloop()
    