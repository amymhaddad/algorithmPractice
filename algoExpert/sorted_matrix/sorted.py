"""
https://www.algoexpert.io/questions/Search%20In%20Sorted%20Matrix
"""




def searchInSortedMatrix(matrix, target):
	return row_array(matrix, target)

def row_array(matrix, target):
	row_bounds = []

	for rows in matrix:
		if target < rows[0]:
			break
		row_bounds.append([rows[0], rows[-1]])
	return valid_rows(row_bounds, target, matrix)

def valid_rows(row_bounds, target, matrix):
	row_vals = []

	for i, row in enumerate(row_bounds):
		lower, upper = row[0], row[1]
		if target >= lower and target <= upper:
			row_vals.append(i)
	return row_index(row_vals, target, matrix)


def row_index(row_vals, target, matrix):
	valid_row = None

	if len(row_vals) == 1:
		row = row_vals[0]
		if target in matrix[row]:
			return find_target(matrix[row], row, target)
		return [-1, -1]
	
	else:	
		for i in range (len(row_vals)):	
			if target in matrix[i]:
				valid_row = i 
				break 
	
	if isinstance(valid_row, int):
		return find_target(matrix[i], valid_row, target)
	
	return [-1, -1]

	
def find_target(row, row_index, target):
	low = 0
	high = len(row) -1

	while low <= high:
		mid = (low + high) // 2
		if row[mid] == target:
			return [row_index, mid]
		elif row[mid] < target:
			low = mid + 1
		else:
			high = mid - 1

	return [-1, -1]



matrix = [
  [1, 4, 7, 12, 15, 1000],
  [2, 5, 19, 31, 32, 1001],
  [3, 8, 24, 33, 35, 1002],
  [40, 41, 42, 44, 45, 1003],
  [99, 100, 103, 106, 128, 1004]
]
target = 1004

print(searchInSortedMatrix(matrix, target))
