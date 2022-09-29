import mat_ops as mat
import vec_ops as vec

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
