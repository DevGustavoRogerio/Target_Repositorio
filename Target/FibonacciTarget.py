def fibonacci(num):
    fib_sequencia = [0, 1]

    while fib_sequencia[-1] < num:
        novo_fib = fib_sequencia[-1] + fib_sequencia[-2]
        fib_sequencia.append(novo_fib)
    return fib_sequencia


numero = int(input("Digite um número: "))
sequencia = fibonacci(numero)

if numero in sequencia:
    print(f"O número {numero} pertence a sequência de Fibonacci")
else:
    print(f"O número {numero} não pertence a sequência de Fibonacci")
