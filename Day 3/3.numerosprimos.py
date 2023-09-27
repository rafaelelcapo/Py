def es_primo(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

num = int(input("Ingrese un número: "))
if es_primo(num):
    print(f"{num} es un número primo.")
else:
    print(f"{num} no es un número primo.")
