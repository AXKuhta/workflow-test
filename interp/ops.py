import sle.ops as sle
import vec.ops as vec
import mat.ops as mat

class linear_model():
	"""
	Модель для линейной интерполяции
	"""

	def __init__(self, points, line_k):
		"""
		[Внутренняя функция] создать модель для линейной интерполяции

		Аргументы:
		points: массив с точками
		line_k: массив с коэффициентами для уравнения прямой
		"""

		assert len(points) > 1
		assert len(points) == len(line_k) + 1

		self.num_points = len(points)
		self.points = points
		self.line_k = line_k

	def __call__(self, x):
		"""
		Вычислить значение y для указанного x
		"""

		# Найти наиболее подходящую пару точек
		best_i = 0

		for i in range(1, self.num_points - 1):
			if (x >= self.points[i][0]):
				best_i = i

		a = self.line_k[best_i][0]
		b = self.line_k[best_i][1]

		return a*x + b


def find_line_k(p1, p2):
	"""
	Найти коэффициенты для уравнения прямой, используя две точки
	"""
	
	a = [ [ p1[0], 1 ], [ p2[0], 1 ] ]
	b = [ p1[1], p2[1] ]
	
	k = sle.solve(a, b)
	
	return k

def linear(points):
	"""
	Создать модель для линейной интерполяции

	Аргументы:
	points: массив с точками

	Подходит как для простой линейной интерполяции (две точки), так и для кусочно-линейной интерполяции (>2 точек)
	"""
	
	vsz = len(points)
	
	assert(vsz > 1)
	
	# На всякий случай отсортировать точки по x
	S = sorted(mat.copy(points), key=lambda x: x[0])
	K = []
	
	for i in range(0, vsz - 1):
		K.append(find_line_k(S[i], S[i + 1]))
	
	return linear_model(S, K)
	
	
def lagrange(points, tgt_x):
	"""
	Интерполяция при помощи полинома Лагранжа
	Принимает массив из точек
	Вторым аргументом является x, для которого нужно интерполировать значение y
	"""

	vsz = len(points)
	
	# Вектор-строки с координатами точек по x и y
	x = mat.col(points, 0)
	y = mat.col(points, 1)
	
	# Базисные полиномы
	l = [1]*vsz
	
	for i in range(vsz):
		for j in range(vsz):
			if i == j:
				continue
			l[i] *= (tgt_x - x[j]) / (x[i] - x[j])
	
	return vec.dot(y, l)
	
