import math


# primes using Sieve of Eratosthenes (storing only odds)
def get_primes(limit):
  odds_only_limit = limit // 2 + 1
  primes = [True] * odds_only_limit
  primes[0] = False

  for i in range(1, math.floor(math.sqrt(limit) + 1)):
    n = 2 * i + 1
    if primes[i]:
      step = n
      start = i + step if step == 3 else i + step * 2
      for j in range(start, odds_only_limit, step):
        primes[j] = False

  return primes


def is_prime(num, primes=None):
  if primes is not None and len(primes) >= num:
    if num % 2 == 0:
      return num == 2
    return primes[math.floor((num - 1) / 2)]

  # primes (sieve) wasn't passed as an argument, naive check if n is prime
  if num < 1:
    return True
  elif num == 2 or num == 3:
    return True
  elif num % 2 == 0 or num % 3 == 0:
    return False
  i = 5
  while i * i <= num:
    if num % i == 0 or num % (i + 2) == 0:
      return False
    i += 6

  return True


def get_prime_factors(num, primes):
  if is_prime(num, primes):
    return []

  prime_factors = []
  if num % 2 == 0:
    base_exp = {'base': int(2), 'exp': int(0)}
    while num % 2 == 0:
      base_exp['exp'] += 1
      num /= 2
    prime_factors.append(base_exp)

  sqrt = math.sqrt(num)
  for i in range(3, math.floor(sqrt + 2), 2):
    if num < i:
      break
    if is_prime(i, primes):
      if num % i == 0:
        base_exp = {'base': int(i), 'exp': int(0)}
        while num % i == 0:
          base_exp['exp'] += 1
          num /= i
        prime_factors.append(base_exp)

  if num > 2:
    prime_factors.append({'base': int(num), 'exp': int(1)})

  return prime_factors
