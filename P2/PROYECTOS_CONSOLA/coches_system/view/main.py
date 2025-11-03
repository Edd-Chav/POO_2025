#Instanciar los objetos para posterior implementarlos 
from model import coches,cochesBD


import os

def verificar(respuesta, tipo):
        if respuesta:
            print(f"\n\t...¡{tipo} insertado correctamente!...")
        else:
            print(f"\n\t...No fue posible agregar el {tipo} correctamente, vuelva a intentar ...") 
            

def borrarPantalla():
    os.system("cls")

def esperarTecla():
    input("\n\t\t Oprima tecla para continuar ...")

def datos_autos(tipo):
    borrarPantalla()
    print(f"\n\t ...Ingresar los datos del Vehiculo de tipo: {tipo}")
    marca=input("Marca: ").upper()
    color=input("Color: ").upper()
    modelo=input("Modelo: ").upper()
    velocidad=int(input("Velocidad: "))
    potencia=int(input("Potencia: "))
    plazas=int(input("No. de plazas: "))
    return marca,color,modelo,velocidad,potencia,plazas

def imprimir_datos_vehiculo(marca,color,modelo,velocidad,potencia,plazas):
    borrarPantalla()
    print(f"\n\tDatos del Vehiculo: \n Marca:{marca} \n color: {color} \n Modelo: {modelo} \n velocidad: {velocidad} \n caballaje: {potencia} \n plazas: {plazas}")

def autos():
    marca,color,modelo,velocidad,potencia,plazas=datos_autos("Auto")
    coche=coches.Coches(marca,color,modelo,velocidad,potencia,plazas)
    borrarPantalla()
    imprimir_datos_vehiculo(coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas)
    #Agregar el registro a la BD
    auto=cochesBD.Autos(coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas)
    respuesta=auto.insertar()
    verificar(respuesta, "Auto")


def camionetas():
    marca,color,modelo,velocidad,potencia,plazas=datos_autos("Camioneta")
    traccion=input("Traccion: ").upper()
    cerrada=input("¿Cerrada (Si/No)?: ").upper().strip()
    if cerrada=="SI":
        cerrada=True
    else:
        cerrada=False    
    coche=coches.Camionetas(marca,color,modelo,velocidad,potencia,plazas,traccion,cerrada)
    imprimir_datos_vehiculo(coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas)
    print(f"traccion: {coche.traccion}\n cerrada: {coche.cerrada}")
    #Acceder a la BD
    respuesta=cochesBD.Camionetas.insertar(coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas,coche.traccion,coche.cerrada)
    verificar(respuesta, "Camioneta")

def menu_camionetas():
    while True:
        borrarPantalla()
        opcion==menu_acciones("Camionetas")
        if opcion=="1" or opcion=="Insertar":
            marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada=camionetas()
            #Acceder  a la BD


def camiones():
    marca,color,modelo,velocidad,potencia,plazas=datos_autos("Camiones")
    eje=int(input("No. de ejes: "))
    capacidadCarga=int(input("Capacidad de carga: "))
    coche=coches.Camiones(marca,color,modelo,velocidad,potencia,plazas,eje,capacidadCarga)
    imprimir_datos_vehiculo(coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas)
    print(f"#Ejes: {coche.eje}\n Capacidad de carga: {coche.capacidadCarga}")
    #Acceder a la BD
    respuesta=cochesBD.Camiones.insertar(coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas,coche.eje,coche.capacidadCarga)
    verificar(respuesta, "Camion")

def menu_acciones(tipo):
    print(f"\n\t...Menu de acciones para {tipo}...\n\t1.-Insertar \n\t2.-Consultar \n\t3.-Actualizar \n\t4.-Eliminar \n\t5.- Regresar")
    opcion=input("\n\t\tElige una opción: ").upper().strip()
    return opcion

def menu_autos():
    borrarPantalla()
    while True:
        opcion=menu_acciones("Autos")
        if opcion=="1" or opcion=="INSERTAR":
            marca, color, modelo, velocidad, caballaje, plazas=autos()
            auto=cochesBD.Autos
            (marca, color, modelo, velocidad, caballaje, plazas)
            print("insertar")
            respuesta=auto.insertar()
            verificar(respuesta, "Auto")
        
        elif opcion=="2" or opcion=="CONSULTAR":
            borrarPantalla()
            registros=cochesBD.Autos.consultar()
            if len(registros)>0:
                num_auto=1
                for fila in registros:
                    print(f"Auto #{num_auto}\n ID: {fila[0]} \n Marca: {fila[1]} \n Color: {fila[2]} \n Modelo: {fila[3]} \n Velocidad: {fila[4]} \n Caballaje: {fila[5]} \n Plazas: {fila[6]}\n")
                    num_auto+=1
                    esperarTecla() 
            else:
                print("\n\t\tNo hay registros")
            print("consultar")
        elif opcion=="3" or opcion=="ACTUALIZAR":
            borrarPantalla()
            id=input("ID del auto a actualizar: ").strip()
            marca, color, modelo, velocidad, caballaje, plazas=autos()
            respuesta=cochesBD.Autos.actualizar(marca, color, modelo, velocidad, caballaje, plazas,id)
            verificar(respuesta, "Auto")

            print("actualizar")
        elif opcion=="4" or opcion=="ELIMINAR":
            borrarPantalla()
            id=input("ID del auto a actualizar: ").strip()
            respuesta=cochesBD.Autos.eliminar(marca, color, modelo, velocidad, caballaje, plazas,id)
            verificar(respuesta, "Auto")
            print("eliminar")

def main():
  opcion=True
  while opcion:
    borrarPantalla()
    opcion=input("\n\t\t ::: Menu Principal ::.\n\t1.- Autos\n\t2.-Camionetas\n\t3.-Camiones\n\t4.-Salir\n\tElige un opción: ").lower().strip()
    match opcion:
        case "1":
            autos()
            esperarTecla()
        case "2":
            camionetas()
            esperarTecla()  
        case "3":
            camiones()
            esperarTecla()
        case "4":
            borrarPantalla()
            input("\n\t\tSalir del Sistema")
            opcion=False   
        case _:
            input("Opcion invalidad ... vuelva a intertarlo ... ")     
            esperarTecla() 

if __name__=="main_":main()