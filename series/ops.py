import vec.ops as vec

def fact_arr(n):
	"""
	Получить массив с факториалами от 1! до n!
	"""
	
	arr = []
	val = 1
	
	for i in range(n):
		val = val * (i + 1)
		arr.append(val)

	return arr
	
def pow_arr(x, n):
	"""
	Получить массив со степенями от x^1 до x^n
	"""
	
	return [x**i for i in range(1, n+1)]

exp_derivatives_at_zero = [1]
sin_derivatives_at_zero = [0, 1, 0, -1]
arcsin_derivatives_at_zero = [1, 0]
cos_derivatives_at_zero = [0, -1, 0, 1]
arccos_derivatives_at_zero = [-1, 0]

exp_at_zero = 1
sin_at_zero = 0
cos_at_zero = 1
arcsin_at_zero = 0
arccos_at_zero = 3.14/2

def init_approx_exp(n):
	"""
	Получить функцию для вычисления exp(x) при помощи ряда Маклорена
	"""

	return init_approx_series(n, exp_at_zero, exp_derivatives_at_zero)
	

def init_approx_series(n, fx_at_zero, dfx_at_zero):
	dfx_series = (dfx_at_zero*(1 + n // len(dfx_at_zero)))[:n]

	k = [a*b for a, b in zip( vec.invert(fact_arr(n)) , dfx_series)]

	return lambda x: fx_at_zero + vec.dot(k, pow_arr(x, n))

