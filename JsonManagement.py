import json
from typing import List, Dict

class MyJsonManagementClass:
    def __init__(self):
        self.json_file = 'Temas.json'

    def read_json(self) -> List[Dict]:
        with open(self.json_file, 'r') as file:
            return json.load(file)
        
    def save_json(self, data: List[Dict]):
        with open(self.json_file, 'w') as file:
            json.dump(data, file, indent=4)
    
    def add_theme(self, title: str, content: List[Dict[str, str]]):
        data = self.read_json()
        print(title)
        if self.get_theme(title) != None:
            print("Error al agregar el tema, ya existe un tema con ese título")
            return False
        data.append({"title": title, "content": content})
        self.save_json(data)
        return True
    
    def update_theme_content(self, title: str, content: List[Dict[str, str]]):
        data = self.read_json()
        if self.get_theme(title) == None:
            print("Error al actualizar el tema, no existe un tema con ese título")
            return False
        for theme in data:
            if theme["title"] == title:
                theme["content"] = content
                self.save_json(data)
                return True
    
    def get_theme(self, title: str) -> Dict:
        data = self.read_json()
        for theme in data:
            if theme["title"] == title:
                return theme
        return None
    
    def get_all_themes(self) -> List[Dict]:
        return self.read_json()
   

if "__main__" == __name__: 
    print("This is a class for the management of the json file")
