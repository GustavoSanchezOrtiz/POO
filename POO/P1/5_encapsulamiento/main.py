from coches import *
'''
coche1=Coches("VW", "blanco", "2022", 220, 150, 5)
coche2=Coches("Nissan", "Azul", "2020", 180, 150, 6)
coche3= Coches("Honda","","",0,0,0)
coche4= Coches("","","",0,0,0)
coche4.marca2 = "volvo"'''

'''print(f"Datos del Vehiculo: 1 \n Marca:{coche1.get_marca()} \n color: {coche1.get_color()} \n Modelo: {coche1.get_modelo()} \n velocidad: {coche1.get_velocidad()} \n caballaje: {coche1.get_caballaje()} \n plazas: {coche1.get_plazas()} \n numero de serie {coche1.numero_de_serie} ")

print(f"Datos del Vehiculo: 2\n Marca:{coche2.get_marca()} \n color: {coche2.get_color()} \n Modelo: {coche2.get_modelo()} \n velocidad: {coche2.get_velocidad()} \n caballaje: {coche2.get_caballaje()} \n plazas: {coche2.get_plazas()} ")


'''
num_coches= int (input("¿cuantos coches tienes?"))
for i in range(0, num_coches):
    print(f"Ingresa los datos del automovil{i+1}")
    marca= input(f"ingresar la marca{i+1}: ").upper()
    color= input(f"ingrese el color{i+1}: ").upper()
    modelo= input(f"ingresa el modelo{i+1}: ").upper()
    velocidad= int(input(f"ingresa la velocidad{i+1}: "))
    caballaje= int(input(f"ingresa el caballaje{i+1}: "))
    plazas= int(input(f"ingresa el # de plazas{i+1}: "))

    coche= Coches(marca, color, modelo, velocidad, caballaje, plazas )

    print(f"\nDatos del Vehiculo: 1 \n Marca:{coche.get_marca()} \n color: {coche.get_color()} \n Modelo: {coche.get_modelo()} \n velocidad: {coche.get_velocidad()} \n caballaje: {coche.get_caballaje()} \n plazas: {coche.get_plazas()} \n ")
