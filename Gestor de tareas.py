# se crean las estructuras 
tareas = []
historial = []
tareasUrgentes = []
arbolTareas= {
    "Proyecto Principal": {
        "fronted": ["Diseño Usuario", "Revision"],
        "backend":["API loging","Gestion DB"]
    }
}
# se crean las funciones
def agregarTarea():
    tarea = input ("ingrese tarea nueva: ")
    tareas.append(tarea)
    historial.append(f"Tarea agregada: {tarea}")
    
def mostrarTareas():
    print("\n Tareas Actuales")
    if not tareas:
        print (" No hay tareas")
    else:
        for i, t in enumerate(tareas):
            print(f"{i+1}.{t}")
def editarTarea ():
    mostrarTareas()
    indice= int(input("Ingrese el numero a editar: "))-1
    if 0<= indice <len(tareas):
        nueva= input("ingrese el nuevo nombre de la tarea: ")
        historial.append(f"Tarea Editada:{tareas[indice]}->{nueva}")
        tareas[indice]=nueva
        print ("Tarea actualizada")
    else:
        print("indice fuera de rango")
def eliminarTarea():
    mostrarTareas()
    indice = int(input("Ingrese el numero de la tarea a eliminar"))
    if 0<= indice <len(tareas):
        historial.append(f"Tareas eliminadas: {tareas[indice]}")
        tareas.pop(indice)
        print("Tarea eliminada con exito")
    else:
        print("Indice invalido")
def agergarUrgencia():
    urgente = input("Ingrese una tarea urgente: ")
    tareasUrgentes.append(urgente)
    historial.append(f"Tarea agergada Urgente: {urgente}")
    print("Tarea urgente registrada")
def procesarUrgente():
    if tareasUrgentes:
        tareas = tareasUrgentes.pop(0)
        print (f" Procesando tarea urgente {tareas}")
        historial.append(f"Tarea urgente procesada: {tareas}")
    else:
        print("No hay tareas urgentes")
        
def mostrarArbol():
    print("\n Organizacion Jerarquica del Proyecto: ")
    for area, subtarea in arbolTareas["Proyecto Principal"].items():
        print(f"{area}:")
        for sub in subtarea:
            print(" ->", sub)
            
def verColaUrgente():
    if tareasUrgentes:
        print("\n Tareas Urgentes en la cola")
        
def mostrarHistorial():
    print("\n Historial de acciones")
    for i in reversed (historial[-5:]):
        print(f"*, {i}")

def menu():
    while True:
        print("\n Menu de sistema de gestion de tareas")
        print("1 Agregar Tarea")
        print ("2 Editar Tarea")
        print("3 ELiminar Tarea")
        print(" 4 Mostrar Tarea")
        print( "5 Agregar Tarea Urgente")
        print (" 6 Procesar Tarea Urgente")
        print("7 Mostrar Historial")
        print("8 Ver estructura de Arbol de Tarea")
        print("9 Ver primera y ultima Tarea Urgente")
        print("10 Salir")
        opcion = int(input (" seleccione una opciion: "))
    
        if opcion==1:
            agregarTarea()
        elif opcion==2:
            editarTarea()
        elif opcion ==3:
            eliminarTarea()
        elif opcion ==4:
            mostrarTareas()
        elif opcion ==5:
            agergarUrgencia()
        elif opcion==6:
            procesarUrgente()
        elif opcion==7:
            mostrarHistorial()
        elif opcion==8:
            mostrarArbol()
        elif opcion==9:
            verColaUrgente()
        elif opcion==10:
            print(" Eso fue todo")
            break
        else:
            print("Opcion No valida")
menu()