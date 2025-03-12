"""
Práctica 5
Librería de manipulación de archivos
Tópicos Avanzado 4SS
Raquel Garibaldo Hernández
11 de marzo de 2025

Se adelantó esta práctica en esta Práctica 4
"""

import tkinter as tk

# Para cambiar el color del texto
from tkinter import colorchooser 
# Devuelve una cadena y esa cadena es la ruta del archivo donde se encuentra nuestro archivo
from tkinter import filedialog   
# (Themed Tkinter widgets) Para agregar botones, etiquetas u otros elementos   
from tkinter import ttk             

# Variable global para recordar el archivo actual
current_file = None  

# Función para crear un Nuevo archivo
def new_file():
    global texto, current_file  
    texto.delete("1.0", tk.END)  
    root.title("New File")
    current_file = None  # Se borra la referencia al archivo actual

# Función para abrir un archivo
def openFile():
    global current_file
    filepath = filedialog.askopenfilename(initialdir="C:\\ITE\\4° SEMESTRE\\TOPICOS AVANZADOS DE PROGRAMACION",
                                          title="Open File", 
                                          filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))                                                      
    if filepath:
        with open(filepath, 'r') as file:
            texto.delete("1.0", tk.END)
            texto.insert("1.0", file.read())
        root.title(filepath)
        current_file = filepath  # Guarda la ruta del archivo abierto

# Función para Guardar el archivo (si ya tiene un nombre)
def save_file():
    global current_file
    if current_file:
        with open(current_file, 'w') as file:
            file.write(texto.get("1.0", tk.END))  
        root.title(current_file)  # Actualiza el título con el nombre del archivo
    else:
        save_as()  # Si no hay archivo, llama a "Guardar como..."

# Función para "Guardar Como" un nuevo archivo
def save_as():
    global current_file
    text_file = filedialog.asksaveasfilename(defaultextension=".txt",
                                             initialdir="C:\\ITE\\4° SEMESTRE\\TOPICOS AVANZADOS DE PROGRAMACION",
                                             title="Save File", 
                                             filetypes=[("Text Files", "*.txt"), 
                                                        ("HTML Files", "*.html"),
                                                        ("Python Files", "*.py"),
                                                        ("All Files", "*.*")])
    if text_file:
        with open(text_file, 'w') as file:
            file.write(texto.get("1.0", tk.END))
        root.title(text_file)       # Actualiza el título con la ruta del archivo
        current_file = text_file    # Guarda la nueva ruta del archivo

# Cambiar el Color del texto
def changeColor():
    color = colorchooser.askcolor()[1]
    if color:
        texto.config(fg=color)

# Borrar todo el texto
def deleteText():
    texto.delete("1.0", tk.END)

# Crear la ventana de "Buscar y Reemplazar"
def findReplaceDialog():
    find_replace_win = tk.Toplevel(root)
    find_replace_win.title("Find and Replace")
    find_replace_win.geometry("250x100")
    
    tk.Label(find_replace_win, text="Find:").grid(row=0, column=0, padx=5, pady=5)
    find_entry = tk.Entry(find_replace_win, width=25)
    find_entry.grid(row=0, column=1, padx=5, pady=5)
    
    tk.Label(find_replace_win, text="Replace:").grid(row=1, column=0, padx=5, pady=5)
    replace_entry = tk.Entry(find_replace_win, width=25)
    replace_entry.grid(row=1, column=1, padx=5, pady=5)
 
    # Función para Reemplazar
    def replace():
        find_text = find_entry.get()
        replace_text = replace_entry.get()
        content = texto.get("1.0", tk.END)
        new_content = content.replace(find_text, replace_text)
        texto.delete("1.0", tk.END)
        texto.insert("1.0", new_content)
    
    tk.Button(find_replace_win, text="Replace", command=replace).grid(row=3, column=1, sticky='w', padx=5, pady=5) 

# Configuración de la ventana principal
root = tk.Tk()
root.title("Text Editor")

# CREAR EL MENÚ
opcmenu = tk.Menu(root)
filemenu = tk.Menu(opcmenu, tearoff=0)
filemenu.add_command(label="New", accelerator="Ctrl+n", command=new_file)
filemenu.add_command(label="Open", accelerator="Ctrl+o", command=openFile)
filemenu.add_command(label="Delete text", accelerator="Ctrl+d", command=deleteText)
filemenu.add_command(label="Save", accelerator="Ctrl+s", command=save_file)  
filemenu.add_command(label="Save as", accelerator="Ctrl+Shift+s", command=save_as)  
filemenu.add_separator()
filemenu.add_command(label="Exit", accelerator="Ctrl+e", command=root.quit)
opcmenu.add_cascade(menu=filemenu, label="File")

# Menú Text Color para cambiar el color del texto
colormenu = tk.Menu(opcmenu, tearoff=0)
colormenu.add_command(label="Change Text Color", command=changeColor)
opcmenu.add_cascade(menu=colormenu, label="Text Color")

# Menú Editar para Buscar y Reemplazar 
editmenu = tk.Menu(opcmenu, tearoff=0)
editmenu.add_command(label="Find and Replace", command=findReplaceDialog)
opcmenu.add_cascade(menu=editmenu, label="Edit")

# Área de texto
texto = tk.Text(root)
texto.pack(fill="both", expand=1)
texto.config(bd=0, padx=6, pady=4, font=("Consolas", 12))

root.config(menu=opcmenu)

# Para darle funcionalidad a los atajos (bind y lambda)
root.bind("<Control-n>", lambda event: new_file())
root.bind("<Control-o>", lambda event: openFile())
root.bind("<Control-s>", lambda event: save_file())
root.bind("<Control-Shift-s>", lambda event: save_as())
root.bind("<Control-d>", lambda event: deleteText())
root.bind("<Control-e>", lambda event: root.quit())

root.mainloop()