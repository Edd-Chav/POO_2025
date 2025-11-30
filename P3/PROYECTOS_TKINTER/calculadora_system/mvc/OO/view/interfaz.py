from tkinter import *
from tkinter import messagebox
from controller import funciones
from model import operaciones

class Vista:
    def __init__(self,ventana):
        ventana.title("Calculadora básica")
        ventana.geometry("800x600")
        ventana.resizable(False,False)
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
        marco_numeros=Frame(ventana,width=70,height=40,bg="lightblue",relief=SOLID)
        marco_numeros.pack_propagate(False)
        marco_numeros.pack(pady=10)
        marco_operaciones=Frame(ventana,width=400,height=200,bg="lightblue",relief=SOLID)
        marco_operaciones.pack_propagate(False)
        marco_operaciones.pack(pady=10)
        numero1=Entry(marco_numeros,textvariable=n1,width=5,justify="right")
        numero1.focus()
        numero1.pack(side="top",anchor="center")

        numero2=Entry(marco_numeros,textvariable=n2,width=5,justify="right")
        numero2.pack(side="top",anchor="center")

        btn_suma=Button(marco_operaciones,text=" + ",command=lambda: funciones.Funciones.insertar(n1.get(),n2.get(),"+"))
        btn_suma.grid(column=0,row=0,padx=3,pady=3)
        btn_resta=Button(marco_operaciones,text=" - ",command=lambda: funciones.Funciones.insertar(n1.get(),n2.get(),"-"))
        btn_resta.grid(column=1,row=0,padx=3,pady=3)

        btn_mult=Button(marco_operaciones,text=" * ",command=lambda: funciones.Funciones.insertar(n1.get(),n2.get(),"x"))
        btn_mult.grid(column=2,row=0,padx=3,pady=3)

        btn_division=Button(marco_operaciones,text=" / ",command=lambda: funciones.Funciones.insertar(n1.get(),n2.get(),"/"))
        btn_division.grid(column=3,row=0,padx=3,pady=3)

        btn_salir=Button(ventana,text="salir",command=ventana.quit)
        btn_salir.pack()
    
 
    @staticmethod    
    def menuPrincipal(ventana):
        menuBar=Menu(ventana)
        ventana.config(menu=menuBar)
        operacionesMenu = Menu(menuBar , tearoff=False)
        menuBar.add_cascade(label="Operaciones",menu=operacionesMenu)
        operacionesMenu.add_command(label="Agregar",command=lambda:Vista.interfaz_principal(ventana) )
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
            btn_volver=Button(ventana,text="Volver",command=lambda: Vista.interfaz_principal(ventana))
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
       

        btn_volver=Button(ventana,text="Volver",command=lambda: Vista.interfaz_principal(ventana))
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
        
            btn_volver=Button(ventana,text="Volver",command=lambda: Vista.interfaz_principal(ventana))
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
        