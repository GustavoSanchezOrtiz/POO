#Instanciar los objetos para posterior implementarlos 
from model import cochesbd
from model import coches
import os

def esperar_tecla():
    input("Oprima una tecla para continuar...")

def limpiar_pantalla():
    os.system("cls")

def datos_autos(tipo):
    limpiar_pantalla()
    print(f"\n\t ...Ingresar los datos del Vehiculo de tipo: {tipo}")
    marca=input("Marca: ").upper()
    color=input("Color: ").upper()
    modelo=input("Modelo: ").upper()
    velocidad=int(input("Velocidad: "))
    potencia=int(input("Potencia: "))
    plazas=int(input("No. de plazas: "))
    return marca,color,modelo,velocidad,potencia,plazas

def imprimir_datos_vehiculo(marca,color,modelo,velocidad,potencia,plazas):
    limpiar_pantalla()
    print(f"\n\tDatos del Vehiculo: \n Marca:{marca} \n color: {color} \n Modelo: {modelo} \n velocidad: {velocidad} \n caballaje: {potencia} \n plazas: {plazas}")

def respuesta_a_datos_insertados_en_bd(resp):
    if resp:
        input("Conexion valida con la base de datos")
    else:
        input("Error al conectar con la base de datos")

def autos():
    marca,color,modelo,velocidad,potencia,plazas=datos_autos(tipo="Auto")
    coche=coches.Coches(marca,color,modelo,velocidad,potencia,plazas)
    imprimir_datos_vehiculo(coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas)
    coche_insertar= cochesbd.autos(marca,color,modelo,velocidad,potencia,plazas)
    resp = cochesbd.autos.insertar_en_bd(coche_insertar)
    respuesta_a_datos_insertados_en_bd(resp)



def camionetas():
    marca,color,modelo,velocidad,caballaje,plazas=datos_autos(tipo="Camioneta")
    traccion=input("Traccion: ").upper()
    cerrada=input("¿Cerrada (Si/No)?: ").upper().strip()
    if cerrada=="SI":
        cerrada=True
    else:
        cerrada=False    
    coche=coches.Camionetas(marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada)
    imprimir_datos_vehiculo(coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas)
    print(f"traccion: {coche.traccion}\n cerrada: {coche.cerrada}")
    resp = cochesbd.camionetas.insertar_en_bd(color, marca, modelo, velocidad, caballaje, plazas, traccion, cerrada)
    respuesta_a_datos_insertados_en_bd(resp)

def camiones():
    marca,color,modelo,velocidad,caballaje,plazas=datos_autos(tipo="Camiones")
    eje=int(input("No. de ejes: "))
    capacidadCarga=int(input("Capacidad de carga: "))
    coche=coches.Camiones(marca,color,modelo,velocidad,caballaje,plazas,eje,capacidadCarga)
    imprimir_datos_vehiculo(coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas)
    print(f"#Ejes: {coche.eje}\n Capacidad de carga: {coche.capacidadCarga}")
    resp = cochesbd.camiones.insertar_en_bd(color, marca, modelo, velocidad, caballaje, plazas, eje, capacidadCarga)
    respuesta_a_datos_insertados_en_bd(resp)

def menu_seleccion_vehiculo():
    os.system("cls")
    opcion=input("\n\t\t ::: Menu Principal ::.\n\t1.- Autos\n\t2.-Camionetas\n\t3.-Camiones\n\t4.-Salir\n\tElige un opción: ").lower().strip()
    match opcion:
        case "1":
            menu_autos()
            esperar_tecla()
        case "2":
            
            menu_camionetas()
            esperar_tecla()  
        case "3":
            menu_camiones()
            esperar_tecla()
        case "4":
            input("Salir del Sistema")
            opcion=False   
        case _:
            input("Opcion invalidad ... vuelva a intertarlo ... ")     

def menu_acciones(tipo):
    os.system("cls")
    opcion=input(f"\n\t\t ::: Menu de {tipo} ::.\n\t1.- Agregar\n\t2.-Consultar\n\t3.-Actualizar\n\t4.-Eliminar\n\t5.-Regresar \n\t\tElige un opción: ").lower().strip()
    return opcion

def menu_autos():
    while True:
        opcion = menu_acciones(tipo="Autos")
        if opcion == "1" or opcion == "AGREGAR":
            limpiar_pantalla()
            print("\n\t...Agregar un nuevo Auto")
            autos()
            
            esperar_tecla()
        elif opcion == "2" or opcion == "CONSULTAR":
            limpiar_pantalla()
            print("\n\t...Listado de Autos en la Base de Datos")
            registros = cochesbd.autos.consultar_en_bd()
            if len(registros) > 0:
                num_auto = 1 
                for registro in registros:
                    print(f" {num_auto}. con ID {registro[0]}\n Marca: {registro[1]}\n Color: {registro[2]}\n Modelo: {registro[3]}\n Velocidad: {registro[4]}\n Caballaje: {registro[5]}\n Plazas: {registro[6]}")
                    num_auto += 1
            else:
                input("No hay registros de autos en la base de datos.")
            esperar_tecla()
        elif opcion == "3" or opcion == "ACTUALIZAR":
            limpiar_pantalla()
            id = int(input("Ingrese el ID del auto que desea actualizar: "))
            marca,color,modelo,velocidad,potencia,plazas=datos_autos(tipo="Auto")
            coche=coches.Coches(marca,color,modelo,velocidad,potencia,plazas)
            imprimir_datos_vehiculo(coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas)
            resp = cochesbd.autos.actualizar_en_bd(marca,color,modelo,velocidad,potencia,plazas,id)
            respuesta_a_datos_insertados_en_bd(resp)
            esperar_tecla()
        elif opcion == "4" or opcion == "ELIMINAR":
            limpiar_pantalla()
            id = int(input("Ingrese el ID del auto que desea eliminar: "))
            resp = cochesbd.autos.eliminar_en_bd(id)
            if resp:
                input(f"El auto con ID {id} ha sido eliminado correctamente.")
            else:
                input(f"No se pudo eliminar el auto con ID {id}.")
            esperar_tecla()
        elif opcion == "5" or opcion == "REGRESAR":
            print("Regresar al menu principal")
            esperar_tecla()
            break
        else:
            input("Opcion invalidad ... vuelva a intertarlo ... ")
            esperar_tecla()

def menu_camionetas():
    while True:
        opcion = menu_acciones(tipo="Camionetas")
        if opcion == "1" or opcion == "AGREGAR":
            limpiar_pantalla()
            print("\n\t...Agregar una nueva Camioneta")
            camionetas()
            esperar_tecla()
        elif opcion == "2" or opcion == "CONSULTAR":
            limpiar_pantalla()
            print("\n\t...Listado de Camionetas en la Base de Datos")
            registros = cochesbd.camionetas.consultar_en_bd()
            if len(registros) > 0:
                num_auto = 1 
                for registro in registros:
                    print(f" {num_auto}. con ID {registro[0]}\n Marca: {registro[1]}\n Color: {registro[2]}\n Modelo: {registro[3]}\n Velocidad: {registro[4]}\n Caballaje: {registro[5]}\n Plazas: {registro[6]}\n Traccion: {registro[7]}\n Cerrada: {registro[8]}")
                    num_auto += 1
            else:
                input("No hay registros de camionetas en la base de datos.")
            esperar_tecla()
        elif opcion == "3" or opcion == "ACTUALIZAR":
            limpiar_pantalla()
            id = int(input("Ingrese el ID de la camioneta que desea actualizar: "))
            marca,color,modelo,velocidad,caballaje,plazas=datos_autos(tipo="Camioneta")
            traccion=input("Traccion: ").upper()
            cerrada=input("¿Cerrada (Si/No)?: ").upper().strip()
            if cerrada=="SI":
                cerrada=True
            else:
                cerrada=False    
            coche=coches.Camionetas(marca,color,modelo,velocidad,caballaje,plazas,traccion,cerrada)
            imprimir_datos_vehiculo(coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas)
            print(f"traccion: {coche.traccion}\n cerrada: {coche.cerrada}")
            resp = cochesbd.camionetas.actualizar_en_bd(color, marca,modelo,velocidad,caballaje,plazas,traccion,cerrada,id)
            respuesta_a_datos_insertados_en_bd(resp)
            esperar_tecla()
        elif opcion == "4" or opcion == "ELIMINAR":
            limpiar_pantalla()
            id = int(input("Ingrese el ID de la camioneta que desea eliminar: "))
            resp = cochesbd.camionetas.eliminar_en_bd(id)
            if resp:
                input(f"La camioneta con ID {id} ha sido eliminada correctamente.")
            else:
                input(f"No se pudo eliminar la camioneta con ID {id}.")
            esperar_tecla()
        elif opcion == "5" or opcion == "REGRESAR":
            print("Regresar al menu principal")
            esperar_tecla()
            break
        else:
            input("Opcion invalidad ... vuelva a intertarlo ... ")
            esperar_tecla()

def menu_camiones():
    while True:
        opcion = menu_acciones(tipo="Camiones")
        if opcion == "1" or opcion == "AGREGAR":
            limpiar_pantalla()
            print("\n\t...Agregar un nuevo Camion")
            camiones()
            esperar_tecla()
        elif opcion == "2" or opcion == "CONSULTAR":
            limpiar_pantalla()
            print("\n\t...Listado de Camiones en la Base de Datos")
            registros = cochesbd.camiones.consultar_en_bd()
            if len(registros) > 0:
                num_auto = 1 
                for registro in registros:
                    print(f" {num_auto}. con ID {registro[0]}\n Marca: {registro[1]}\n Color: {registro[2]}\n Modelo: {registro[3]}\n Velocidad: {registro[4]}\n Caballaje: {registro[5]}\n Plazas: {registro[6]}\n Ejes: {registro[7]}\n Capacidad de carga: {registro[8]}")
                    num_auto += 1
            else:
                input("No hay registros de camiones en la base de datos.")
            esperar_tecla()
        elif opcion == "3" or opcion == "ACTUALIZAR":
            limpiar_pantalla()
            id = int(input("Ingrese el ID del camion que desea actualizar: "))
            marca,color,modelo,velocidad,caballaje,plazas=datos_autos(tipo="Camion")
            eje=int(input("No. de ejes: "))
            capacidadCarga=int(input("Capacidad de carga: "))
            coche=coches.Camiones(marca,color,modelo,velocidad,caballaje,plazas,eje,capacidadCarga)
            imprimir_datos_vehiculo(coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas)
            print(f"#Ejes: {coche.eje}\n Capacidad de carga: {coche.capacidadCarga}")
            resp = cochesbd.camiones.actualizar_en_bd(marca,color,modelo,velocidad,caballaje,plazas,eje,capacidadCarga,id)
            respuesta_a_datos_insertados_en_bd(resp)
            esperar_tecla()
        elif opcion == "4" or opcion == "ELIMINAR":
            limpiar_pantalla()
            id = int(input("Ingrese el ID del camion que desea eliminar: "))
            resp = cochesbd.camiones.eliminar_en_bd(id)
            if resp:
                input(f"El camion con ID {id} ha sido eliminado correctamente.")
            else:
                input(f"No se pudo eliminar el camion con ID {id}.")
            esperar_tecla()
        elif opcion == "5" or opcion == "REGRESAR":
            print("Regresar al menu principal")
            esperar_tecla()
            break
        else:
            input("Opcion invalidad ... vuelva a intertarlo ... ")
            esperar_tecla()

def main ():
    opcion=True
    while opcion:
        menu_seleccion_vehiculo()

if __name__ == "__main__":
    main()
