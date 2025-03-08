"""
Práctica 4
Editor de Texto Simple
Tópicos Avanzado 4SS
Raquel Garibaldo Hernández
"""

import tkinter as tk
from tkinter import colorchooser # Módulo para activar al geenrardor de colores y poder elegir el color
                                 
root = tk.Tk()
root.title("Text Editor ")

def openFile():
    print("Open File")

def changeColor():
    color = colorchooser.askcolor()[1]
    if color:
        texto.config(fg=color)

# Crear el Menú, tk.Menu
opcmenu = tk.Menu(root)
# tearoff elimina el Index 0, que hace que el Menú aparezca en una ventana adicional
filemenu = tk.Menu(opcmenu, tearoff=0)

"""
Crear las opciones del Menú
Hace que una opción realizce una actividad add.command
Crear atajos con accelerator """
filemenu.add_command(label="New", accelerator="Ctrl+N")
filemenu.add_command(label="Open", accelerator="Ctrl+O", command=openFile)
filemenu.add_command(label="Delete text", accelerator="Ctrl+D")
filemenu.add_command(label="Save", accelerator="Ctrl+S")
filemenu.add_command(label="Save as", accelerator="Ctrl+Shift+S")

# Para marcar las opciones con un separador, se usa add_separator 
# y se marcará una línea de separación en el Menú
filemenu.add_separator()

# quit Es para que opción Exit salga del Menú
filemenu.add_command(label="Exit", accelerator="Ctrl+E", command= root.quit)  

# add_cascade Hace que el Menú aparezca en cascada
opcmenu.add_cascade(menu=filemenu, label="File")

# Agregar otra categoría al Menú con una opción para cambiar el color del texto
# Se escribe el texto y se subraya para poder cambiar el color
colormenu = tk.Menu(opcmenu, tearoff=0)
colormenu.add_command(label="Change Text Color", command=changeColor)
opcmenu.add_cascade(menu=colormenu, label="Format")

# Menú Buscar y Reemplazar
editmenu = tk.Menu(editmenu, tearoff=0)
editmenu.add_command(label="Find")
editmenu.add_command(label="Replace")
editmenu.add_cascade(menu=editmenu, label="Edit")


# lamda Llama al evento para que se ejecute lo que se indicó en la función
root.bind("<Control-O>", lambda event:openFile())

# Para poder escribir el editor
texto = tk.Text(root)
texto.pack(fill="both", expand=1)
texto.config(bd=0, padx=6, pady=4, font=("Consolas", 12))

root.config(menu=opcmenu)
root.mainloop()

