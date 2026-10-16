import tkinter as tk
from tkinter import Frame, PhotoImage, messagebox, ttk

class SistemaPrincipal:
    def __init__(self):
        self.ventP = tk.Tk()
        
        self.ventP.title("Sistema Principal")
        self.ventP.geometry("1000x600+400+100")
        self.ventP.iconbitmap("./iconos/iconoxd.ico")
        self.ventP.config(bg="#ffffff")
        #self.objeto = DatabaseManager("./BaseDatos/sistema.db")
        self.ventP.resizable(False, False)
        self.ventP.protocol("WM_DELETE_WINDOW", self.confirmar_salida)
        self.ventP.wm_attributes("-alpha", 0.93)
 
        # Menú vertical
        self.menu_vertical = tk.Frame(self.ventP,  bg="#1f3c88", width=200)
        self.menu_vertical.pack(side="left", fill="y")

        # logo institucional
        self.logo = tk.PhotoImage(file="./imagenes/logo.png")
        label_img = tk.Label(
            self.menu_vertical,
            image=self.logo,
            text="MI SISTEMA",
            bg="#1f3c88",
            fg="white",
        )
        label_img.pack(pady=5)

        # Frame para las interfaces
        self.contenido = tk.Frame(self.ventP, bg="#fff")
        self.contenido.pack(side="right", fill="both", expand=True)

        #creacion de objetos
        #self.usuario = UsuarioView(self.contenido, self.objeto, ventana=self.ventP)
        #self.sumita = SumaView(self.contenido, self.objeto)
        #self.triangulito = TrianguloView(self.contenido, self.objeto)

        # Botones del menú
        btn_inicio = tk.Button(
            self.menu_vertical,
            text="🏠 Inicio",
            command=self.mostrar_inicio,
            width=20,
        )
        btn_inicio.pack(pady=10)
        btn_inicio.config(
            bg="#2c5282",
            fg="#ffffff",
            font=("Verdana", 12, "bold"),
            bd=0,
            cursor="hand2",
            activebackground="#1a365d",
            activeforeground="white",
        )

        btn_registro = tk.Button(
            self.menu_vertical,
            text="👤Registro de Usuarios",
            command="",
            width=20,
        )  # self.mostrar_inicio)
        btn_registro.pack(pady=10)
        btn_registro.config(
            bg="#2c5282",
            fg="#ffffff",
            font=("Verdana", 12, "bold"),
            bd=0,
            cursor="hand2",
            activebackground="#1a365d",
            activeforeground="white",
        )

        btn_suma = tk.Button(
            self.menu_vertical,
            text="➕Sumar Dos Números",
            command="",
            width=20,
        )
        btn_suma.pack(pady=10)
        btn_suma.config(
            bg="#2c5282",
            fg="#ffffff",
            font=("Verdana", 12, "bold"),
            bd=0,
            cursor="hand2",
            activebackground="#1a365d",
            activeforeground="white",
        )

        btn_triangulo = tk.Button(
            self.menu_vertical,
            text="🔺Triángulo",
            command=self.mostrar_triangulo,
            width=20,
        )
        btn_triangulo.pack(pady=10)
        btn_triangulo.config(
            bg="#2c5282",
            fg="#ffffff",
            font=("Verdana", 12, "bold"),
            bd=0,
            cursor="hand2",
            activebackground="#1a365d",
            activeforeground="white",
        )

        btn_salir = tk.Button(
            self.menu_vertical,
            text="🛑Salir",
            command=self.confirmar_salida,
            width=20,
        )
        btn_salir.pack(pady=10)
        btn_salir.config(
            bg="#2c5282",
            fg="#ffffff",
            font=("Verdana", 12, "bold"),
            bd=0,
            cursor="hand2",
            activebackground="#1a365d",
            activeforeground="white",
        )

        self.mostrar_inicio()

        self.ventP.mainloop()
 
    def mostrar_inicio(self):
        # Limpiar contenido
        for widget in self.contenido.winfo_children():
            widget.destroy()
    
        # Fondo pastel
        self.contenido.config(bg="#eaf3ff")
    
        # Frame centrado
        frame_central = Frame(self.contenido, bg="#eaf3ff")
        frame_central.place(relx=0.5, rely=0.5, anchor="center")
    
        self.img_inicio = PhotoImage(file="./imagenes/logo.png")
        label_img = tk.Label(frame_central, image=self.img_inicio, bg="#eaf3ff")
        label_img.pack(pady=10)
    
        # Título principal
        titulo = tk.Label(
            frame_central,
            text="Bienvenido al Sistema Principal",
            font=("Verdana", 24, "bold"),
            bg="#eaf3ff",
            fg="#1f3c88"
        )
        titulo.pack(pady=10)
    
        # Subtítulo
        subtitulo = tk.Label(
            frame_central,
            text="Sistema de Gestión Académica",
            font=("Verdana", 14),
            bg="#eaf3ff",
            fg="#555"
        )
        subtitulo.pack(pady=5)
    
        # Línea decorativa
        linea = Frame(frame_central, bg="#3273db", height=3, width=400)
        linea.pack(pady=15)

    def mostrar_triangulo(self):
        triangulito = getattr(self, "triangulito", None)
        if triangulito is None:
            messagebox.showinfo(
                "Vista no disponible",
                "La vista del triángulo todavía no está conectada.",
            )
            return

        triangulito.mostrar()

    def confirmar_salida(self):
        respuesta = messagebox.askyesno(
            "Confirmar salida",
            "¿Estás seguro de salir del sistema?"
        )
    
        if respuesta:  # Si presiona "Sí"
            self.ventP.destroy()