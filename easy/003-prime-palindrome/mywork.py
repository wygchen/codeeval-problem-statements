def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True

def is_palindrome(n):
    return str(n) == str(n)[::-1]

for num in range(999, 1, -1):
    if is_prime(num) and is_palindrome(num):
        print(num)
        break

# time: O(root(N)) best case
# space: O(1)