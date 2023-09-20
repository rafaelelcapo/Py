num1 = input("Ingresa el primer número: ")
num2 = input("Ingresa el segundo número: ")

if num1.isnumeric() and num2.isnumeric():
    resul = int(num1) + int(num2)
    print("La suma de", num1, "+", num2, "es:", resul)
else:
    print("Entrada no válida, favor de ingresa números enteros.")
