# 5. Mover Ceros
# Mueve todos los ceros de un arreglo al final, manteniendo el orden de los demás elementos.

arreglo = [0 , 1, 2, 0, 3, 5, 0, 5]

indice = 0

for num in arreglo:
    if num != 0:
        arreglo[indice] = num
        indice += 1
    
for i in range(indice, len(arreglo)):
    arreglo[i] = 0
    
print('Arreglo con 0 al final ', arreglo)