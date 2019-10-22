"""
	Manejo de colecciones y listas
"""
listA  = [(100, 2), (20, 4), (30, 1)]
listB = ["b", "a", "c"] 
# Uso de .zip, .sorted y reverse para unir, ordenar e invertir las listas
print(list(sorted(listA), sorted(listB, reverse = True))