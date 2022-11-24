import interp.ops as interp

def test_lerp2d():
	assert interp.lerp2d( [0,0], [1,5], 0.5 ) == 2.5
	assert interp.lerp2d( [0,0], [1,5], -0.5 ) == -2.5

def test_linear():
	points = [
		[1, 2],
		[3, 4],
		[3.5, 3],
		[6, 7]
	]
	
	assert interp.linear(points, -1.5) == -0.5
	assert interp.linear(points, 8.5) == 11.0
	assert interp.linear(points, 3.0) == 4.0

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

