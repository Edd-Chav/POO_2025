from tkinter import *
from tkinter import messagebox

# Simple button style settings (sólo colores y contraste básicos)
BTN_BG = '#2E86AB'         # azul suave
BTN_FG = 'white'
BTN_ACTIVE_BG = '#1B4F72'  # azul más oscuro cuando se presiona
BTN_SECONDARY_BG = '#F39C12'  # tono cálido para botones secundarios

def btn(parent, **kwargs):
    """Crea un Button con estilo consistente (sencillo y superficial)."""
    style = dict(bg=BTN_BG, fg=BTN_FG, activebackground=BTN_ACTIVE_BG,
                 activeforeground=BTN_FG, font=("Helvetica", 10, "bold"), bd=2, relief='raised')
    # allow caller to override style via kwargs
    style.update(kwargs)
    return Button(parent, **style)

class View:
    def __init__(self, ventana):
        self.ventana=ventana
        ventana.title("..: Coches System :..")
        ventana.geometry("800x700")
        ventana.resizable(False,False)
        self.menu_principal(ventana)

    @staticmethod
    def borrarPantalla(ventana):
        for widget in ventana.winfo_children():
            widget.destroy()
    @staticmethod
    def menu_principal(ventana):
        View.borrarPantalla(ventana)
        lbl_titulo=Label(ventana,text="..:: Menu Principal ::..",justify="center")
        lbl_titulo.pack(pady=10)
        btn_registro=btn(ventana,text="1.- Autos",justify="center",command=lambda: View.menu_autos(ventana))
        btn_registro.pack(pady=15)
        btn_login=btn(ventana,text="2.- Camionetas",justify="center", command=lambda: View.menu_camionetas(ventana))
        btn_login.pack(pady=15)
        btn_login=btn(ventana,text="3.- Camiones",justify="center", command=lambda: View.menu_camiones(ventana))
        btn_login.pack(pady=15)
        btn_salir=btn(ventana,text="4.- Salir",justify="center",command=ventana.quit, bg='#C0392B')
        btn_salir.pack(pady=15)
    
    @staticmethod
    def menu_autos(ventana):
        View.borrarPantalla(ventana)
        lbl_titulo=Label(ventana,text="..:: Menú Autos ::..",justify="center")
        lbl_titulo.pack(pady=15)
        btn_registro=btn(ventana,text="1.- Insertar",justify="center",command=lambda: View.auto_registro(ventana))
        btn_registro.pack(pady=10)
        btn_login=btn(ventana,text="2.- Consultar",justify="center", command=lambda: View.consultar_autos(ventana))
        btn_login.pack(pady=10)
        btn_salir=btn(ventana,text="3.- Actualizar",justify="center",command=lambda: View.cambiar_autos(ventana))
        btn_salir.pack(pady=10)
        btn_salir=btn(ventana,text="4.- Eliminar",justify="center",command=lambda: View.borrar_autos(ventana), bg='#922B21')
        btn_salir.pack(pady=10)
        btn_volver=btn(ventana,text="5.- Regresar",command=lambda: View.menu_principal(ventana), bg=BTN_SECONDARY_BG)
        btn_volver.pack(pady=10)
    
    @staticmethod
    def menu_camionetas(ventana):
        View.borrarPantalla(ventana)
        lbl_titulo=Label(ventana,text="..:: Menu Camionetas ::..",justify="center")
        lbl_titulo.pack(pady=15)
        btn_registro=btn(ventana,text="1.- Insertar",justify="center",command=lambda: ""(ventana))
        btn_registro.pack(pady=10)
        btn_login=btn(ventana,text="2.- Consultar",justify="center", command=lambda: ""(ventana))
        btn_login.pack(pady=10)
        btn_salir=btn(ventana,text="3.- Actualizar",justify="center",command=lambda: ""(ventana))
        btn_salir.pack(pady=10)
        btn_salir=btn(ventana,text="4.- Eliminar",justify="center",command=lambda:""(ventana))
        btn_salir.pack(pady=10)
        btn_volver=btn(ventana,text="5.- Regresar",command=lambda: View.menu_principal(ventana), bg=BTN_SECONDARY_BG)
        btn_volver.pack(pady=10)

    @staticmethod
    def menu_camiones(ventana):
        View.borrarPantalla(ventana)
        lbl_titulo=Label(ventana,text="..:: Menu Camiones ::..",justify="center")
        lbl_titulo.pack(pady=15)
        btn_registro=btn(ventana,text="1.- Insertar",justify="center",command=lambda: ""(ventana))
        btn_registro.pack(pady=10)
        btn_login=btn(ventana,text="2.- Consultar",justify="center", command=lambda: ""(ventana))
        btn_login.pack(pady=10)
        btn_salir=btn(ventana,text="3.- Actualizar",justify="center",command=lambda: ""(ventana))
        btn_salir.pack(pady=10)
        btn_salir=btn(ventana,text="4.- Eliminar",justify="center",command=lambda:""(ventana))
        btn_salir.pack(pady=10)
        btn_volver=btn(ventana,text="5.- Regresar",command=lambda: View.menu_principal(ventana), bg=BTN_SECONDARY_BG)
        btn_volver.pack(pady=10)

    @staticmethod
    def auto_registro(ventana):
        View.borrarPantalla(ventana)
        lbl_titulo=Label(ventana,text="...: Registro de Autos :...", justify="center")
        lbl_titulo.pack(pady=15)

        lbl_marca=Label(ventana,text="Marca: ",justify="center")
        lbl_marca.pack(pady=10)
        txt_marca=Entry(ventana)
        txt_marca.pack(pady=10)
        txt_marca.focus()
        
        lbl_color=Label(ventana,text="Color: ",justify="center")
        lbl_color.pack(pady=10)
        txt_color=Entry(ventana)
        txt_color.pack(pady=10)
        
        lbl_modelo=Label(ventana,text="Modelo: ",justify="center")
        lbl_modelo.pack(pady=10)
        txt_modelo=Entry(ventana)
        txt_modelo.pack(pady=10)
        
        lbl_velocidad=Label(ventana,text="Velocidad: ",justify="center")
        lbl_velocidad.pack(pady=10)
        txt_velocidad=Entry(ventana)
        txt_velocidad.pack(pady=10)

        lbl_potencia=Label(ventana,text="Potencia: ",justify="center")
        lbl_potencia.pack(pady=10)
        txt_potencia=Entry(ventana)
        txt_potencia.pack(pady=10)

        lbl_nro_plazas=Label(ventana,text="Numero de Plazas: ",justify="center")
        lbl_nro_plazas.pack(pady=10)
        txt_nro_plazas=Entry(ventana)
        txt_nro_plazas.pack(pady=10)

        btn_guardar=btn(ventana,text="Guardar", command=lambda: [messagebox.showinfo("Guardar", "Auto registrado correctamente"), View.menu_autos(ventana)])
        btn_guardar.pack(pady=10)
        btn_volver=btn(ventana,text="Volver",command=lambda: View.menu_autos(ventana), bg=BTN_SECONDARY_BG)
        btn_volver.pack(pady=10)

    @staticmethod
    def consultar_autos(ventana):
        View.borrarPantalla(ventana)
        lbl_titulo=Label(ventana,text="...: Consultar Autos :...", justify="center")
        lbl_titulo.pack(pady=15)
        
        # Aquí iría la lógica para mostrar los autos
        messagebox.showinfo("Consultar Autos", "Listado de autos")
        View.menu_autos(ventana)
    
    @staticmethod
    def cambiar_autos(ventana):
        View.borrarPantalla(ventana)
        lbl_titulo=Label(ventana,text="...: Actualizar Autos :...", justify="center")
        lbl_titulo.pack(pady=15)
        
        lbl_id=Label(ventana,text="ID del Auto: ",justify="center")
        lbl_id.pack(pady=10)
        txt_id=Entry(ventana)
        txt_id.pack(pady=10)
        txt_id.focus()
        
        lbl_marca=Label(ventana,text="Nueva Marca: ",justify="center")
        lbl_marca.pack(pady=10)
        txt_marca=Entry(ventana)
        txt_marca.pack(pady=10)
        
        lbl_color=Label(ventana,text="Nuevo Color: ",justify="center")
        lbl_color.pack(pady=10)
        txt_color=Entry(ventana)
        txt_color.pack(pady=10)
        
        btn_actualizar=btn(ventana,text="Actualizar", command=lambda: [messagebox.showinfo("Actualizar", "Auto actualizado correctamente"), View.menu_autos(ventana)])
        btn_actualizar.pack(pady=10)
        btn_volver=btn(ventana,text="Volver",command=lambda: View.menu_autos(ventana), bg=BTN_SECONDARY_BG)
        btn_volver.pack(pady=10)
    
    @staticmethod
    def borrar_autos(ventana):
        View.borrarPantalla(ventana)
        lbl_titulo=Label(ventana,text="...: Eliminar Autos :...", justify="center")
        lbl_titulo.pack(pady=15)
        
        lbl_id=Label(ventana,text="ID del Auto a Eliminar: ",justify="center")
        lbl_id.pack(pady=10)
        txt_id=Entry(ventana)
        txt_id.pack(pady=10)
        txt_id.focus()
        
        btn_eliminar=btn(ventana,text="Eliminar", command=lambda: [messagebox.showinfo("Eliminar", "Auto eliminado correctamente"), View.menu_autos(ventana)], bg='#922B21')
        btn_eliminar.pack(pady=10)
        btn_volver=btn(ventana,text="Volver",command=lambda: View.menu_autos(ventana), bg=BTN_SECONDARY_BG)
        btn_volver.pack(pady=10)
