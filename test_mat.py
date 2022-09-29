import mat_ops as mat

def test_equal():
	a = [[1,2], [3,4]]
	b = [[1,2], [3,4]]
	assert mat.equal(a, b)

def test_add():
	a = [[1,1], [1,1]]
	b = [[1,1], [1,1]]
	c = [[2,2], [2,2]]
	assert mat.equal( mat.add(a, b), c )

def test_sub():
	a = [[5,4], [3,2]]
	b = [[1,1], [1,1]]
	c = [[4,3], [2,1]]
	assert mat.equal( mat.sub(a, b), c )

