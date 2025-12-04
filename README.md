Calculadora Modular en Python

Este proyecto es una calculadora modular desarrollada en Python, que permite realizar operaciones aritméticas básicas utilizando un módulo separado llamado operaciones.
El objetivo es mostrar una estructura organizada del código mediante la separación de funciones en distintos archivos.

📁 Estructura del proyecto
📂 calculadora_modular
│── main.py
│── operaciones.py
│── README.md


main.py → Contiene el menú interactivo y la lógica principal del programa.

operaciones.py → Contiene todas las funciones matemáticas utilizadas por la calculadora.

▶️ ¿Cómo usar la calculadora?

Ejecuta el archivo main.py:

python main.py


El menú mostrará las siguientes opciones:

1. Suma
2. Resta
3. Multiplicación
4. División
5. Potencia
6. División entera
0. Salir


Selecciona una operación ingresando el número correspondiente.

Ingresa los valores solicitados.

El resultado se mostrará por consola.

📌 Código de ejemplo
main.py
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
    elif opcion == "4":
        print("Resultado:", operaciones.division(a, b))
    elif opcion == "5":
        print("Resultado:", operaciones.potencia(a, b))
    elif opcion == "6":
        print("Resultado:", operaciones.division_entera(a, b))
    else:
        print("Opción inválida.")

operaciones.py
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"

def potencia(a, b):
    return a ** b

def division_entera(a, b):
    if b != 0:
        return a // b
    else:
        return "Error: División por cero"

🧠 Conceptos prácticos aplicados

Modularidad en Python

Manejo básico de funciones

Entrada y salida por consola

Control de errores simples (como división por cero)
