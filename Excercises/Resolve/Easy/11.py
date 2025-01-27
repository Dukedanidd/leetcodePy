# 11. Suma de Pares
# Encuentra todas las parejas en un arreglo que sumen un número dado.

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 10

def sum_pares(array, target):
    pares = []
    seen = set()
    
    for num in array:
        complement = target - num
        if complement in seen:
            pares.append((complement, num))
        seen.add(num)
    
    return pares

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 10
resultado = sum_pares(array, target)
print(f"Parejas que suman {target}:", resultado)
            
