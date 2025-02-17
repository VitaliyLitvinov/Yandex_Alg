import sys
def factorization():
    n = int(sys.stdin.readline().rstrip())
    lp: list[int] = [0] * (n+1)
    primes: list[int] = []
    for i in range(2, n+1):
        if lp[i] == 0:
            lp[i] = i
            primes.append(i)
        for p in primes:
            x = p * i
            if (x > n) or (p > lp[i]):
                break
            lp[x] = p

    result: list[int] = []
    i = 0
    while n != 1:
        if n % primes[i] == 0:
            n /= primes[i]
            result.append(primes[i])
            i = 0
            continue
        i += 1
    sys.stdout.write(' '.join(map(str, result)))
if __name__ == '__main__':
    factorization()
