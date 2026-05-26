# Heidy Yulieth Torres
# Programa: Ingenieria de Sistemas
# Grupo: 213022_702

LIMITE_HORAS = 40

def calcular_jornada(horas):

    total = sum(horas)

    if total > LIMITE_HORAS:
        clasificacion = "Sobretiempo"
    else:
        clasificacion = "Horario Estandar"

    return total, clasificacion


dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]

matriz = []

for i in range(4):

    nombre = input("\nIngrese el nombre del recurso: ")

    horas = []

    for dia in dias:
        cantidad = int(input(f"Ingrese las horas trabajadas el {dia}: "))
        horas.append(cantidad)

    # Guardar el recurso completo
    matriz.append([nombre] + horas)

print("\nRESULTADOS")

for recurso in matriz:

    nombre = recurso[0]
    horas = recurso[1:]

    total, clasificacion = calcular_jornada(horas)

    print(f"\nRecurso: {nombre}")
    print(f"Total de horas: {total}")
    print(f"Clasificacion: {clasificacion}")
