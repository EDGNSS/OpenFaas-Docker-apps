def handle(req):

    try:
        m = int(req)
        primes = list()
        co = 2
        while len(primes) < m:
            if is_prime(co):
                primes.append(co)
            co +=1

        return len(primes)
    except:
        return "the input is not a number"

def is_prime(n):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    return False
