import interp.ops as interp

def test_lerp2d():
	assert interp.lerp2d( [0,0], [1,5], 0.5 ) == 2.5
	assert interp.lerp2d( [0,0], [1,5], -0.5 ) == -2.5

def test_multilerp2d():
	points = [
		[1, 2],
		[3, 4],
		[3.5, 3],
		[6, 7]
	]
	
	assert interp.multilerp2d(points, -1.5) == -0.5
	assert interp.multilerp2d(points, 8.5) == 11.0
	assert interp.multilerp2d(points, 3.0) == 4.0


