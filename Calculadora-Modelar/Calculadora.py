import operaciones


def menu():
    print("Calculadora Modular")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia")
    print("6. División entera")
    print("0. Salir")

while True:
    menu()
    opcion = input("Selecciona una operación: ")

    if opcion == "0":
        print("Hasta luego.")
        break

    a = float(input("Ingresa el primer número: "))
    b = float(input("Ingresa el segundo número: "))

    if opcion == "1":
        print("Resultado:", operaciones.suma(a, b))
    elif opcion == "2":
        print("Resultado:", operaciones.resta(a, b))
    elif opcion == "3":
        print("Resultado:", operaciones.multiplicacion(a, b))