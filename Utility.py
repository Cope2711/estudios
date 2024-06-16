import tkinter.messagebox

def is_string_not_valid(string: str, error_message: str) -> bool:
    """
    Comprueba si un string es válido comparándolo con una cadena vacía o None
    Args:
        string (str): El string a comprobar
        error_message (str): El mensaje de error a mostrar
    Returns:
        bool: True si el string no es válido, False si es válido
    """
    # Comprobar si el string es una cadena vacía o None
    if string == "" or string == None:
        tkinter.messagebox.showerror("Error", error_message)
        return True
    return False

def is_string_not_valid_and_confirm_delete_cancel(string, error_message: str, delete_message: str):
    """
    Comprueba si un string es válido comparándolo con una cadena vacía o None y si el usuario confirma la eliminación
    Args:
        string (str): El string a comprobar
        error_message (str): El mensaje de error a mostrar
        delete_message (str): El mensaje de confirmación de eliminación
    Returns:
        bool: True si el string no es válido o si el usuario cancela la eliminación, False si es válido y el usuario confirma la eliminación
    """
    # Comprobar si el string es una cadena vacía o None
    if is_string_not_valid(string, error_message): return True
    # Comprobar si el usuario confirma la eliminación
    if tkinter.messagebox.askyesno("Eliminar", delete_message) == False: return True
    return False

def delete_text_content(text_widget: tkinter.Text) -> None:
    """
    Elimina el contenido de un widget Text.
    Args:
        text_widget (tk.Text): El widget Text a limpiar.
    Returns:
        None
    """
    # Obtener el estado actual del widget Text
    original_state = text_widget.cget("state")
    # Cambiar temporalmente a estado "normal" si está en estado "readonly" o "disabled"
    if original_state in ("disabled",):
        text_widget.config(state="normal")
    # Eliminar el contenido del widget Text
    text_widget.delete("1.0", tkinter.END)
    # Restaurar el estado original del widget Text si fue cambiado temporalmente
    if original_state in ("disabled",):
        text_widget.config(state=original_state)

