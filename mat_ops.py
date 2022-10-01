import vec_ops as vec

# Проверка совпадения размерности матриц
def dimensions_must_match(a, b):
	if len(a) != len(b):
		raise Exception("Row count doesn't match")
		
	if type(a[0]) != type([]):
		raise Exception("A is a vector")
		
	if type(b[0]) != type([]):
		raise Exception("B is a vector")
		
	for i in range( len(a) ):
		if len(a[i]) != len(b[i]):
			raise Exception("Row length doesn't match")

# Проверка наличия в матрице строки с указанным индексом
def index_must_exist(a, i):
	if i > len(a) - 1:
		raise Exception("Index out of range")

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

# Умножение матрицы на скаляр
def kmul(a, k, do_copy=True):
	if do_copy:
		a = [] + a

	for i in range( len(a) ):
		a[i] = vec.mul(a[i], k, do_copy)
	
	return a

# Транспонирование матрицы
# Всегда создаёт новую копию, поскольку может изменится размерность
def transpose(a):
	b = []

	for i in range( len(a) ):
		for j in range( len(a[i]) ):
			if len(b) <= j:
				b.append([])
				
			b[j].append(a[i][j])

	return b

# Умножение матрицы на матрицу
def mul(a, b):
	t = transpose(b)
	mat = []

	for i in range( len(a) ):
		row = []

		for j in range( len(t) ):
			row.append( vec.dot(a[i], t[j]) )

		mat.append(row)

	return mat

# Извлечение строки
def row(a, i):
	index_must_exist(a, i)

	return a[i]

# Извлечение столбца
def col(a, i):
	t = transpose(a)

	index_must_exist(t, i)

	return t[i]

# Перестановка строк
def rowswap(a, i, j, do_copy=True):
	index_must_exist(a, i)
	index_must_exist(a, j)

	if do_copy:
		a = [] + a

	t = a[i]
	a[i] = a[j]
	a[j] = t

	return a

# Умножение строки на скаляр
# a[i] = k*a[i]
def rowk(a, i, k, do_copy=True):
	index_must_exist(a, i)

	if do_copy:
		a = [] + a

	a[i] = vec.mul(a[i], k, do_copy)

	return a

# Добавляет к строке i строку j, умноженную на скаляр
# a[i] = a[i] + k*a[j]
def rowkadd(a, i, j, k, do_copy=True):
	index_must_exist(a, i)
	index_must_exist(a, j)

	if do_copy:
		a = [] + a

	krow = vec.mul(a[j], k, do_copy)
	a[i] = vec.add(a[i], krow, do_copy)

	return a
