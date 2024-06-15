class MyTemaStructureClass:
    def __init__(self, title: str, content: dict):
        self.title = title
        self.content = content

    def __init__(self):
        self.title = ""
        self.content = []

    def add_subtitle(self, subtitle, text):
        if subtitle in self.get_subtitles():
            print("Error al agregar la sección, ya existe una sección con ese título")
            return False
        self.content.append({"subtitle": subtitle, "text": text})
        return True

    def update_subtitle_content(self, subtitle, text):
        if subtitle not in self.get_subtitles():
            print("Error al actualizar la sección, no existe una sección con ese título")
            return False
        for section in self.content:
            if section["subtitle"] == subtitle:
                section["text"] = text
                return True
    
    def update_subtitle_name(self, subtitle, new_subtitle):
        if subtitle not in self.get_subtitles():
            print("Error al actualizar la sección, no existe una sección con ese título")
            return False
        if new_subtitle in self.get_subtitles():
            print("Error al actualizar la sección, ya existe una sección con ese título")
            return False
        for section in self.content:
            if section["subtitle"] == subtitle:
                section["subtitle"] = new_subtitle
                return True

    def delete_subtitle(self, subtitle) -> bool:
        if subtitle not in self.get_subtitles():
            print("Eror al borrar la sección, no existe una sección con ese título")
            return False
        for section in self.content:
            if section["subtitle"] == subtitle:
                self.content.remove(section)
                return True
    
    def get_subtitles(self):
        if len(self.content) == 0:
            return []
        return [section["subtitle"] for section in self.content]
    
    def get_text(self, subtitle):
        for section in self.content:
            if section["subtitle"] == subtitle:
                return section["text"]
        return None


if "__main__" == __name__:
    print("This is a class for the structure of a Tema")

    



    


    


if "__main__" == __name__:
    print("This is a class for the structure of a Tema")
