class Mascota:
    #atributo de clase
    id = 0

    #crear mascota
    def __init__(self, tipo, raza, nombre, edad, peso):
        Mascota.id += 1 
        self.id = Mascota.id
        self.tipo = tipo
        self.raza = raza
        self.nombre = nombre
        self.edad = edad
        self.peso = peso

mascotas_lista = []

def mostrar_mascotas():
    #se recorre la lista y se muestra objeto por objeto
    for i in range(len(mascotas_lista)):
        print(mascotas_lista[i].id, " ", 
              mascotas_lista[i].tipo, " ", 
              mascotas_lista[i].raza, " ", 
              mascotas_lista[i].nombre, " ", 
              mascotas_lista[i].edad, " ", 
              mascotas_lista[i].peso)
        
def eliminar_mascota(m):
    orden = int(input("Ingrese el id de la mascota que desea eliminar: "))
    #se recorre la lista, si encuentra un objeto con id igual al ingresado lo elimina
    for i in range(1, len(mascotas_lista)):
        if mascotas_lista[i].id == int(orden):
            mascotas_lista.remove(m)
    print("Mascota eliminada de la lista")

i = 0
while i == 0:
    print("Menú")
    print("1. Agregar mascota")
    print("2. Consultar listado de mascotas")
    print("3. Eliminar mascota")
    print("4. Salir")
    opcion = int(input())

    if opcion == 1:
        print()
        t = input("Ingresar tipo de mascota: ")
        r = input("Ingresar la raza de tu mascota: ")
        n = input("Ingresar el nombre de tu mascota: ")
        e = input("Ingresar la edad de tu mascota: ")
        p = input("Ingresar el peso de tu mascota: ")
        m = Mascota(t, r, n, e, p)
        mascotas_lista.append(m)
        print("Mascota guardada en la lista")
        print()
    elif opcion == 2:
        print("Lista de mascotas:")
        mostrar_mascotas()
        print()
    elif opcion == 3:
        print("Eliminar mascota:")
        eliminar_mascota(m)
        print()
    elif opcion == 4:
        exit()
    else: 
        print("Opción inválida")






