import vec.ops as vec
import sle.ops as sle

def test_solve_n2():
	a = [[2, 3], [4, 3]]
	b = [[2], [7]]

	assert sle.solve(a, b) == [2.5, -1.0]
	assert a == [[2, 3], [4, 3]]

def test_solve_n3():
	a = [[-1, 2, 6], [3, -6, 0], [1, 0, 6]]
	b = [[15], [-9], [5]]

	assert sle.solve(a, b) == [-7, -2, 2]
	assert a == [[-1, 2, 6], [3, -6, 0], [1, 0, 6]]

def test_solve_n4():
	a = [[1, 2, 3, -2], [2, -1, -2, -3], [3, 2, -1, 2], [2, -3, 2, 1]]
	b = [[1], [2], [-5], [11]]

	assert vec.close(sle.solve(a, b), [2/3, -43/18, 13/9, -7/18])
	assert a == [[1, 2, 3, -2], [2, -1, -2, -3], [3, 2, -1, 2], [2, -3, 2, 1]]

def test_inv_solve_n2():
	a = [[2, 3], [4, 3]]
	b = [[2], [7]]

	assert vec.close(sle.inv_solve(a, b), [2.5, -1.0])
	assert a == [[2, 3], [4, 3]]
