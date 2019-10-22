"""
	Manejo de colecciones y tuplas
	@royerjmasache
"""
listA = [(100, 2), (20, 4), (30, 1)]
listB = ["a", "b", "c"]
# Transformación a mayúsculas
letter = map(lambda a: a.upper(), listB)
# Uso de .zip para adjuntar las listas, ordenamiento con .sorted y función anónima para seleccionar la posición
print(list(zip(sorted(listA), sorted(letter, reverse = True))))
