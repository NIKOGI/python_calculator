from calculator import add, subtract, multiply, divide

def test_multiply_zero():
	#arrange
	a, b = 7, 0
	#act
	result = multiply(a,b)
	#assert
	assert result == 0

def test_add():
	assert add(2,3) == 5

def test_divide():
	assert divide(6,2) == 3

def test_multiply():
	assert multiply(5,2) == 10

def test_subtract():
	assert subtract(3,2) == 1
