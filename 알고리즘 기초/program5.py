'''1부터 n까지의 합 구하기 (Algorithm 1) 을
 재귀 알고리즘으로 구현하는 방법을 생각해보세요'''
def sum_n(n):
    if n==0:
        return 0
    return sum_n(n-1) +n
print(sum_n(10))
