#선택 정렬 Solution 1
def find_min_idx(a):
    n = len(a)
    min_idx = 0
    for i in range(1, n):
        if a[i] < a[min_idx]:
            min_idx = i
    return min_idx
def sel_sort(a):
    result = [] # 새 리스트를 만들어 정렬된 값을 저장
    while a: # 주어진 리스트에 값이 남아있는 동안 계속
        min_idx = find_min_idx(a) # 리스트에 남아 있는 값 중 최소값의 위치
        value = a.pop(min_idx) # 찾은 최소값을 빼내어 value에 저장
        result.append(value) # value를 결과 리스트 끝에 추가
        print(result)
    return result
d = [2, 4, 5, 1, 3]
print(sel_sort(d))
