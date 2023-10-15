# Josmar Gustavo Palomino Castelan
# Josmar360

#Declaro variables para hacer validaciones
nota_mayor = 0
nota_menor = 21

#Crear variable para ingresar la cantidad de alumnos
N = int(input("Dame la cantidad de alumnos a registrar: "))
i = 1

#Ciclo While para registrar a los alumnos
while N >= i:
    print("========== Registro del alumno {} ==========".format(i))
    Nombre_Alumno = input("Dame el nombre del alumno: ")
    Apellido_Alumno = input("Dame el apellido del alumno: ")
    Seccion_Alumno = input("Dame la seccion del alumno: ")
    Grado_Alumno = input("Dame el grado del alumno: ")

    #crear variable para ingresar el numero de cursos
    M = int(input("Dame el numero de materias que registraras para el alumno: "))
    j = 1
    Sum_Calificacion = 0

    #Ciclo while para registrar las materias
    while M >= j:
        print("========== Registro de la materia {} ==========".format(j))
        Nombre_Curso = input("Dame el nombre del curso: ")
        Calificacion_Curso = float(input("Dame la calificacion de la materia: "))

        #Condicion If para validar la califiacion
        if (0 <= Calificacion_Curso <= 10):  
            #Condicion if para comparar la calificion maxima y minima
            if (Calificacion_Curso > nota_mayor):
                nota_mayor = Calificacion_Curso
            else:
                nota_menor = Calificacion_Curso
            Sum_Calificacion += Calificacion_Curso
        else:
            print("El valor de la nota no pertenece a un rango valido...")
        j += 1

    #Calcular el promedio del alumno
    Promedio = Sum_Calificacion / M
    print("============== Informacion de registro ==============")
    print("El nombre completo del alumno es: ", Nombre_Alumno, Apellido_Alumno)
    print("La seccion del alumno es: ", Seccion_Alumno)
    print("El grado del alumno es: ", Grado_Alumno)

    #Uso de for para imprimir las materias y su califficacion
    for aux in range(M):
        print("El nombre de la materia es: ", Nombre_Curso)
        print("La calificacion del curso es: ", Calificacion_Curso)

    #Uso de if para indicar si paso el curso o no
    print("El promedio del alumno es: ", Promedio)
    if (Promedio > 6):
        print("Felicidades, aprobo el curso...")
    else:
        print("Ha desaprobado el curso...")
    print("Calificacion maxima del alumno: ", nota_mayor)
    if (nota_menor == 21):
        print("Calificacion minima del alumno: 0")
    else:
        print("Calificacion minima del alumno: ", nota_menor)
    print("=" * 47)

    i += i