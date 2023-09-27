def contar_palabras(lista_palabras):
    contador = 0
    for palabra in lista_palabras:
        if len(palabra) > 5:
            contador += 1
    return contador

lista_palabras = ["platano", "perro", "computadora", "sistemas", "productividad"]
contador_palabras_largas = contar_palabras(lista_palabras)
print(f"Palabras con cinco caracteres: {contador_palabras_largas}")
