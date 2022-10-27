import mat.ops as mat

def log_function_call(func):
	"""Получает функцию и возвращаёт обёртку, при вызове которой будут напечатаны аргументы и результат выполнения функции"""

	def wrapper(*args, **kwargs):
		print(func.__name__, args)
		result = func(*args, **kwargs)
		print("->", result)
		return result
		
	return wrapper

def solve(a, b, log=False):
	"""
	Решить систему линейных уравнений
	Требует квадратную матрицу A
	"""
	
	if log:
		l_rowswap = log_function_call(mat.rowswap)
		l_rowk = log_function_call(mat.rowk)
		l_rowkadd = log_function_call(mat.rowkadd)
	else:
		l_rowswap = mat.rowswap
		l_rowk = mat.rowk
		l_rowkadd = mat.rowkadd

	c = mat.cat(a, b)
	vsz = len(c)

	for i in range(vsz):
		elem = c[i][i]
		
		# Проверить, не попался ли нам ноль на главной диагонали
		# Если попался, то текущую строку нужно отправить куда-нибудь ниже
		if elem == 0:
			l_rowswap(c, i, i + 1, do_copy=False)
			elem = c[i][i]
		
		assert elem != 0
		
		# Привести элемент на главной диагонали к единице
		l_rowk(c, i, 1/elem, do_copy=False)
		
		# Привести все элементы выше и ниже к нулям
		for j in range(vsz):
			if j == i:
				continue
			
			if c[j][i] != 0.0:
				l_rowkadd(c, j, i, -c[j][i], do_copy=False)
				
	return mat.col(c, vsz)

def inv_solve(a, b):
	return mat.transpose( mat.mul( mat.inverse(a), b ) )[0]
