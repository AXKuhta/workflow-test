import sle.ops as sle
import vec.ops as vec
import mat.ops as mat

def lerp2d(p1, p2, x):
	"""
	Линейная интерполяция
	Получает координаты двух точек в формате [x, y]
	Третьим агрументом является x, для которого нужно интерполировать значение y
	"""
	
	a = [ [ p1[0], 1 ], [ p2[0], 1 ] ]
	b = [ p1[1], p2[1] ]
	
	k = sle.solve(a, b)
	
	return k[0]*x + k[1]

def linear(points, x):
	"""
	Кусочно-линейная интерполяция
	Принимает массив из точек
	Вторым аргументом является x, для которого нужно интерполировать значение y
	"""
	
	vsz = len(points)
	
	assert(vsz > 1)
	
	# На всякий случай отсортировать точки по x
	S = sorted(mat.copy(points), key=lambda x: x[0])
	
	point_a = points[0]
	point_b = points[1]
	
	for i in range(1, vsz - 1):
		if (x >= points[i][0]):
			point_a = points[i]
			point_b = points[i + 1]
	
	return lerp2d(point_a, point_b, x)
	
	
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
	
