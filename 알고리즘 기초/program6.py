'''리스트에 있는 n개의 숫자 중에서 최대값 찾기 알고리즘을
재귀 알고리즘으로 구현하는 방법을 생각해보세요.'''
def find_max(a, n): # 리스트 a의 앞부분 n개 중 최댓값을 구하는 재귀 함수
    if n == 1:
        return a[0]
    max_n_1 = find_max(a, n - 1) # n-1개 중 최댓값을 구함
    if max_n_1 > a[n - 1]: # n-1개 중 최댓값과 n-1번 위치 값을 비교
        return max_n_1
    else:
        return a[n - 1]
v = [17, 92, 18, 33, 58, 7, 33, 42]
print(find_max(v, len(v)))