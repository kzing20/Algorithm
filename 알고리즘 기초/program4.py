def Hanoi(N, from_pos, to_pos, via_pos):
    if N == 1: # 원반 한 개를 옮기는 문제면 그냥 옮기면 됨
        print( from_pos, "번 기둥에 있는 원반을 ", to_pos, "번 기둥으로 옮긴다." )
        return
    Hanoi(N - 1, from_pos, via_pos, to_pos)
    print( from_pos, " 번 기둥에 있는 원반을 ", to_pos, "번 기둥으로 옮긴다." )
    Hanoi(N - 1, via_pos, to_pos, from_pos)
print(" N = 1")
Hanoi(1, 1, 3, 2) # 원반 한 개를 1번 기둥에서 3번 기둥으로 이동 (2번을 경유 기둥으로)
print("\n N = 2")
Hanoi(2, 1, 3, 2) # 원반 두 개를 1번 기둥에서 3번 기둥으로 이동 (2번을 경유 기둥으로)
print("\n N = 3")
Hanoi(3, 1, 3, 2) # 원반 세 개를 1번 기둥에서 3번 기둥으로 이동 (2번을 경유 기둥으로)
