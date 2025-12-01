from tkinter import *
from tkinter import messagebox, ttk
import tkinter.font as tkfont
from controller import funciones
from model import operaciones

class Vista:
    def __init__(self,ventana):
        ventana.title("Calculadora bonita")
        ventana.geometry("420x480")
        ventana.resizable(False,False)
        self.bg_color = "#f0f4f8"
        self.panel_color = "#ffffff"
        self.primary = "#4a90e2"
        self.accent = "#50c878"
        ventana.configure(bg=self.bg_color)
        self.default_font = tkfont.Font(family="Segoe UI", size=11)
        self.big_font = tkfont.Font(family="Segoe UI", size=14, weight="bold")
        self.int_principal(ventana)
    
    @staticmethod
    def borrarPantalla(ventana):
        for widget in ventana.winfo_children():
            widget.destroy()
    
    @staticmethod
    def int_principal(ventana):
        Vista.borrarPantalla(ventana)
        Vista.menuPrincipal(ventana)

        n1=IntVar()
        n2=IntVar()

        # Header
        header = Frame(ventana, bg=ventana['bg'])
        header.pack(pady=(12,6))
        lbl_title = Label(header, text="Calculadora", bg=ventana['bg'], fg="#333333", font=("Segoe UI",18,"bold"))
        lbl_title.pack()

        # Input panel
        panel = Frame(ventana, bg="#ffffff", bd=0, relief=FLAT)
        panel.pack(padx=20, pady=10, fill="x")
        panel.config(highlightbackground="#e2e8f0", highlightthickness=1)

        lbl1 = Label(panel, text="Número 1", bg="#ffffff", fg="#444444", font=("Segoe UI",10))
        lbl1.pack(anchor="w", padx=12, pady=(12,0))
        numero1 = Entry(panel, textvariable=n1, justify="right", font=("Segoe UI",14), bd=0, bg="#f7fafc")
        numero1.pack(fill="x", padx=12, pady=(4,10))
        numero1.focus()

        lbl2 = Label(panel, text="Número 2", bg="#ffffff", fg="#444444", font=("Segoe UI",10))
        lbl2.pack(anchor="w", padx=12)
        numero2 = Entry(panel, textvariable=n2, justify="right", font=("Segoe UI",14), bd=0, bg="#f7fafc")
        numero2.pack(fill="x", padx=12, pady=(4,12))

        # Buttons frame
        botones = Frame(ventana, bg=ventana['bg'])
        botones.pack(pady=8)

        btn_opts = [('+', lambda: funciones.Funciones.insertar(n1.get(),n2.get(),"+")),
                    ('-', lambda: funciones.Funciones.insertar(n1.get(),n2.get(),"-")),
                    ('×', lambda: funciones.Funciones.insertar(n1.get(),n2.get(),"x")),
                    ('÷', lambda: funciones.Funciones.insertar(n1.get(),n2.get(),"/"))]

        btn_style = { 'font': ("Segoe UI", 14, 'bold'), 'width':5, 'height':1, 'bd':0 }

        for i, (txt, cmd) in enumerate(btn_opts):
            b = Button(botones, text=txt, command=cmd, bg="#4a90e2", fg="#ffffff", activebackground="#357ab8", **btn_style)
            b.grid(row=0, column=i, padx=6, pady=6)

        # Action row
        actions = Frame(ventana, bg=ventana['bg'])
        actions.pack(pady=(6,12))

        btn_clear = Button(actions, text="Limpiar", command=lambda: (numero1.delete(0,END), numero2.delete(0,END)), bg="#f44336", fg="#ffffff", **btn_style)
        btn_clear.grid(row=0, column=0, padx=8)

        btn_consultar = Button(actions, text="Consultar", command=lambda: Vista.consultar(ventana), bg="#6c757d", fg="#ffffff", **btn_style)
        btn_consultar.grid(row=0, column=1, padx=8)

        btn_salir = Button(actions, text="Salir", command=ventana.quit, bg="#2d3748", fg="#ffffff", **btn_style)
        btn_salir.grid(row=0, column=2, padx=8)
    
    @staticmethod    
    def menuPrincipal(ventana):
        menuBar=Menu(ventana)
        ventana.config(menu=menuBar)
        operacionesMenu = Menu(menuBar , tearoff=False)
        menuBar.add_cascade(label="Operaciones",menu=operacionesMenu)
        operacionesMenu.add_command(label="Agregar",command=lambda:Vista.int_principal(ventana) )
        operacionesMenu.add_command(label="Consultar",command=lambda:Vista.consultar(ventana))
        operacionesMenu.add_command(label="Cambiar",command=lambda:Vista.buscar_id(ventana,"cambiar"))
        operacionesMenu.add_command(label="Borrar",command=lambda: Vista.buscar_id(ventana,"borrar"))
        operacionesMenu.add_separator()
        operacionesMenu.add_command(label="Salir",command=ventana.quit)

  
    @staticmethod
    def eliminar_id(ventana,id_):
        registro=operaciones.Operaciones.consultar_id(id_)
        if registro is None:
            messagebox.showinfo(icon="info",message="No existe esta operacion en la BD")
        else:
            Vista.borrarPantalla(ventana)
            Vista.menuPrincipal(ventana)
            lbl_1=Label(ventana,text="..:: Eliminar una operacion ::..")
            lbl_1.pack(pady=10)
            lbl_2=Label(ventana,text="ID de la Operacion: ")
            lbl_2.pack(pady=5)
            id=IntVar()
            txt_id_eliminar=Entry(ventana,textvariable=id,width=5)
            id.set(id_)
            txt_id_eliminar.focus()
            txt_id_eliminar.pack(pady=5)
            btn_eliminar=Button(ventana,text="Eliminar",command= lambda: funciones.Funciones.eliminar(id.get()))
            btn_eliminar.pack()
            btn_volver=Button(ventana,text="Volver",command=lambda: Vista.int_principal(ventana))
            btn_volver.pack()
        
  
    @staticmethod
    def consultar(ventana):
        Vista.borrarPantalla(ventana)
        Vista.menuPrincipal(ventana)
        
        lbl_1=Label(ventana,text=".:: Lista de Operaciones ::.")
        lbl_1.pack()
        
        ops=funciones.Funciones.consultar()
        operacion=0
        if len(ops)>0:
            for i in ops:
                operacion+=1
                lbl_operaciones=Label(ventana,text=f"")    
                lbl_operaciones.config(text=f"Operacion: {operacion} ID: {i[0]} Fecha de Creación: {i[1]} \n Operacion: {i[2]}{i[4]}{i[3]}={i[5]}")
                lbl_operaciones.pack()
        else:
            messagebox.showinfo(icon="info",message="No existen operaciones guardadas en la BD")
       

        btn_volver=Button(ventana,text="Volver",command=lambda: Vista.int_principal(ventana))
        btn_volver.pack()
    
    @staticmethod
    def cambiar_id(ventana,id_):
        registro=operaciones.Operaciones.consultar_id(id_)
        if registro is None:
            messagebox.showinfo(icon="info",message="No existe esta operacion en la BD")
        else:
            Vista.borrarPantalla(ventana)
            Vista.menuPrincipal(ventana)
        
            lbl_1=Label(ventana,text=".:: Cambiar una Operacion ::.")
            lbl_1.pack(pady=10)
            lbl_id=Label(ventana,text="ID de la operación: ")
            lbl_id.pack(pady=5)
            id=IntVar()
            txt_id=Entry(ventana,textvariable=id,width=5,justify="right",state="readonly")
            id.set(id_)
            txt_id.focus()
            txt_id.pack(pady=5)
            
            lbl_num1=Label(ventana,text="Nuevo numero 1: ")
            lbl_num1.pack(pady=5)
            n1=IntVar()
            numero1=Entry(ventana,textvariable=n1,width=10,justify="right")
            n1.set(registro[2])
            numero1.pack(pady=5)           
            
            lbl_num2=Label(ventana,text="Nuevo numero 2: ")
            lbl_num2.pack(pady=5) 
            n2=IntVar()
            numero2=Entry(ventana,textvariable=n2,width=10,justify="right")
            n2.set(registro[3])
            numero2.pack(pady=5)
                
            lbl_signo=Label(ventana,text="Nuevo Signo: ")
            lbl_signo.pack(pady=5)
            signo=StringVar()
            txt_nuevo_signo=Entry(ventana,textvariable=signo,width=10,justify="center")
            signo.set(registro[4])
            txt_nuevo_signo.pack(pady=5)
        
            lbl_resultado=Label(ventana,text="Nuevo resultado: ")
            lbl_resultado.pack(pady=5)
        
            resultado=DoubleVar()
            txt_nuevo_resultado=Entry(ventana,textvariable=resultado,width=10,justify="right")
            resultado.set(registro[5])
            txt_nuevo_resultado.pack(pady=5)
        
            btn_guardar=Button(ventana,text="Guardar",command=lambda:funciones.Funciones.actualizar(n1.get(),n2.get(),signo.get(),resultado.get(),id.get()))
            btn_guardar.pack(pady=5)
        
            btn_volver=Button(ventana,text="Volver",command=lambda: Vista.int_principal(ventana))
            btn_volver.pack(pady=5)
    
    @staticmethod
    def buscar_id(ventana,tipo):
        Vista.borrarPantalla(ventana)
        Vista.menuPrincipal(ventana)
        
        lbl_1=Label(ventana,text=".:: Buscar una Operacion ::.")
        lbl_1.pack(pady=10)
       
       
        lbl_id=Label(ventana,text="ID de la operación a buscar: ")
        lbl_id.pack(pady=5)
        id=IntVar()
        txt_id=Entry(ventana,textvariable=id,width=5,justify="right")
        txt_id.focus()
        txt_id.pack(pady=5)
        
        if tipo=="cambiar":
            Button(ventana,text="Buscar",command=lambda: Vista.cambiar_id(ventana, id.get(),)).pack(pady=5)
        elif tipo=="borrar":
            Button(ventana,text="Buscar",command=lambda: Vista.eliminar_id(ventana, id.get(),)).pack(pady=5)
        
    