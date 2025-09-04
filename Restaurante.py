from tkinter import Tk, Toplevel, Label, Button, Entry, Frame, messagebox
from PIL import Image, ImageTk
from openpyxl import Workbook, load_workbook
import os

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

    def regresar(self,ventana):
        self.ventana.destroy()
        ventana.deiconify()
        
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
        self.estado_mesas = {}   # {1: "Libre", 2: "Libre", ...}
        self.botones_mesas = {}  # Guardamos los botones para cambiar color

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
                bg="green",  # verde = libre
                command=lambda n=i: Reservar_mesa(self.ventana, self.tipo, self, n)
            )
            btn.pack(side="left", padx=10, pady=10)
            self.estado_mesas[i] = "Libre"
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
        self.estado_mesas[self.mesas] = "Libre"
        self.botones_mesas[self.mesas] = btn


class Reservar_mesa:
    def __init__(self, ventana, tipo, restaurante, numero_mesa):
        self.tipo = tipo
        self.restaurante = restaurante
        self.numero_mesa = numero_mesa

        self.ventana = Toplevel(ventana)
        self.ventana.geometry("400x400")
        self.ventana.title(f"Mesa {numero_mesa}")

        fondo = "#88FFB4"
        self.ventana.configure(bg=fondo)

        # Título con número de mesa
        Label(self.ventana, text=f"Mesa {numero_mesa}", font=("Calisto MT", 24, "bold"), bg=fondo).pack(pady=20)

        if self.tipo == "Administrador":
            Button(self.ventana, text="Desocupar", width=16, font=("Arial", 12),
                   command=self.desocupar).pack(pady=5)
            Button(self.ventana, text="Modificar", width=16, font=("Arial", 12),
                   command=self.modificar).pack(pady=5)
            Button(self.ventana, text="Eliminar", width=16, font=("Arial", 12),
                   command=self.eliminar).pack(pady=5)
            Button(self.ventana, text="Atras", width=16, font=("Arial", 12),
                   command=self.ventana.destroy).pack(pady=5)
        else:
            Label(self.ventana, text="Nombre:", font=("Arial", 16), bg=fondo).pack(pady=10)
            self.entry_nombre = Entry(self.ventana, font=("Arial", 16))
            self.entry_nombre.pack(pady=5)

            Button(self.ventana, text="Guardar", width=16, font=("Arial", 12),
                   command=self.guardar).pack(pady=5)
            Button(self.ventana, text="Atras", width=16, font=("Arial", 12),
                   command=self.ventana.destroy).pack(pady=5)

    def guardar(self):
        nombre = self.entry_nombre.get()
        if nombre.strip() != "":
            self.restaurante.estado_mesas[self.numero_mesa] = "Ocupada"
            self.restaurante.botones_mesas[self.numero_mesa].configure(bg="red")
            self.ventana.destroy()

    def desocupar(self):
        self.restaurante.estado_mesas[self.numero_mesa] = "Libre"
        self.restaurante.botones_mesas[self.numero_mesa].configure(bg="green")
        self.ventana.destroy()

    def modificar(self):
        # Para implementar: modificar datos de la reserva
        self.ventana.destroy()

    def eliminar(self):
        btn = self.restaurante.botones_mesas[self.numero_mesa]
        btn.destroy()
        del self.restaurante.estado_mesas[self.numero_mesa]
        del self.restaurante.botones_mesas[self.numero_mesa]
        self.ventana.destroy()
        
ventana= Tk()
aplicacion=SeleccionarTipo(ventana)
ventana.mainloop()

