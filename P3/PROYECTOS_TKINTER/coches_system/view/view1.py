from tkinter import *
from tkinter import messagebox
from controller import controller1

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
        lbl_titulo=Label(ventana,text="..:: Menú Principal ::..",justify="center")
        lbl_titulo.pack(pady=10)
        btn_registro=Button(ventana,text="1.- Autos",justify="center",command=lambda: View.menu_autos(ventana))
        btn_registro.pack(pady=15)
        btn_login=Button(ventana,text="2.- Camionetas",justify="center", command=lambda: View.menu_camionetas(ventana))
        btn_login.pack(pady=15)
        btn_login=Button(ventana,text="3.- Camiones",justify="center", command=lambda: View.menu_camiones(ventana))
        btn_login.pack(pady=15)
        btn_salir=Button(ventana,text="4.- Salir",justify="center",command=ventana.quit)
        btn_salir.pack(pady=15)
    
    @staticmethod
    def menu_autos(ventana):
        View.borrarPantalla(ventana)
        lbl_titulo=Label(ventana,text="..:: Menú Autos ::..",justify="center")
        lbl_titulo.pack(pady=15)
        btn_registro=Button(ventana,text="1.- Insertar",justify="center",command=lambda: View.auto_registro(ventana))
        btn_registro.pack(pady=10)
        btn_login=Button(ventana,text="2.- Consultar",justify="center", command=lambda: View.auto_consultar(ventana))
        btn_login.pack(pady=10)
        btn_salir=Button(ventana,text="3.- Actualizar",justify="center",command=lambda: View.auto_id(ventana,"cambiar"))
        btn_salir.pack(pady=10)
        btn_salir=Button(ventana,text="4.- Eliminar",justify="center",command=lambda:View.auto_id(ventana,"eliminar"))
        btn_salir.pack(pady=10)
        btn_volver=Button(ventana,text="5.- Regresar",command=lambda: View.menu_principal(ventana))
        btn_volver.pack(pady=10)
    
    @staticmethod
    def menu_camionetas(ventana):
        View.borrarPantalla(ventana)
        lbl_titulo=Label(ventana,text="..:: Menú Camionetas ::..",justify="center")
        lbl_titulo.pack(pady=15)
        btn_registro=Button(ventana,text="1.- Insertar",justify="center",command=lambda: View.camioneta_registro(ventana))
        btn_registro.pack(pady=10)
        btn_login=Button(ventana,text="2.- Consultar",justify="center", command=lambda: View.camioneta_consultar(ventana))
        btn_login.pack(pady=10)
        btn_salir=Button(ventana,text="3.- Actualizar",justify="center",command=lambda: View.camioenta_id(ventana,"cambiar"))
        btn_salir.pack(pady=10)
        btn_salir=Button(ventana,text="4.- Eliminar",justify="center",command=lambda:View.camioenta_id(ventana,"eliminar"))
        btn_salir.pack(pady=10)
        btn_volver=Button(ventana,text="5.- Regresar",command=lambda: View.menu_principal(ventana))
        btn_volver.pack(pady=10)

    @staticmethod
    def menu_camiones(ventana):
        View.borrarPantalla(ventana)
        lbl_titulo=Label(ventana,text="..:: Menú Camiones ::..",justify="center")
        lbl_titulo.pack(pady=15)
        btn_registro=Button(ventana,text="1.- Insertar",justify="center",command=lambda: View.camioneta_registro(ventana))
        btn_registro.pack(pady=10)
        btn_login=Button(ventana,text="2.- Consultar",justify="center", command=lambda: View.camioneta_consultar(ventana))
        btn_login.pack(pady=10)
        btn_salir=Button(ventana,text="3.- Actualizar",justify="center",command=lambda: View.camioenta_id(ventana, "cambiar"))
        btn_salir.pack(pady=10)
        btn_salir=Button(ventana,text="4.- Eliminar",justify="center",command=lambda: View.camioenta_id(ventana, "eliminar"))
        btn_salir.pack(pady=10)
        btn_volver=Button(ventana,text="5.- Regresar",command=lambda: View.menu_principal(ventana))
        btn_volver.pack(pady=10)

    @staticmethod
    def auto_registro(ventana):
        View.borrarPantalla(ventana)
        lbl_titulo = Label(ventana, text="...: Registro de Autos :...", justify="center")
        lbl_titulo.pack(pady=15)

        lbl_marca = Label(ventana, text="Marca: ", justify="center")
        lbl_marca.pack(pady=5)
        txt_marca = Entry(ventana)
        txt_marca.pack(pady=5)
        txt_marca.focus()
        
        lbl_color = Label(ventana, text="Color: ", justify="center")
        lbl_color.pack(pady=5)
        txt_color = Entry(ventana)
        txt_color.pack(pady=5)
        
        lbl_modelo = Label(ventana, text="Modelo: ", justify="center")
        lbl_modelo.pack(pady=5)
        txt_modelo = Entry(ventana)
        txt_modelo.pack(pady=5)
        
        lbl_velocidad = Label(ventana, text="Velocidad: ", justify="center")
        lbl_velocidad.pack(pady=5)
        txt_velocidad = Entry(ventana)
        txt_velocidad.pack(pady=5)

        lbl_potencia = Label(ventana, text="Potencia: ", justify="center")
        lbl_potencia.pack(pady=5)
        txt_potencia = Entry(ventana)
        txt_potencia.pack(pady=5)

        lbl_nro_plazas = Label(ventana, text="Numero de Plazas: ", justify="center")
        lbl_nro_plazas.pack(pady=5)
        txt_nro_plazas = Entry(ventana)
        txt_nro_plazas.pack(pady=5)


        btn_guardar = Button(ventana, text="Guardar", command=lambda: [
            controller1.Controller.registro_auto(
                txt_marca.get(), 
                txt_color.get(), 
                txt_modelo.get(), 
                txt_velocidad.get(), 
                txt_potencia.get(), 
                txt_nro_plazas.get()
            ),
            View.menu_autos(ventana)
        ])
        btn_guardar.pack(pady=10)
        
        btn_volver = Button(ventana, text="Volver", command=lambda: View.menu_autos(ventana))
        btn_volver.pack(pady=10)

    @staticmethod
    def auto_consultar(ventana):
        View.borrarPantalla(ventana)
        lbl_titulo = Label(ventana, text="...: Consulta de Autos :...", justify="center")
        lbl_titulo.pack(pady=15)

        txt_consulta = Text(ventana, height=20, width=80)
        txt_consulta.pack(pady=10)

        encabezado = "ID | Marca | Color | Modelo | Vel. | Potencia | Plazas\n"
        encabezado += "-" * 80 + "\n"
        txt_consulta.insert(END, encabezado)

        # ADAPTACIÓN: Llamamos al controlador para obtener los datos
        # Nota: Asegúrate de que Controller.consultar_autos() retorne la lista de autos (return autos)
        registros = controller1.Controller.consultar_autos()
        
        if registros and len(registros) > 0:
            for fila in registros:
                texto_fila = f"{fila[0]} | {fila[1]} | {fila[2]} | {fila[3]} | {fila[4]} | {fila[5]} | {fila[6]}\n"
                txt_consulta.insert(END, texto_fila)
        else:
            pass
        txt_consulta.config(state=DISABLED) 

        btn_volver = Button(ventana, text="Regresar", command=lambda: View.menu_autos(ventana))
        btn_volver.pack(pady=10)

    @staticmethod
    def auto_id(ventana, tipo):
        View.borrarPantalla(ventana)
        accion = "Modificar" if tipo == "cambiar" else "Eliminar"
        lbl_titulo = Label(ventana, text=f"...: Ingresa ID del Auto a {accion} :...", justify="center")
        lbl_titulo.pack(pady=15)

        lbl_id = Label(ventana, text="ID:", justify="center")
        lbl_id.pack(pady=5)
        
        txt_id = Entry(ventana, justify="center", width=10)
        txt_id.focus()
        txt_id.pack(pady=5)

        if tipo == "cambiar":
            Button(ventana, text="Buscar", command=lambda: View.cambiar_auto(ventana, txt_id.get())).pack(pady=10)
        elif tipo == "eliminar":
            Button(ventana, text="Buscar", command=lambda: View.eliminar_auto(ventana, txt_id.get())).pack(pady=10)

        btn_regresar = Button(ventana, text="Regresar", command=lambda: View.menu_autos(ventana))
        btn_regresar.pack(pady=10)

    @staticmethod
    def cambiar_auto(ventana, id_auto):
        View.borrarPantalla(ventana)
        lbl_titulo = Label(ventana, text=f"...: Modificación de Auto ID: {id_auto} :...", justify="center")
        lbl_titulo.pack(pady=15)

        lbl_marca = Label(ventana, text="Nueva Marca: ", justify="center")
        lbl_marca.pack(pady=5)
        txt_marca = Entry(ventana)
        txt_marca.pack(pady=5)
        txt_marca.focus()
        
        lbl_color = Label(ventana, text="Nuevo Color: ", justify="center")
        lbl_color.pack(pady=5)
        txt_color = Entry(ventana)
        txt_color.pack(pady=5)
        
        lbl_modelo = Label(ventana, text="Nuevo Modelo: ", justify="center")
        lbl_modelo.pack(pady=5)
        txt_modelo = Entry(ventana)
        txt_modelo.pack(pady=5)
        
        lbl_velocidad = Label(ventana, text="Nueva Velocidad: ", justify="center")
        lbl_velocidad.pack(pady=5)
        txt_velocidad = Entry(ventana)
        txt_velocidad.pack(pady=5)

        lbl_potencia = Label(ventana, text="Nueva Potencia: ", justify="center")
        lbl_potencia.pack(pady=5)
        txt_potencia = Entry(ventana)
        txt_potencia.pack(pady=5)

        lbl_nro_plazas = Label(ventana, text="Nuevo Numero de Plazas: ", justify="center")
        lbl_nro_plazas.pack(pady=5)
        txt_nro_plazas = Entry(ventana)
        txt_nro_plazas.pack(pady=5)

        # Llamada al controlador para actualizar
        btn_guardar = Button(ventana, text="Guardar Cambios", command=lambda: [
            controller1.Controller.cambiar_auto(
                txt_marca.get(),
                txt_color.get(),
                txt_modelo.get(),
                txt_velocidad.get(),
                txt_potencia.get(),
                txt_nro_plazas.get(),
                id_auto
            ),
            View.menu_autos(ventana)
        ])
        btn_guardar.pack(pady=10)
        
        btn_volver = Button(ventana, text="Volver", command=lambda: View.menu_autos(ventana))
        btn_volver.pack(pady=10)

    @staticmethod
    def eliminar_auto(ventana, id_auto):
        View.borrarPantalla(ventana)
        lbl_titulo = Label(ventana, text=f"...: Eliminar Auto {id_auto} :...", justify="center")
        lbl_titulo.pack(pady=15)

        lbl_confirmacion = Label(ventana, text="¿Estás seguro de que deseas eliminar este registro?", justify="center")
        lbl_confirmacion.pack(pady=10)

        btn_borrar = Button(ventana, text="Confirmar Eliminar", command=lambda: [
            controller1.Controller.borrar_auto(id_auto), 
            View.menu_autos(ventana)])
        btn_borrar.pack(pady=10)
        
        btn_volver = Button(ventana, text="Cancelar / Volver", command=lambda: View.menu_autos(ventana))
        btn_volver.pack(pady=10)

    @staticmethod
    def camioneta_registro(ventana):
        View.borrarPantalla(ventana)
        lbl_titulo=Label(ventana,text="...: Registro de Camionetas :...", justify="center")
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

        lbl_cerrada=Label(ventana,text="¿Es Cerrada? (Si/No): ", justify="center")
        lbl_cerrada.pack(pady=10)
        txt_cerrada=Entry(ventana)
        txt_cerrada.pack(pady=10)

        btn_guardar=Button(ventana,text="Guardar", command=lambda: [messagebox.showinfo("Guardar", "Camioneta registrada correctamente"), View.menu_camionetas(ventana)])
        btn_guardar.pack(pady=10)
        btn_volver=Button(ventana,text="Volver",command=lambda: View.menu_camionetas(ventana))
        btn_volver.pack(pady=10)

    @staticmethod
    def camioneta_consultar(ventana):
        View.borrarPantalla(ventana)
        lbl_titulo = Label(ventana, text="...: Consulta de Camionetas :...", justify="center")
        lbl_titulo.pack(pady=15)

        txt_consulta = Text(ventana, height=20, width=80)
        txt_consulta.pack(pady=10)

        datos_simulados = (
            "ID | Marca | Color | Modelo | Vel. | Potencia | Plazas | Cerrada/Abierta\n"
            "--------------------------------------------------------------------------------\n"
            "1 | Ford | Rojo | Mustang | 250 | 450 | 4 | Si\n"
            "2 | Honda | Azul | Civic | 180 | 158 | 5 | No\n"
            "3 | Toyota | Blanco | Corolla | 190 | 169 | 5 | Si\n"
            "4 | Tesla | Negro | Model 3 | 261 | 450 | 5 | No\n"
        )
        
        txt_consulta.insert(END, datos_simulados)
        txt_consulta.config(state=DISABLED) 

        btn_volver = Button(ventana, text="Regresar", command=lambda: View.menu_camionetas(ventana))
        btn_volver.pack(pady=10)

    @staticmethod
    def camioenta_id(ventana,tipo):
        View.borrarPantalla(ventana)
        lbl_titulo=Label(ventana,text="...: Ingresa ID de la Camioneta :...", justify="center")
        lbl_titulo.pack(pady=15)

        id=IntVar()
        txt_id=Entry(ventana,textvariable=id, justify="center", width=5)
        txt_id.focus()
        txt_id.pack(pady=5)

        if tipo=="cambiar":
            Button(ventana,text="Buscar", command=lambda:View.cambiar_camioneta(ventana,id.get())).pack(pady=5)
        elif tipo=="eliminar":
            Button(ventana,text="Buscar", command=lambda:View.eliminar_camioneta(ventana,id.get())).pack(pady=5)
        
        btn_regresar=Button(ventana,text="Regresar", command=lambda: View.menu_camiones(ventana))
        btn_regresar.pack(pady=5)

    @staticmethod
    def cambiar_camioneta(ventana, id):
        View.borrarPantalla(ventana)
        lbl_titulo=Label(ventana,text=f"...: Modificacion de Camioneta {id} :...", justify="center")
        lbl_titulo.pack(pady=15)

        lbl_marca=Label(ventana,text="Nueva Marca: ",justify="center")
        lbl_marca.pack(pady=10)
        txt_marca=Entry(ventana)
        txt_marca.pack(pady=10)
        txt_marca.focus()
        
        lbl_color=Label(ventana,text="NuevoColor: ",justify="center")
        lbl_color.pack(pady=10)
        txt_color=Entry(ventana)
        txt_color.pack(pady=10)
        
        lbl_modelo=Label(ventana,text="Nuevo Modelo: ",justify="center")
        lbl_modelo.pack(pady=10)
        txt_modelo=Entry(ventana)
        txt_modelo.pack(pady=10)
        
        lbl_velocidad=Label(ventana,text="NuevaVelocidad: ",justify="center")
        lbl_velocidad.pack(pady=10)
        txt_velocidad=Entry(ventana)
        txt_velocidad.pack(pady=10)

        lbl_potencia=Label(ventana,text="Nueva Potencia: ",justify="center")
        lbl_potencia.pack(pady=10)
        txt_potencia=Entry(ventana)
        txt_potencia.pack(pady=10)

        lbl_nro_plazas=Label(ventana,text="Nuevo Numero de Plazas: ",justify="center")
        lbl_nro_plazas.pack(pady=10)
        txt_nro_plazas=Entry(ventana)
        txt_nro_plazas.pack(pady=10)

        lbl_cerrada=Label(ventana,text="¿Es Cerrada? (Si/No): ", justify="center")
        lbl_cerrada.pack(pady=10)
        txt_cerrada=Entry(ventana)
        txt_cerrada.pack(pady=10)

        btn_guardar=Button(ventana,text="Guardar", command=lambda: [messagebox.showinfo("Guardar", f"Camioneta {id} modificada correctamente"), View.menu_camionetas(ventana)])
        btn_guardar.pack(pady=10)
        btn_volver=Button(ventana,text="Volver",command=lambda: View.menu_camionetas(ventana))
        btn_volver.pack(pady=10)

    @staticmethod
    def eliminar_camioneta(ventana, id):
        View.borrarPantalla(ventana)
        lbl_titulo=Label(ventana,text=f"...: Eliminar Camioneta {id} :...", justify="center")
        lbl_titulo.pack(pady=15)

        btn_borrar=Button(ventana,text="Eliminar", command=lambda: [messagebox.showinfo("Eliminar", f"Camioneta {id} eliminada correctamente"), View.menu_camionetas(ventana)])
        btn_borrar.pack(pady=10)
        btn_volver=Button(ventana,text="Volver",command=lambda: View.menu_camionetas(ventana))
        btn_volver.pack(pady=10)

    @staticmethod
    def camion_registro(ventana):
        View.borrarPantalla(ventana)
        lbl_titulo=Label(ventana,text="...: Registro de Camiones :...", justify="center")
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

        lbl_ejes=Label(ventana,text="Ejes: ", justify="center")
        lbl_ejes.pack(pady=10)
        txt_ejes=Entry(ventana)
        txt_ejes.pack(pady=10)

        lbl_capacidad=Label(ventana,text="Capacidad: ", justify="center")
        lbl_capacidad.pack(pady=10)
        txt_capacidad=Entry(ventana)
        txt_capacidad.pack(pady=10)

        btn_guardar=Button(ventana,text="Guardar", command=lambda: [messagebox.showinfo("Guardar", "Camion registrada correctamente"), View.menu_camiones(ventana)])
        btn_guardar.pack(pady=10)
        btn_volver=Button(ventana,text="Volver",command=lambda: View.menu_camiones(ventana))
        btn_volver.pack(pady=10)

    @staticmethod
    def camion_consultar(ventana):
        View.borrarPantalla(ventana)
        lbl_titulo = Label(ventana, text="...: Consulta de Camiones :...", justify="center")
        lbl_titulo.pack(pady=15)

        txt_consulta = Text(ventana, height=20, width=80)
        txt_consulta.pack(pady=10)

        datos_simulados = (
            "ID | Marca | Color | Modelo | Vel. | Potencia | Plazas | Ejes | Capacidad |\n"
            "--------------------------------------------------------------------------------\n"
            "1 | Ford | Rojo | Mustang | 250 | 450 | 4 | 3 | 1000 |\n"
            "2 | Honda | Azul | Civic | 180 | 158 | 5 | 2 | 800 |\n"
            "3 | Toyota | Blanco | Corolla | 190 | 169 | 5 | 2 | 900 |\n"
            "4 | Tesla | Negro | Model 3 | 261 | 450 | 5 | 2 | 1200 |\n"
        )
        
        txt_consulta.insert(END, datos_simulados)
        txt_consulta.config(state=DISABLED) 

        btn_volver = Button(ventana, text="Regresar", command=lambda: View.menu_camiones(ventana))
        btn_volver.pack(pady=10)

    @staticmethod
    def camion_id(ventana,tipo):
        View.borrarPantalla(ventana)
        lbl_titulo=Label(ventana,text="...: Ingresa ID de la Camion :...", justify="center")
        lbl_titulo.pack(pady=15)

        id=IntVar()
        txt_id=Entry(ventana,textvariable=id, justify="center", width=5)
        txt_id.focus()
        txt_id.pack(pady=5)

        if tipo=="cambiar":
            Button(ventana,text="Buscar", command=lambda:View.cambiar_camiones(ventana,id.get())).pack(pady=5)
        elif tipo=="eliminar":
            Button(ventana,text="Buscar", command=lambda:View.eliminar_camiones(ventana,id.get())).pack(pady=5)

        btn_regresar=Button(ventana,text="Regresar", command=lambda: View.menu_camiones(ventana))
        btn_regresar.pack(pady=5)

    @staticmethod
    def cambiar_camiones(ventana, id):
        View.borrarPantalla(ventana)
        lbl_titulo=Label(ventana,text=f"...: Modificacion de Camion {id} :...", justify="center")
        lbl_titulo.pack(pady=15)

        lbl_marca=Label(ventana,text="Nueva Marca: ",justify="center")
        lbl_marca.pack(pady=10)
        txt_marca=Entry(ventana)
        txt_marca.pack(pady=10)
        txt_marca.focus()
        
        lbl_color=Label(ventana,text="NuevoColor: ",justify="center")
        lbl_color.pack(pady=10)
        txt_color=Entry(ventana)
        txt_color.pack(pady=10)
        
        lbl_modelo=Label(ventana,text="Nuevo Modelo: ",justify="center")
        lbl_modelo.pack(pady=10)
        txt_modelo=Entry(ventana)
        txt_modelo.pack(pady=10)
        
        lbl_velocidad=Label(ventana,text="NuevaVelocidad: ",justify="center")
        lbl_velocidad.pack(pady=10)
        txt_velocidad=Entry(ventana)
        txt_velocidad.pack(pady=10)

        lbl_potencia=Label(ventana,text="Nueva Potencia: ",justify="center")
        lbl_potencia.pack(pady=10)
        txt_potencia=Entry(ventana)
        txt_potencia.pack(pady=10)

        lbl_nro_plazas=Label(ventana,text="Nuevo Numero de Plazas: ",justify="center")
        lbl_nro_plazas.pack(pady=10)
        txt_nro_plazas=Entry(ventana)
        txt_nro_plazas.pack(pady=10)

        lbl_ejes=Label(ventana,text="Nuevos Ejes: ", justify="center")
        lbl_ejes.pack(pady=10)
        txt_ejes=Entry(ventana)
        txt_ejes.pack(pady=10)

        lbl_capacidad=Label(ventana,text="Nueva Capacidad: ", justify="center")
        lbl_capacidad.pack(pady=10)
        txt_capacidad=Entry(ventana)
        txt_capacidad.pack(pady=10)

        btn_guardar=Button(ventana,text="Guardar", command=lambda: [messagebox.showinfo("Guardar", f"Camion {id} modificado correctamente"), View.menu_camiones(ventana)])
        btn_guardar.pack(pady=10)
        btn_volver=Button(ventana,text="Volver",command=lambda: View.menu_camiones(ventana))
        btn_volver.pack(pady=10)

    @staticmethod
    def eliminar_camiones(ventana, id):
        View.borrarPantalla(ventana)
        lbl_titulo=Label(ventana,text=f"...: Eliminar Camion {id} :...", justify="center")
        lbl_titulo.pack(pady=15)

        btn_borrar=Button(ventana,text="Eliminar", command=lambda: [messagebox.showinfo("Eliminar", f"Camion {id} eliminado correctamente"), View.menu_camiones(ventana)])
        btn_borrar.pack(pady=10)
        btn_volver=Button(ventana,text="Volver",command=lambda: View.menu_camiones(ventana))
        btn_volver.pack(pady=10)