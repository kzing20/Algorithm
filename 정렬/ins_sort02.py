# 삽입 정렬 Solution 2
# 값의 이동(Shift)과 삽입 이용
def ins_sort(a):
    n = len(a)
    for i in range(1,n):
        key = a[i]  #리스트의 i번째 값을 삽입하고자 함(저장)
        j = i - 1

        while j >=0 and a[j] > key: #삽입될 값보다 크면 오른쪽으로 한 칸씩 옮김
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key

d= [2,4,5,1,3]
ins_sort(d)
print(d)