"""
	Manejo de colecciones y tuplas
	@royerjmasache
"""
listA = [10. 2, 3, 4]
listB = ["a", "b", "c", "d"]
# Ordenado de listA
first = sorted(listA)
# Ordenado de listB de forma inversa 
second = sorted(listB, reverse = True)
# Adjuntado de  listas
attach =  zip(first, second)
# Presentación de resultados
print(list(attach))