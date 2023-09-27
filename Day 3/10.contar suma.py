def suma_digitos(numero):
    suma = 0
    while numero > 0:
        digito = numero % 10
        suma += digito
        numero //= 10
    return suma

numero = int(input("Ingrese un número: "))
resultado = suma_digitos(numero)
print(f"La suma de los digitos de {numero} es {resultado}")
