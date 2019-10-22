"""
	Manejo de colecciones y tuplas
	@royerjmasache
"""
courseA = [(19, 10, 20), (1, 2, 10), (20, 10, 9), (1, 4, 9)]
names = ["Luis", "Ángel", "José", "Ana"]
# Obtención del promedio de cada tupla
average = list(map(lambda a: sum(a) / len(a), courseA))
# Sumatoria de cada una de las tuplas
tgrade = list(map(lambda a: sum(a), courseA))
# Uso de .zip para poder unir las listas
result = list(zip(average, tgrade, names))
# Presentación de resultados en forma de lista
print(list(filter(lambda a: a[0] <= 5, result)))
