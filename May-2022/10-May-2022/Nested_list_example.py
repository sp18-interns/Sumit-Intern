import  string
matrix = []

for i in range(7):

	# Append an empty sublist inside the list
	matrix.append([])

	for j in range(5):
		matrix[i].append(j)

print(matrix)

matrix = [[j for j in (string.ascii_lowercase)] for i in range(1)]

for i in range(0,26):
	print(chr(i+65))
	print(chr(i + 97))

print(matrix)