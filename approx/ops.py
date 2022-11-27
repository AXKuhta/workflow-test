import vec.ops as vec
import mat.ops as mat
import sle.ops as sle
from math import cos

# Различные методы
linear = 		[ lambda x: x, lambda x: 1 ]
polynomial_2 = 	[ lambda x: x*x, lambda x: x, lambda x: 1 ]
polynomial_3 = 	[ lambda x: x*x*x, lambda x: x*x, lambda x: x, lambda x: 1 ]
cos3 = 			[ lambda x: cos(3*x), lambda x: cos(2*x), lambda x: cos(x), lambda x: 1 ]
dct_xy = 		[ lambda x, y: cos(x)*cos(y), lambda x, y: cos(x), lambda x, y: cos(y), lambda x, y: 1 ]

class model():
	"""
	Модель для аппроксимации
	"""

	def __init__(self, points, method):
		"""
		Создать модель для аппроксимации

		Аргументы:
		points: массив с точками
		method: массив с функциями уравнения
		"""

		args = [v[:-1] for v in points]
		vals = [v[-1:] for v in points]
		b = vals
		
		# Из-за того что здесь матрицы упорядочены по строкам, проще найти сразу транспонированную A
		A_t = []

		for fn in method:
			A_t.append([fn(*v) for v in args])

		A = mat.transpose(A_t)
		A_x = mat.mul(A_t, A)
		b_x = mat.mul(A_t, b)

		term_k = sle.solve(A_x, mat.transpose(b_x)[0] )

		self.k = term_k
		self.fn = method


	def __call__(self, *args):
		"""
		Вычислить значение f для указанного x или x, y или x, y, z 
		"""

		return vec.dot(self.k, [fn(*args) for fn in self.fn])
