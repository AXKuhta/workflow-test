import vec.ops as vec
import mat.ops as mat
import sle.ops as sle
from math import cos

# Различные методы
linear = 	lambda x: [x, 1]
polynomial_2 = 	lambda x: [x*x, x, 1]
polynomial_3 = 	lambda x: [x*x*x, x*x, x, 1]
cos3 = 		lambda x: [cos(3*x), cos(2*x), cos(x), 1]
cos_xy = 	lambda x, y: [cos(x)*cos(y), cos(x), cos(y), 1]

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
		
		A = [method(*v) for v in args]

		A_t = mat.transpose(A)
		A_x = mat.mul(A_t, A)
		b_x = mat.mul(A_t, b)

		term_k = sle.solve(A_x, mat.transpose(b_x)[0] )

		self.k = term_k
		self.fn = method


	def __call__(self, *args):
		"""
		Вычислить значение f для указанного x или x, y или x, y, z 
		"""

		return vec.dot(self.k, self.fn(*args))
