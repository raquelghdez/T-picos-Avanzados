"""
Práctica 6
Pantalla de inicio de proyecto
Tópicos Avanzado 4SS
Raquel Garibaldo Hernández

"""

from tkinter import Tk
import tkinter as tk
# (Themed Tkinter widgets) Para agregar botones, etiquetas u otros elementos   
from tkinter import ttk  

class Aplication(Tk):
    def __init__(self):
        super().__init__()
        self.initialize_gui()

    # Se agregó la función Enter para que se cierre la ventana
        self.bind('<Return>', self.close_window)

    def initialize_gui(self):
        self.title('MENU GENERAL DEL SISTEMA')
        self.attributes('-fullscreen', True)
        self.configure(bg='#8FB3C9')            # Color de la pantalla

        # Título del Menú
        title_label = tk.Label(self, text="MENU GENERAL DEL SISTEMA", font=("Helvetica", 16), bg='#8FB3C9')
        title_label.pack(pady=20)            # Espacio para el título
        
        # Opciones del Menú con botones
        consulta_botton = tk.Button(self, text="Consulta de Documentos",
                                    font=("Helvetica", 14), bg='#D9EAF3')
        consulta_botton.pack(pady=10)                               # Espacio entre botones

        alta_usuario_botton = tk.Button(self, text="Alta de Usuario",
                                    font=("Helvetica", 14), bg='#D9EAF3')
        alta_usuario_botton.pack(pady=10)                               # Espacio entre botones

        alta_docto_botton = tk.Button(self, text="Alta de Documento",
                                    font=("Helvetica", 14), bg='#D9EAF3')
        alta_docto_botton.pack(pady=10)                               # Espacio entre botones
    
        salir_botton = tk.Button(self, text="Salir del Sistema",
                                    font=("Helvetica", 14), bg='#D9EAF3', command=self.close_window)
        salir_botton.pack(pady=10)                               # Espacio entre botones
  

    # Método para cerrar la ventana
    def close_window(self, event=None):
        self.destroy()

def main():
    app = Aplication()
    app.mainloop()

if __name__ == '__main__':
    main()
