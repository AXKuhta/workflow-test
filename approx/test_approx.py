import approx.ops as approx
import vec.ops as vec

points = [
	[1, 2],
	[3, 4],
	[3.5, 3],
	[6, 7]
]

def test_linear_approx():
	linear_model = approx.model(points, approx.linear)
	
	for x, y in points:
		assert vec.value_close( linear_model(x), y, eps=1.5 )

def test_polyn2_approx():
	polyn2_model = approx.model(points, approx.polynomial_2)
	
	for x, y in points:
		assert vec.value_close( polyn2_model(x), y, eps=0.75 )

def test_polyn3_approx():
	polyn3_model = approx.model(points, approx.polynomial_3)
	
	for x, y in points:
		assert vec.value_close( polyn3_model(x), y )

def test_cos3_approx():
	cos3_model = approx.model(points, approx.cos3)
	
	for x, y in points:
		assert vec.value_close( cos3_model(x), y )

points_xy = [
	[0, 0, 1],
	[1, 0, 0],
	[0, 1, 0],
	[1, 1, 1]
]

def test_xy_approx():
	cos3_model = approx.model(points_xy, approx.dct_xy)
	
	for x, y, z in points_xy:
		assert vec.value_close( cos3_model(x, y), z )
