import mat.mat_ops as mat
import vec.vec_ops as vec

def test_copy():
	a = [[1,1], [1,1]]
	b = mat.copy(a)

	b[0] += [1]
	b[1] += [1]

	assert a == [[1,1], [1,1]]

def test_add():
	a = [[1,1], [1,1]]
	b = [[1,1], [1,1]]

	assert mat.add(a, b) == [[2,2], [2,2]]

def test_sub():
	a = [[5,4], [3,2]]
	b = [[1,1], [1,1]]

	assert mat.sub(a, b) == [[4,3], [2,1]]

def test_kmul():
	a = [[1,0], [0,1]]
	k = 5

	assert mat.kmul(a, k) == [[5,0], [0,5]]
	
def test_transpose():
	a1 = [[1,2], [3,4]]
	a2 = [[1,2], [3,4], [5,6]]
	a3 = [[9,8,7], [6,5,4]]
	
	assert mat.transpose(a1) == [[1,3], [2,4]]
	assert mat.transpose(a2) == [[1,3,5], [2,4,6]]
	assert mat.transpose(a3) == [[9,6], [8,5], [7,4]]

def test_mul():
	a = [[1,0], [0,1]]
	b = [[3], [7]]

	assert mat.mul(a, b) == [[3],[7]]

def test_row():
	a = [[1,2], [3,4]]

	assert mat.row(a, 0) == [1,2]

def test_col():
	a = [[1,2], [3,4]]

	assert mat.col(a, 0) == [1,3]

def test_rowswap():
	a = [[1,2], [3,4]]

	assert mat.rowswap(a, 0, 1) == [[3,4], [1,2]]

def test_rowk():
	a = [[1,0], [0,1]]
	k = 5

	assert mat.rowk(a, 0, k) == [[5,0], [0,1]]

def test_rowkadd():
	a = [[1,0], [0,1]]
	k = -5

	assert mat.rowkadd(a, 0, 1, k) == [[1,-5], [0,1]]
	
def test_cat():
	a = [[1, 2], [3, 4]]
	b = [[5], [6]]
	
	assert mat.cat(a, b) == [[1, 2, 5], [3, 4, 6]]

def test_identity():
	a = mat.identity(4)
	b = [[1,0,0,0], [0,1,0,0], [0,0,1,0], [0,0,0,1]]

	assert a == b

def test_inverse():
	a = [[0.6996, 0.6475, 0.4556, 0.7469],
		 [0.8762, 0.1583, 0.4804, 0.2811],
		 [0.6259, 0.5043, 0.0467, 0.2307],
		 [0.3482, 0.4055, 0.1531, 0.4739]]

	r = [[-3.2523,  1.8306,  0.5797,  3.7577],
		 [ 5.4488, -2.8294,  2.3508, -8.0534],
		 [ 6.7410, -1.1770, -0.5004, -9.6825],
		 [-4.4507,  1.4562, -2.2756,  9.3683]]

	assert mat.close(mat.inverse(a), r)

def test_solve_n2():
	a = [[2, 3], [4, 3]]
	b = [[2], [7]]

	assert mat.solve(a, b) == [2.5, -1.0]
	assert a == [[2, 3], [4, 3]]

def test_solve_n3():
	a = [[-1, 2, 6], [3, -6, 0], [1, 0, 6]]
	b = [[15], [-9], [5]]

	assert mat.solve(a, b) == [-7, -2, 2]
	assert a == [[-1, 2, 6], [3, -6, 0], [1, 0, 6]]

def test_solve_n4():
	a = [[1, 2, 3, -2], [2, -1, -2, -3], [3, 2, -1, 2], [2, -3, 2, 1]]
	b = [[1], [2], [-5], [11]]

	assert vec.close(mat.solve(a, b), [2/3, -43/18, 13/9, -7/18])
	assert a == [[1, 2, 3, -2], [2, -1, -2, -3], [3, 2, -1, 2], [2, -3, 2, 1]]

