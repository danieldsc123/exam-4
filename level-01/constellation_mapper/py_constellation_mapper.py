def constellation_mapper(stars: list[tuple[int, int]], dim: int) -> list[str]:
	dst: list[str] = []

	for line in range(dim):
		lines:str = ""

		for col in range(dim):
			if (line, col) in stars:
				lines += "*"

			else:
				lines += "."

		dst.append(lines)

	return dst



if __name__ == "__main__":
	print("Result:", constellation_mapper([(0, 0), (1, 1), (2, 2)], 3), "| Expected:", ['*..', '.*.', '..*'])
	print("Result:", constellation_mapper([(1, 1), (0, 1), (2, 1), (1, 0), (1, 2)], 3), "| Expected:", ['.*.', '***', '.*.'])
	print("Result:", constellation_mapper([], 2), "| Expected:", ['..', '..'])
	print("Result:", constellation_mapper([(0, 0), (0, 0), (1, 1)], 2), "| Expected:", ['*.', '.*'])
	print("Result:", constellation_mapper([(0, 0), (5, 5)], 3), "| Expected:", ['*..', '...', '...'])
	print("Result:", constellation_mapper([(1, 0), (1, 1), (1, 2)], 3), "| Expected:", ['...', '***', '...'])
