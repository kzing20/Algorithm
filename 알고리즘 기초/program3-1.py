def fact(n):
    f = 1 # 곱을 계산할 변수, 초기값은 1
    for i in range(1, n + 1): # 1부터 n까지 반복
        f = f * i # 곱셈 연산으로 수정
    return f
print(fact(0)) # 0! = 1
print(fact(5)) # 5! = 120
print(fact(10)) # 10! = 3628800
