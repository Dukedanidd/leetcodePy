# 6. Mayor Número de Palabras en una Oración
# Encuentra la cantidad máxima de palabras en una oración dentro de una lista.

def count_words(oracion):
    palabras = oracion.split()
    count = 0
    
    for i in palabras:
        count += 1
        
    print(count)
    
count_words('Hola mi gente')
count_words('Que pasa mi gente del tistos est dia venimos terminando el modelo de machine learning para la prediccion de eurusd')