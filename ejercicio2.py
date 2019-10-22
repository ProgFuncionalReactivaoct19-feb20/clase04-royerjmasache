"""
	Manejo de colecciones y tuplas
	@royerjmasache
"""
listA = [(100, 2), (20, 4), (30, 1)]
listB = ["a", "b", "c"]
# Uso de .zip para adjuntar las listas, ordenamiento con .sorted y función anónima para seleccionar la posición
print(list(zip(sorted(listA), sorted(listB, key = lambda a: a[1]))))