from tkinter import Tk, Toplevel, Label, Button, Entry, Frame, messagebox
from PIL import Image, ImageTk
from openpyxl import Workbook, load_workbook
import os

#creo los archivos de datos 
archivo_usuarios = "Datos_Usuarios.xlsx"
if os.path.exists(archivo_usuarios):
    wb = load_workbook(archivo_usuarios)
    ws = wb.active
else:
    wb = Workbook()
    ws = wb.active
    ws.append(["Usuario", "Contraseña", "Tipo"])
    wb.save(archivo_usuarios)

#Arranca el sistema

class SeleccionarTipo:
    def __init__(self, ventana):
        self.ventana= ventana
        self.ventana.geometry("400x700")
        self.ventana.title("Tipo de Usuario")

        fondo = "#88FFB4"

        #Dividimos en dos partes

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

        Label(self.parte_superior, text="¿Quién eres?", font=("Calisto MT", 30, "bold"), bg=fondo).pack(pady=10)

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
    def __init__(self, ventana, tipo):
        self.tipo=tipo
        self.ventana=Toplevel(ventana)
        self.ventana.geometry("400x700")
        self.ventana.title("Seleccione el tipo de usuario")

        fondo = "#88FFB4"

        #dividimos en dos partes 
       
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

class Registro:
        def __init__(self, ventana, tipo):
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

            if not usuario or not contrasena:
                messagebox.showwarning("Cuidado!", "Se deben completar ambos campos")
                return

            ws.append([usuario, contrasena, self.tipo])
            wb.save(archivo_usuarios)
            messagebox.showinfo("Datos", "Se guardaron los datos")

            self.entry_usuario.delete(0, "end")
            self.entry_contrasena.delete(0, "end")

            self.ventana.destroy()
            Login_Ingresar(ventana, self.tipo)

class Login_Ingresar:
    def __init__(self, ventana, tipo):
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
        self.tipo=tipo
        self.ventana= Toplevel(ventana)
        self.ventana.geometry("700x700")
        self.ventana.title("Restaurante")
        
        fondo = "#88FFB4"

        self.ventana.configure(bg=fondo)

        #dividimos
        self.parte_superior = Frame(self.ventana, bg=fondo)
        self.parte_superior.pack(fill="both", expand=True)

        self.parte_inferior = Frame(self.ventana, bg=fondo)
        self.parte_inferior.pack(fill="both", expand=True)

        self.parte_inferior.columnconfigure(0, weight=1)
        self.parte_inferior.columnconfigure(1, weight=1)

        #Agregamos la imagen del restaurante 
        self.imagen = Image.open(r"Logo.png").resize((170, 180))
        self.render = ImageTk.PhotoImage(self.imagen)
        Label(self.parte_superior, image=self.render, bg=fondo).pack(pady=10)

        Button(self.parte_inferior, text="Cerrar Sesion", width=16, font=("Arial", 12), command=lambda: self.cerrar_sesion(ventana)).pack(side="bottom", anchor="w", padx=25, pady=10)

        if self.tipo == "Administrador":
            #Agregar funciones que haga el admin, esto solo le aparece al administrador (ordenar)
            Button(self.parte_inferior, text="Agregar Mesa", width=16,font=("Arial", 12)).pack(side="bottom", anchor="n", padx=25, pady=10)

    def reserva(self,ventana):
        self.ventana.destroy()
        Reservar_mesa(ventana, self.tipo)
    
    def cerrar_sesion(self,ventana):
        self.ventana.destroy()
        ventana.deiconify()


#clase que va cuando apretamos la mesa, cuando se apreta el boton de la mesa se abre esto
class Reservar_mesa:
    def __init__(self, ventana, tipo):
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
        Label(self.parte_superior, text="Reservar Mesa:", font=("Calisto MT", 30, "bold"), bg=fondo).pack(side="top", pady=20)

        #Imagen
        self.imagen = Image.open(r"reserva.png").resize((210, 220))
        self.render = ImageTk.PhotoImage(self.imagen)
        Label(self.parte_superior, image=self.render, bg=fondo).pack(expand=True, fill="both", side="top")
        
        #Entradas

        Label(self.parte_inferior, text="Nombre:", font=("Arial", 16), bg=fondo).grid(row=0, column=0, pady=10, sticky="e")
        self.entry_nombre = Entry(self.parte_inferior, bd=0, width=14, font=("Arial", 16))
        self.entry_nombre .grid(row=0, column=1, columnspan=3, padx=5, sticky="w")

        #Iria un label que diga el numero de mesa y cantidad de personas de la que es la mesa

         #el primer boton es para guardar, llamaria a una funcion que guarda los datos y hace que cambie de color el boton
        Button(self.parte_inferior, text="Guardar", width=16, font=("Arial", 12), command=lambda: self.regresar(ventana)).grid(row=2, column=0, columnspan=4, padx=35, pady=5)

        Button(self.parte_inferior, text="Atras", width=16, font=("Arial", 12), command=lambda: self.regresar(ventana)).grid(row=8, column=0, columnspan=4, padx=35, pady=5)
    
    def regresar(self,ventana):
        self.ventana.destroy()
        Restaurante(ventana, self.tipo)

ventana= Tk()
aplicacion=SeleccionarTipo(ventana)
ventana.mainloop()