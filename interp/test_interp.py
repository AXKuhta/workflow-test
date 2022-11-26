import interp.ops as interp

def test_lerp2d():
	model = interp.linear( [[0,0], [1,5]] )

	assert model(0.5) == 2.5
	assert model(-0.5) == -2.5

def test_linear():
	points = [
		[1, 2],
		[3, 4],
		[3.5, 3],
		[6, 7]
	]

	model = interp.linear(points)
	
	assert model(-1.5) == -0.5
	assert model(8.5) == 11.0
	assert model(3.0) == 4.0

def test_lagrange():
	points = [
		[1, 2],
		[3, 4],
		[3.5, 3],
		[6, 7]
	]
	
	assert interp.lagrange(points, 1) == 2
	assert interp.lagrange(points, 3) == 4
	assert interp.lagrange(points, 3.5) == 3
	assert interp.lagrange(points, 6) == 7

