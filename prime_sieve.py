def get_primes(n):
    """Return list of all primes less than n,
    Using sieve of Eratosthenes.
    """
    if n <= 0:
        raise ValueError("'n' must be a positive integer.")
    # If x is even, exclude x from list (-1):
    sieve_size = (n // 2 - 1) if n % 2 == 0 else (n // 2)
    sieve = [True for _ in range(sieve_size)]   # Sieve
    primes = []      # List of Primes
    if n >= 2:
        primes.append(2)      # 2 is prime by default
    for i in range(sieve_size):
        if sieve[i]:
            value_at_i = i*2 + 3
            primes.append(value_at_i)
            for j in range(i, sieve_size, value_at_i):
                sieve[j] = False
    return primes
