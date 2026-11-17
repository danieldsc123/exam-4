def list_intersection_finder(lists: list[list[int]]) -> list[int]:
	if not lists or any(not lst for lst in lists):
		return []

	result = set(lists[0])

	for nums in lists[1:]:
		result = result.intersection(nums)

	return sorted(result)
