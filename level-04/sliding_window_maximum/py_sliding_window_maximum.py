def sliding_window_maximum(nums: list[int], k: int) -> list[int]:
	result = []
	if not nums or k <= 0:
		return []
	for init in range(len(nums) - k + 1):
		window = nums[init:init + k]
		result.append(max(window))
	return result


if __name__ == "__main__":
	print("Result:", sliding_window_maximum([1, 3, -1, -3, 5, 3, 6, 7], 3), "| Expected:", [3, 3, 5, 5, 6, 7])
	print("Result:", sliding_window_maximum([1, 2, 3, 4, 5], 2), "| Expected:", [2, 3, 4, 5])
	print("Result:", sliding_window_maximum([5, 4, 3, 2, 1], 1), "| Expected:", [5, 4, 3, 2, 1])
	print("Result:", sliding_window_maximum([1, 2, 3], 3), "| Expected:", [3])
	print("Result:", sliding_window_maximum([1, 2, 3], 4), "| Expected:", [])
	print("Result:", sliding_window_maximum([], 2), "| Expected:", [])
	print("Result:", sliding_window_maximum([1, 2, 3], 0), "| Expected:", [])
