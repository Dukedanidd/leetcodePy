"""
    Escribir un programa que nos diga si un numero entero es par o impar
"""
def par_impar(num):
    if num % 2 == 0:
        return  'Par'
    else:
        return 'Impar' 

print(par_impar(10))