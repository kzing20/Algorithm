def fact(n):
    if n <= 1: # 재귀호출 시 종료조건 필요
        return 1
    return n * fact(n - 1)
print(fact(0)) # 0! = 1
print(fact(5)) # 5! = 120
print(fact(10)) # 10! = 3628800