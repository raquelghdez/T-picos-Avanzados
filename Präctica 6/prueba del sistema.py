import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import mysql.connector
import datetime
from pdf2image import convert_from_path  # Importar pdf2image para convertir PDFs en imágenes
import os
from tkinter import filedialog
import sys
import subprocess

# ------------------------- CONEXIÓN A BASE DE DATOS -------------------------
def conectar_bd():
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="rgh23",
            database="sistema_documentos"
        )
    except mysql.connector.Error as err:
        messagebox.showerror("Error de Conexión", f"No se pudo conectar a la base de datos: {err}")
        return None

# ------------------------- PANTALLA DE BIENVENIDA -------------------------
class PantallaBienvenida(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Bienvenido")
        self.attributes('-fullscreen', True)  # Pantalla completa
        self.configure(bg='#78BDB8')  

        # Definir manualmente parámetros de imágenes
        self.logo_params = {"ruta": "C:/ITE/4° SEMESTRE/FUNDAMENTOS DE BASES DE DATOS/IMAGENES/LOGO portada.jpg", 
                            "size": (340, 280), "x": 90, "y": 60}  # Ajusta tamaño y posición
        self.lema_params = {"ruta": "C:/ITE/4° SEMESTRE/FUNDAMENTOS DE BASES DE DATOS/IMAGENES/LEMA.jpg",
                            "size": (310, 200), "x":570, "y": 360}  # Ajusta tamaño y posición

        # Cargar imágenes con parámetros manuales
        self.logo = self.cargar_imagen(self.logo_params["ruta"], self.logo_params["size"])
        self.lema = self.cargar_imagen(self.lema_params["ruta"], self.lema_params["size"])

        # Mostrar imágenes con `place()` para ubicar manualmente
        if self.logo:
            logo_label = tk.Label(self, image=self.logo, bg='#78BDB8')
            logo_label.place(x=self.logo_params["x"], y=self.logo_params["y"])  # Ubicación manual

        if self.lema:
            lema_label = tk.Label(self, image=self.lema, bg='#78BDB8')
            lema_label.place(x=self.lema_params["x"], y=self.lema_params["y"])  # Ubicación manual

        # Botón para continuar al login
        tk.Button(self, text="Ingresar al sistema", font=("Helvetica", 16), bg="#008080", fg="white",
                  command=self.cerrar_pantalla).place(x=155, y=450)  # 🔹 Ajustar posición manualmente

    def cargar_imagen(self, ruta, size):
        """Función para cargar y redimensionar imágenes."""
        try:
            imagen = Image.open(ruta)
            imagen = imagen.resize(size)
            return ImageTk.PhotoImage(imagen)
        except Exception as e:
            print(f"Error al cargar la imagen {ruta}: {e}")
            return None

    def cerrar_pantalla(self):
        """Cerrar la pantalla de bienvenida y abrir el login."""
        self.destroy()
        self.master.mostrar_login()  # Llamar al login después de cerrar bienvenida

# ------------------------- VENTANA DE LOGIN (Pantalla Completa con Imagen de Fondo) -------------------------
class LoginWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Inicio de Sesión")
        self.attributes('-fullscreen', True)  # 🔹 Pantalla completa
        self.configure(bg='#78BDB8')  # 🔹 Fondo igual a la imagen

        # 🔹 Definir manualmente los parámetros de la imagen de fondo
        self.bg_params = {"ruta": "C:/ITE/4° SEMESTRE/FUNDAMENTOS DE BASES DE DATOS/IMAGENES/LOGO portada.jpg",
                          "size": (1090, 612), "x": 0, "y": 0}  # 🔹 Ajusta tamaño y posición

        # Cargar imagen con parámetros manuales
        self.bg_image = self.cargar_imagen(self.bg_params["ruta"], self.bg_params["size"])

        if self.bg_image:
            fondo_label = tk.Label(self, image=self.bg_image)
            fondo_label.place(x=self.bg_params["x"], y=self.bg_params["y"])  # 🔹 Ubicación manual

        self.intentos = 0  # Contador de intentos fallidos

        # 🔹 Definir ubicación manual de los cuadros de entrada en la derecha
        self.form_params = {"x": 50, "y": 50, "width": 350, "height": 250}

        # Contenedor con el color de fondo correcto
        frame_login = tk.Frame(self, bg="#78BDB8", bd=5, width=self.form_params["width"], height=self.form_params["height"])
        frame_login.place(x=self.form_params["x"], y=self.form_params["y"])  # 🔹 Posiciona a la derecha

        tk.Label(frame_login, text="Usuario:", font=("Helvetica", 14), bg='#78BDB8', fg="white").place(x=20, y=20)
        self.entry_username = tk.Entry(frame_login, width=30, font=("Helvetica", 12))
        self.entry_username.place(x=20, y=50)

        tk.Label(frame_login, text="Contraseña:", font=("Helvetica", 14), bg='#78BDB8', fg="white").place(x=20, y=90)
        self.entry_password = tk.Entry(frame_login, width=30, show="*", font=("Helvetica", 12))
        self.entry_password.place(x=20, y=120)

        # 🔹 Botones "Ingresar" y "Salir del sistema"
        tk.Button(frame_login, text="Ingresar", font=("Helvetica", 12), bg="#007bff", fg="white",
                  command=self.validar_usuario, width=10).place(x=20, y=170)

        tk.Button(frame_login, text="Salir del sistema", font=("Helvetica", 12), bg="#007bff", fg="white",
                  command=self.salir_sistema, width=15).place(x=148, y=170)

    def cargar_imagen(self, ruta, size):
        """Carga y redimensiona una imagen."""
        try:
            imagen = Image.open(ruta)
            imagen = imagen.resize(size)  # 🔹 Ajusta tamaño manualmente
            return ImageTk.PhotoImage(imagen)
        except Exception as e:
            print(f"Error al cargar la imagen {ruta}: {e}")
            return None

    def validar_usuario(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        conexion = conectar_bd()
        if not conexion:
            return

        cursor = conexion.cursor()
        cursor.execute("SELECT id_usuario, rol FROM usuario WHERE username=%s AND password=%s", (username, password))
        resultado = cursor.fetchone()
        conexion.close()

        if resultado:
            id_usuario, rol_usuario = resultado
            messagebox.showinfo("Acceso Permitido", f"Bienvenido, {username} ({rol_usuario})")
            self.destroy()
            self.master.iniciar_aplicacion(id_usuario, rol_usuario)
        else:
            self.intentos += 1
            messagebox.showerror("Error", f"Usuario o contraseña incorrectos. Intentos restantes: {3 - self.intentos}")

            if self.intentos >= 3:
                messagebox.showerror("Error", "Se ha excedido el número de intentos. Cerrando sistema.")
                self.master.quit()
                self.master.destroy()
                sys.exit()

    def salir_sistema(self):
        """Cerrar completamente el sistema."""
        self.master.quit()
        self.master.destroy()
        sys.exit()

# ------------------------- CLASE PRINCIPAL -------------------------
class Aplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.withdraw()  # Ocultar la ventana principal hasta que el usuario inicie sesión
        self.conexion = conectar_bd()  # Conectar a la base de datos al iniciar
        if self.conexion:  
            self.pantalla_bienvenida = PantallaBienvenida(self)  # Mostrar pantalla de bienvenida

    def mostrar_login(self):
        """Iniciar la ventana de login después de la pantalla de bienvenida."""
        LoginWindow(self)  # Solo se llama una vez, eliminando instancias innecesarias

    def iniciar_aplicacion(self, id_usuario, rol_usuario):
        """Cargar la interfaz después de un inicio de sesión exitoso."""
        self.id_usuario_actual = id_usuario
        self.rol_actual = rol_usuario
        self.deiconify()  # Mostrar ventana principal

        self.initialize_gui()
        self.registrar_entrada()  # Registrar la entrada al sistema al iniciar sesión

    def registrar_entrada(self):
        """Registrar la entrada del usuario en la base de datos."""
        conn = conectar_bd()
        if conn is None:
            print("Error: No se pudo conectar a la base de datos.")
            return

        cursor = conn.cursor()

        if self.id_usuario_actual is None:
            print("Error: No hay usuario autenticado.")
            return

        print(f"Ejecutando registrar_entrada() para usuario {self.id_usuario_actual}")  # 🔹 Debugging

        # Insertar el registro con fecha de entrada
        cursor.execute("INSERT INTO salir_sistema (id_usuario, fecha_entrada) VALUES (%s, NOW())", (self.id_usuario_actual,))
        conn.commit()

        # Verificar si el registro se insertó correctamente
        cursor.execute("SELECT * FROM salir_sistema WHERE id_usuario = %s ORDER BY fecha_entrada DESC LIMIT 1;", (self.id_usuario_actual,))
        resultado = cursor.fetchone()
        print(f"Registro insertado: {resultado}")  # 🔹 Debugging

        conn.close()
        print(f"✅ Sesión iniciada correctamente para usuario {self.id_usuario_actual}.")

    def salir_sistema(self):
        conn = conectar_bd()
        cursor = conn.cursor()

        if self.id_usuario_actual is None:
            print("Error: No hay usuario autenticado.")
            return

        # Actualizar el registro más reciente con la fecha de salida
        cursor.execute("UPDATE salir_sistema SET fecha_salida = NOW() WHERE id_usuario = %s AND fecha_salida IS NULL", (self.id_usuario_actual,))

        conn.commit()
        print(f"Sesión cerrada correctamente para usuario {self.id_usuario_actual}.")
        conn.close()

        ventana_temporal = tk.Toplevel()
        ventana_temporal.title("Saliendo del Sistema...")
        
        ventana_temporal.geometry("500x300")
        ventana_temporal.configure(bg="black")  # Fondo negro


        try:
            ruta_imagen = "C:/Users/RGbus/OneDrive/Documents/GitHub/T-picos-Avanzados/IMAGENES DEL PROYECTO/Cerrando sesión.jpg"  # Cambia a la ruta correcta
            imagen = Image.open(ruta_imagen)
            imagen = imagen.resize((500, 300))
            img_tk = ImageTk.PhotoImage(imagen)

            # Mostrar imagen
            label_imagen = tk.Label(ventana_temporal, image=img_tk)
            label_imagen.image = img_tk  # Mantener referencia
            label_imagen.pack()
        except Exception as e:
            print(f"Error al cargar la imagen: {e}")

        # Cerrar la ventana de imagen después de 3 segundos y salir del sistema
        ventana_temporal.after(3000, lambda: ventana_temporal.destroy())  # Cierra la ventana
        ventana_temporal.after(3200, lambda: os._exit(0)) 

        # sys.exit()


    def cargar_imagen(self, ruta, size=None):
        """Función para cargar y redimensionar imágenes."""
        try:
            imagen = Image.open(ruta)
            if size:
                imagen = imagen.resize(size)
            return ImageTk.PhotoImage(imagen)
        except Exception as e:
            print(f"Error al cargar la imagen {ruta}: {e}")
            return None

    def initialize_gui(self):
        self.title('Menú General del Sistema')
        self.attributes('-fullscreen', True)  # Configurar pantalla completa
        self.configure(bg='#8FB3C9')  # Fondo azul claro

        # Marco principal para dividir izquierda y derecha
        main_frame = tk.Frame(self, bg='#8FB3C9')
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Marco para el lado izquierdo (menú centrado)
        left_frame = tk.Frame(main_frame, bg='#8FB3C9', width=600)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, padx=120, pady=50)

        # Título del menú general con recuadro
        title_frame = tk.Frame(left_frame, bg='#008080', relief="solid", borderwidth=2)
        title_frame.pack(fill=tk.X, pady=20)
        title_label = tk.Label(
            title_frame,
            text="Menú General del Sistema",
            font=("Helvetica", 16, "bold"),
            bg='#008080',
            fg="white"
        )
        title_label.pack(padx=10, pady=10)

        # Crear botones del menú
        button_size = (50, 50)
        button_width = 400

        consulta_icon = self.cargar_imagen("C:/Users/RGbus/OneDrive/Documents/GitHub/T-picos-Avanzados/IMAGENES DEL PROYECTO/saerch.jpg", button_size)
        consulta_button = tk.Button(left_frame, text="Consulta de Documentos", image=consulta_icon, compound="left",
                                    font=("Helvetica", 14), bg='#D9EAF3', padx=10, width=button_width,
                                    command=self.abrir_consultas)
        if consulta_icon:
            consulta_button.image = consulta_icon
            consulta_button.pack(pady=15)

        alta_documento_icon = self.cargar_imagen("C:/Users/RGbus/OneDrive/Documents/GitHub/T-picos-Avanzados/IMAGENES DEL PROYECTO/icono doctos.jpg", button_size)
        alta_documento_button = tk.Button(left_frame, text="Alta de Documento", image=alta_documento_icon, compound="left",
                                    font=("Helvetica", 14), bg='#D9EAF3', padx=10, width=button_width,
                                    command=self.alta_documento)
        if alta_documento_icon:
            alta_documento_button.image = alta_documento_icon
            alta_documento_button.pack(pady=15)

        alta_usuario_icon = self.cargar_imagen("C:/Users/RGbus/OneDrive/Documents/GitHub/T-picos-Avanzados/IMAGENES DEL PROYECTO/usuario.jpg", button_size)
        alta_usuario_button = tk.Button(left_frame, text="Alta de Usuario", image=alta_usuario_icon, compound="left",
                                    font=("Helvetica", 14), bg='#D9EAF3', padx=10, width=button_width,
                                    command=self.alta_usuario)
        if alta_usuario_icon:
            alta_usuario_button.image = alta_usuario_icon
            alta_usuario_button.pack(pady=15)

        salir_icon = self.cargar_imagen("C:/Users/RGbus/OneDrive/Documents/GitHub/T-picos-Avanzados/IMAGENES DEL PROYECTO/EXIT.jpg", button_size)
        salir_button = tk.Button(left_frame, text="Salir del Sistema", image=salir_icon, compound="left",
                                    font=("Helvetica", 14), bg='#D9EAF3', padx=10, width=button_width,
                                    command=self.salir_sistema)
        if salir_icon:
            salir_button.image = salir_icon
            salir_button.pack(pady=15)

        # Marco derecho (imagen decorativa)
        right_frame = tk.Frame(main_frame, bg='#012965', width=int(self.winfo_screenwidth() / 3))
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH)

        decor_image = self.cargar_imagen(
            "C:/Users/RGbus/OneDrive/Documents/GitHub/T-picos-Avanzados/IMAGENES DEL PROYECTO/background 2.jpg", 
            size=(int(self.winfo_screenwidth() / 3), self.winfo_screenheight())
        )
        decor_label = tk.Label(right_frame, image=decor_image, bg='#012965')
        if decor_image:
            decor_label.image = decor_image
            decor_label.pack(expand=True, fill=tk.BOTH)

    def abrir_consultas(self):
        """Abrir la ventana de Consulta de Documentos."""
        consulta_window = tk.Toplevel(self)
        consulta_window.attributes('-fullscreen', True)
        consulta_window.title("Consulta de Documentos")
        consulta_window.configure(bg='#a0c4d3')

        # Marco para definir el tamaño del recuadro
        titulo_frame = tk.Frame(consulta_window, bg='#008080', relief="solid", borderwidth=2, width=341, height=40)
        titulo_frame.place(x=0, y=152)

        # Etiqueta dentro del Frame centrada
        titulo_label = tk.Label(
            titulo_frame,  
            text="Menú Consulta de Documentos",
            font=("Helvetica", 14),
            bg='#008080',
            fg="white"
        )

        # Ubicar la etiqueta en el centro del Frame sin modificar su tamaño
        titulo_label.place(relx=0.5, rely=0.5, anchor="center")

        # Imagen decorativa en el menú de consultas (parte superior)
        consulta_image = self.cargar_imagen(
            "C:/Users/RGbus/OneDrive/Documents/GitHub/T-picos-Avanzados/IMAGENES DEL PROYECTO/P. Superior Pantalla.jpg", 
            size=(self.winfo_screenwidth(), 150)  # Redimensionar para abarcar todo el ancho
        )
        consulta_label = tk.Label(consulta_window, image=consulta_image, bg='#a0c4d3')
        if consulta_image:
            consulta_label.image = consulta_image
            consulta_label.pack(fill=tk.X)

        # Opciones del menú de consultas
        options_frame = tk.Frame(consulta_window, bg='#a0c4d3')
        options_frame.pack(fill=tk.BOTH, expand=True, padx=0, pady=39)

        tipos = [
            "Listas de Asistencia",
            "Actas de Calificaciones",
            "Extraordinarios",
            "Títulos de Suficiencia",
            "Recursamientos"
        ]

        for tipo in tipos:
            tk.Button(options_frame, text=tipo, font=("Helvetica", 14),
                    bg="#007bff", fg="white", width=30, pady=0, 
                    command=lambda t=tipo: self.consultar_documentos(t)).pack(pady=0, anchor="w")

        regresar_button = tk.Button(
            consulta_window,
            text="Regresar al Menú General",
            font=("Helvetica", 14),
            bg="#008080",
            fg="white",
            command=consulta_window.destroy
        )
        regresar_button.place(y=380, x=45)

# ------------------ CONSULTAR DOCUMENTO -------------------------------------------
    def consultar_documentos(self, tipo):
        # Crear una nueva ventana dentro de la interfaz
        consulta_window = tk.Toplevel(self)
        consulta_window.title(f"Consultar Documento - {tipo}")
        consulta_window.geometry("400x250")
        consulta_window.configure(bg='#a0c4d3')

        tk.Label(consulta_window, text="Ingrese Grupo:", font=("Helvetica", 12), bg='#a0c4d3').pack(pady=5)
        grupo_entry = tk.Entry(consulta_window)
        grupo_entry.pack(pady=5)

        tk.Label(consulta_window, text="Ingrese Ciclo Escolar (Ejemplo: 2025-1):", font=("Helvetica", 12), bg='#a0c4d3').pack(pady=5)
        ciclo_entry = tk.Entry(consulta_window)
        ciclo_entry.pack(pady=5)

        def buscar_documento():
            grupo = grupo_entry.get()
            ciclo = ciclo_entry.get()

            conexion = conectar_bd()
            if conexion:
                cursor = conexion.cursor()
                cursor.execute("SELECT ruta_archivo FROM documentos WHERE tipo=%s AND grupo=%s AND ciclo_escolar=%s",
                            (tipo, grupo, ciclo))
                resultado = cursor.fetchone()
                conexion.close()

                if resultado:
                    ruta_archivo = resultado[0]
                    if ruta_archivo.endswith(".pdf"):  # Asegurar que el archivo sea un PDF
                        try:
                            os.startfile(ruta_archivo)  # Abre el archivo PDF con el visor predeterminado
                        except Exception as e:
                            messagebox.showerror("Error", f"No se pudo abrir el archivo: {str(e)}")
                    else:
                        messagebox.showerror("Error", "El documento encontrado no es un archivo PDF.")
                else:
                    messagebox.showerror("Error", "No se encontró un documento con los datos ingresados.")
                    consulta_window.deiconify()  # Reactiva la ventana si está oculta

        tk.Button(consulta_window, text="Abrir Documento", font=("Helvetica", 12), bg="#007bff", fg="white", 
                command=buscar_documento).pack(pady=10)

        tk.Button(consulta_window, text="Regresar al Menú de Consultas", font=("Helvetica", 12), bg="#008080", fg="white",
                command=consulta_window.destroy).pack(pady=10)  
                 
# --------------------------- ALTA DE DOCUMENTO --------------------------------------
    def alta_documento(self):
        # Crear una nueva ventana dentro de la interfaz
        alta_window = tk.Toplevel(self)
        alta_window.title("Alta de Documento")
        # Obtener tamaño de pantalla
        ancho_pantalla = alta_window.winfo_screenwidth()
        alto_pantalla = alta_window.winfo_screenheight()

        # Calcular posición centrada
        x_pos = (ancho_pantalla - 800) // 2  # Ajusta al ancho de la ventana
        y_pos = (alto_pantalla - 480) // 2  # Ajusta al alto de la ventana

        # Establecer la posición fija en pantalla
        alta_window.geometry(f"800x480+{x_pos}+{y_pos}") 

        alta_window.configure(bg='#a0c4d3')

        tk.Label(alta_window, text="Ingresar ID del documento:", font=("Helvetica", 12), bg='#a0c4d3').pack(pady=5)
        id_entry = tk.Entry(alta_window, width=40)
        id_entry.pack(pady=5)

        tk.Label(alta_window, text="Ingresar Tipo de documento:", font=("Helvetica", 12), bg='#a0c4d3').pack(pady=5)
        tipo_entry = tk.Entry(alta_window, width=40)
        tipo_entry.pack(pady=5)

        tk.Label(alta_window, text="Ingresar Grupo:", font=("Helvetica", 12), bg='#a0c4d3').pack(pady=5)
        grupo_entry = tk.Entry(alta_window, width=40)
        grupo_entry.pack(pady=5)

        tk.Label(alta_window, text="Ingresar Ciclo escolar (Ejemplo: 2025-1):", font=("Helvetica", 12), bg='#a0c4d3').pack(pady=5)
        ciclo_entry = tk.Entry(alta_window, width=40)
        ciclo_entry.pack(pady=5)

        # Botón para buscar archivo antes de la entrada
        def seleccionar_archivo():
            ruta = filedialog.askopenfilename(filetypes=[("Archivos PDF", "*.pdf")])
            if ruta:
                ruta_entry.delete(0, tk.END)
                ruta_entry.insert(0, ruta)
                messagebox.showinfo("Archivo Seleccionado", "El archivo se ha seleccionado correctamente.\nCompleta el resto de los datos antes de registrar.")
                alta_window.focus_force()  

        tk.Button(alta_window, text="Buscar Archivo", font=("Helvetica", 12), bg="#007bff", fg="white",
                width=26, command=seleccionar_archivo).pack(pady=5)

        tk.Label(alta_window, text="Ruta del archivo PDF:", font=("Helvetica", 12), bg='#a0c4d3').pack(pady=5)
        ruta_entry = tk.Entry(alta_window, width=130)
        ruta_entry.pack(pady=5)

        # Función para registrar el documento
        def registrar_documento():
            id_documento = id_entry.get().strip()
            tipo = tipo_entry.get().strip()
            grupo = grupo_entry.get().strip()
            ciclo_escolar = ciclo_entry.get().strip()
            ruta_archivo = ruta_entry.get().strip()

            if not all([id_documento, tipo, grupo, ciclo_escolar, ruta_archivo]):
                messagebox.showerror("Error", "Todos los campos son obligatorios.")
                return

            conexion = conectar_bd()
            if conexion:
                try:
                    cursor = conexion.cursor()
                    cursor.execute("""
                        INSERT INTO documentos (id_documento, tipo, grupo, ciclo_escolar, ruta_archivo) 
                        VALUES (%s, %s, %s, %s, %s)
                    """, (id_documento, tipo, grupo, ciclo_escolar, ruta_archivo))

                    conexion.commit()  
                    messagebox.showinfo("Éxito", "Documento registrado exitosamente.")
                    alta_window.destroy()  

                except mysql.connector.Error as e:
                    messagebox.showerror("Error de Base de Datos", f"No se pudo registrar el documento: {str(e)}")

                finally:
                    cursor.close()
                    conexion.close()
            else:
                messagebox.showerror("Error", "No se pudo establecer conexión con la base de datos.")

        # Botón para registrar documento con el mismo tamaño que las entradas
        tk.Button(alta_window, text="Registrar Documento", font=("Helvetica", 12), bg="#007bff", fg="white", 
                width=26, command=registrar_documento).pack(pady=10)

        # Botón para cerrar la ventana de alta
        tk.Button(alta_window, text="Cancelar", font=("Helvetica", 12), bg="#008080", fg="white",
                width=26, command=alta_window.destroy).pack(pady=10)
        

# --------------------------- ALTA DE USUARIO --------------------------------------

    def alta_usuario(self):
        if self.rol_actual != "Directora":
            messagebox.showerror("Acceso Denegado", "Solo la Directora puede dar de alta usuarios")
            return

        # Crear la ventana centrada
        ventana = tk.Toplevel(self)
        ventana.title("Alta de Usuario")

        # Obtener tamaño de pantalla
        ancho_pantalla = ventana.winfo_screenwidth()
        alto_pantalla = ventana.winfo_screenheight()

        # Calcular posición centrada
        x_pos = (ancho_pantalla - 800) // 2
        y_pos = (alto_pantalla - 480) // 2

        # Establecer el tamaño fijo en pantalla
        ventana.geometry(f"600x480+{x_pos}+{y_pos}")
        ventana.configure(bg='#a0c4d3')

        # Establecer el ancho estándar para los campos de entrada
        entry_width = 40

        tk.Label(ventana, text="Nombre completo del Usuario:", font=("Helvetica", 12), bg='#a0c4d3').pack(pady=5)
        entry_nombre = tk.Entry(ventana, width=entry_width)
        entry_nombre.pack(pady=5)

        tk.Label(ventana, text="Puesto (Rol):", font=("Helvetica", 12), bg='#a0c4d3').pack(pady=5)
        entry_rol = tk.Entry(ventana, width=entry_width)
        entry_rol.pack(pady=5)

        tk.Label(ventana, text="Email:", font=("Helvetica", 12), bg='#a0c4d3').pack(pady=5)
        entry_email = tk.Entry(ventana, width=entry_width)
        entry_email.pack(pady=5)

        tk.Label(ventana, text="Usuario:", font=("Helvetica", 12), bg='#a0c4d3').pack(pady=5)
        entry_username = tk.Entry(ventana, width=entry_width)
        entry_username.pack(pady=5)

        tk.Label(ventana, text="Contraseña:", font=("Helvetica", 12), bg='#a0c4d3').pack(pady=5)
        entry_user_password = tk.Entry(ventana, width=entry_width, show="*")
        entry_user_password.pack(pady=5)

        def guardar():
            nombre = entry_nombre.get().strip()
            rol = entry_rol.get().strip()
            email = entry_email.get().strip()
            username = entry_username.get().strip()
            password = entry_user_password.get().strip()

            # Validación de campos vacíos
            if not nombre or not rol or not email or not username or not password:
                messagebox.showerror("Error", "Todos los campos son obligatorios.")
                return

            conexion = conectar_bd()
            if conexion:
                try:
                    cursor = conexion.cursor()

                    # Verificar si el usuario ya existe
                    cursor.execute("SELECT COUNT(*) FROM usuario WHERE email = %s OR username = %s", (email, username))
                    if cursor.fetchone()[0] > 0:
                        messagebox.showerror("Error", "El email o username ya están registrados.")
                        return

                    # Insertar usuario si no está duplicado
                    cursor.execute(
                        "INSERT INTO usuario (nombre, rol, email, username, password) VALUES (%s, %s, %s, %s, %s)",
                        (nombre, rol, email, username, password)
                    )
                    conexion.commit()
                    messagebox.showinfo("Éxito", "Usuario registrado correctamente")
                    ventana.destroy()
                except mysql.connector.Error as e:
                    messagebox.showerror("Error de Base de Datos", f"No se pudo registrar el usuario: {str(e)}")
                finally:
                    cursor.close()
                    conexion.close()
            else:
                messagebox.showerror("Error", "No se pudo conectar a la base de datos.")

        # Botón para registrar usuario
        tk.Button(ventana, text="Registrar Usuario", font=("Helvetica", 12), bg="#007bff", fg="white",
                width=26, command=guardar).pack(pady=10)

        # Botón "Regresar al Menú General"
        tk.Button(ventana, text="Regresar al Menú General", font=("Helvetica", 12), bg="#008080", fg="white",
                width=26, command=ventana.destroy).pack(pady=10)


# ------------------------- EJECUCIÓN PRINCIPAL -------------------------
def main():
    app = Aplication()
    app.mainloop()

if __name__ == '__main__':
    main()
