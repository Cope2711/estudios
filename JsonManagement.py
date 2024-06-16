import json
from typing import List, Dict

class MyJsonManagementClass:
    def __init__(self):
        # Se define el nombre del archivo json
        self.json_file = 'Temas.json'

    def read_json(self) -> List[Dict]:
        """
        Lee los datos del archivo json
        Returns:
            List[Dict]: Los datos del archivo json
        """
        # Se lee el archivo json
        with open(self.json_file, 'r') as file:
            return json.load(file)
        
    def save_json(self, data: List[Dict]):
        """
        Guarda los datos en el archivo json
        Args:
            data (List[Dict]): Los datos a guardar
        """
        # Se guardan los datos en el archivo json
        with open(self.json_file, 'w') as file:
            json.dump(data, file, indent=4)
    
    def add_theme(self, title: str, content: List[Dict[str, str]]) -> bool:
        """
        Agrega un nuevo tema
        Args:
            title (str): El título del tema
            content (List[Dict[str, str]]): El contenido del tema
        Returns:
            bool: True si se agregó el tema, False si no se agregó
        """
        # Se leen los datos del archivo json
        data = self.read_json()
        # Se comprueba si ya existe un tema con ese título
        if self.get_theme(title) != None:
            print("Error al agregar el tema, ya existe un tema con ese título")
            return False
        # Se agrega el nuevo tema
        data.append({"title": title, "content": content})
        # Se guardan los datos en el archivo json
        self.save_json(data)
        return True
    
    def update_theme_content(self, title: str, content: List[Dict[str, str]]) -> bool:
        """
        Actualiza el contenido de un tema
        Args:
            title (str): El título del tema
            content (List[Dict[str, str]]): El contenido del tema
        Returns:
            bool: True si se actualizó el contenido, False si no se actualizó
        """
        # Se leen los datos del archivo json
        data = self.read_json()
        # Se comprueba si existe un tema con ese título
        if self.get_theme(title) == None:
            print("Error al actualizar el tema, no existe un tema con ese título")
            return False
        # Se actualiza el contenido del tema
        for theme in data:
            # Se busca el tema con el título indicado
            if theme["title"] == title:
                theme["content"] = content
                # Se guardan los datos en el archivo json
                self.save_json(data)
                return True
    
    def get_theme(self, title: str) -> Dict:
        """
        Retorna un tema y su contenido
        Args:
            title (str): El título del tema
        Returns:
            Dict: El tema y su contenido
        """
        # Se leen los datos del archivo json
        data = self.read_json()
        # Se busca el tema con el título indicado
        for theme in data:
            # Se retorna el tema si se encuentra
            if theme["title"] == title:
                return theme
        # Se retorna None si no se encuentra el tema
        return None
    
    def get_all_themes(self) -> List[Dict]:
        """
        Retorna una lista con todos los temas y su contenido
        Returns:
            List[Dict]: Lista con todos los temas y su contenido
        """
        # Se leen los datos del archivo json
        return self.read_json()
    
    def get_all_titles(self) -> List[str]:
        """
        Retorna una lista con los títulos de los temas
        Returns:
            List[str]: Lista con los títulos de los temas
        """
        # Se leen los datos del archivo json
        data = self.read_json()
        # Se retorna una lista con los títulos de los temas
        return [theme["title"] for theme in data]
    
    def delete_theme(self, title) -> bool:
        """
        Elimina un tema
        Args:
            title ([type]): El título del tema
        Returns:
            bool: True si se eliminó el tema, False si no se eliminó
        """
        # Se leen los datos del archivo json
        data = self.read_json()
        # Se busca el tema con el título indicado
        for theme in data:
            # Se elimina el tema si se encuentra
            if theme["title"] == title:
                data.remove(theme)
                # Se guardan los datos en el archivo json
                self.save_json(data)
                return True
        return False

   

if "__main__" == __name__: 
    print("This is a class for the management of the json file")
