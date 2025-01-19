"""
    Escribir una función sum() y una función multip() que sumen 
    y multipliquen respectivamente todos los números de una lista. 
    Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.
"""

def sum(lista):
    """La funcion espera una lista de numeros y lo que hara sera sumar cada uno de los numeros que existan

    Args:
        lista ([type]): [description]
    """
    result = 0
    for n in lista:
        result = result + (n)
        
    print(result)


sum([1,2,3])

def mult(lista):
    """La funcion espera una lista de numeros y lo que hara sera multiplicar cada uno de los numeros que existan

    Args:
        lista ([type]): [description]
    """
    result = lista[0]
    i = 1
    while i in range(1, len(lista)):
        result =  result * lista[i]
        i += 1
    print(result)

mult([2,2,2])
