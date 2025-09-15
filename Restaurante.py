from tkinter import Tk, Toplevel, Label, Button, Entry, Frame, messagebox
from PIL import Image, ImageTk
from openpyxl import Workbook, load_workbook
import os
import tkinter as tk
from tkinter import Frame, Label, Button, Toplevel


#creo los archivos de datos 
#BDD PARA USUARIOS
archivo_usuarios = "Datos_Usuarios.xlsx"
if os.path.exists(archivo_usuarios):
    wb = load_workbook(archivo_usuarios)
    ws = wb.active
else:
    wb = Workbook()
    ws = wb.active
    ws.append(["Usuario", "Contraseña", "Tipo"])
    wb.save(archivo_usuarios)

#BDD PARA MESAS/RESERVAS
archivo_Reservas = "Datos_Reservas.xlsx"
if os.path.exists(archivo_Reservas):
    reservas = load_workbook(archivo_Reservas)
    wreservas = reservas.active
else:
    reservas = Workbook()
    wreservas = reservas.active
    wreservas.append(["ID", "Usuario", "Estado", "Capacidad"])
    reservas.save(archivo_Reservas)


#Arranca el sistema
class SeleccionarTipo:
    def __init__(self, ventana):
        self.ventana= ventana
        self.ventana.geometry("400x700")
        self.ventana.title("Tipo de Usuario")

        fondo = "#88FFB4"
        #Dividimos en dos partes la pantalla

        self.parte_superior= Frame(self.ventana, bg=fondo)
        self.parte_superior.pack(fill="both", expand=True)

        self.parte_inferior= Frame(self.ventana, bg=fondo)
        self.parte_inferior.pack(fill="both", expand=True)

        self.parte_inferior.columnconfigure(0, weight=1)
        self.parte_inferior.columnconfigure(1, weight=1)

        #Agregamos la imagen del restaurante 
        self.imagen = Image.open(r"Logo.png").resize((210, 220))
        self.render = ImageTk.PhotoImage(self.imagen)
        Label(self.parte_superior, image=self.render, bg=fondo).pack(expand=True, fill="both", side="top")

        # titulos
        Label(self.parte_superior, text="¿Quién eres?", font=("Calisto MT", 30, "bold"), bg=fondo).pack(pady=10)

        #Botones
        Button(self.parte_inferior, text="Cliente", width=35, height=2, font=("Arial", 14), command=lambda: self.elegir_cliente("Cliente")).grid(row=2, column=0, columnspan=2, padx=35, pady=5)

        Button(self.parte_inferior, text="Administrador", width=35, height=2, font=("Arial", 14), command=lambda: self.elegir_admin("Administrador")).grid(row=4, column=0, columnspan=4, padx=35, pady=5)

   
    def elegir_cliente(self,tipo):
        self.ventana.withdraw()
        Login(self.ventana, tipo)

    def elegir_admin(self,tipo):
        self.ventana.withdraw()
        Login_Ingresar(self.ventana, tipo)


#Clase para cliente donde ingresa o registra
class Login:
    def __init__(self, ventana, tipo): #Constructores
        self.tipo=tipo
        self.ventana=Toplevel(ventana)
        self.ventana.geometry("400x700")
        self.ventana.title("Seleccione el tipo de usuario")

        fondo = "#88FFB4"

        #Dividimos en dos partes la pantalla 
       
        self.parte_superior= Frame(self.ventana, bg=fondo)
        self.parte_superior.pack(fill="both", expand=True)

        self.parte_inferior= Frame(self.ventana, bg=fondo)
        self.parte_inferior.pack(fill="both", expand=True)

        self.parte_inferior.columnconfigure(0, weight=1)
        self.parte_inferior.columnconfigure(1, weight=1)

        #Agregamos la imagen 
        self.imagen = Image.open(r"Logo.png").resize((210, 220))
        self.render = ImageTk.PhotoImage(self.imagen)
        Label(self.parte_superior, image=self.render, bg=fondo).pack(expand=True, fill="both", side="top")

        Label(self.parte_superior, text="Bienvenido", font=("Calisto MT", 30, "bold"), bg=fondo).pack(pady=10)

        Button(self.parte_inferior, text="Registrar", width=35, height=2, font=("Arial", 14), command=lambda: self.eleccion_registrar(ventana)).grid(row=2, column=0, columnspan=2, padx=35, pady=5)

        Button(self.parte_inferior, text="Ingresar", width=35, height=2, font=("Arial", 14), command=lambda: self.eleccion_ingresar(ventana)).grid(row=4, column=0, columnspan=4, padx=35, pady=5)

        Button(self.parte_inferior, text="Atras", width=35, height=2, font=("Arial", 14), command=lambda: self.regresar(ventana)).grid(row=6, column=0, columnspan=6, padx=35, pady=5)


         # --- BOTÓN DE INFORMACIÓN REDONDO ARRIBA A LA DERECHA ---
        self.canvas_info = tk.Canvas(self.parte_superior, width=30, height=30, highlightthickness=0, bg=fondo)
        self.canvas_info.place(relx=1.0, x=-15, y=15, anchor="ne")

        circulo = self.canvas_info.create_oval(2, 2, 28, 28, fill="#3498db", outline="#2980b9")
        texto = self.canvas_info.create_text(15, 15, text="i", fill="white", font=("Times New Roman", 14, "italic"))

        # hacer que tanto el círculo como la letra sean clickeables
        self.canvas_info.tag_bind(circulo, "<Button-1>", lambda e: self.mostrar_info())
        self.canvas_info.tag_bind(texto, "<Button-1>", lambda e: self.mostrar_info())

    def regresar(self,ventana):
        self.ventana.destroy()
        ventana.deiconify()
    
    def mostrar_info(self):
        ventana_info = Toplevel(self.ventana)
        ventana_info.title("Información")
        ventana_info.geometry("400x200")
        Label(ventana_info, text="Abrimos de jueves a domingo...\n\n Te acompañamos en tus momentos especiales,\n ya sea en el almuerzo o en la cena. ¡Te esperamos! \n\n\n Número de contacto: 3546 879736", wraplength=280, justify="center").pack(pady=20)
        Button(ventana_info, text="Cerrar", command=ventana_info.destroy).pack(pady=10)

        
    def eleccion_ingresar(self, ventana):
        self.ventana.destroy()
        Login_Ingresar(ventana,self.tipo)

    def eleccion_registrar(self, ventana):
        self.ventana.destroy()
        Registro(ventana,self.tipo)

#clase cuando se toma la opcion de registrar y si todo esta bien se va a la pestaña login
class Registro:
        def __init__(self, ventana, tipo): #Constructores
            self.tipo=tipo
            self.ventana= Toplevel(ventana)
            self.ventana.geometry("400x700")
            self.ventana.title("Registro")

            fondo = "#88FFB4"

            self.parte_superior = Frame(self.ventana, bg=fondo)
            self.parte_superior.pack(fill="both", expand=True)

            self.parte_inferior = Frame(self.ventana, bg=fondo)
            self.parte_inferior.pack(fill="both", expand=True)

            self.parte_inferior.columnconfigure(0, weight=1)
            self.parte_inferior.columnconfigure(1, weight=1)
          
            #titulo
            Label(self.parte_superior, text=f"Tipo: {self.tipo}", font=("Calisto MT", 30, "bold"), bg=fondo).pack(side="top", pady=20)

            #Imagen Registro
            self.imagen = Image.open(r"registrarse.png").resize((210, 220))
            self.render = ImageTk.PhotoImage(self.imagen)
            Label(self.parte_superior, image=self.render, bg=fondo).pack(expand=True, fill="both", side="top")

            #Entradas
            Label(self.parte_inferior, text="Usuario", font=("Arial", 18), bg=fondo).grid(row=0, column=0, padx=10, sticky="e")
            self.entry_usuario = Entry(self.parte_inferior, bd=0, width=14, font=("Arial", 18))
            self.entry_usuario.grid(row=0, column=1, columnspan=3, padx=5, sticky="w")

            Label(self.parte_inferior, text="Contraseña:", font=("Arial", 18), bg=fondo).grid(row=1, column=0, pady=10, sticky="e")
            self.entry_contrasena = Entry(self.parte_inferior, bd=0, width=14, font=("Arial", 18), show="*")
            self.entry_contrasena.grid(row=1, column=1, columnspan=3, padx=5, sticky="w")

            Button(self.parte_inferior, text="Guardar", width=16, font=("Arial", 12), command=lambda: self.guardar_datos(ventana)).grid(row=2, column=0, columnspan=2, padx=35, pady=5)

            Button(self.parte_inferior, text="Atras", width=16, font=("Arial", 12), command=lambda: self.regresar(ventana)).grid(row=8, column=0, columnspan=4, padx=35, pady=5)

        def regresar(self,ventana):
            self.ventana.destroy()
            Login(ventana,self.tipo)

        def guardar_datos(self, ventana):
            usuario = self.entry_usuario.get()
            contrasena = self.entry_contrasena.get()

            #se valida que los campos se hayan completado
            if not usuario or not contrasena:
                messagebox.showwarning("Cuidado!", "Se deben completar ambos campos")
                return

            #Agregamos usuario y contraseña al excel de usuarios
            ws.append([usuario, contrasena, self.tipo])
            wb.save(archivo_usuarios)
            messagebox.showinfo("Datos", "Se guardaron los datos")

            self.entry_usuario.delete(0, "end")
            self.entry_contrasena.delete(0, "end")

            self.ventana.destroy()
            Login_Ingresar(ventana, self.tipo)

class Login_Ingresar:
    def __init__(self, ventana, tipo): #Constructores
        self.tipo=tipo
        self.ventana= Toplevel(ventana)
        self.ventana.geometry("400x700")
        self.ventana.title("Ingresar")

        fondo = "#88FFB4"

        #dividimos
        self.parte_superior = Frame(self.ventana, bg=fondo)
        self.parte_superior.pack(fill="both", expand=True)

        self.parte_inferior = Frame(self.ventana, bg=fondo)
        self.parte_inferior.pack(fill="both", expand=True)

        self.parte_inferior.columnconfigure(0, weight=1)
        self.parte_inferior.columnconfigure(1, weight=1)

        #Etiqueta
        Label(self.parte_superior, text="Inicio de sesión", font=("Calisto MT", 30, "bold"), bg=fondo).pack(side="top", pady=20)

        #Imagen
        self.imagen = Image.open(r"Imagen_Login.png").resize((210, 220))
        self.render = ImageTk.PhotoImage(self.imagen)
        Label(self.parte_superior, image=self.render, bg=fondo).pack(expand=True, fill="both", side="top")
        
        #Entradas
        Label(self.parte_inferior, text="Usuario", font=("Arial", 18), bg=fondo).grid(row=0, column=0, padx=10, sticky="e")
        self.entry_usuario = Entry(self.parte_inferior, bd=0, width=14, font=("Arial", 18))
        self.entry_usuario.grid(row=0, column=1, columnspan=3, padx=5, sticky="w")

        Label(self.parte_inferior, text="Contraseña:", font=("Arial", 18), bg=fondo).grid(row=1, column=0, pady=10, sticky="e")
        self.entry_contrasena = Entry(self.parte_inferior, bd=0, width=14, font=("Arial", 18), show="*")
        self.entry_contrasena.grid(row=1, column=1, columnspan=3, padx=5, sticky="w")

        Button(self.parte_inferior, text="Ingresar", width=16, font=("Arial", 12), command=self.verificacion_datos).grid(row=2, column=0, columnspan=2, padx=35, pady=5)
        
        Button(self.parte_inferior, text="Atras", width=16, font=("Arial", 12), command=lambda: self.regresar(ventana)).grid(row=8, column=0, columnspan=4, padx=35, pady=5)
    
    def regresar(self,ventana):
        self.ventana.destroy()
        ventana.deiconify()

    def verificacion_datos(self):
        usuario = self.entry_usuario.get()
        contrasena = self.entry_contrasena.get()

        if not usuario or not contrasena:
            messagebox.showwarning("Cuidado!", "Se deben completar ambos campos")
            return

        if not os.path.exists(archivo_usuarios):
            messagebox.showerror("Error", "No hay usuarios registrados")
            return
        
        if self.tipo == "Administrador" and usuario == "admin" and contrasena == "123":
            messagebox.showinfo("Éxito", "Bienvenido admin como Administrador")
            self.ventana.destroy()
            Restaurante(self.ventana.master, self.tipo)
            return

        wb_temp = load_workbook(archivo_usuarios)
        ws_temp = wb_temp.active

        encontrado = False
        for fila in ws_temp.iter_rows(values_only=True):
            if fila[0] == usuario and fila[1] == contrasena and fila[2] == self.tipo:
                encontrado = True
                break

        if encontrado:
            messagebox.showinfo("Éxito", f"Bienvenido {usuario} como {self.tipo}")
            self.ventana.destroy()
            Restaurante(ventana, self.tipo)
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrecto")
            
class Restaurante:
    def __init__(self, ventana, tipo):
        self.tipo = tipo
        self.ventana = Toplevel(ventana)
        self.ventana.geometry("700x700")
        self.ventana.title("Restaurante")
        
        fondo = "#88FFB4"
        self.ventana.configure(bg=fondo)

        # Frames principales
        self.parte_superior = Frame(self.ventana, bg=fondo)
        self.parte_superior.pack(fill="both", expand=True)

        self.parte_inferior = Frame(self.ventana, bg=fondo)
        self.parte_inferior.pack(fill="both", expand=True)

                 # --- BOTÓN DE INFORMACIÓN REDONDO ARRIBA A LA DERECHA ---
        self.canvas_info = tk.Canvas(self.parte_superior, width=30, height=30, highlightthickness=0, bg=fondo)
        self.canvas_info.place(relx=1.0, x=-15, y=15, anchor="ne")

        circulo = self.canvas_info.create_oval(2, 2, 28, 28, fill="#3498db", outline="#2980b9")
        texto = self.canvas_info.create_text(15, 15, text="i", fill="white", font=("Times New Roman", 14, "italic"))

        # hacer que tanto el círculo como la letra sean clickeables
        self.canvas_info.tag_bind(circulo, "<Button-1>", lambda e: self.mostrar_info())
        self.canvas_info.tag_bind(texto, "<Button-1>", lambda e: self.mostrar_info())
        



        # Imagen del restaurante
        self.imagen = Image.open(r"Logo.png").resize((170, 180))
        self.render = ImageTk.PhotoImage(self.imagen)
        Label(self.parte_superior, image=self.render, bg=fondo).pack(pady=10)

        # Botón Cerrar Sesión
        Button(self.parte_inferior, text="Cerrar Sesion", width=16, font=("Arial", 12),
               command=lambda: self.cerrar_sesion(ventana)).pack(pady=10)

        # Inicializamos mesas y filas
        self.mesas = 6
        self.filas = []
        self.estado_mesas = {}   # {1: {"estado":"Libre","nombre":""}, ...}
        self.botones_mesas = {}

        # Dibujar mesas iniciales
        for i in range(1, self.mesas + 1):
            if (i - 1) % 3 == 0:
                fila_frame = Frame(self.parte_superior, bg=fondo)
                fila_frame.pack()
                self.filas.append(fila_frame)
            
            btn = Button(
                self.filas[-1],
                text=f"Mesa {i}",
                width=12,
                height=3,
                bg="green",
                command=lambda n=i: Reservar_mesa(self.ventana, self.tipo, self, n)
            )
            btn.pack(side="left", padx=10, pady=10)
            self.estado_mesas[i] = {"estado": "Libre", "nombre": ""}
            self.botones_mesas[i] = btn

        # Botón Agregar mesa solo para admin
        if self.tipo == "Administrador":
            Button(self.parte_inferior, text="Agregar Mesa", width=16, font=("Arial", 12),
                   command=self.agregar_mesa).pack(pady=10)

    def cerrar_sesion(self, ventana):
        self.ventana.destroy()
        ventana.deiconify()

    def agregar_mesa(self):
        self.mesas += 1
        fila_index = (self.mesas - 1) // 3

        if fila_index >= len(self.filas):
            fila_frame = Frame(self.parte_superior, bg="#88FFB4")
            fila_frame.pack()
            self.filas.append(fila_frame)
        else:
            fila_frame = self.filas[fila_index]

        btn = Button(
            fila_frame,
            text=f"Mesa {self.mesas}",
            width=12,
            height=3,
            bg="green",
            command=lambda n=self.mesas: Reservar_mesa(self.ventana, self.tipo, self, n)
        )
        btn.pack(side="left", padx=10, pady=10)
        self.estado_mesas[self.mesas] = {"estado": "Libre", "nombre": ""}
        self.botones_mesas[self.mesas] = btn

#funcion que muestra mensaje de historia del restaurante
    def mostrar_info(self):
        ventana_info = Toplevel(self.ventana)
        ventana_info.title("Nuestra Historia")
        ventana_info.geometry("400x250")
        Label(
            ventana_info,
            text="Hace más de 20 años abrimos nuestras puertas\n"
                "con la idea de compartir el sabor de la cocina casera.\n\n"
                "Con el tiempo nos convertimos en un punto de encuentro\n"
                "para familias y amigos que buscan disfrutar\n"
                "de buena comida y momentos inolvidables.",
            wraplength=320,
            justify="center"
        ).pack(pady=20)
        Button(ventana_info, text="Cerrar", command=ventana_info.destroy).pack(pady=10)


class Reservar_mesa:
    def __init__(self, ventana, tipo, restaurante, mesa_id):
        self.tipo = tipo
        self.restaurante = restaurante
        self.mesa_id = mesa_id

        self.ventana = Toplevel(ventana)
        self.ventana.geometry("400x700")
        self.ventana.title("Reservar Mesa")

        fondo = "#88FFB4"

        # Frames
        self.parte_superior = Frame(self.ventana, bg=fondo)
        self.parte_superior.pack(fill="both", expand=True)

        self.parte_inferior = Frame(self.ventana, bg=fondo)
        self.parte_inferior.pack(fill="both", expand=True)

        self.parte_inferior.columnconfigure(0, weight=1)
        self.parte_inferior.columnconfigure(1, weight=1)

        # Título
        if self.tipo == "Administrador":
            Label(self.parte_superior, text=f"Admin - Mesa {mesa_id}", font=("Calisto MT", 30, "bold"), bg=fondo).pack(pady=20)
        else:
            Label(self.parte_superior, text=f"Reservar Mesa {mesa_id}", font=("Calisto MT", 30, "bold"), bg=fondo).pack(pady=20)

        # Imagen
        self.imagen = Image.open(r"reserva.png").resize((210, 220))
        self.render = ImageTk.PhotoImage(self.imagen)
        Label(self.parte_superior, image=self.render, bg=fondo).pack(expand=True, fill="both", side="top")
        
        # Entradas y botones
        if self.tipo == "Administrador":
            Button(self.parte_inferior, text="Desocupar", width=16, font=("Arial", 12),
                   command=self.desocupar).grid(row=2, column=0, columnspan=2, padx=35, pady=5)

            Button(self.parte_inferior, text="Eliminar", width=16, font=("Arial", 12),
                   command=self.eliminar).grid(row=4, column=0, columnspan=2, padx=35, pady=5)

            Button(self.parte_inferior, text="Atrás", width=16, font=("Arial", 12),
                   command=self.regresar).grid(row=6, column=0, columnspan=2, padx=35, pady=5)

        else:   
            Label(self.parte_inferior, text="Nombre:", font=("Arial", 16), bg=fondo).grid(row=0, column=0, pady=10, sticky="e")
            self.entry_nombre = Entry(self.parte_inferior, bd=0, width=14, font=("Arial", 16))
            self.entry_nombre.grid(row=0, column=1, padx=5, sticky="w")

            Button(self.parte_inferior, text="Guardar", width=16, font=("Arial", 12),
                   command=self.guardar).grid(row=2, column=0, columnspan=2, padx=35, pady=5)

            Button(self.parte_inferior, text="Atrás", width=16, font=("Arial", 12),
                   command=self.regresar).grid(row=4, column=0, columnspan=2, padx=35, pady=5)

    def guardar(self):
        nombre = self.entry_nombre.get().strip()
        if nombre:
            self.restaurante.estado_mesas[self.mesa_id] = {"estado": "Ocupada", "nombre": nombre}
            self.restaurante.botones_mesas[self.mesa_id].configure(bg="red")
        self.ventana.destroy()

    def desocupar(self):
        self.restaurante.estado_mesas[self.mesa_id] = {"estado": "Libre", "nombre": ""}
        self.restaurante.botones_mesas[self.mesa_id].configure(bg="green")
        self.ventana.destroy()

    def eliminar(self):
        btn = self.restaurante.botones_mesas[self.mesa_id]
        btn.destroy()
        del self.restaurante.botones_mesas[self.mesa_id]
        del self.restaurante.estado_mesas[self.mesa_id]
        self.ventana.destroy()

    def regresar(self):
        self.ventana.destroy()



ventana= Tk()
aplicacion=SeleccionarTipo(ventana)
ventana.mainloop()

