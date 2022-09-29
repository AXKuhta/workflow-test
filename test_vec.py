import vec_ops as vec
	
def test_close():
	assert vec.close( [5, 0.00005, 1], [5, 0.00006, 1], 0.0001 )

def test_add():
	assert vec.add( [1,2,3], [4,5,6] ) == [5,7,9]

def test_sub():
	assert vec.sub( [1,1,1], [1,1,1] ) == [0,0,0]

def test_mul():
	assert vec.mul( [1,2,3], 3 ) == [3,6,9]
	
def test_div():
	assert vec.div( [4,6,8], 2 ) == [2,3,4]

def test_dot():
	assert vec.dot( [2,3,4], [5,6,7] ) == 2*5 + 3*6 + 4*7

def test_mag():
	assert vec.mag( [2,3,-50] ) == (2*2 + 3*3 + -50*-50)**0.5

def test_cos():
	assert vec.value_close(vec.cos( [1,1], [-1,-1] ), -1.0) == True

def test_deg():
	assert vec.value_close(vec.deg( [1,1], [-1,-1] ), 180.0) == True

def test_not_opposing():
	assert vec.not_opposing( [1, 1], [100,100] ) == True
	assert vec.not_opposing( [1, 1], [100,-100] ) == False
	
def test_opposing():
	assert vec.opposing( [1, 1], [-100,-100] ) == True
	assert vec.opposing( [1, 1], [100,-100] ) == False
	
def test_collinear():
	assert vec.collinear( [1, 1], [-100,-100] ) == True
	assert vec.collinear( [1, 1], [100,100] ) == True
	assert vec.opposing( [1, 1], [100,-100] ) == False
	
def test_orthogonal():
	assert vec.orthogonal( [1, 1], [100,-100] ) == True
	assert vec.orthogonal( [1, 1], [-100,-100] ) == False
	assert vec.orthogonal( [1, 1], [100,100] ) == False

def test_invert():
	assert vec.invert( [1,-1] ) == [-1,1]

def test_norm():
	assert vec.norm( [1, 5, 10] ) == [0.1/(1.26**0.5), 0.5/(1.26**0.5), 1.0/(1.26**0.5)]

def test_project():
	assert vec.project([1,1], [0,-1]) == [-0.5, -0.5]

def test_sproject():
	assert vec.sproject([1,1], [0,-1]) == 0.5**0.5

