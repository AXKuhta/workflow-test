import math

def value_close(a, b):
	return abs(abs(a) - abs(b)) < 0.0001

# Точное соответствие
def equal(a, b):
	if len(a) != len(b):
		raise Exception("Length mismatch")

	for i in range( len(a) ):
		if a[i] != b[i]:
			return False
			
	return True

# Примерное соответствие
def close(a, b, eps = 0.0001):
	if len(a) != len(b):
		raise Exception("Length mismatch")

	for i in range( len(a) ):
		if abs(a[i] - b[i]) > eps:
			return False
			
	return True

# Без копирования: a += b
# При копировании: c = a + b
def add(a, b, do_copy=True):
	if do_copy:
		a = [] + a
		
	if len(a) != len(b):
		raise Exception("Length mismatch")
		
	for i in range( len(a) ):
		a[i] += b[i]
		
	return a

# Без копирования: a -= b
# При копировании: c = a - b
def sub(a, b, do_copy=True):
	if do_copy:
		a = [] + a
		
	if len(a) != len(b):
		raise Exception("Length mismatch")
		
	for i in range( len(a) ):
		a[i] -= b[i]
		
	return a

def mul(a, k, do_copy=True):
	if do_copy:
		a = [] + a
		
	for i in range( len(a) ):
		a[i] *= k
		
	return a

def div(a, k, do_copy=True):
	if do_copy:
		a = [] + a
		
	for i in range( len(a) ):
		a[i] /= k
		
	return a

def dot(a, b):
	if len(a) != len(b):
		raise Exception("Length mismatch")
	
	acc = 0.0
	
	for i in range( len(a) ):
		acc += a[i] * b[i]
		
	return acc

def mag(a):
	acc = 0.0
	
	for i in range( len(a) ):
		acc += a[i] * a[i]
		
	return acc ** 0.5

def cos(a, b):
	return dot(a, b) / ( mag(a) * mag(b) )

def deg(a, b):
	return math.degrees(math.acos(cos(a, b)))

def not_opposing(a, b):
	return value_close(cos(a, b), 1.0)

def opposing(a, b):
	return value_close(cos(a, b), -1.0)
	
def collinear(a, b):
	k = cos(a, b)
	return value_close(k, -1.0) or value_close(k, 1.0)
	
def orthogonal(a, b):
	return value_close(cos(a,b), 0.0)

def invert(a, do_copy=True):
	if do_copy:
		a = [] + a
		
	for i in range( len(a) ):
		a[i] = -a[i]
		
	return a

def norm(a, do_copy=True):
	if do_copy:
		a = [] + a
		
	k = mag(a)
		
	for i in range( len(a) ):
		a[i] = a[i] / k
		
	return a

def project(a, b, do_copy=True):
	return mul(a, dot(b, a) / dot(a, a), do_copy=do_copy)

def sproject(a, b):
	return mag(project(a, b))

