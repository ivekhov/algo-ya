'''Решето Эратосфена работает за (n * log(logn)). '''
import sys


def eratosthenes(n):
    numbers = list(range(n + 1))
    numbers[0] = numbers[1] = False
    for num in range(2, n):
        if numbers[num]:
            for j in range(2 * num, n + 1, num):
                numbers[j] = False
    return numbers


def eratosthenes_effective(n):
    numbers = list(range(n + 1))
    numbers[0] = numbers[1] = False
    for num in range(2, n):
        if numbers[num]:
            for j in range(num * num, n + 1, num):
                numbers[j] = False
    return numbers


def get_least_primes_linear(n):
    lp = [0] * (n + 1)
    primes = []
    for i in range(2, n + 1):
        print(f'i: {i}')
        if lp[i] == 0:
            lp[i] = i
            primes.append(i)
        print(f'lp: {lp}')
        for p in primes:
            print(f'p: {p}')
            x = p * i
            print(f'x: {x}')
            if (p > lp[i]) or (x > n):
                break
            lp[x] = p
            print(f'primes: {primes}')
        print('---------')

    return primes, lp
    


import math


def is_prime(num):
	for i in range(2, int(math.sqrt(num)) + 1):
		if num % i == 0:
			return False
	return True



if __name__ == '__main__':
    num = sys.stdin.readline().rstrip()
    num = int(num)

    # print(eratosthenes_effective(num))
    print(get_least_primes_linear(num))
