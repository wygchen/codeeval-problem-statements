# time O(n log log n)
# space O(n)
def sieve_of_eratosthenes(n: int) -> list[int]:
    if n < 2:
        return []

    is_prime = [True] * (n+1)
    is_prime[0] = is_prime[1] = False

    # mark multiples start from 2 up to sqrt(n)
    for p in range(2, int(n**0.5)+1):
        if is_prime[p]:
            # mark multiples of p start from p^2 up to n in steps of p
            for i in range(p**2, n+1, p):
                is_prime[i] = False

    return [i for i, prime in enumerate(is_prime) if prime]

# prime number theorem: p = n ln n, 1000 ln1000 = 6908
# 1000th prime is well below 10,000

print(sum(sieve_of_eratosthenes(10000)[:1000]))
