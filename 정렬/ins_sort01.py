#삽입 정렬 Solution 1
def find_ins_idx(r,v):
    for i in range(len(r)):
        # 정렬된 리스트에서 자신보다 작은 값들을 모두 지나고 큰 값 바로 앞에서 멈춘 위치, i
        if v < r[i]:
            return i
    return len(r)

def ins_sort(a):
    result = [] # 새 리스트를 만들어 정렬된 값을 저장
    while a: # 기존 리스트에 값이 남아 있는 동안 반복
        value = a.pop(0) # 기존 리스트에서 한 개를 꺼냄
        ins_idx = find_ins_idx(result, value)# 꺼낸 값이 들어갈 적당한 위치 찾기
        result.insert(ins_idx,value) # 찾은 위치에 값 삽입(이후 값은 한 칸씩 밀려남)
        print(result)
    return result

d = [2,4,6,5,7,1,3]
print(ins_sort(d))
