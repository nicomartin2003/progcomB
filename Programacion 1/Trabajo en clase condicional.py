fecha_actual = input("Ingrese la fecha actual en formato día, DD/MM: ").lower()
dia_semana, fecha = fecha_actual.split(', ')
dia, mes = fecha.split('/')
dia = int(dia)
mes = int(mes)

if not (1 <= dia <= 31) or not (1 <= mes <= 12):
            raise ValueError("Fecha inválida")

if dia_semana == 'lunes':
            nivel = "inicial"
elif dia_semana == 'martes':
            nivel = "intermedio"
elif dia_semana == 'miércoles':
            nivel = "avanzado"
elif dia_semana == 'jueves':
            nivel = "práctica hablada"
elif dia_semana == 'viernes':
            nivel = "inglés para viajeros"
else:
            raise ValueError("Día de la semana inválido")

if nivel in ["inicial", "intermedio", "avanzado"]:
            examenes = input("¿Hubo exámenes? (s/n): ").lower()
            if examenes == 's':
                aprobados = int(input("Ingrese la cantidad de alumnos aprobados: "))
                reprobados = int(input("Ingrese la cantidad de alumnos reprobados: "))
                total_alumnos = aprobados + reprobados
                porcentaje_aprobados = (aprobados / total_alumnos) * 100
                print(f"Porcentaje de aprobados: {porcentaje_aprobados:.2f}%")

if nivel == "práctica hablada":
            asistencia = float(input("Ingrese el porcentaje de asistencia a clase: "))
            if asistencia > 50:
                print("Asistió la mayoría")
            else:
                print("No asistió la mayoría")

if nivel == "inglés para viajeros" and (mes == 1 or mes == 7) and dia == 1:
            print("Comienzo de nuevo ciclo")
            cantidad_alumnos = int(input("Ingrese la cantidad de alumnos del nuevo ciclo: "))
            arancel = float(input("Ingrese el arancel en $ por cada alumno: "))
            ingreso_total = cantidad_alumnos * arancel
            print(f"Ingreso total en $: {ingreso_total:.2f}")


