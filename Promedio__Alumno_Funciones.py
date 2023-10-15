# Josmar Gustavo Palomino Castelan
# Josmar360

#Crear una lista vacia para el registro de alumnos
Alumnos = []

#Funcion para obtener la calificacion minima de una materia
def Min_Calificacion_Materia(Materias):
    if (Materias):
        Min_Calificacion = min(Materia["Calificacion"] for Materia in Materias)
        return Min_Calificacion
    else:
        print("No se le registro ninguna calificacion al alumno...")
        return 0
    
#Funcion para obtener la calificacion maxima de una materia
def Max_Calificacion_Materia(Materias):
    if (Materias):
        Max_Calificacion = max(Materia["Calificacion"] for Materia in Materias)
        return Max_Calificacion
    else:
        print("No se le registro ninguna calificacion al alumno...")
        return 0

#Funcion para poder sacar el promedio del alumno
def Promedio_Alumno(Calificaciones):
    if (Calificaciones):
        return sum(Calificaciones) / len(Calificaciones)
    else:
        print("No se le registro ninguna calificacion al alumno...")
        return 0

#Funcion para poder realizar el registro de las materias
def Registro_Materias():
    Nombre_Materia = input("Dame el nombre de la materia: ")
    Calificacion_Materia = float(input("Dame la calificacion de la materia: "))
    if (Calificacion_Materia > 0 and Calificacion_Materia < 20):
        return {
            "Materia": Nombre_Materia,
            "Calificacion": Calificacion_Materia
        }
    else:
        print("El valor de la nota no pertenece a un rango válido...")
        Calificacion_Materia = 0
        return {
            "Materia": Nombre_Materia,
            "Calificacion": Calificacion_Materia
        }

#Funcion para poder registrar los alumnos
def Registro_Alumnos():
    Nombre_Alumno = input("Dame el nombre del alumno: ")
    Apellido_Alumno = input("Dame el apellido del alumno: ")
    Seccion_Alumno = input("Dame la seccion que tiene el alumno: ")
    Grado_Alumno = input("Dame el grado que tiene el alumno: ")

    #Crear una lista vacia para el registro de las materias
    Materias = []
    M = int(input("Dame el numero de materias que vas a registrar para el alumno: "))
    if (M >= 1):
        for _ in range(M):
            Materia = Registro_Materias()
            Materias.append(Materia)

    #Calculo del promedio de las materias de los alumnos
    Calificaciones_Alumno = [Materia["Calificacion"] for Materia in Materias]
    Promedio = Promedio_Alumno(Calificaciones_Alumno)
    return {
        "Nombre": Nombre_Alumno,
        "Apellido": Apellido_Alumno,
        "Seccion": Seccion_Alumno,
        "Grado": Grado_Alumno,
        "Materias": Materias,
        "Promedio": Promedio
    }

N = int(input("Dame la cantidad de alumnos que registraras: "))

if (N >= 1):
    for _ in range(N):
        Alumno = Registro_Alumnos()
        Alumnos.append(Alumno)

#Imprimir la lista de alumnos
print("========== Lista de registro ==========")
for Alumno in Alumnos:
    print(f"Nombre del alumno: {Alumno['Nombre']}")
    print(f"Apellido del alumno: {Alumno['Apellido']}")
    print(f"Seccion del alumno: {Alumno['Seccion']}")
    print(f"Grado del alumno: {Alumno['Grado']}")
    for Materia in Alumno['Materias']:
        print(f"Nombre de materia: {Materia['Materia']}")
        print(f"Calificacion de la materia: {Materia['Calificacion']}")
    if (Alumno['Promedio'] > 6):
        print(f"El alumno aprobo el curso con un promedio de: {Alumno['Promedio']}")
    else:
        print(f"El alumno reprobo el curso con un promedio de: {Alumno['Promedio']}")
    #Calcula la calificacion maxima que tuvo en las materias
    Calificacion_Maxima = Max_Calificacion_Materia(Alumno['Materias'])
    print(f"La calificacion más alta del alumno es: {Calificacion_Maxima}")
    #Calcula la calificacion minima que tuvo en las materias
    Calificacion_Min = Min_Calificacion_Materia(Alumno['Materias'])
    print(f"La calificacion mas bajaa del alumno es: {Calificacion_Min}")
    print("=" * 39)