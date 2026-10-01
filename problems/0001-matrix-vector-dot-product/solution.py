import numpy as np
def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	A = np.array(a)
	v = np.array(b)

	if A.ndim != 2 or v.ndim != 1 or A.shape[1] != v.shape[0]:
		return -1
	return (A @ v).tolist()