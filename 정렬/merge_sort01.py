#병합 정렬 Solution 1
def merge_sort(a):
    n = len(a)

    if n<=1:
        return a

    mid = n//2 #중간을 기준으로 두 그룹으로 나눔
    g1 = merge_sort(a[:mid])
    g2 = merge_sort(a[mid:])

    result = []

    while g1 and g2:
        if g1[0] > g2[0]:
            result.append(g1.pop(0))
        else:
            result.append(g2.pop(0))
    
    result = result + g1 + g2
    return result

d = [6,8,3,9,10,1,2,4,7,5]
print(merge_sort(d))