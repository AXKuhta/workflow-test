import vec_ops as vec

def dimensions_must_match(a, b):
	"""Проверка совпадения размерности матриц"""

	if len(a) != len(b):
		raise ValueError("Row count doesn't match")
		
	if type(a[0]) != type([]):
		raise TypeError("A is a vector")
		
	if type(b[0]) != type([]):
		raise TypeError("B is a vector")
		
	for i in range( len(a) ):
		if len(a[i]) != len(b[i]):
			raise ValueError("Row length doesn't match")

def index_must_exist(a, i):
	"""Проверка наличия в матрице строки с указанным индексом"""

	if i > len(a) - 1:
		raise ValueError("Index out of range")

def add(a, b, do_copy=True):
	dimensions_must_match(a, b)

	if do_copy:
		a = [] + a

	for i in range( len(a) ):
		a[i] = vec.add(a[i], b[i], do_copy)
	
	return a
	
def sub(a, b, do_copy=True):
	dimensions_must_match(a, b)

	if do_copy:
		a = [] + a

	for i in range( len(a) ):
		a[i] = vec.sub(a[i], b[i], do_copy)
	
	return a

def kmul(a, k, do_copy=True):
	"""Умножение матрицы на скаляр"""

	if do_copy:
		a = [] + a

	for i in range( len(a) ):
		a[i] = vec.mul(a[i], k, do_copy)
	
	return a

def transpose(a):
	"""
	Транспонирование матрицы
	Всегда создаёт новую копию, поскольку может изменится размерность
	"""

	b = []

	for i in range( len(a) ):
		for j in range( len(a[i]) ):
			if len(b) <= j:
				b.append([])
				
			b[j].append(a[i][j])

	return b

def mul(a, b):
	"""Умножение матрицы на матрицу"""

	t = transpose(b)
	mat = []

	for i in range( len(a) ):
		row = []

		for j in range( len(t) ):
			row.append( vec.dot(a[i], t[j]) )

		mat.append(row)

	return mat

def row(a, i):
	"""Извлечение строки"""

	index_must_exist(a, i)

	return a[i]

def col(a, i):
	"""Извлечение столбца"""

	t = transpose(a)

	index_must_exist(t, i)

	return t[i]

def rowswap(a, i, j, do_copy=True):
	"""Перестановка строк"""

	index_must_exist(a, i)
	index_must_exist(a, j)

	if do_copy:
		a = [] + a

	t = a[i]
	a[i] = a[j]
	a[j] = t

	return a

def rowk(a, i, k, do_copy=True):
	"""
	Умножение строки на скаляр
	a[i] = k*a[i]
	"""

	index_must_exist(a, i)

	if do_copy:
		a = [] + a

	a[i] = vec.mul(a[i], k, do_copy)

	return a

def rowkadd(a, i, j, k, do_copy=True):
	"""
	Добавляет к строке i строку j, умноженную на скаляр
	a[i] = a[i] + k*a[j]
	"""

	index_must_exist(a, i)
	index_must_exist(a, j)

	if do_copy:
		a = [] + a

	krow = vec.mul(a[j], k, do_copy)
	a[i] = vec.add(a[i], krow, do_copy)

	return a
