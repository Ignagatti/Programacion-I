from tkinter import Tk
from usuarios import SeleccionarTipo

#Iniciar la app
ventana = Tk()
aplicacion = SeleccionarTipo(ventana)
ventana.mainloop()