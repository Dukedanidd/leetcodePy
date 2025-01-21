"""
    Escribe un programa que imprima los números del 1 al 100, pero:

        Si es divisible por 3, imprime "Fizz".
        Si es divisible por 5, imprime "Buzz".
        Si es divisible por ambos, imprime "FizzBuzz".
"""
for num in range(1, 101):
    if num % 3 == 0  and num % 5 == 0:
        print('FizzBuzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print(num)