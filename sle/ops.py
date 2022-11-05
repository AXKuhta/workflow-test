import mat.ops as mat

def log_function_call(func):
	"""
	Получает функцию и возвращает обёртку, при вызове которой будут напечатаны аргументы и результат выполнения функции
	"""

	def wrapper(*args, **kwargs):
		print(func.__name__, args)
		result = func(*args, **kwargs)
		print("->", result)
		return result
		
	return wrapper

def solve(a, b, log=False):
	"""
	Решить систему линейных уравнений методом Жордана-Гаусса
	Требует квадратную матрицу A и вектор-строку B
	Всегда возвращает новый вектор-строку
	"""

	c = mat.cat( a, mat.transpose( [b] ) )
	vsz = len(c)
	
	mat.gj_solve(c, log_function_call if log else lambda x: x)

	return mat.col(c, vsz)

def inv_solve(a, b):
	"""
	Решить систему линейных уравнений, используя обратную матрицу
	Этот метод менее эффективен, чем просто solve()
	Требует квадратную матрицу A и вектор-строку B
	Всегда возвращает новый вектор-строку
	"""

	return mat.transpose( mat.mul( mat.inverse(a), mat.transpose( [b] ) ) )[0]
