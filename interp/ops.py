import sle.ops as sle
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

def multilerp2d(points, x):
	"""
	Кусочно-линейная интерполяция
	Принимает массив из точек
	Вторым аргументом является x, для которого нужно интерполировать значение y
	"""
	
	vsz = len(points)
	
	# X = матрица, где первый столбец заполнен значением x
	# D = матрица с расстоянием от всех точек до требуемого x
	# S = матрица D, отсортированная по уменьшению абсолютного расстояния
	# R = матрица с координатами начальных точек, отсортированная по уменьшению абсолютного расстояния
	X = [[x, 0]]*vsz
	D = mat.sub(points, X)
	S = sorted(D, key=lambda x: abs(x[0]))
	R = mat.add(S, X)
	
	return lerp2d(R[0], R[1], x)
	
	
