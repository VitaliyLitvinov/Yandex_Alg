import sys
def factorization():
    n = int(sys.stdin.readline().rstrip())
    primes: list[int] = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,41, 43, 47,
                         53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109,]
    result: list[int] = []
    i = 0
    while n != 1:
        if n % primes[i] == 0:
            n /= primes[i]
            result.append(primes[i])
            i = 0
        i += 1
    sys.stdout.write(' '.join(map(str, result)))
if __name__ == '__main__':
    factorization()
