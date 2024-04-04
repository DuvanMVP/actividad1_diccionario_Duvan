#elaborar un programa en python que capture la siguiente informacion de un estudiante
#codigo, nombre, apellidos, contacto, correo, sexo, telefono, solo se registrta los estudiantes que tengan el siguiente criterio
# sexo masculino, edad 15-25, estrato 1 2 . 2 sexo femenino 
#edad (20-35), estrato (1-4) en caso de que no plique guardar su contrato en una lista llamada pendiente
# Función para verificar si el estudiante cumple con los criterios especificados
def fnt_verificar_criterios(estudiante):
    if estudiante['sexo'] == "masculino":
        if 15 <= estudiante['edad'] <= 25 and estudiante['estrato'] in [1, 2]:
            return True
    elif estudiante['sexo'] == "femenino":
        if 20 <= estudiante['edad'] <= 35 and 1 <= estudiante['estrato'] <= 4:
            return True
    return False

def fnt_capturar_estudiante():
    estudiante = {}
    estudiante['codigo'] = input("Ingrese el código del estudiante: ")
    estudiante['nombre'] = input("Ingrese el nombre del estudiante: ")
    estudiante['apellidos'] = input("Ingrese los apellidos del estudiante: ")
    estudiante['contacto'] = input("Ingrese el contacto del estudiante: ")
    estudiante['correo'] = input("Ingrese el correo del estudiante: ")
    estudiante['sexo'] = input("Ingrese el sexo del estudiante (masculino/femenino): ").lower()
    estudiante['telefono'] = input("Ingrese el teléfono del estudiante: ")
    estudiante['edad'] = int(input("Ingrese la edad del estudiante: "))
    estudiante['estrato'] = int(input("Ingrese el estrato del estudiante: "))

    return estudiante

def main():
    estudiantes_aprobados = []
    estudiantes_pendientes = []

    while True:
        estudiante = fnt_capturar_estudiante()

        if fnt_verificar_criterios(estudiante):
            estudiantes_aprobados.append(estudiante)
            print("El estudiante ha sido registrado exitosamente.")
        else:
            estudiantes_pendientes.append(estudiante)
            print("El estudiante no cumple con los criterios y ha sido agregado a la lista de pendientes.")

        continuar = input("¿Desea registrar otro estudiante? (s/n): ").lower()
        if continuar != 's':
            break

    print("\nEstudiantes Aprobados:")
    for estudiante in estudiantes_aprobados:
        print(f"Código: {estudiante['codigo']}, Nombre: {estudiante['nombre']} {estudiante['apellidos']}, Sexo: {estudiante['sexo']}, Edad: {estudiante['edad']}, Estrato: {estudiante['estrato']}")

    print("\nEstudiantes Pendientes:")
    for estudiante in estudiantes_pendientes:
        print(f"Código: {estudiante['codigo']}, Nombre: {estudiante['nombre']} {estudiante['apellidos']}, Sexo: {estudiante['sexo']}, Edad: {estudiante['edad']}, Estrato: {estudiante['estrato']}")

if __name__ == "__main__":
    main()