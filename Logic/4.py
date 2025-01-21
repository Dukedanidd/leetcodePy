"""
    Escribe un programa que imprima los números del 1 al 100, pero:

        Si es divisible por 3, imprime "Fizz".
        Si es divisible por 5, imprime "Buzz".
        Si es divisible por ambos, imprime "FizzBuzz".
"""

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)