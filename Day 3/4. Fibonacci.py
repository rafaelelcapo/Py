def fibonacci(n):
    fibo = [0, 1]
    while len(fibo) < n:
        next_term = fibo[-1] + fibo[-2]
        fibo.append(next_term)
    return fibo

n = int(input("Ingrese el número de terminos de la secuencia de Fibonacci que desea generar: "))
fibo_secu = fibonacci(n)
print("Secuencia de Fibonacci:", fibo_secu)
