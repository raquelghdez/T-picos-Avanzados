"""
Práctica 4
Editor de Texto Simple
Tópicos Avanzado 4SS
Raquel Garibaldo Hernández
"""

import tkinter as tk
from tkinter import colorchooser, simpledialog  # Se agregó simpledialog para Buscar y Reemplazar

def openFile():
    print("Open File")

def changeColor():
    color = colorchooser.askcolor()[1]
    if color:
        texto.config(fg=color)

def deleteText():
    """Función para borrar todo el texto."""
    texto.delete("1.0", tk.END)

def findReplace():
    """Función para buscar y reemplazar texto."""
    buscar = simpledialog.askstring("Buscar", "Texto a buscar:")
    reemplazar = simpledialog.askstring("Reemplazar", "Texto de reemplazo:")
    if buscar and reemplazar:
        contenido = texto.get("1.0", tk.END)
        nuevo_contenido = contenido.replace(buscar, reemplazar)
        texto.delete("1.0", tk.END)
        texto.insert("1.0", nuevo_contenido)

root = tk.Tk()
root.title("Text Editor")

# Crear el Menú
opcmenu = tk.Menu(root)
filemenu = tk.Menu(opcmenu, tearoff=0)

# Opciones del Menú Archivo
filemenu.add_command(label="New", accelerator="Ctrl+N")
filemenu.add_command(label="Open", accelerator="Ctrl+O", command=openFile)
filemenu.add_command(label="Delete text", accelerator="Ctrl+D", command=deleteText)  # Se agregó el comando deleteText
filemenu.add_command(label="Save", accelerator="Ctrl+S")
filemenu.add_command(label="Save as", accelerator="Ctrl+Shift+S")
filemenu.add_separator()
filemenu.add_command(label="Exit", accelerator="Ctrl+E", command=root.quit)
opcmenu.add_cascade(menu=filemenu, label="File")

# Menú Formato
colormenu = tk.Menu(opcmenu, tearoff=0)
colormenu.add_command(label="Change Text Color", command=changeColor)
opcmenu.add_cascade(menu=colormenu, label="Format")

# Menú Editar (Buscar y Reemplazar agregado)
editmenu = tk.Menu(opcmenu, tearoff=0)
editmenu.add_command(label="Find and Replace", command=findReplace)  # Se unificó en una sola opción con funcionalidad
opcmenu.add_cascade(menu=editmenu, label="Edit")

# Vincular atajos de teclado
root.bind("<Control-o>", lambda event: openFile())
root.bind("<Control-d>", lambda event: deleteText())  # Se agregó atajo para borrar texto

# Área de texto
texto = tk.Text(root)
texto.pack(fill="both", expand=1)
texto.config(bd=0, padx=6, pady=4, font=("Consolas", 12))

root.config(menu=opcmenu)
root.mainloop()
