def binary_search(array : List[int]) -> int:
	def condition(value) -> bool:
		"""loop exist condition"""
		pass

	left, right = min(search_space), max(search_space) # could be [0, n], [1, n] etc. Depends on problem
	while left < right: # 같아지면 의미가 없어진다. 끝난것
		mid = left + (right - left) //2
		if condition(mid):
			right = mid
		else:
			left = mid + 1
	return left