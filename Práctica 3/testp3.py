import tkinter as tk
from tkinter import messagebox
import re  # Para validar el correo
from tkinter import ttk  # Importar ttk para usar Combobox

# Función para cerrar la ventana
def close_window():
    mywindow.destroy()

# Función para enviar el formulario
def enviar():
    nombre = entrada_nombre.get().strip()
    correo = entrada_correo.get().strip()
    edad = entrada_edad.get().strip()
    escolaridad = entrada_escolaridad.get().strip()  # Aquí se usa entrada_escolaridad en lugar de variable_escolaridad
    
    # Validar que el nombre no esté vacío
    if not nombre:
        messagebox.showerror("Error", "El nombre no puede estar vacío.")
        return
    
    # Validar que el correo tenga un formato válido
    if not re.match(r"[^@]+@[^@]+\.[^@]+", correo):
        messagebox.showerror("Error", "El correo electrónico no es válido.")
        return
    
    # Validar que la edad sea un número
    if not edad.isdigit():
        messagebox.showerror("Error", "La edad debe ser un número.")
        return
    
    # Validar que la escolaridad esté seleccionada
    if not escolaridad:
        messagebox.showerror("Error", "La escolaridad no puede estar vacía.")
        return
    
    # Si todas las validaciones pasan
    messagebox.showinfo("Formulario Enviado", f"Nombre: {nombre}\nCorreo: {correo}\nEdad: {edad}\nEscolaridad: {escolaridad}")

# Función para limpiar el formulario
def limpiar():
    entrada_nombre.delete(0, tk.END)
    entrada_correo.delete(0, tk.END)
    entrada_edad.delete(0, tk.END)
    entrada_escolaridad.set("")

# Crear la ventana
mywindow = tk.Tk()

# Tamaño y color de la ventana
mywindow.title("Ejercicio Práctico 3")
mywindow.geometry("400x300")
mywindow.config(bg="ivory3")

# Etiqueta principal
label1 = tk.Label(mywindow, text="FORMULARIO DE DATOS", bg="ivory3")
label1.grid(row=1, column=1, columnspan=2, pady=10)

# Nombre
label2 = tk.Label(mywindow, text="Nombre:", bg="ivory3")
label2.grid(row=2, column=1, padx=20, pady=10, sticky="e")
entrada_nombre = tk.Entry(mywindow, width=40)
entrada_nombre.grid(row=2, column=2, padx=20, pady=10, sticky="w")

# Correo
label3 = tk.Label(mywindow, text="Correo:", bg="ivory3")
label3.grid(row=3, column=1, padx=20, pady=10, sticky="e")
entrada_correo = tk.Entry(mywindow, width=40)
entrada_correo.grid(row=3, column=2, padx=20, pady=10, sticky="w")

# Edad
label4 = tk.Label(mywindow, text="Edad:", bg="ivory3")
label4.grid(row=4, column=1, padx=20, pady=10, sticky="e")
entrada_edad = tk.Entry(mywindow, width=10)
entrada_edad.grid(row=4, column=2, padx=20, pady=10, sticky="w")

# Escolaridad máxima
label5 = tk.Label(mywindow, text="Escolaridad\nmáxima:", bg="ivory3")
label5.grid(row=5, column=1, padx=20, pady=10, sticky="e")
opciones_escolaridad = ["Primaria", "Secundaria", "Preparatoria", "Licenciatura", "Posgrado"]
variable_escolaridad = tk.StringVar(mywindow)
entrada_escolaridad = ttk.Combobox(mywindow, textvariable=variable_escolaridad, values=opciones_escolaridad, state="readonly")
entrada_escolaridad.set("")  # Valor por defecto
entrada_escolaridad.grid(row=5, column=2, padx=20, pady=10, sticky="w")

# Botón para enviar el formulario
enviar_button = tk.Button(mywindow, text="Enviar", bg="ivory4", command=enviar)
enviar_button.place(x=50, y=250)

# Botón para limpiar el formulario
limpiar_button = tk.Button(mywindow, text="Limpiar", bg="ivory4", command=limpiar)
limpiar_button.grid(row=8, column=2, padx=20, pady=10)
limpiar_button.place(x=150, y=250)

# Botón para cerrar la aplicación
close_button = tk.Button(mywindow, text="Cerrar Aplicación", bg="ivory4", command=close_window)
close_button.place(x=270, y=250)

mywindow.mainloop()