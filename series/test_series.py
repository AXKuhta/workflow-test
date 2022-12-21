import series.ops as series
import vec.ops as vec
import math

def test_approx_exp():
	exp = series.init_approx_exp(20)
	
	assert vec.value_close(exp(1), 2.71828182)

def test_approx_sin():
	sin = series.init_approx_sin(20)

	assert vec.value_close(sin(0.0), 0.0)
	assert vec.value_close(sin(math.pi/2.0), 1.0)
	assert vec.value_close(sin(1.0), math.sin(1.0))

def test_approx_cos():
	cos = series.init_approx_cos(20)

	assert vec.value_close(cos(0.0), 1.0)
	assert vec.value_close(cos(math.pi/2.0), 0.0)
	assert vec.value_close(cos(1.0), math.cos(1.0))

def test_approx_arcsin():
	arcsin = series.init_approx_arcsin(10)

	assert vec.value_close(arcsin(0.0), 0.0)
	assert vec.value_close(arcsin(0.5), math.asin(0.5))

def test_approx_arccos():
	arccos = series.init_approx_arccos(10)

	assert vec.value_close(arccos(0), math.pi/2)
	assert vec.value_close(arccos(0.5), math.acos(0.5))
