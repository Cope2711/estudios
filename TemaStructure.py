class MyTemaStructureClass:
    def __init__(self, title: str, content: dict):
        # Se define el título del tema
        self.title = title
        # Se define el contenido del tema
        self.content = content

    def __init__(self):
        # Se define el título del tema
        self.title = ""
        # Se define el contenido del tema
        self.content = []

    def add_subtitle(self, subtitle, text) -> bool:
        """
        Agrega una nueva sección al tema
        Args:
            subtitle (str): El subtítulo de la sección
            text (str): El texto de la sección
        Returns:
            bool: True si se agregó la sección, False si no se agregó
        """
        # Se comprueba si ya existe una sección con ese subtítulo
        if subtitle in self.get_subtitles():
            print("Error al agregar la sección, ya existe una sección con ese título")
            return False
        # Se agrega la nueva sección
        self.content.append({"subtitle": subtitle, "text": text})
        return True

    def update_subtitle_content(self, subtitle, text) -> bool:
        """
        Actualiza el texto de una sección
        Args:
            subtitle (str): El subtítulo de la sección
            text (str): El nuevo texto
        Returns:
            bool: True si se actualizó el texto, False si no se actualizó
        """
        # Se comprueba si existe una sección con ese subtítulo
        if subtitle not in self.get_subtitles():
            print("Error al actualizar la sección, no existe una sección con ese título")
            return False
        # Se actualiza el texto de la sección
        for section in self.content:
            # Se busca la sección con el subtítulo indicado
            if section["subtitle"] == subtitle:
                # Se actualiza el texto de la sección
                section["text"] = text
                return True
    
    def update_subtitle_name(self, subtitle, new_subtitle) -> bool:
        """
        Actualiza el subtítulo de una sección
        Args:
            subtitle (str): El subtítulo de la sección
            new_subtitle (str): El nuevo subtítulo
        Returns:
            bool: True si se actualizó el subtítulo, False si no se actualizó
        """
        # Se comprueba si existe una sección con ese subtítulo
        if subtitle not in self.get_subtitles():
            print("Error al actualizar la sección, no existe una sección con ese título")
            return False
        # Se comprueba si ya existe una sección con el nuevo subtítulo
        if new_subtitle in self.get_subtitles():
            print("Error al actualizar la sección, ya existe una sección con ese título")
            return False
        # Se actualiza el subtítulo de la sección
        for section in self.content:
            # Se busca la sección con el subtítulo indicado
            if section["subtitle"] == subtitle:
                # Se actualiza el subtítulo de la sección
                section["subtitle"] = new_subtitle
                return True

    def delete_subtitle(self, subtitle) -> bool:
        """
        Elimina una sección con el subtítulo dado
        Args:
            subtitle (str): El subtítulo de la sección
        Returns:
            bool: True si se eliminó la sección, False si no se eliminó
        """
        # Se comprueba si existe una sección con ese subtítulo
        if subtitle not in self.get_subtitles():
            print("Eror al borrar la sección, no existe una sección con ese título")
            return False
        # Se elimina la sección
        for section in self.content:
            # Se busca la sección con el subtítulo indicado
            if section["subtitle"] == subtitle:
                # Se elimina la sección
                self.content.remove(section)
                return True
    
    def get_subtitles(self) -> list[str]:
        """
        Retorna una lista con los subtítulos de las secciones
        Returns:
            List[str]: Una lista con los subtítulos de las secciones
        """
        # Se retorna una lista con los subtítulos de las secciones
        if len(self.content) == 0:
            return []
        return [section["subtitle"] for section in self.content]
    
    
    def get_text(self, subtitle) -> str:
        """
        Retorna el texto de la sección con el subtítulo dado
        Args:
            subtitle (str): El subtítulo de la sección
        Returns:
            str: El texto de la sección
        """
        # Se busca la sección con el subtítulo indicado
        for section in self.content:
            if section["subtitle"] == subtitle:
                return section["text"]
        return None


if "__main__" == __name__:
    print("This is a class for the structure of a Tema")

    



    


    


if "__main__" == __name__:
    print("This is a class for the structure of a Tema")
