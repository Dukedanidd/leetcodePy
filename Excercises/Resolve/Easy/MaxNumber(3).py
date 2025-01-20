'''
    Definir una funcion max 3 que reciba 3 numeros y retorne
    el mayor de esos 3 numeros
'''

def max_tres(n1, n2, n3):
    '''
        Tomara 3 valores numericos y devolvera el mayor de esos 3
        
        Args:
            n1: int Numero 1 a comparar
            n2: int Numero 2 a comparar
            n3: int Numero 3 a comparar
            
        Returns:
            int: Numero mayor de los 3 comparados
    '''
    if n1 > n2 and n3:
        return n1
    elif n2 > n1 and n3:
        return n2
    else:
        return n3

print(max_tres(120,300,43))
        