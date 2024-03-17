MOD = 1000000007

# 분할 정복을 이용한 거듭제곱 계산
def fast_power(base, power, modulo):
    result = 1
    base %= modulo
    while power > 0:
        if power % 2 == 1:  # 홀수이면
            result = (result * base) % modulo
        base = (base * base) % modulo
        power //= 2
    return result

# 모듈로 역원 계산
def mod_inverse(number, modulo):
    return fast_power(number, modulo-2, modulo)

# 팩토리얼을 모듈로 M으로 계산
def factorial_mod(n, modulo):
    result = 1
    for i in range(1, n+1):
        result = (result * i) % modulo
    return result

# 이항 계수 계산
def binomial_coefficient(n, k, modulo):
    if k == 0 or k == n:
        return 1
    return (factorial_mod(n, modulo) * mod_inverse(factorial_mod(k, modulo), modulo) * mod_inverse(factorial_mod(n-k, modulo), modulo)) % modulo

N, K = map(int, input().split())
print(binomial_coefficient(N, K, MOD))
