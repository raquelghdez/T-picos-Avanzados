"""
Práctica 2
Manejo de Eventos en la Interfaz
Tópicos Avanzado 4SS
Raquel Garibaldo Hernández
"""

import tkinter as tk

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        """ La línea self.master = master guarda la referencia a la
        ventana principal (que se pasa como argumento master) dentro de la
        clase App. Esto permite que otras partes del programa, dentro de la
        clase App, puedan usar y hacer cambios en la ventana principal. """
        
        self.master = master
        
        # Bind: para declarar lo eventos del mouse y teclado 
        self.master.bind('<Button-1>', self.mouse_click)
        self.master.bind('<Motion>', self.mouse_motion)
        self.master.bind('<Double-1>', self.double_click)
        self.master.bind('<space>', self.clear_label)
        self.master.bind('<Key>', self.key_press)

        # Crea una etiqueta para mostrar los eventos capturados
        self.label = tk.Label(self, text="Eventos del mouse y teclado aparecerán aquí", font=("Helvetica", 12))
        self.label.pack(pady=20)

        self.entrythingy = tk.Entry(self, font=("Helvetica", 12))
        self.entrythingy.pack(pady=20)

        # Crea un cuadro de entrada
        self.contents = tk.StringVar()
        self.contents.set("Está es una variable: ")
        self.entrythingy["textvariable"] = self.contents

        # Botón para cerrar la aplicación 
        self.close_button = tk.Button(self, text="Cerrar ventana", bg="ivory3", command=self.close_window)
        self.close_button.pack(pady=20)

        # Definir los movientos del mouse 
    def mouse_click(self, event):
        self.label.config(text=f"Clic del mouse en: ({event.x}, {event.y})")

    def mouse_motion(self, event):
        self.label.config(text=f"Movimiento del mouse en ({event.x}, {event.y})")

    def double_click(self, event):
        self.master.config(bg="orchid1")
        self.label.config(text="Doble clic detectado, color cambiado a orquidia")

    def clear_label(self, event):
        self.label.config(text="Eventos del mouse y teclado aparecerán aquí")

    def key_press(self, event):
        self.label.config(text=f"Tecla presionada: {event.keysym}")

    def close_window(self):
        self.master.destroy()

# Ventana principal
root = tk.Tk()
root.geometry("600x200")
root.title("Ejercio 2. Clasificación de bases de datos")

app = App(root)
app.mainloop()
