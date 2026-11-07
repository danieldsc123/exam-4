def merge_sorted_lists(lists: list[list[int]]) -> list[int]:
	result = []
	for num in lists:
		result.extend(num)
	return sorted(result)

if __name__ == "__main__":
	print("Result:", merge_sorted_lists([[1, 3, 5], [2, 4, 6]]), "| Expected:", [1, 2, 3, 4, 5, 6])
	print("Result:", merge_sorted_lists([[1, 5, 9], [2, 3, 8], [4, 6, 7]]), "| Expected:", [1, 2, 3, 4, 5, 6, 7, 8, 9])
	print("Result:", merge_sorted_lists([[5], [1, 3], [2, 4]]), "| Expected:", [1, 2, 3, 4, 5])
	print("Result:", merge_sorted_lists([[1, 1, 2], [2, 3, 3]]), "| Expected:", [1, 1, 2, 2, 3, 3])
	print("Result:", merge_sorted_lists([[], [1, 2, 3]]), "| Expected:", [1, 2, 3])
	print("Result:", merge_sorted_lists([[]]), "| Expected:", [])
	print("Result:", merge_sorted_lists([[-5, -1, 0], [-3, 2, 4]]), "| Expected:", [-5, -3, -1, 0, 2, 4])
	print("Result:", merge_sorted_lists([[10], [10], [10]]), "| Expected:", [10, 10, 10])
