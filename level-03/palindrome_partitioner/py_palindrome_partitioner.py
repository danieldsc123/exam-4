def palindrome_partitioner(s: str) -> int:
	count = 0
	reverse = s[::-1]

	if s == reverse:
		return 0

	small = len(s) - 1

	for position in range(1, len(s)):
		left = s[:position]
		right = s[position:]

		if left == left[::-1]:
			count = 1 + palindrome_partitioner(right)

			if count < small:
				small = count

	return small




if __name__ == "__main__":
	print("Result:", palindrome_partitioner("aab"), "| Expected:", 1)
	print("Result:", palindrome_partitioner("aba"), "| Expected:", 0)
	print("Result:", palindrome_partitioner("abc"), "| Expected:", 2)
