'''
    Definir una funcion max () que tome como argumento 2 numeros y
    devuelva el mayor de ellos
    Es cierto que Python tiene una funcion max() incorporada, pero hacer
    el ejercicio sin usarla es un buen ejercicio.
'''

def num_max(n1:int, n2:int):
    ''' Devolveremos el numero mayor al comparar ambos numeros
    
       Args:
        n1: int Numero 1 a comparar
        n2: int Numero 2 a comparar
        
       Returns:
        int: El numero mayor de los 2 
    '''
    if n1 > n2:
        return n1
    else:
        return n2
    
print(num_max(3,2))