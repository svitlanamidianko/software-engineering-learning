import operator

def liskov_substitution_principle(x):
	x = operator.__mod__(x, x)
	x = operator.__mul__(x, 2)
	print(x)

x = [2, 3]
print(dir(x))
liskov_substitution_principle(x)

#int Y, list N for mod, float Y, string N for mod
print (2.9 % 2)