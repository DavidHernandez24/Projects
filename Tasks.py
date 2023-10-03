tasks = []

def add_task(task):
    tasks.append(task)
    print("Tarea agregada: ", task)

def list_tasks():
    if not tasks:
        print("No hay tareas pendientes.")
    else:
        print("Tareas pendientes:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def delete_task(task_index):
    if task_index >= 1 and task_index <= len(tasks):
        deleted_task = tasks.pop(task_index - 1)
        print("Tarea eliminada: ", deleted_task)
    else:
        print("Índice de tarea no válido.")

while True:
    print("\nGestor de Tareas")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Eliminar tarea")
    print("4. Salir")

    choice = input("Seleccione una opción (1/2/3/4): ")

    if choice == '1':
        task = input("Ingrese la tarea: ")
        add_task(task)
    elif choice == '2':
        list_tasks()
    elif choice == '3':
        list_tasks()
        task_index = int(input("Ingrese el número de tarea a eliminar: "))
        delete_task(task_index)
    elif choice == '4':
        print("Saliendo del Gestor de Tareas. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione 1, 2, 3 o 4.")
