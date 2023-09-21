def es_palindromo(cadena):
    cadena = cadena.lower().replace(" ", "")
    return cadena == cadena[::-1]
texto = input("Ingresa una cadena de texto: ")
if es_palindromo(texto):
    print("La cadena es un palindroma")
else:
    print("La cadena no es un palandromoa")
