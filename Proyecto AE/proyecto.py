import csv
import json

class Empresa:
    def __init__(self, id, nombre, descripcion, fecha_creacion, direccion, telefono, correo, gerente, equipo_contacto):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_creacion = fecha_creacion
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.gerente = gerente
        self.equipo_contacto = equipo_contacto

    def __str__(self):
        return (f"ID: {self.id}, Nombre: {self.nombre}, Descripción: {self.descripcion}, "
                f"Fecha de Creación: {self.fecha_creacion}, Dirección: {self.direccion}, "
                f"Teléfono: {self.telefono}, Correo: {self.correo}, Gerente: {self.gerente}, "
                f"Equipo de Contacto: {self.equipo_contacto}")

class Proyecto:
    def __init__(self, id, empresa_id, nombre, descripcion, fecha_inicio, fecha_vencimiento, estado_actual, gerente, equipo):
        self.id = id
        self.empresa_id = empresa_id
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio
        self.fecha_vencimiento = fecha_vencimiento
        self.estado_actual = estado_actual
        self.gerente = gerente
        self.equipo = equipo

    def __str__(self):
        return (f"ID: {self.id}, Nombre: {self.nombre}, Descripción: {self.descripcion}, "
                f"Fecha de Inicio: {self.fecha_inicio}, Fecha de Vencimiento: {self.fecha_vencimiento}, "
                f"Estado Actual: {self.estado_actual}, Gerente: {self.gerente}, Equipo: {self.equipo}")

class Tarea:
    def __init__(self, id, nombre, descripcion, fecha_inicio, fecha_vencimiento, estado_actual, porcentaje, subtareas=None):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio
        self.fecha_vencimiento = fecha_vencimiento
        self.estado_actual = estado_actual
        self.porcentaje = porcentaje
        self.subtareas = subtareas if subtareas is not None else []

    def __str__(self):
        return (f"ID: {self.id}, Nombre: {self.nombre}, Descripción: {self.descripcion}, "
                f"Fecha de Inicio: {self.fecha_inicio}, Fecha de Vencimiento: {self.fecha_vencimiento}, "
                f"Estado Actual: {self.estado_actual}, Porcentaje: {self.porcentaje}, Subtareas: {self.subtareas}")

class Sprint:
    def __init__(self, id, nombre, fecha_inicio, fecha_fin, estado, objetivos, equipo, tareas=None):
        self.id = id
        self.nombre = nombre
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.estado = estado
        self.objetivos = objetivos
        self.equipo = equipo
        self.tareas = tareas if tareas is not None else []

    def __str__(self):
        return (f"ID: {self.id}, Nombre: {self.nombre}, Fecha de Inicio: {self.fecha_inicio}, "
                f"Fecha de Fin: {self.fecha_fin}, Estado: {self.estado}, Objetivos: {self.objetivos}, "
                f"Equipo: {self.equipo}, Tareas: {self.tareas}")

class AVLNode:
    def __init__(self, key, sprint):
        self.key = key
        self.sprint = sprint
        self.height = 1
        self.left = None
        self.right = None

class AVLTree:
    def insert(self, root, key, sprint):
        if not root:
            return AVLNode(key, sprint)
        elif key < root.key:
            root.left = self.insert(root.left, key, sprint)
        else:
            root.right = self.insert(root.right, key, sprint)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        # Rotations
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        return root

    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def pre_order(self, root):
        res = []
        if root:
            res.append(root.sprint)
            res = res + self.pre_order(root.left)
            res = res + self.pre_order(root.right)
        return res

    def post_order(self, root):
        res = []
        if root:
            res = res + self.post_order(root.left)
            res = res + self.post_order(root.right)
            res.append(root.sprint)
        return res

def cargar_empresas(archivo_csv):
    empresas = []
    with open(archivo_csv, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            empresa = Empresa(**row)
            empresas.append(empresa)
    return empresas

def guardar_empresas(empresas, archivo_csv):
    with open(archivo_csv, mode='w', newline='') as file:
        fieldnames = ['id', 'nombre', 'descripcion', 'fecha_creacion', 'direccion', 'telefono', 'correo', 'gerente', 'equipo_contacto']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for empresa in empresas:
            writer.writerow(empresa.__dict__)

def crear_empresa(empresas):
    id = input("ID: ")
    nombre = input("Nombre: ")
    descripcion = input("Descripción: ")
    fecha_creacion = input("Fecha de Creación: ")
    direccion = input("Dirección: ")
    telefono = input("Teléfono: ")
    correo = input("Correo: ")
    gerente = input("Gerente: ")
    equipo_contacto = input("Equipo de Contacto: ")
    empresa = Empresa(id, nombre, descripcion, fecha_creacion, direccion, telefono, correo, gerente, equipo_contacto)
    empresas.append(empresa)

def listar_empresas(empresas):
    for empresa in empresas:
        print(empresa)

def modificar_empresa(empresas):
    id = input("ID de la empresa a modificar: ")
    for empresa in empresas:
        if empresa.id == id:
            empresa.nombre = input(f"Nombre ({empresa.nombre}): ") or empresa.nombre
            empresa.descripcion = input(f"Descripción ({empresa.descripcion}): ") or empresa.descripcion
            empresa.fecha_creacion = input(f"Fecha de Creación ({empresa.fecha_creacion}): ") or empresa.fecha_creacion
            empresa.direccion = input(f"Dirección ({empresa.direccion}): ") or empresa.direccion
            empresa.telefono = input(f"Teléfono ({empresa.telefono}): ") or empresa.telefono
            empresa.correo = input(f"Correo ({empresa.correo}): ") or empresa.correo
            empresa.gerente = input(f"Gerente ({empresa.gerente}): ") or empresa.gerente
            empresa.equipo_contacto = input(f"Equipo de Contacto ({empresa.equipo_contacto}): ") or empresa.equipo_contacto
            print("Empresa modificada.")
            return
    print("Empresa no encontrada.")

def eliminar_empresa(empresas):
    id = input("ID de la empresa a eliminar: ")
    for empresa in empresas:
        if empresa.id == id:
            empresas.remove(empresa)
            print("Empresa eliminada.")
            return
    print("Empresa no encontrada.")

def consultar_empresa(empresas):
    id = input("ID de la empresa a consultar: ")
    for empresa in empresas:
        if empresa.id == id:
            print(empresa)
            return
    print("Empresa no encontrada.")

def cargar_proyectos(archivo_csv):
    proyectos = []
    with open(archivo_csv, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            proyecto = Proyecto(**row)
            proyectos.append(proyecto)
    return proyectos

def listar_proyectos(proyectos):
    for proyecto in proyectos:
        print(proyecto)

def insertar_proyecto(avl_tree, proyectos, root):
    id = input("ID: ")
    empresa_id = input("ID de Empresa: ")
    nombre = input("Nombre: ")
    descripcion = input("Descripción: ")
    fecha_inicio = input("Fecha de Inicio: ")
    fecha_vencimiento = input("Fecha de Vencimiento: ")
    estado_actual = input("Estado Actual: ")
    gerente = input("Gerente: ")
    equipo = input("Equipo: ")
    proyecto = Proyecto(id, empresa_id, nombre, descripcion, fecha_inicio, fecha_vencimiento, estado_actual, gerente, equipo)
    proyectos.append(proyecto)
    root = avl_tree.insert(root, fecha_vencimiento, proyecto)
    return root

def modificar_proyecto(proyectos):
    id = input("ID del proyecto a modificar: ")
    for proyecto in proyectos:
        if proyecto.id == id:
            proyecto.nombre = input(f"Nombre ({proyecto.nombre}): ") or proyecto.nombre
            proyecto.descripcion = input(f"Descripción ({proyecto.descripcion}): ") or proyecto.descripcion
            proyecto.fecha_inicio = input(f"Fecha de Inicio ({proyecto.fecha_inicio}): ") or proyecto.fecha_inicio
            proyecto.fecha_vencimiento = input(f"Fecha de Vencimiento ({proyecto.fecha_vencimiento}): ") or proyecto.fecha_vencimiento
            proyecto.estado_actual = input(f"Estado Actual ({proyecto.estado_actual}): ") or proyecto.estado_actual
            proyecto.gerente = input(f"Gerente ({proyecto.gerente}): ") or proyecto.gerente
            proyecto.equipo = input(f"Equipo ({proyecto.equipo}): ") or proyecto.equipo
            print("Proyecto modificado.")
            return
    print("Proyecto no encontrado.")

def cargar_tareas(archivo_json):
    with open(archivo_json, 'r') as file:
        tareas = json.load(file)
    return tareas

def guardar_tareas(tareas, archivo_json):
    with open(archivo_json, 'w') as file:
        json.dump(tareas, file, indent=4)

def agregar_tarea(tareas):
    proyecto_id = input("ID del Proyecto: ")
    tarea_id = input("ID de la Tarea: ")
    nombre = input("Nombre: ")
    descripcion = input("Descripción: ")
    fecha_inicio = input("Fecha de Inicio: ")
    fecha_vencimiento = input("Fecha de Vencimiento: ")
    estado_actual = input("Estado Actual: ")
    porcentaje = int(input("Porcentaje: "))
    nueva_tarea = {
        "id": tarea_id,
        "nombre": nombre,
        "descripcion": descripcion,
        "fecha_inicio": fecha_inicio,
        "fecha_vencimiento": fecha_vencimiento,
        "estado_actual": estado_actual,
        "porcentaje": porcentaje,
        "subtareas": []
    }
    if proyecto_id not in tareas:
        tareas[proyecto_id] = []
    tareas[proyecto_id].append(nueva_tarea)
    guardar_tareas(tareas, 'tareas.json')

def listar_tareas(tareas):
    proyecto_id = input("ID del Proyecto: ")
    if proyecto_id in tareas:
        for tarea in tareas[proyecto_id]:
            print(tarea)
    else:
        print("No hay tareas para este proyecto.")

def cargar_sprints(archivo_json):
    with open(archivo_json, 'r') as file:
        sprints = json.load(file)
    return sprints

def guardar_sprints(sprints, archivo_json):
    with open(archivo_json, 'w') as file:
        json.dump(sprints, file, indent=4)

def agregar_sprint(sprints):
    sprint_id = input("ID del Sprint: ")
    nombre = input("Nombre: ")
    fecha_inicio = input("Fecha de Inicio: ")
    fecha_fin = input("Fecha de Fin: ")
    estado = input("Estado: ")
    objetivos = input("Objetivos: ")
    equipo = input("Equipo: ")
    nuevo_sprint = {
        "id": sprint_id,
        "nombre": nombre,
        "fecha_inicio": fecha_inicio,
        "fecha_fin": fecha_fin,
        "estado": estado,
        "objetivos": objetivos,
        "equipo": equipo,
        "tareas": []
    }
    sprints[sprint_id] = nuevo_sprint
    guardar_sprints(sprints, 'sprints.json')

def listar_sprints(sprints):
    for sprint_id, sprint in sprints.items():
        print(sprint)

def tareas_criticas(tareas, proyecto_id):
    if proyecto_id in tareas:
        print("Tareas críticas en postorden:")
        for tarea in postorden_tareas(tareas[proyecto_id]):
            if tarea["estado_actual"] != "Completado":
                print(tarea)
    else:
        print("No hay tareas para este proyecto.")

def postorden_tareas(tareas):
    res = []
    for tarea in tareas:
        res.extend(postorden_tareas(tarea["subtareas"]))
        res.append(tarea)
    return res

def listar_sprints_nivel(avl_tree, nivel):
    sprints = listar_sprints_nivel_aux(avl_tree, nivel, 0)
    for sprint in sprints:
        print(sprint)

def listar_sprints_nivel_aux(root, nivel, actual):
    if root is None:
        return []
    if actual == nivel:
        return [root.sprint]
    return (listar_sprints_nivel_aux(root.left, nivel, actual + 1) +
            listar_sprints_nivel_aux(root.right, nivel, actual + 1))

def mostrar_tareas_preorden(tareas):
    if isinstance(tareas, dict):
        for tarea in preorden_tareas(tareas):
            print(tarea)

def preorden_tareas(tareas):
    res = []
    for tarea in tareas:
        res.append(tarea)
        res.extend(preorden_tareas(tarea["subtareas"]))
    return res
class NodoArbolNario:
    def _init_(self, datos):
        self.datos = datos
        self.hijos = []

    def eliminar_hijo(self, hijo):
        self.hijos = [h for h in self.hijos if h != hijo]

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)

class ArbolNario:
    def _init_(self, datos_raiz):
        self.raiz = NodoArbolNario(datos_raiz)

    def agregar_hijo(self, padre, datos_hijo):
        hijo = NodoArbolNario(datos_hijo)
        padre.agregar_hijo(hijo)
        return hijo

    def recorrer(self, nodo, tipo):
        if nodo:
            if tipo == 'preorden':
                print(nodo.datos, end=" ")
            for hijo in nodo.hijos:
                self.recorrer(hijo, tipo)
            if tipo == 'postorden':
                print(nodo.datos, end=" ")

    def profundidad(self, nodo):
        if not nodo:
            return 0
        return 1 + max((self.profundidad(h) for h in nodo.hijos), default=0)

    def encontrar(self, datos):
        return self._encontrar_recursivo(self.raiz, datos)

    def _encontrar_recursivo(self, nodo, datos):
        if nodo and nodo.datos == datos:
            return nodo
        for hijo in nodo.hijos:
            resultado = self._encontrar_recursivo(hijo, datos)
            if resultado:
                return resultado
        return None

    def encontrar_por_atributo(self, atributo, valor):
        return self._encontrar_por_atributo_recursivo(self.raiz, atributo, valor)

    def _encontrar_por_atributo_recursivo(self, nodo, atributo, valor):
        if nodo and getattr(nodo.datos, atributo, None) == valor:
            return nodo
        for hijo in nodo.hijos:
            resultado = self._encontrar_por_atributo_recursivo(hijo, atributo, valor)
            if resultado:
                return resultado
        return None

    def modificar_por_atributo(self, atributo, valor, nuevos_datos):
        nodo = self.encontrar_por_atributo(atributo, valor)
        if nodo:
            for key, value in nuevos_datos.items():
                setattr(nodo.datos, key, value)
            return True
        return False

    def eliminar_nodo(self, objetivo):
        if self.raiz == objetivo:
            self.raiz = None
        else:
            padre = self.encontrar_padre(self.raiz, objetivo)
            if padre:
                padre.eliminar_hijo(objetivo)

    def encontrar_padre(self, actual, objetivo):
        if not actual:
            return None
        for hijo in actual.hijos:
            if hijo == objetivo:
                return actual
            padre = self.encontrar_padre(hijo, objetivo)
            if padre:
                return padre
        return None

    def nodos_en_nivel(self, nivel):
        if not self.raiz:
            return []
        cola, actual = [self.raiz], 0

        while cola and actual < nivel:
            cola = [h for nodo in cola for h in nodo.hijos]
            actual += 1

        return [nodo.datos for nodo in cola] if actual == nivel else []

    def mostrar_arbol(self, nodo, nivel=0):
        if nodo:
            print(' ' * nivel * 2 + str(nodo.datos))
            for hijo in nodo.hijos:
                self.mostrar_arbol(hijo, nivel + 1)

def reportes(arbol):
    opciones = {
        1: ("Recorrer las tareas de un proyecto en PostOrden", recorrer_tareas_postorden),
        2: ("Listar sprints de un proyecto", listar_sprints)
    }
    for i, (desc, _) in opciones.items():
        print(f"{i}. {desc}")
    opcion = int(input("Ingrese una opción: "))

    if opcion in opciones:
        opciones[opcion][1](arbol)
    else:
        print("Opción no válida.")

def recorrer_tareas_postorden(arbol):
    nombre_proyecto = input("Ingrese el nombre del proyecto: ")
    proyecto = arbol.encontrar_por_atributo('nombre', nombre_proyecto)
    if proyecto:
        arbol.recorrer(proyecto, 'postorden')
        print()
    else:
        print("No se encontró el proyecto.")

def listar_sprints(arbol):
    nombre_proyecto = input("Ingrese el nombre del proyecto: ")
    proyecto = arbol.encontrar_por_atributo('nombre', nombre_proyecto)
    if proyecto:
        nivel = int(input("Ingrese la altura desde donde desea mostrar los sprints: "))
        nodos = arbol.nodos_en_nivel(nivel)
        for nodo in nodos:
            print(nodo)
    else:
        print("No se encontró el proyecto.")

def menu5():
    arbol = None
    opciones = {
        0: ("Crear Arbol", crear_arbol),
        1: ("Agregar un nodo al árbol", agregar_nodo),
        2: ("Modificar un nodo", modificar_nodo),
        3: ("Eliminar un nodo", eliminar_nodo),
        4: ("Mostrar el árbol", mostrar_arbol),
        5: ("Buscar un nodo por atributo", buscar_nodo_por_atributo),
        6: ("Reportes", reportes),
        7: ("Salir", lambda _: print("Saliendo del menú.") or exit())
    }

    while True:
        print("\n--- Menú de Gestión de Proyecto ---")
        for i, (desc, _) in opciones.items():
            print(f"{i}. {desc}")

        opcion = int(input("Seleccione una opción: "))
        if opcion in opciones:
            opciones[opcion][1](arbol)
        else:
            print("Opción no válida. Intente de nuevo.")

def crear_arbol(_):
    nombre = input('Ingrese el nombre del Arbol: ')
    return ArbolNario(f"Arbol {nombre}")

def agregar_nodo(arbol):
    if arbol:
        datos_padre = input("Ingrese los datos del nodo padre: ")
        padre = arbol.encontrar(datos_padre)
        if padre:
            datos_hijo = input("Ingrese los datos del nuevo nodo: ")
            arbol.agregar_hijo(padre, datos_hijo)
            print("Nodo agregado exitosamente.")
        else:
            print("Nodo padre no encontrado.")
    else:
        print("Primero debe crear un árbol.")

def modificar_nodo(arbol):
    if arbol:
        atributo = input("Ingrese el atributo del nodo a modificar (por ejemplo, 'nombre'): ")
        valor = input("Ingrese el valor del atributo del nodo a modificar: ")
        nuevos_datos = input("Ingrese los nuevos datos del nodo (formato: id,nombre,descripcion,fecha_inicio,fecha_vencimiento,estado,empresa,porcentaje): ").split(',')
        nuevos_datos_nodo = {
            'id': int(nuevos_datos[0]),
            'nombre': nuevos_datos[1],
            'descripcion': nuevos_datos[2],
            'fecha_inicio': nuevos_datos[3],
            'fecha_vencimiento': nuevos_datos[4],
            'estado': nuevos_datos[5],
            'empresa': nuevos_datos[6],
            'porcentaje': float(nuevos_datos[7])
        }
        exito = arbol.modificar_por_atributo(atributo, valor, nuevos_datos_nodo)
        if exito:
            print("Nodo modificado exitosamente.")
        else:
            print("No se encontró el nodo o no se pudo modificar.")
    else:
        print("Primero debe crear un árbol.")

def eliminar_nodo(arbol):
    if arbol:
        atributo = input("Ingrese el atributo del nodo a eliminar (por ejemplo, 'nombre'): ")
        valor = input("Ingrese el valor del atributo del nodo a eliminar: ")
        exito = arbol.eliminar_por_atributo(atributo, valor)
        if exito:
            print("Nodo eliminado exitosamente.")
        else:
            print("No se encontró el nodo o no se pudo eliminar.")
    else:
        print("Primero debe crear un árbol.")

def mostrar_arbol(arbol):
    if arbol:
        arbol.mostrar_arbol(arbol.raiz)
    else:
        print("Primero debe crear un árbol.")

def buscar_nodo_por_atributo(arbol):
    if arbol:
        atributo = input("Ingrese el atributo del nodo a buscar (por ejemplo, 'nombre'): ")
        valor = input("Ingrese el valor del atributo del nodo a buscar: ")
        nodo = arbol.encontrar_por_atributo(atributo, valor)
        if nodo:
            print("Nodo encontrado:", nodo.datos)
        else:
            print("No se encontró el nodo.")
    else:
        print("Primero debe crear un árbol.")
def menu():
    empresas = cargar_empresas('empresas.csv')
    proyectos = cargar_proyectos('proyectos.csv')
    tareas = cargar_tareas('tareas.json')
    sprints = cargar_sprints('sprints.json')
    avl_tree = AVLTree()
    root = None
    for proyecto in proyectos:
        root = avl_tree.insert(root, proyecto.fecha_vencimiento, proyecto)

    while True:
        print("\nGestión de Empresas, Proyectos, Tareas y Sprints")
        print("1. Crear Empresa")
        print("2. Listar Empresas")
        print("3. Modificar Empresa")
        print("4. Consultar Empresa")
        print("5. Eliminar Empresa")
        print("6. Crear Proyecto")
        print("7. Listar Proyectos")
        print("8. Modificar Proyecto")
        print("9. Agregar Tarea")
        print("10. Listar Tareas")
        print("11. Agregar Sprint")
        print("12. Listar Sprints")
        print("13. Mostrar Tareas Críticas")
        print("14. Listar Sprints por Nivel")
        print("15. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            crear_empresa(empresas)
            guardar_empresas(empresas, 'empresas.csv')
        elif opcion == '2':
            listar_empresas(empresas)
        elif opcion == '3':
            modificar_empresa(empresas)
            guardar_empresas(empresas, 'empresas.csv')
        elif opcion == '4':
            consultar_empresa(empresas)
        elif opcion == '5':
            eliminar_empresa(empresas)
            guardar_empresas(empresas, 'empresas.csv')
        elif opcion == '6':
            root = insertar_proyecto(avl_tree, proyectos, root)
        elif opcion == '7':
            listar_proyectos(proyectos)
        elif opcion == '8':
            modificar_proyecto(proyectos)
        elif opcion == '9':
            agregar_tarea(tareas)
        elif opcion == '10':
            listar_tareas(tareas)
        elif opcion == '11':
            agregar_sprint(sprints)
        elif opcion == '12':
            listar_sprints(sprints)
        elif opcion == '13':
            proyecto_id = input("ID del Proyecto: ")
            tareas_criticas(tareas, proyecto_id)
        elif opcion == '14':
            nivel = int(input("Nivel del Árbol: "))
            listar_sprints_nivel(avl_tree, nivel)
        elif opcion == '15':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
