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
		
def equal(a, b):
	dimensions_must_match(a, b)
	
	for i in range( len(a) ):
		if not vec.equal(a[i], b[i]):
			return False
			
	return True

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
	

