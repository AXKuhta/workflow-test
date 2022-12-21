import vec.ops as vec
import math

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

def init_approx_series(n, fx_at_zero, dfx_at_zero):
	"""
	Получить функцию для примерного вычисления при помощи ряда Маклорена

	``n`` - количество членов в ряде
	``fx_at_zero`` - значение функции в точке ноль
	``dfx_at_zero`` - значение производных функции в точке ноль
	"""

	dfx_series = (dfx_at_zero*(1 + n // len(dfx_at_zero)))[:n]

	k = [a*b for a, b in zip( vec.invert(fact_arr(n)) , dfx_series)]

	return lambda x: fx_at_zero + vec.dot(k, pow_arr(x, n))

def init_approx_exp(n):
	"""
	Получить функцию для вычисления exp(x) при помощи ряда Маклорена
	"""

	return init_approx_series(n, 1, [1])

def init_approx_sin(n):
	"""
	Получить функцию для вычисления sin(x) при помощи ряда Маклорена
	"""

	return init_approx_series(n, 0, [1, 0, -1, 0])

def init_approx_cos(n):
	"""
	Получить функцию для вычисления cos(x) при помощи ряда Маклорена
	"""

	return init_approx_series(n, 1, [0, -1, 0, 1])

def init_approx_arcsin(n):
	"""
	Получить функцию для вычисления arcsin(x) при помощи ряда Маклорена

	Предупреждение: производная arcsin(x) в точке 0 не является периодичной; не используйте n > 10 или x > 0.5
	"""

	return init_approx_series(n, 0, [1, 0, 1, 0, 9, 0, 225, 0, 11025, 0])

def init_approx_arccos(n):
	"""
	Получить функцию для вычисления arccos(x) при помощи ряда Маклорена

	Предупреждение: производная arccos(x) в точке 0 не является периодичной; не используйте n > 10 или x > 0.5
	"""

	return init_approx_series(n, math.pi/2, [-1, 0, -1, 0, -9, 0, -225, 0, -11025, 0])