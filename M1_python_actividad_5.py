#1. ESTRUCTURA DE DATOS (Base de Datos en Memoria)

# Almacenamiento central para todos los datos del sistema.
datos_sistema = {
    # Almacenará estudiantes: {id_estudiante: {'nombre': '...', 'edad': '...', ...}}
    "estudiantes": {}, 
    # Almacenará materias: {codigo_materia: {'nombre': '...', 'creditos': '...', ...}}
    "materias": {}, 
    # Almacenará asignaciones: {id_estudiante: {codigo_materia: []}}
    "asignaciones": {}, 
    # Almacenará notas: {id_estudiante: {codigo_materia: [nota1, nota2, ...]}}
    "notas": {} 
}

# Variable global para generar IDs de estudiantes y códigos de materias
ESTUDIANTE_ID_COUNTER = 1
MATERIA_CODIGO_COUNTER = 1

# 2. GESTIÓN DE ESTUDIANTES (Opción 1 del Menú Principal)

# Funciones de Acción de Estudiantes

def registrar_estudiante():
    """Registra un nuevo estudiante en el sistema."""
    global ESTUDIANTE_ID_COUNTER
    print("\n--- 1. Registrar Estudiante ---")
    
    nombre = input("Ingrese el nombre del estudiante: ")
    if not nombre:
        print("El nombre no puede estar vacío.")
        return

    # Usamos un ID autoincremental
    nuevo_id = ESTUDIANTE_ID_COUNTER
    datos_sistema["estudiantes"][nuevo_id] = {
        "nombre": nombre,
        "materias_inscritas": 0 # Nuevo campo para reportes
    }
    ESTUDIANTE_ID_COUNTER += 1
    
    print(f"Estudiante '{nombre}' registrado con éxito. ID: {nuevo_id}")

def listar_estudiantes():
    """Muestra todos los estudiantes registrados."""
    print("\n2. Listar Estudiantes")
    if not datos_sistema["estudiantes"]:
        print("No hay estudiantes registrados.")
        return
        
    for id_e, datos in datos_sistema["estudiantes"].items():
        print(f"ID: {id_e} | Nombre: {datos['nombre']}")

def consultar_estudiante():
    """Consulta un estudiante por su ID."""
    print("\n3. Consultar Estudiante por ID")
    try:
        estudiante_id = int(input("Ingrese el ID del estudiante a consultar: "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        return
    
    datos = datos_sistema["estudiantes"].get(estudiante_id)
    if datos:
        print("\nDatos del Estudiante")
        print(f"ID: {estudiante_id}")
        print(f"Nombre: {datos['nombre']}")
        # Lógica para mostrar materias y notas (se implementará más tarde)
        print("Materias inscritas: (Aún no implementado)")
    else:
        print(f"Estudiante con ID {estudiante_id} no encontrado.")

def eliminar_estudiante():
    """Elimina un estudiante por su ID."""
    print("\n4. Eliminar Estudiante")
    try:
        estudiante_id = int(input("Ingrese el ID del estudiante a eliminar: "))
    except ValueError:
        print("⚠ Por favor, ingrese un número válido.")
        return
    
    if estudiante_id in datos_sistema["estudiantes"]:
        nombre_estudiante = datos_sistema["estudiantes"][estudiante_id]['nombre']
        
        # Eliminar de todas las estructuras de datos
        del datos_sistema["estudiantes"][estudiante_id]
        datos_sistema["asignaciones"].pop(estudiante_id, None)
        datos_sistema["notas"].pop(estudiante_id, None)
        
        print(f"Estudiante '{nombre_estudiante}' (ID: {estudiante_id}) y todos sus registros eliminados con éxito.")
    else:
        print(f"Estudiante con ID {estudiante_id} no encontrado.")

# Menú de Estudiantes

def menu_gestion_estudiantes():
    """Menú para la gestión de estudiantes (registrar, listar, consultar, eliminar)."""
    while True:
        print("""
   * Gestión de Estudiantes *
1. Registrar estudiante
2. Listar estudiantes
3. Consultar estudiante por ID
4. Eliminar estudiante
5. Volver al menú principal
""")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_estudiante()
        elif opcion == "2":
            listar_estudiantes()
        elif opcion == "3":
            consultar_estudiante()
        elif opcion == "4":
            eliminar_estudiante()
        elif opcion == "5":
            break
        else:
            print("Opción no válida.")

#3. GESTIÓN DE MATERIAS (Opción 2 del Menú Principal)


# Funciones de Acción de Materias 

def registrar_materia():
    """Registra una nueva materia en el sistema."""
    global MATERIA_CODIGO_COUNTER
    print("\n 1. Registrar Materia")
    
    nombre = input("Ingrese el nombre de la materia: ")
    creditos = input("Ingrese la cantidad de créditos: ")
    
    if not nombre or not creditos.isdigit():
        print("Entrada no válida. Asegúrese de que el nombre no esté vacío y los créditos sean un número.")
        return

    # Usamos un código autoincremental (C + número)
    nuevo_codigo = f"C{MATERIA_CODIGO_COUNTER:03d}"
    datos_sistema["materias"][nuevo_codigo] = {
        "nombre": nombre,
        "creditos": int(creditos),
        "estudiantes_inscritos": 0 # Nuevo campo para reportes
    }
    MATERIA_CODIGO_COUNTER += 1
    
    print(f"Materia '{nombre}' registrada con éxito. Código: {nuevo_codigo}")

def listar_materias():
    """Muestra todas las materias disponibles."""
    print("\n2. Listar Materias")
    if not datos_sistema["materias"]:
        print("No hay materias registradas.")
        return
        
    for codigo, datos in datos_sistema["materias"].items():
        print(f"Código: {codigo} | Nombre: {datos['nombre']} ({datos['creditos']} créditos)")

def consultar_materia():
    """Consulta una materia por su código."""
    print("\n3. Consultar Materia por Código")
    codigo = input("Ingrese el código de la materia a consultar (Ej: C001): ").upper()
    
    datos = datos_sistema["materias"].get(codigo)
    if datos:
        print("\nDatos de la Materia")
        print(f"Código: {codigo}")
        print(f"Nombre: {datos['nombre']}")
        print(f"Créditos: {datos['creditos']}")
        print(f"Estudiantes inscritos: (Aún no implementado)")
    else:
        print(f"Materia con código {codigo} no encontrada.")

def eliminar_materia():
    """Elimina una materia por su código."""
    print("\n4. Eliminar Materia")
    codigo = input("Ingrese el código de la materia a eliminar: ").upper()
    
    if codigo in datos_sistema["materias"]:
        nombre_materia = datos_sistema["materias"][codigo]['nombre']
        
        # Eliminar de todas las estructuras de datos
        del datos_sistema["materias"][codigo]
        
        # Eliminar la materia de las asignaciones y notas de TODOS los estudiantes
        for est_id in list(datos_sistema["asignaciones"].keys()):
            datos_sistema["asignaciones"][est_id].pop(codigo, None)
            # Limpiar asignación si queda vacía
            if not datos_sistema["asignaciones"][est_id]:
                 datos_sistema["asignaciones"].pop(est_id, None) 
                 
        for est_id in datos_sistema["notas"]:
            datos_sistema["notas"][est_id].pop(codigo, None)
            
        print(f"Materia '{nombre_materia}' (Código: {codigo}) y todos sus registros eliminados con éxito.")
    else:
        print(f"Materia con código {codigo} no encontrada.")

# Menú de Materias

def menu_gestion_materias():
    """Menú para la gestión de materias (registrar, listar, consultar, eliminar)."""
    while True:
        print("""
    Gestión de Materias
1. Registrar materia
2. Listar materias
3. Consultar materia por código
4. Eliminar materia
5. Volver al menú principal
""")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_materia()
        elif opcion == "2":
            listar_materias()
        elif opcion == "3":
            consultar_materia()
        elif opcion == "4":
            eliminar_materia()
        elif opcion == "5":
            break
        else:
            print("Opción no válida.")


#4. ASIGNACIONES (Opción 3 del Menú Principal)


#Funciones de Acción de Asignaciones

def asignar_materia_a_estudiante():
    """Asigna una materia a un estudiante."""
    print("\n1. Asignar Materia a Estudiante ")
    # Validación de existencia de datos
    if not datos_sistema["estudiantes"] or not datos_sistema["materias"]:
        print("Debe haber al menos un estudiante y una materia registrados para asignar.")
        return

    try:
        est_id = int(input("Ingrese el ID del estudiante (Ej: 1): "))
        cod_materia = input("Ingrese el código de la materia a asignar (Ej: C001): ").upper()
    except ValueError:
        print("ID de estudiante no válido.")
        return
        
    estudiante = datos_sistema["estudiantes"].get(est_id)
    materia = datos_sistema["materias"].get(cod_materia)

    if not estudiante:
        print(f" Estudiante con ID {est_id} no encontrado.")
    elif not materia:
        print(f" Materia con código {cod_materia} no encontrada.")
    else:
        # Inicializar estructuras si es necesario
        if est_id not in datos_sistema["asignaciones"]:
            datos_sistema["asignaciones"][est_id] = {}
        
        if cod_materia in datos_sistema["asignaciones"][est_id]:
            print(f"El estudiante '{estudiante['nombre']}' ya está inscrito en la materia '{materia['nombre']}'.")
            return
            
        # Asignar
        datos_sistema["asignaciones"][est_id][cod_materia] = [] # Lista de notas (aunque las notas se manejen en otra estructura, sirve para la lista de asignaciones)
        
        # Inicializar estructura de notas
        if est_id not in datos_sistema["notas"]:
             datos_sistema["notas"][est_id] = {}
        datos_sistema["notas"][est_id][cod_materia] = []
        
        # Actualizar contadores para reportes
        estudiante['materias_inscritas'] += 1
        materia['estudiantes_inscritos'] += 1
        
        print(f"Materia '{materia['nombre']}' asignada con éxito al estudiante '{estudiante['nombre']}'.")


def listar_asignaciones_por_estudiante():
    """Muestra todas las materias asignadas a un estudiante específico."""
    print("\n2. Consultar Asignaciones por Estudiante")
    if not datos_sistema["asignaciones"]:
        print(" No hay asignaciones registradas aún.")
        return
        
    try:
        est_id = int(input("Ingrese el ID del estudiante a consultar: "))
    except ValueError:
        print("ID de estudiante no válido.")
        return

    asignaciones = datos_sistema["asignaciones"].get(est_id)
    if asignaciones:
        nombre_estudiante = datos_sistema["estudiantes"].get(est_id, "Desconocido")
        print(f"\nMaterias de {nombre_estudiante} (ID: {est_id})")
        
        for codigo in asignaciones:
            nombre_materia = datos_sistema["materias"].get(codigo, {}).get('nombre', 'Materia Eliminada')
            print(f"Código: {codigo} | Nombre: {nombre_materia}")
    else:
        print(f"El estudiante con ID {est_id} no tiene materias asignadas o no existe.")

def desasignar_materia():
    """Desasigna una materia de un estudiante."""
    print("\n3. Desasignar Materia")
    if not datos_sistema["asignaciones"]:
        print("No hay asignaciones registradas para desasignar.")
        return
        
    try:
        est_id = int(input("Ingrese el ID del estudiante: "))
        cod_materia = input("Ingrese el código de la materia a desasignar: ").upper()
    except ValueError:
        print("ID de estudiante no válido.")
        return

    if est_id in datos_sistema["asignaciones"] and cod_materia in datos_sistema["asignaciones"][est_id]:
        
        nombre_estudiante = datos_sistema["estudiantes"].get(est_id, {}).get('nombre', 'Estudiante Desconocido')
        nombre_materia = datos_sistema["materias"].get(cod_materia, {}).get('nombre', 'Materia Desconocida')
        
        # Desasignar
        del datos_sistema["asignaciones"][est_id][cod_materia]
        datos_sistema["notas"][est_id].pop(cod_materia, None)
        
        # Limpiar si la lista de asignaciones/notas del estudiante queda vacía
        if not datos_sistema["asignaciones"][est_id]:
            datos_sistema["asignaciones"].pop(est_id, None)
        if not datos_sistema["notas"][est_id]:
            datos_sistema["notas"].pop(est_id, None)
        
        # Actualizar contadores para reportes (si el estudiante/materia existe aún)
        if est_id in datos_sistema["estudiantes"]:
            datos_sistema["estudiantes"][est_id]['materias_inscritas'] -= 1
        if cod_materia in datos_sistema["materias"]:
            datos_sistema["materias"][cod_materia]['estudiantes_inscritos'] -= 1
            
        print(f" Materia '{nombre_materia}' desasignada con éxito del estudiante '{nombre_estudiante}'.")
    else:
        print(" Asignación no encontrada (ID de estudiante o código de materia incorrectos).")


#Menú de Asignaciones

def menu_asignaciones():
    """Menú para la gestión de asignaciones (Estudiante ↔ Materias)."""
    while True:
        print("""
--- Asignaciones (Estudiante ↔ Materias) ---
1. Asignar materia a estudiante
2. Consultar asignaciones por estudiante
3. Desasignar materia
4. Volver al menú principal
""")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            asignar_materia_a_estudiante()
        elif opcion == "2":
            listar_asignaciones_por_estudiante()
        elif opcion == "3":
            desasignar_materia()
        elif opcion == "4":
            break
        else:
            print("Opción no válida.")


# 5. NOTAS Y CALIFICACIONES (Opción 4 del Menú Principal)

# --- Funciones de Acción de Notas ---

def registrar_nota():
    """Permite registrar una nota para un estudiante en una materia específica."""
    print("\n1. Registrar Nota")
    if not datos_sistema["notas"]:
        print("No hay materias asignadas para registrar notas.")
        return

    try:
        est_id = int(input("Ingrese el ID del estudiante: "))
        cod_materia = input("Ingrese el código de la materia: ").upper()
        nota = float(input("Ingrese la nota a registrar (0.0 a 5.0): "))
    except ValueError:
        print("Entrada no válida. Asegúrese de ingresar números para ID y nota.")
        return
        
    if not (0.0 <= nota <= 5.0):
         print("La nota debe estar en el rango de 0.0 a 5.0.")
         return

    if est_id in datos_sistema["notas"] and cod_materia in datos_sistema["notas"][est_id]:
        datos_sistema["notas"][est_id][cod_materia].append(nota)
        
        nombre_estudiante = datos_sistema["estudiantes"].get(est_id, {}).get('nombre', 'Estudiante Desconocido')
        nombre_materia = datos_sistema["materias"].get(cod_materia, {}).get('nombre', 'Materia Desconocida')
        
        print(f"Nota {nota} registrada con éxito para '{nombre_estudiante}' en '{nombre_materia}'.")
    else:
        print("Asignación no encontrada. El estudiante no está inscrito en esa materia o no existe.")

def listar_notas_por_estudiante():
    """Muestra todas las notas de un estudiante en todas sus materias."""
    print("\n 2. Listar Notas por Estudiante")
    if not datos_sistema["notas"]:
        print("No hay notas registradas aún.")
        return
        
    try:
        est_id = int(input("Ingrese el ID del estudiante a consultar: "))
    except ValueError:
        print("ID de estudiante no válido.")
        return

    notas_estudiante = datos_sistema["notas"].get(est_id)
    if notas_estudiante:
        nombre_estudiante = datos_sistema["estudiantes"].get(est_id, "Desconocido")
        print(f"\nCalificaciones de {nombre_estudiante} (ID: {est_id})")
        
        for codigo, notas in notas_estudiante.items():
            nombre_materia = datos_sistema["materias"].get(codigo, {}).get('nombre', 'Materia Eliminada')
            promedio = sum(notas) / len(notas) if notas else 0
            
            print(f"Materia: {nombre_materia} ({codigo})")
            print(f"  Notas: {', '.join(map(str, notas))}")
            print(f"  Promedio: {promedio:.2f}")
    else:
        print(f"El estudiante con ID {est_id} no tiene notas registradas o no existe.")

def consultar_nota_final():
    """Calcula y muestra la nota final (promedio) de un estudiante en una materia."""
    print("\n3. Consultar Nota Final por Materia")
    if not datos_sistema["notas"]:
        print("No hay notas registradas para calcular promedios.")
        return
        
    try:
        est_id = int(input("Ingrese el ID del estudiante: "))
        cod_materia = input("Ingrese el código de la materia: ").upper()
    except ValueError:
        print("Entrada no válida.")
        return

    if est_id in datos_sistema["notas"] and cod_materia in datos_sistema["notas"][est_id]:
        notas = datos_sistema["notas"][est_id][cod_materia]
        
        if not notas:
            print("No hay notas registradas para esta materia.")
            return

        nombre_estudiante = datos_sistema["estudiantes"].get(est_id, {}).get('nombre', 'Estudiante Desconocido')
        nombre_materia = datos_sistema["materias"].get(cod_materia, {}).get('nombre', 'Materia Desconocida')
        
        promedio = sum(notas) / len(notas)
        estado = "Aprobado (≥ 3.0)" if promedio >= 3.0 else "Reprobado (< 3.0)"
        
        print(f"\nNota Final")
        print(f"Estudiante: {nombre_estudiante}")
        print(f"Materia: {nombre_materia}")
        print(f"Promedio Final: {promedio:.2f}")
        print(f"Estado: {estado}")
    else:
        print("Asignación no encontrada. Verifique ID de estudiante y código de materia.")

#Menú de Notas y Calificaciones

def menu_notas_y_calificaciones():
    """Menú para la gestión de notas y calificaciones."""
    while True:
        print("""
*** Notas y Calificaciones ***
1. Registrar nota
2. Listar todas las notas de un estudiante
3. Consultar nota final de una materia
4. Volver al menú principal
""")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_nota()
        elif opcion == "2":
            listar_notas_por_estudiante()
        elif opcion == "3":
            consultar_nota_final()
        elif opcion == "4":
            break
        else:
            print("Opción no válida.")

# 6. REPORTES Y ESTADÍSTICAS (Opción 5 del Menú Principal)

# Funciones de Acción de Reportes

def reporte_promedios_generales():
    """Calcula y muestra el promedio general de todos los estudiantes."""
    print("\n1. Reporte de Promedios Generales de Estudiantes")
    if not datos_sistema["notas"]:
        print(" No hay notas registradas para generar el reporte.")
        return
        
    for est_id, notas_estudiante in datos_sistema["notas"].items():
        nombre_estudiante = datos_sistema["estudiantes"].get(est_id, {}).get('nombre', 'Estudiante Desconocido')
        
        total_notas = 0
        conteo_notas = 0
        
        # Sumar todas las notas de todas las materias
        for notas in notas_estudiante.values():
            total_notas += sum(notas)
            conteo_notas += len(notas)
            
        promedio_general = total_notas / conteo_notas if conteo_notas > 0 else 0
        
        print(f"ID: {est_id} | Nombre: {nombre_estudiante} | Promedio General: {promedio_general:.2f}")

def reporte_estudiantes_por_materia():
    """Muestra la lista de estudiantes inscritos en cada materia."""
    print("\n2. Reporte de Estudiantes por Materia")
    if not datos_sistema["materias"]:
        print("No hay materias registradas.")
        return
        
    for cod_materia, datos_materia in datos_sistema["materias"].items():
        print(f"\n- Materia: {datos_materia['nombre']} ({cod_materia})")
        estudiantes_en_materia = []
        
        # Buscar en las asignaciones quién tiene esta materia
        for est_id, asignaciones in datos_sistema["asignaciones"].items():
            if cod_materia in asignaciones:
                nombre_estudiante = datos_sistema["estudiantes"].get(est_id, {}).get('nombre', 'Estudiante Desconocido')
                estudiantes_en_materia.append(f"ID {est_id}: {nombre_estudiante}")
        
        if estudiantes_en_materia:
            print("  Estudiantes Inscritos:")
            for est in estudiantes_en_materia:
                print(f"    - {est}")
        else:
            print("  (Ningún estudiante inscrito)")


def reporte_analisis_desempeno():
    """Muestra estadísticas de materias: promedio de la materia y conteo de aprobados/reprobados."""
    print("\n3. Reporte de Análisis de Desempeño por Materia")
    if not datos_sistema["materias"] or not datos_sistema["notas"]:
        print("No hay materias o notas registradas para generar el reporte.")
        return
        
    for cod_materia, datos_materia in datos_sistema["materias"].items():
        todas_las_notas = []
        aprobados = 0
        reprobados = 0
        
        # Recorrer las notas de todos los estudiantes para esta materia
        for notas_estudiante in datos_sistema["notas"].values():
            if cod_materia in notas_estudiante:
                notas = notas_estudiante[cod_materia]
                if notas:
                    promedio = sum(notas) / len(notas)
                    todas_las_notas.extend(notas)
                    
                    if promedio >= 3.0:
                        aprobados += 1
                    else:
                        reprobados += 1
        
        promedio_materia = sum(todas_las_notas) / len(todas_las_notas) if todas_las_notas else 0
        
        print(f"\nMateria: {datos_materia['nombre']} ({cod_materia})")
        print(f"  Promedio General de la Materia: {promedio_materia:.2f}")
        print(f"  Total Estudiantes con Notas: {aprobados + reprobados}")
        print(f"  Aprobados (≥ 3.0): {aprobados}")
        print(f"  Reprobados (< 3.0): {reprobados}")
        
# Menú de Reportes y Estadísticas

def menu_reportes_y_estadisticas():
    """Menú para generar reportes y estadísticas académicas."""
    while True:
        print("""
--- Reportes y Estadísticas ---
1. Promedios Generales de Estudiantes
2. Listado de Estudiantes por Materia
3. Análisis de Desempeño por Materia (Promedio, Aprobados/Reprobados)
4. Volver al menú principal
""")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            reporte_promedios_generales()
        elif opcion == "2":
            reporte_estudiantes_por_materia()
        elif opcion == "3":
            reporte_analisis_desempeno()
        elif opcion == "4":
            break
        else:
            print("Opción no válida.")


# 7. MENÚ PRINCIPAL


def menu_principal():
    """Menú principal del Sistema de Gestión Académica."""
    while True:
        print("""
<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3
     SISTEMA DE GESTIÓN ACADÉMICA
<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3
1. Gestión de Estudiantes
2. Gestión de Materias
3. Asignaciones (Estudiante ↔ Materias)
4. Notas y Calificaciones
5. Reportes y Estadísticas
6. Salir
""")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_gestion_estudiantes()
        elif opcion == "2":
            menu_gestion_materias()
        elif opcion == "3":
            menu_asignaciones()
        elif opcion == "4":
            menu_notas_y_calificaciones()
        elif opcion == "5":
            menu_reportes_y_estadisticas()
        elif opcion == "6":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.")

# Ejecutar el programa
if __name__ == "__main__":
    menu_principal()
