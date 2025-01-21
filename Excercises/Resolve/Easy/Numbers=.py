# 10. Dos Números Iguales
# Determina si un arreglo contiene números duplicados.

def has_duplicate(numbers):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] == numbers[j]:
                return True
    return False
            
array = [1,2,2,3,1,4,5,6]
print(has_duplicate(array))