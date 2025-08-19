from tkinter import Tk, Label, Button, Entry, Frame, messagebox, mainloop
from PIL import Image, ImageTk
from openpyxl import Workbook, load_workbook
import os

class Login:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.geometry("400x700")
        self.ventana.title("Seleccione tipo de usuario")

        fondo= "#88FFB4"

        self.frame_superior= Frame(self.ventana)
        self.frame_superior.configure(bg=fondo)
        self.frame_superior.pack(fill="both", expand=True)

        self.frame_inferior= Frame(self.ventana)
        self.frame_inferior.configure(bg=fondo)
        self.frame_inferior.pack(fill="both", expand=True)

        self.frame_inferior.columnconfigure(0, weight=1)
        self.frame_inferior.columnconfigure(1, weight=1)

        #Imagen

        self.titulo_eleccion=Label(self.frame_superior, text="Bienvenido", font=("Calisto MT", 30, "bold"), bg=fondo)
        self.titulo_eleccion.pack(pady=10)

        btn_cliente = Button(self.frame_inferior, text="Registrar", width=35, height=2, font=("Arial", 14), command=lambda: self.eleccion_ingresar("Registrar"))
        btn_cliente.pack(pady=10)

        btn_usuario = Button(self.frame_inferior, text="Ingresar", width=35, height=2, font=("Arial", 14), command=lambda: self.eleccion_ingresar("Ingresar"))
        btn_usuario.pack(pady=10)

        self.ventana.mainloop()

    def eleccion_ingresar(self):
        self.ventana.destroy()  # Cierra la ventana 
        
        #Login_Ingresar()

    def eleccion_registar(self):
        self.ventana.destroy()
        #Login_Registrar()

    
