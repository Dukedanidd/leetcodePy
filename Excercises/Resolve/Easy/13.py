# 13. Buscar Pico en un Arreglo
# Encuentra un elemento pico en un arreglo (mayor que sus vecinos).

def find_peak(array):
    # Si el primer elemento es mayor que el segundo, es un pico
    if array[0] > array[1]:
        return array[0]
        
    # Si el último elemento es mayor que el penúltimo, es un pico
    if array[-1] > array[-2]:
        return array[-1]
        
    # Buscar un pico en el medio del array
    left, right = 0, len(array) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # Si el elemento del medio es un pico, lo retornamos
        if array[mid-1] < array[mid] > array[mid+1]:
            return array[mid]
            
        # Si el elemento a la izquierda es mayor, el pico está a la izquierda
        if array[mid-1] > array[mid]:
            right = mid - 1
        # Si no, el pico está a la derecha
        else:
            left = mid + 1

array = [1, 2, 3, 1]
print(find_peak(array))

        