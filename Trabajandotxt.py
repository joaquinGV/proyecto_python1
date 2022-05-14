def read():
    names = []
    route_read = input("ingrese el nombre del archivo que desea leer : ")
    froute_read = "./Files/"+route_read+".txt"
    with open(froute_read, "r", encoding="utf-8") as f:
        for line in f:
            if len(line.strip()) > 0:
                names.append(line.strip())
    if len(names) > 0:
        print(names)
    else:
        print("Archivo vacio")


def write():
    names = []
    nfile = input("ingrese el nombre del archivo : ")
    froute = "./Files/"+nfile+".txt"
    with open(froute, "w", encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write('\n')


def agregar_nombre(nombre):
    nroute_ap = input("ingrese el nombre del archivo que desea abrir : ")
    froute_ap = "./Files/"+nroute_ap+".txt"
    with open(froute_ap, "a", encoding="utf-8") as f:
        f.write(nombre)
        f.write("\n")


def borrar_nombre(nombre):
    names = []
    route_del = input("ingrese el nombre del archivo que desea abrir : ")
    route_ap = "./Files/"+route_del+".txt"
    with open(route_ap, "r", encoding="utf-8") as f:
        for line in f:
            if len(line.strip()) > 0 and line.strip() != nombre:
                names.append(line.strip())
    with open(route_ap, "w", encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write('\n')


def run():
    sw = True
    while sw:
        try:
            print("""  
----------------------------------------------------------------------
            Seleccione un numero:
            1. Crear un nuevo archivo 
            2. Agregar nombre
            3. Listar nombre
            4. Borrar nombre
            5. Salir del programa
----------------------------------------------------------------------
            """)
            n = int(input("Ingrese una opcion :   "))
            if n == 1:
                write()
            elif n == 2:
                nombre = input("Ingrese el nombre a agregar: ")
                agregar_nombre(nombre)
            elif n == 3:
                read()
            elif n == 4:
                nombre = input("Ingrese el nombre a borrar : ")
                borrar_nombre(nombre)
            elif n == 5:
                sw = False
                print("Programa Terminado!")
        except ValueError:
            print("Error seleccione una opcion correcta")
    # write()


if __name__ == '__main__':
    run()
