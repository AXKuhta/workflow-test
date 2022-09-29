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

def test_kmul():
	a = [[1,0], [0,1]]
	k = 5
	c = [[5,0], [0,5]]
	assert mat.equal( mat.kmul(a, k), c )
	
def test_transpose():
	a = [[1,2], [3,4]]
	t = [[1,3], [2,4]]
	
	a2 = [[1,2], [3,4], [5,6]]
	t2 = [[1,3,5], [2,4,6]]
	
	a3 = [[9,8,7], [6,5,4]]
	t3 = [[9,6], [8,5], [7,4]]
	
	assert mat.equal( mat.transpose(a), t )
	assert mat.equal( mat.transpose(a2), t2 )
	assert mat.equal( mat.transpose(a3), t3 )

