def fibonacci(n):

    # FUNÇÃO QUE RETORNA O N-ÉSIMO TERMO DE UMA FUNÇÃO FIBONACCI
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# ENTRADA PARA O USUÁRIO

numero = int(input("Digite um número: "))

# Verificação se o número pertence à sequência de Fibonacci
pertence = False
i = 0
while not pertence:
    termo = fibonacci(i)
    if termo == numero:
        pertence = True
        print("O número", numero, "pertence à sequência de Fibonacci!")
    elif termo > numero:
        print("O número", numero, "não pertence à sequência de Fibonacci.")
        break
    i += 1
