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
	
	# Расстояние x до всех других точек
	dsts = mat.sub(mat.cat(points, points), [[x, 0, 0, 0]]*vsz)
	sdts = sorted(dsts, key=lambda x: abs(x[0]))
	
	return lerp2d(sdts[0][2:], sdts[1][2:], x)
	
	
