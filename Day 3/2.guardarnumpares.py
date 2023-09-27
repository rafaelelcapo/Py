def num_pares(lista):
    pares = []
    for num in lista:
        if num % 2 == 0:
            pares.append(num)
    return pares

lista_original = [1, 2, 23, 4, 5, 6, 56, 8, 91, 100]
pares = num_pares(lista_original)
print("Los números pares son:", pares)
