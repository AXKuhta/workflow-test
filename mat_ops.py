import vec_ops as vec

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
	if do_copy:
		a = [] + a

	for i in range( len(a) ):
		a[i] = vec.mul(a[i], k, do_copy)
	
	return a

# Всегда создаёт новую копию, поскольку может изменится размерность
def transpose(a):
	b = []

	for i in range( len(a) ):
		for j in range( len(a[i]) ):
			if len(b) <= j:
				b.append([])
				
			b[j].append(a[i][j])

	return b
	
def mul(a, b):
	t = transpose(b)
	mat = []

	for i in range( len(a) ):
		row = []

		for j in range( len(t) ):
			row.append( vec.dot(a[i], t[j]) )

		mat.append(row)

	return mat

def row(a, i):
	if i > len(a) - 1:
		raise Exception("Index out of range")

	return a[i]

def col(a, i):
	t = transpose(a)

	if i > len(t) - 1:
		raise Exception("Index out of range")

	return t[i]

def rowswap(a, i, j, do_copy=True):
	if do_copy:
		a = [] + a

	if i > len(a) - 1:
		raise Exception("Index out of range")

	if j > len(a) - 1:
		raise Exception("Index out of range")

	t = a[i]
	a[i] = a[j]
	a[j] = t

	return a

# a[i] = k*a[i]
def rowk(a, i, k, do_copy=True):
	if do_copy:
		a = [] + a

	if i > len(a) - 1:
		raise Exception("Index out of range")

	a[i] = vec.mul(a[i], k, do_copy)

	return a

# a[i] = a[i] + k*a[j]
def rowkadd(a, i, j, k, do_copy=True):
	if do_copy:
		a = [] + a

	if i > len(a) - 1:
		raise Exception("Index out of range")

	if j > len(a) - 1:
		raise Exception("Index out of range")

	krow = vec.mul(a[j], k, do_copy)
	a[i] = vec.add(a[i], krow, do_copy)

	return a