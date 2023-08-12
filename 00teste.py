def complex_manipulation(a, b, c):
	if a % 2 == 0:
		a+=3
	else:
		a -= 2
	b += 1
	
	if b % 3 == 0:
		b *= 2

	c = (a+b) * c -(a //a)
	
	if c > 100:
		c += 10
	else:
		c -= 5
	return a, b, c

a = 7
b = 11
c = 15

print(complex_manipulation(a, b, c))


