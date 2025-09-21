# restaurante.py
import tkinter as tk
from tkinter import Toplevel, Frame, Button, Label, Entry, messagebox

from tkinter import Toplevel, Frame, Button, Label, Entry, messagebox
from PIL import Image, ImageTk
from openpyxl import Workbook, load_workbook
import os
from reservas import Reservar_mesa

archivo_Reservas = "Datos_Reservas.xlsx"
if os.path.exists(archivo_Reservas):
    reservas = load_workbook(archivo_Reservas)
    wreservas = reservas.active
else:
    reservas = Workbook()
    wreservas = reservas.active
    wreservas.append(["ID", "Usuario", "Estado", "Capacidad"])
    reservas.save(archivo_Reservas)

class Restaurante:
    def __init__(self, ventana, tipo, usuario):
        #Constructores
        self.tipo = tipo
        self.usuario = usuario
        self.ventana = Toplevel(ventana)
        self.ventana.geometry("700x700")
        self.ventana.title("Restaurante")

        fondo = "#588E6B"
        color_botones= "#A7CBBF"

        self.ventana.configure(bg=fondo)

        #Dividimos pantalla en superiro e inferior
        self.parte_superior = Frame(self.ventana, bg=fondo)
        self.parte_superior.pack(fill="both", expand=True)

        self.parte_inferior = Frame(self.ventana, bg=fondo)
        self.parte_inferior.pack(fill="both", expand=True)

        # Botón de información
        self.canvas_info = tk.Canvas(self.parte_superior, width=30, height=30, highlightthickness=0, bg=fondo)
        self.canvas_info.place(relx=1.0, x=-15, y=15, anchor="ne")
        circulo = self.canvas_info.create_oval(2, 2, 28, 28, fill="#3498db", outline="#2980b9")
        texto = self.canvas_info.create_text(15, 15, text="i", fill="white", font=("Times New Roman", 14, "italic"))
        self.canvas_info.tag_bind(circulo, "<Button-1>", lambda e: self.mostrar_info())
        self.canvas_info.tag_bind(texto, "<Button-1>", lambda e: self.mostrar_info())

        # Imagen
        try:
            self.imagen = Image.open("Logo.png").resize((120, 140))
            self.render = ImageTk.PhotoImage(self.imagen)
            Label(self.parte_superior, image=self.render, bg=fondo).pack(pady=10)
        except Exception:
            Label(self.parte_superior, text="[Logo no encontrado]", bg=fondo, font=("Arial", 14, "italic"), fg="gray").pack(pady=10)

        #Fijamos las mesas principales en 6
        self.mesas = 9
        self.filas = [] 
        self.estado_mesas = {} #Diccionario donde guardamos el estado, el nombre y la capacidad
        self.botones_mesas = {} #Diccionario donde se guardan los botones

        # Crear mesas iniciales
        for i in range(1, self.mesas + 1):
            if (i - 1) % 3 == 0:
                fila_frame = Frame(self.parte_superior, bg=fondo)
                fila_frame.pack()
                self.filas.append(fila_frame)

            capacidad_defecto = 4  # capacidad por defecto

            btn = Button(
                self.filas[-1],
                text=f"Mesa {i}\nCapacidad: {capacidad_defecto}",
                width=12,
                height=3,
                bg="green",
                command=lambda n=i: Reservar_mesa(self.ventana, self.tipo, self, n)
            )
            btn.pack(side="left", padx=40, pady=10)

            # guardo el estado con capacidad
            self.estado_mesas[i] = {"estado": "Libre", "nombre": "", "capacidad": capacidad_defecto}
            self.botones_mesas[i] = btn

        # Cargar estado desde Excel
        archivo_Reservas = "Datos_Reservas.xlsx"
        if os.path.exists(archivo_Reservas):
            reservas = load_workbook(archivo_Reservas)
            hoja = reservas.active
            max_id = 0
            for fila in hoja.iter_rows(min_row=2, values_only=True):
                # Validar que la fila tenga al menos 4 columnas y que mesa_id no sea None
                if fila is None or len(fila) < 4 or fila[0] is None:
                    continue
                mesa_id, nombre, estado, capacidad = fila[:4]
                try:
                    mesa_id = int(mesa_id)
                except (TypeError, ValueError):
                    continue
                max_id = max(max_id, mesa_id)
                if mesa_id not in self.botones_mesas:
                    self.mesas += 1
                    fila_index = (self.mesas - 1) // 3
                    if fila_index >= len(self.filas):
                        fila_frame = Frame(self.parte_superior, bg=fondo)
                        fila_frame.pack()
                        self.filas.append(fila_frame)
                    else:
                        fila_frame = self.filas[fila_index]
            
                    btn = Button(
                        fila_frame,
                        text=f"Mesa {mesa_id}\nCapacidad: {capacidad}",
                        width=12,
                        height=3,
                        bg="green",
                        command=lambda n=mesa_id: Reservar_mesa(self.ventana, self.tipo, self, n)
                    )
                    btn.pack(side="left", padx=40, pady=10)
                    self.botones_mesas[mesa_id] = btn
            
                self.estado_mesas[mesa_id] = {"estado": estado, "nombre": nombre, "capacidad": capacidad}
                color = "red" if estado == "Ocupada" else "green"
                texto = f"Mesa {mesa_id}\nCapacidad: {capacidad}" if estado == "Libre" else f"Mesa {mesa_id}\n({nombre})\nCapacidad: {capacidad}"
                self.botones_mesas[mesa_id].configure(bg=color, text=texto)

        #Boton solo para administradores para que agregue mesas
        if self.tipo == "Administrador":
            Button(self.parte_inferior, text="Agregar Mesa", width=16, font=("Arial", 12),bg=color_botones, command=self.agregar_mesa).pack(pady=10)
    
        Button(self.parte_inferior, text="Cerrar Sesión", width=16, font=("Arial", 12),bg=color_botones, command=lambda: self.cerrar_sesion(ventana)).pack(pady=10)

    def cerrar_sesion(self, ventana):
        self.ventana.destroy()
        ventana.deiconify()

    def agregar_mesa(self):
            ventana_capacidad = Toplevel(self.ventana)
            ventana_capacidad.title("Capacidad de la Mesa")
            ventana_capacidad.geometry("300x150")
            
            Label(ventana_capacidad, text="Ingrese la capacidad:", font=("Arial", 14)).pack(pady=10)
            entry_capacidad = Entry(ventana_capacidad, font=("Arial", 14))
            entry_capacidad.pack(pady=5)

            def guardar_capacidad():
                capacidad = entry_capacidad.get()
                if not capacidad.isdigit() or int(capacidad) <= 0:
                    messagebox.showerror("Error", "Ingrese un número válido")
                    return

                self.mesas += 1
                fila_index = (self.mesas - 1) // 3

                if fila_index >= len(self.filas):
                    fila_frame = Frame(self.parte_superior, bg="#588E6B")
                    fila_frame.pack()
                    self.filas.append(fila_frame)
                else:
                    fila_frame = self.filas[fila_index]

                btn = Button(
                    fila_frame,
                    text=f"Mesa {self.mesas}\nCapacidad: {capacidad}",
                    width=12,
                    height=3,
                    bg="green",
                    command=lambda n=self.mesas: Reservar_mesa(self.ventana, self.tipo, self, n)
                )
                btn.pack(side="left", padx=40, pady=10)
                self.estado_mesas[self.mesas] = {"estado": "Libre", "nombre": "", "capacidad": capacidad}
                self.botones_mesas[self.mesas] = btn

                archivo_Reservas = "Datos_Reservas.xlsx"
                reservas = load_workbook(archivo_Reservas)
                hoja = reservas.active
                hoja.append([self.mesas, "", "Libre", capacidad])
                reservas.save(archivo_Reservas)

                ventana_capacidad.destroy()

            Button(ventana_capacidad, text="Guardar", command=guardar_capacidad).pack(pady=10)

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