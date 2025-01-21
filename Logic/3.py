"""
    Encuentra el número más grande en una lista.
"""

def numero_mayor(lista):
    mayor = lista[0]
    for num in lista:
        if num > mayor:
            mayor = num
    return mayor

print(numero_mayor([1,2,44,567,34,2121]))