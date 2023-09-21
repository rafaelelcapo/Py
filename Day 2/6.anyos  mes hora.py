dias = int(input("Ingresa el número de días: "))

anyos = dias // 365
semanas = (dias % 365) // 7
dias_restantes = (dias % 365) % 7

print(f"{dias} dias equivalen a {anyos} años, {semanas} semanas y {dias_restantes} días.")
