def es_bisiesto(anyo):
    if (anyo % 4 == 0 and anyo % 100 != 0) or (anyo % 400 == 0):
        return True
    else:
        return False

anyo = int(input("Ingrese un año: "))
if es_bisiesto(anyo):
    print(f"{anyo} es un año bisiesto.")
else:
    print(f"{anyo} no es un año bisiesto.")
