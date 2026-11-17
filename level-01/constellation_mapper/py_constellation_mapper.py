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
