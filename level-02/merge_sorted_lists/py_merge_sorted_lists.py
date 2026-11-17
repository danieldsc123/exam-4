def merge_sorted_lists(lists: list[list[int]]) -> list[int]:
	result = []

	for num in lists:
		result.extend(num)

	return sorted(result)
