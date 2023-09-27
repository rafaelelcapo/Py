def nombres_con_A(nombres):
    nombres_con_a = [a for a in nombres if a.startswith('A')]
    return nombres_con_a

lista_nombres = ["Rafael", "Alejandro", "Alberto", "Marta", "Carlos"]
nombres_A = nombres_con_A(lista_nombres)
print("Nombres que comienzan con 'A':", nombres_A)
