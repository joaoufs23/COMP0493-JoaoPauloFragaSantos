def binary_exponentiation(x, n):
    if n == 0:
        return 1
    half = binary_exponentiation(x, n // 2)
    half_squared = half * half

    if n % 2 == 0:
        return half_squared
    else:
        return x * half_squared

x = 3
n = 5
resultado = binary_exponentiation(x, n)
print(f'{x}^{n} = {resultado}')
