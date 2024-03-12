from secret import code, flag
from random import randint
from Crypto.Util.number import long_to_bytes
from math import gcd

def dominance(n, i = -1):
	if i == -1:
		i = randint(1, n)
	
	arr = []
	for x in range(n):
		if gcd(x, n) == 1:
			arr.append(x)
	
	k = 1
	for _ in range(n+1):
		if k in arr:
			arr.remove(k)
		k *= i
		k %= n


	return len(arr) == 0

print("Here is the code -")
print(type(code))
print(code)
print()

assert(dominance(code))

coins = 0
for i in range(1, code):
	coins += dominance(code, i)

print("Here is the encoded flag -")
print(type(flag))
print(len(flag))

for b in zip(long_to_bytes(coins), flag):
	print(b[0]^b[1], end = " ")
