import series.ops as series
import vec.ops as vec

def test_approx_exp():
	exp = series.init_approx_exp(20)
	
	assert vec.value_close(exp(1), 2.71828182)

