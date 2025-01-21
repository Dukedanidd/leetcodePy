"""
    Quieres contar cuántas vocales hay en una cadena:

        Lee la cadena.
        Recorre cada letra.
        Verifica si es una vocal.
        Lleva la cuenta de las vocales.
"""

def contar_vocales(cadena):
    vocales = 'aeiouAEIOU'
    cuenta = 0
    for letra in cadena:
        if letra in vocales:
            cuenta += 1
    return cuenta

print(contar_vocales('Hola Mundo'))
        