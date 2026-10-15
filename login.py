from tkinter import ttk
import tkinter as tk

class login(ttk.Frame):
    def __init__(self, ventana):
        super().__init__(ventana)

        self.ven = ventana
        self.ven.geometry("350x450+800+150")
        self.ven.title("Sistema de Login")
        self.ven.config(bg="#0000ff")
        self.ven.resizable(False, False)
        self.ven.wm_attributes("-alpha", 0.9)
        self.ven.iconbitmap("iconos/iconoxd.ico")        

        #Quitamos la barra de menu
        self.ven.overrideredirect(True)

        #creamos un boton para cerrar la ventana
        def Salir():
            self.ven.destroy()
        self.boton_cerrar = tk.Button(self.ven, text="X", width=6, height=2, command= Salir)
        self.boton_cerrar.place(x=300, y=5)
        self.boton_cerrar.config(bg="#ff0000")
