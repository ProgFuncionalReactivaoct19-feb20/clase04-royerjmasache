"""
	Manejo de colecciones y tuplas
	@royerjmasache
"""
courseA = [(19, 10, 20), (20, 20, 10), (20, 10, 9)]
names = ["Ángel", "José", "Ana"]
# Uso de map para iterar en las tuplas y funciones sum y len para calcular el promedio
average = list(map(lambda a: sum(a) / len(a), courseA))
# Uso de .zip para unir las tuplas
result = list(zip(average, names))
# Cálculo del valor máximo de la variable
grade = max(result, key = lambda a: a)
# Presentación de resultados en función del promedio y nombre
print(result)
# Presentación del valor máximo
print(grade)
#  Presentación de los resultados principales de forma inversa
print(list(sorted(result, key = lambda a: a[1])))

