"""
Práctica 3
Creación de un Formulario con Validaciones
Tópicos Avanzado 4SS
Raquel Garibaldo Hernández
"""

import tkinter as tk
from tkinter import messagebox


    # Mostrar el nombre que se ingrese al presionar el botón
    def show_message():
        message= entry.get()
        messagebox.showinfo("Mensaje", message)


    # Cerrar ventana
    def close_window():
        mywindow.destroy()
    
    # Crea la ventana
    mywindow = tk.Tk()

    # Tamaño y color de la ventana
    mywindow.title("Ejercicio Práctico 1")
    mywindow.geometry("600x300")
    mywindow.config(bg= "medium orchid")


    # Etiqueta
    label = tk.Label(mywindow, text="Bienvenidos al curso\nTópicos Avanzados de Programación",
                     fg="black", bg="medium orchid", font= "italic 10 bold")
    label.pack()

    # Ingresar información
    label2 = tk.Label(mywindow, text="Ingrese información", fg="black", bg="medium orchid")
    label2.pack()
    entry = tk.Entry(mywindow)
    entry.pack()

    show_message = tk.Button(mywindow, text="Mostrar Mensaje", fg="purple", bg="pale violet red", command=show_message)
    show_message.pack()
    
    close_button = tk.Button(mywindow, text="Cerrar Aplicación", fg="purple", bg="pale violet red", command=close_window)
    close_button.pack()

# Preventing closing using mainloop.method()
mywindow.mainloop()

