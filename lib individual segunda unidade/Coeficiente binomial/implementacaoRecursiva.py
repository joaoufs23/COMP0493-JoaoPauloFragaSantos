def coeficiente_binomial_recursivo(n, k, memo={}):
    if (n, k) in memo:
        return memo[(n, k)]
    
    if k == 0 or k == n:
        return 1
    
    if k < 0 or k > n:
        return 0
    
    memo[(n, k)] = coeficiente_binomial_recursivo(n - 1, k - 1, memo) + coeficiente_binomial_recursivo(n - 1, k, memo)
    
    return memo[(n, k)]
