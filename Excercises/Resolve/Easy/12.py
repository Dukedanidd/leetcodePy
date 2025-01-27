# 12. Fibonacci Recursivo
# Calcula el n-ésimo número de Fibonacci de forma recursiva.

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

if __name__ == '__main__':
    for i in range(1, 11):
        print(f'F({i}) = {fibonacci(i)}')
