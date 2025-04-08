def fatorial(n, memo={0: 1, 1: 1}):
    if n not in memo:
        memo[n] = n * fatorial(n - 1, memo)
    return memo[n]

def coeficiente_binomial_analitico(n, k):
    if k < 0 or k > n:
        return 0
    return fatorial(n) // (fatorial(k) * fatorial(n - k))
