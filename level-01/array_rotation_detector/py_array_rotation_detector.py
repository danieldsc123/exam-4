def array_rotation_detector(arr1: list, arr2: list) -> bool:
	rotation = arr1.copy()

	if len(arr1) != len(arr2):
		return False
	
	if len(arr1) == 0 and len(arr2) == 0:
		return True
	
	for _ in range(len(arr1)):
		if rotation == arr2:
			return True
		
		rotation.append(rotation.pop(0))

	return False


if __name__ == "__main__":
	print("Result:", array_rotation_detector([1, 2, 3, 4, 5], [4, 5, 1, 2, 3]), "| Expected:", True)
	print("Result:", array_rotation_detector([1, 2, 3, 4, 5], [5, 1, 2, 3, 4]), "| Expected:", True)
	print("Result:", array_rotation_detector([1, 2, 3], [3, 2, 1]), "| Expected:", False)
	print("Result:", array_rotation_detector([1, 2], [1, 2, 3]), "| Expected:", False)
	print("Result:", array_rotation_detector([], []), "| Expected:", True)
