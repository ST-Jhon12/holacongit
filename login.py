from tkinter import ttk
import tkinter as tk


class login(ttk.Frame):
    def __init__(self, ventana):
        super().__init__(ventana)

        self.ven = ventana
        self.ven.title("Sistema de Login")
        self.ven.configure(bg="#f3f6fb")
        self.ven.resizable(False, False)
        self.ven.iconbitmap("iconos/iconoxd.ico")
        self.ven.overrideredirect(True)

        style = ttk.Style(self)
        style.configure("Login.TFrame", background="#f3f6fb")
        self.configure(style="Login.TFrame")
        self.pack(fill="both", expand=True)

        self.card = tk.Frame(
            self,
            bg="#ffffff",
            highlightthickness=0,
        )
        self.card.pack(fill="both", expand=True)

        self.boton_cerrar = tk.Button(
            self.card,
            text="X",
            command=self.ven.destroy,
            font=("Segoe UI", 10, "bold"),
            fg="#ffffff",
            bg="#d64545",
            activeforeground="#ffffff",
            activebackground="#b83232",
            relief="flat",
            cursor="hand2",
            borderwidth=0,
            padx=10,
            pady=6,
        )
        self.boton_cerrar.place(relx=1, x=-8, y=8, anchor="ne")

        self.user = tk.StringVar()
        self.pas = tk.StringVar()

        self.img = tk.PhotoImage(file="imagenes/logo.png")

        self.lblLogo = tk.Label(self.card, image=self.img, bg="#ffffff")
        self.lblLogo.pack(pady=(28, 10))

        self.lblTitulo = tk.Label(
            self.card,
            text="Sistema de Login",
            font=("Segoe UI", 21, "bold"),
            fg="#172b4d",
            bg="#ffffff",
        )
        self.lblTitulo.pack()

        self.lblSubtitulo = tk.Label(
            self.card,
            text="Ingresa tus datos para continuar",
            font=("Segoe UI", 10),
            fg="#68778d",
            bg="#ffffff",
        )
        self.lblSubtitulo.pack(pady=(6, 0))

        form = tk.Frame(self.card, bg="#ffffff")
        form.pack(fill="x", padx=34, pady=(28, 0))
        form.columnconfigure(0, weight=1)

        self.lblUser = tk.Label(
            form,
            text="Usuario",
            font=("Segoe UI", 10, "bold"),
            fg="#344563",
            bg="#ffffff",
        )
        self.lblUser.grid(row=0, column=0, sticky="w", pady=(0, 7))

        self.txtUser = tk.Entry(
            form,
            textvariable=self.user,
            font=("Segoe UI", 11),
            relief="solid",
            bd=1,
            highlightthickness=1,
            highlightbackground="#dfe5ee",
            highlightcolor="#4778d0",
        )
        self.txtUser.grid(row=1, column=0, sticky="ew", ipady=8, pady=(0, 18))

        self.lblPass = tk.Label(
            form,
            text="Contraseña",
            font=("Segoe UI", 10, "bold"),
            fg="#344563",
            bg="#ffffff",
        )
        self.lblPass.grid(row=2, column=0, sticky="w", pady=(0, 7))

        self.txtPass = tk.Entry(
            form,
            textvariable=self.pas,
            font=("Segoe UI", 11),
            show="*",
            relief="solid",
            bd=1,
            highlightthickness=1,
            highlightbackground="#dfe5ee",
            highlightcolor="#4778d0",
        )
        self.txtPass.grid(row=3, column=0, sticky="ew", ipady=8)

        self.btnLogin = tk.Button(
            self.card,
            text="Iniciar sesión",
            font=("Segoe UI", 11, "bold"),
            fg="#ffffff",
            bg="#3267c8",
            activeforeground="#ffffff",
            activebackground="#2858ae",
            relief="flat",
            cursor="hand2",
            pady=10,
        )
        self.btnLogin.pack(fill="x", padx=34, pady=(28, 30))

        window_width = 430
        window_height = 590
        screen_x = (self.ven.winfo_screenwidth() - window_width) // 2
        screen_y = (self.ven.winfo_screenheight() - window_height) // 2
        self.ven.geometry(
            f"{window_width}x{window_height}+{screen_x}+{screen_y}"
        )