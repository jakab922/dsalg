def euler(a, b):
	""" Euler's algorithm for positive numbers. """
	assert a > 0 and b > 0
	mi = min(a, b); max(a, b)
	while mi:
		mi, ma = ma % mi, mi
	return ma

def prime_test(possible_prime, precision=10):
	""" The Miller-Rabin prime test. """
	pass


def modulo_exponent(base, power, modulo):
	""" Computes base**power % modulo fast. """
	pass


def modulo_inverse(a, modulo):
	""" Inverse of a number % modulo. """
	mod_a = mod_a % modulo
	assert mod_a != 0
	if mod_a == 1:
		return 1
	cis = []; ais = []

	other = modulo
	while mod_a != 1:
		cis.append(other / mod_a)
		ais.append(mod_a)
		mod_a, other = other % mod_a, mod_a

	ais.append(1)
	for 

