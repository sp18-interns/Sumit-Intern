matrix = []

for i in range(7):

	# Append an empty sublist inside the list
	matrix.append([])

	for j in range(5):
		matrix[i].append(j)

print(matrix)

matrix = [[j for j in ('a', 'd')] for i in range(4)]

print(matrix)