#퀵 정렬 Solution 01
def quick_sort(a):
    n = len(a)
    if n<=1:     #재귀 종료 조건                        
        return a       

    pivot = a[-1]
    g1 = []
    g2 = []
    for i in range(n-1):
        if a[i] < pivot:
            g1.append(a[i])
        else:
            g2.append(a[i])

    return quick_sort(g1) + [pivot] + quick_sort(g2)

d  = [6, 8, 3, 9, 10, 1, 2 ,4, 7, 5]
print(quick_sort(d))
