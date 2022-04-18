#퀵 정렬 Solution 02
#퀵 정렬의 실제 구현(partiton)은 매번 새로운 메모리 할당 없이
#값의 교환(swap)을 이용해서 구현됨
def partition(a,start,end):
    pivot = a[end]
    i = start
    for j in range(start, end):
        if a[j] <= pivot:
            a[i], a[j] = a[j], a[i]
            i+=1
    a[i], a[end] = a[end], a[i]
    return i

def quick_sort_sub(a,start,end):
    if start <end:
        pos = partition(a,start,end)
        quick_sort_sub(a,start,pos-1)
        quick_sort_sub(a,pos+1,end)

def quick_sort(a):
    quick_sort_sub(a, 0 , len(a)-1)

d= [6,8,3,9,10,1,2,4,7,5]
quick_sort(d)
print(d)