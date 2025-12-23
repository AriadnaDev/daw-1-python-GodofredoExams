
#Proyecto 3: Godofredo

#Importo los módulos que voy a usar
import os
import colorama
from colorama import *

#Limpio pantalla para comenzar el programa
os.system("cls")


#Inicio el colorama
colorama.init(autoreset=True)

#Inicializo el diccionario que guardará los datos 
clases_registradas = {}


#Funcion para la opción 1: Registro de las clases y numero de alumnos
def op1(clases_registradas):
        
        #Pregunto hasta que se escriba ya, añadiendo los datos al diccionario
        while True:
            os.system("cls")
            clase = input("\n¿Qué clase desea registrar? (Escriba 'ya' para volver al menú ): ")
            
            clase = clase.lower()
            
            if clase == "ya":
                os.system("cls")
                break
            
            num_alumnos = input(f"Número de alumnos que van a la clase {clase}: ").strip()
            
            if num_alumnos.isdigit():
                clases_registradas[clase] = {
            "alumnos": {}, 
            "examenes": {},
            "num_alumnos": int(num_alumnos)
        }
            else:
                print("Por favor escriba un número válido")
        return clases_registradas



#Menú principal

while True:
    os.system("cls")
    print(Fore.LIGHTBLUE_EX +'''
          
   ████████               █████             ██████                         █████           ██        
  ███░░░░░███             ░░███             ███░░███                       ░░███           ███        
 ███     ░░░   ██████   ███████   ██████   ░███ ░░░  ████████   ██████   ███████   ██████ ░░░   █████ 
░███          ███░░███ ███░░███  ███░░███ ███████   ░░███░░███ ███░░███ ███░░███  ███░░███     ███░░  
░███    █████░███ ░███░███ ░███ ░███ ░███░░░███░     ░███ ░░░ ░███████ ░███ ░███ ░███ ░███    ░░█████ 
░░███  ░░███ ░███ ░███░███ ░███ ░███ ░███  ░███      ░███     ░███░░░  ░███ ░███ ░███ ░███     ░░░░███
 ░░█████████ ░░██████ ░░████████░░██████   █████     █████    ░░██████ ░░████████░░██████      ██████ 
  ░░░░░░░░░   ░░░░░░   ░░░░░░░░  ░░░░░░   ░░░░░     ░░░░░      ░░░░░░   ░░░░░░░░  ░░░░░░      ░░░░░░  
                                                                                                      
                                                                                                   
                    ██████████                                              
                   ░░███░░░░░█                                              
                    ░███  █ ░  █████ █████  ██████   █████████████    █████ 
                    ░██████   ░░███ ░░███  ░░░░░███ ░░███░░███░░███  ███░░  
                    ░███░░█    ░░░█████░    ███████  ░███ ░███ ░███ ░░█████ 
                    ░███ ░   █  ███░░░███  ███░░███  ░███ ░███ ░███  ░░░░███
                    ██████████ █████ █████░░████████ █████░███ █████ ██████ 
                    ░░░░░░░░░░ ░░░░░ ░░░░░  ░░░░░░░░ ░░░░░ ░░░ ░░░░░ ░░░░░░  
                            
          ''')
    
    print(Fore.LIGHTBLUE_EX + "\nEl programa dedicado a facilitarle la corrección de exámenes")

    print(Style.DIM +"\n*Es recomendable seguir el orden de las opciones para un mejor funcionamiento del programa*")
    
    #Menú de opciones
    print("\nOpción 1: Registrar las clases que imparte")
    print("\nOpción 2: Registro de exámenes")
    print("\nOpción 3: Comprobar respuestas")
    print("\nOpción 4: Ver resultados de los exámenes")
    
    
    opcion = input("\n¿Qué opción quiere elegir?: ")
    
    
        
    #Opción 1: Registro de las clases
    if opcion == "1":
            
            #Menú de las clases
            while True:
                os.system("cls")
                print(Fore.LIGHTMAGENTA_EX +"REGISTRO DE CLASES") 
                print("1. Registrar clases")
                print("2. Mostrar clases registradas")
                print("3. Salir")
                
                opcion_clase = input("Seleccione una opción: ")
                
                #El diccionario incorpora las claves/valores llamando a la función
                if opcion_clase == "1":
                    os.system("cls")
                    clases_registradas = op1(clases_registradas)  
                    print("\nClases registradas con éxito.")
                    input("\nPresione ENTER para continuar ")
                
                #Muestro por pantalla los resultados, solo si hay clases registradas
                elif opcion_clase == "2":
                    os.system("cls")
                    if not clases_registradas:
                        print("No hay clases registradas aún")
                        input("\nPresione ENTER para volver al menú")  
                    else:
                        #Muestro si hay clases  
                        print("\nLas clases registradas son:")
                        for clase, datos in clases_registradas.items():
                            print(f"Clase: {clase} - Número de alumnos: {datos}")
                        input("\nPresiona ENTER para volver al menú") 
                        
                #Vuelvo al menú
                elif opcion_clase == "3":
                    print("Va a volver al menú principal")
                    break
                
                else:
                    print("Opción no válida, inténtelo de nuevo")
                    input()
                    os.system("cls")
            
            
    #Opción 2: Registro de exámenes
    elif opcion == "2":
        while True:
            os.system("cls")
            print(Fore.LIGHTGREEN_EX + "REGISTRO DE EXAMENES")   

            #Verifico si hay clases registradas
            if not clases_registradas:
                print("Aún no hay clases registradas, primero debe registrar una clase para registrar un examen. \nSerá redirigido al menú principal")
                input("Pulse ENTER para continuar ")
                os.system("cls")
                break
            
            #Si ya hay clases registradas
            else:
                while True:
                    os.system("cls")
                    
                    #Las muestro ordenadas empezando desde el 1
                    for num, clase in enumerate(clases_registradas.keys(), start=1):
                        print(f"Número: {num}, Nombre de la clase: {clase}")

                    opcion_examenes = input("\n¿De qué clase quieres registrar los exámenes? (Escriba el número de clase correspondiente): ")

                    #Verifico que la opción ingresada sea válida (si se suma 1 ya estaría fuera de rango)
                    if not opcion_examenes.isdigit() or int(opcion_examenes) not in range(1, len(clases_registradas) + 1):
                        print("No existe ese número de clase, por favor ingrese un número correcto.")
                        input()
                        
                    else:
                        #Creo una lista con las clases introducidas para poder enumerarlas, que reste 1 para que se asigne correctamente al número que ha ingresado por pantalla
                        clase_seleccionada = list(clases_registradas.keys())[int(opcion_examenes) - 1]
                        print(f"Clase seleccionada: {clase_seleccionada}")
                        break

                #Guardo los exámenes de la clase seleccionada en su lugar correspondiente
                examenes = clases_registradas[clase_seleccionada]["examenes"]


               #Una vez todo esté correcto, menú dentro de la clase seleccionada                 
                while True:
                    os.system("cls")
                    print(Fore.LIGHTGREEN_EX + f"Gestión de Exámenes de la clase: {clase_seleccionada}")
                    print("1. Registrar un nuevo examen")
                    print("2. Ver exámenes registrados")
                    print("3. Modificar respuestas ya registradas en un examen")
                    print("4. Volver al menú principal")

                    opcion_class_exam = input("\nSeleccione una opción: ")

                    #Gestión de exámenes, registrar uno nuevo
                    if opcion_class_exam == "1":
                        os.system("cls")
                        
                        #Creo un nombre para el examen
                        nombre_examen = input("\nIntroduzca el nombre del examen: ").strip()

                        #Compruebo que aún no exista
                        if nombre_examen in examenes:
                            print("Ya ha registrado ese examen")
                            
                        else:
                            os.system("cls")
                            #Registro el número de preguntas
                            num_preguntas = input("Digame el número de preguntas: ")
                            if not num_preguntas.isdigit():
                                print("\nDebe ingresar un número válido, por favor")
                                
                            else:
                                os.system("cls")
                                num_preguntas = int(num_preguntas)
                                
                                #Creo un diccionario para almacenar el num y letra del examen que se registra
                                respuestas = {}

                                #Recorro la cantidad de preguntas añadiendo su correspondiente letra rellenando el diccionario
                                for i in range(1, num_preguntas + 1):
                                    respuesta = input(f"Respuesta correcta para la pregunta {i}: ").lower()
                                    respuestas[i] = respuesta
                                
                                #Se asignan dichas respuestas    
                                examenes[nombre_examen] = respuestas
                                print(f"Examen {nombre_examen} registrado correctamente ")
                        input("Pulse ENTER para continuar...")

                    #Ver examenes registrados
                    elif opcion_class_exam == "2":
                        os.system("cls")

                        #Compruebo si hay alguno
                        if not examenes:
                            print("No hay exámenes registrados para esta clase.")
                        
                        #En caso de que haya
                        else:
                            print(f"Los exámenes registrados de: {clase_seleccionada}:")
                            
                            #Muestro por pantalla todos los elementos dentro de examenes
                            for nombre, respuestas in examenes.items():
                                print(f"\n{nombre}")
                                for num, resp in respuestas.items():
                                    print(f"Pregunta {num}: {resp}")
                        
                        input("\nPresione ENTER para continuar ")
                        
                    #Modificar las respuestas   
                    elif opcion_class_exam == "3":
                        os.system("cls")
                        
                        #Accedo al diccionario 
                        examenes = clases_registradas[clase_seleccionada]["examenes"]

                        #En caso de que no haya examenes
                        if not examenes:
                            print("No hay exámenes registrados para modificar ")
                        
                        #En caso de que los haya mostrar por pantalla
                        else:
                            print("Exámenes disponibles: ")
                            for nombre in examenes.keys():
                                print(f"- {nombre}")

                            #Pido que escriba el nombre para que se pueda modificar el examen
                            examen_modificar = input("Ingrese el nombre del examen a modificar: ").strip()

                            #Compruebo que exista
                            if examen_modificar not in examenes:
                                print("Ese examen no existe, inténtelo de nuevo")
                            else:
                                print(f"Va a modificar el examen: {examen_modificar}")
                                
                            #Creo un bucle para modificarlo
                            while True:
                                os.system("cls")
                                #Correspondiente al diccionario de respuestas
                                pregunta_modificar = input("\nIngrese el número de la pregunta que desea modificar: ")

                                #Hago las comprobaciones previas
                                if pregunta_modificar.isdigit():
                                    pregunta_modificar = int(pregunta_modificar)
                                    
                                    #Si existe dicha respuesta en el examen ingresado anteriormente
                                    if pregunta_modificar in examenes[examen_modificar]:
                                        
                                        #Esta nueva respuesta sustituirá a la registrada anteriormente 
                                        nueva_respuesta = input(f"Respuesta actual para la pregunta {pregunta_modificar}: {examenes[examen_modificar][pregunta_modificar]}\nIngrese la nueva respuesta: ")
                                        nueva_respuesta = nueva_respuesta.lower()
                                        
                                        #Ahora se sobreescriben los datos dentro de los diccionarios asignados
                                        examenes[examen_modificar][pregunta_modificar] = nueva_respuesta
                                        print(f"Respuesta de la pregunta {pregunta_modificar} actualizada correctamente.")
                                        break
                                    
                                    else:
                                        print("Esa pregunta no existe en este examen")
                                else:
                                    print("Por favor ingrese un número válido de pregunta.")
                                

                        input("\nPresione ENTER para continuar ")

                    elif opcion_class_exam == "4":
                         break
                    

                    else:
                        print("Opción inválida, intenta de nuevo.")
                        input()
                    
                break
                                
    
    #Opción 3: Comprobar respuestas                    
    elif opcion == "3":
        os.system("cls")
        print(Fore.RED + "COMPROBACIÓN DE RESPUESTAS")
        
        #Compruebo si hay clases registradas con exámenes
        if not clases_registradas:
            print("No hay clases registradas aún.")
            input("\nPresione ENTER para volver al menú.")
           

        #Muestro las clases disponibles
        print("\nClases registradas:")
        for num, clase in enumerate(clases_registradas.keys(), start=1):
            print(f"{num}. {clase}")

        opcion_clase = input("\nSeleccione el número de la clase: ")

        if not opcion_clase.isdigit() or int(opcion_clase) not in range(1, len(clases_registradas) + 1):
            print("Número inválido, inténtelo de nuevo")
            

        clase_seleccionada = list(clases_registradas.keys())[int(opcion_clase) - 1]

        #Compruebo si hay exámenes registrados en la clase seleccionada
        if not clases_registradas[clase_seleccionada]["examenes"]:
            print("No hay exámenes registrados para esta clase.")
            input("\nPresione ENTER para volver al menú ")
        
        
        #Los muestro
        print(f"\nExámenes disponibles en {clase_seleccionada}:")
        for num, examen in enumerate(clases_registradas[clase_seleccionada]["examenes"].keys(), start=1):
            print(f"{num}. {examen}")

        opcion_examen = input("\nSeleccione el número del examen: ")

        if not opcion_examen.isdigit() or int(opcion_examen) not in range(1, len(clases_registradas[clase_seleccionada]["examenes"]) + 1):
            print("Número inválido, intente nuevamente.")
            input()
            
        
        #Ya puedo acceder al examen para recopilar las preguntas de los alumnos
        examen_seleccionado = list(clases_registradas[clase_seleccionada]["examenes"].keys())[int(opcion_examen) - 1]
        
        #Registro las respuestas correctas
        respuestas_correctas = clases_registradas[clase_seleccionada]["examenes"][examen_seleccionado]

        #Compruebo el máximo de alumnos accediendo a los datos dados en la opción 1
        num_maximo = clases_registradas[clase_seleccionada]["num_alumnos"]
        num_registrados = len(clases_registradas[clase_seleccionada]["alumnos"])

        #Me aseguro de no sobrepasar el número máximo de alumnos
        if num_registrados >= num_maximo:
            print("Ya se han registrado todos los alumnos. Volviendo al menú.")
            input("\nPresione ENTER para volver al menú.")
            os.system("cls")
            

        #Registro los alumnos pidiéndole datos al usuario
        while num_registrados < num_maximo:
            
            #Registro el nombre
            nombre_alumno = input(f"\nIngrese el nombre del alumno/alumna {num_registrados + 1}: ").capitalize()

            if nombre_alumno not in clases_registradas[clase_seleccionada]["alumnos"]:
                clases_registradas[clase_seleccionada]["alumnos"][nombre_alumno] = {}

                #Almaceno las respuestas del alumno 
                respuestas_alumno = {}
                correctas = 0
                incorrectas = 0
                blanco = 0

                print(f"\nIngrese las respuestas del alumno {nombre_alumno} (puede dejarlas en blanco presionando ENTER): ")

                #Conforme escribe las preguntas, indica el estado y las almacena en el contador
                for num_pregunta, respuesta_correcta in respuestas_correctas.items():
                    
                    respuesta_alumno = input(f"Pregunta {num_pregunta}: ").lower()

                    if respuesta_alumno == "":
                        estado = "En blanco"
                        blanco += 1
                    elif respuesta_alumno == respuesta_correcta:
                        estado = Fore.GREEN + "Correcta"
                        correctas += 1
                    else:
                        estado = Fore.RED + "Incorrecta"
                        incorrectas += 1

                    respuestas_alumno[num_pregunta] = {"respuesta": respuesta_alumno, "estado": estado}
                    print(f"Pregunta {num_pregunta}: {estado}")

                #Guardo las respuestas del alumno en la estructura correcta
                clases_registradas[clase_seleccionada]["alumnos"][nombre_alumno][examen_seleccionado] = {
                    "respuestas": respuestas_alumno,
                    "correctas": correctas,
                    "incorrectas": incorrectas,
                    "no_respondidas": blanco
                }

                print(f"\n{nombre_alumno} se ha registrado")
                num_registrados += 1

            else:
                print(f"{nombre_alumno} ya ha sido registrado, ingrese otro nombre, por favor")
                
        
        os.system("cls")
        
        #Una vez que se han registrado todos los alumnos, se muestran las notas
        print("\nNotas de los alumnos:")
        for nombre_alumno, datos_alumno in clases_registradas[clase_seleccionada]["alumnos"].items():
            respuestas_alumno = datos_alumno[examen_seleccionado]["respuestas"]
            correctas = datos_alumno[examen_seleccionado]["correctas"]
            incorrectas = datos_alumno[examen_seleccionado]["incorrectas"]
            no_respondidas = datos_alumno[examen_seleccionado]["no_respondidas"]

            print(f"\nAlumno: {nombre_alumno}")
            print(f"Correctas: {correctas}")
            print(f"Incorrectas: {incorrectas}")
            print(f"No respondidas: {blanco}")
        
        input("\nPresione ENTER para volver al menú principal...")
        
    #Opción 4: Resultados de los exámenes    
    elif opcion == "4":
        os.system("cls")
        print(Fore.MAGENTA + "INFORME DE NOTAS DEL EXAMEN")

    
        #Realizo de nuevo todas las comprobaciones
        #Si hay clases registradas con exámenes
        if not clases_registradas:
            print("No hay clases registradas aún.")
            input("\nPresione ENTER para volver al menú.")
            

        #Muestro las clases disponibles
        print("\nClases registradas:")
        for num, clase in enumerate(clases_registradas.keys(), start=1):
            print(f"{num}. {clase}")

        opcion_clase = input("\nSeleccione el número de la clase: ")
        os.system("cls")

        if not opcion_clase.isdigit() or int(opcion_clase) not in range(1, len(clases_registradas) + 1):
            print("Número inválido, inténtelo de nuevo")
            input()
           

        clase_seleccionada = list(clases_registradas.keys())[int(opcion_clase) - 1]

        #Si hay exámenes registrados en la clase seleccionada
        if not clases_registradas[clase_seleccionada]["examenes"]:
            print("No hay exámenes registrados para esta clase.")
            input("\nPresione ENTER para volver al menú ")
            

        #Muestro los exámenes disponibles
        print(f"\nExámenes disponibles en {clase_seleccionada}:")
        for num, examen in enumerate(clases_registradas[clase_seleccionada]["examenes"].keys(), start=1):
            print(f"{num}. {examen}")

        opcion_examen = input("\nSeleccione el número del examen: ")

        if not opcion_examen.isdigit() or int(opcion_examen) not in range(1, len(clases_registradas[clase_seleccionada]["examenes"]) + 1):
            print("Número inválido, intente nuevamente.")
            input()
            

        examen_seleccionado = list(clases_registradas[clase_seleccionada]["examenes"].keys())[int(opcion_examen) - 1]

        # Verificar si existen alumnos registrados en esa clase
        if "alumnos" not in clases_registradas[clase_seleccionada] or not clases_registradas[clase_seleccionada]["alumnos"]:
            print("No hay alumnos registrados en esta clase.")
            input("\nPresione ENTER para volver al menú")
            

        #Creo un listado según las notas de los alumnos
        notas_alumnos = []
        
        for nombre_alumno, datos_alumno in clases_registradas[clase_seleccionada]["alumnos"].items():
            if examen_seleccionado in datos_alumno:
                correctas = datos_alumno[examen_seleccionado]["correctas"]
                incorrectas = datos_alumno[examen_seleccionado]["incorrectas"]
                blanco = datos_alumno[examen_seleccionado]["no_respondidas"]

                #Compruebo de nuevo el total de preguntas para realizar los cálculos pertinentes
                total_preguntas = len(clases_registradas[clase_seleccionada]["examenes"][examen_seleccionado])

                #Respuesta correcta
                valor_respuesta_correcta = round(10 / total_preguntas,2)
                
                #Respuesta incorrecta
                valor_respuesta_incorrecta = round(valor_respuesta_correcta / 3,2)
                
                #Calculo la nota
                nota = round((correctas * valor_respuesta_correcta) - (incorrectas * valor_respuesta_incorrecta),2)

                #Añado los resultados a la lista
                
                notas_alumnos.append((nombre_alumno, nota))

        #Muestro las notas de los alumnos
        print(Fore.MAGENTA + f"\nListado de notas para el examen: {examen_seleccionado}:")
        for nombre_alumno, nota in notas_alumnos:
            print(f"{nombre_alumno}: {round(nota,2)} de 10")

        
        lista_notas = []
        for alumno in notas_alumnos:
            lista_notas.append(alumno[1])
        
        #Calculo la nota máxima, mínima y la media
        max_nota = round(max(lista_notas),2)
        min_nota = round(min(lista_notas),2)
        media_nota = round(sum(lista_notas) / len (lista_notas),2)

        #Muestro los resultados por pantalla
        print(Fore.MAGENTA + "\nResultados estadísticos del examen:")
        print(f"Nota máxima: {max_nota} sobre 10")
        print(f"Nota más baja: {min_nota} sobre 10")
        print(f"Nota media: {media_nota} sobre 10")

        input("\nPresione ENTER para volver al menú principal...")

input()