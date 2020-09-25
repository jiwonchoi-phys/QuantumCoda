def winlose_condition (player):
    global p, public_field # 플레이어 i가 가지고 있는 패 (공개되지 않은것), 플레이어 i가 가지고 있는 패중 공개된 것들
    for i in range(0,pn): # 0부터 플레이어 pn까지 검사
        if "?" not in public_field[i]: # 플레이어 자신이 가지고 있는 패중 숨겨진 패가 없을 때. len으로 원소의 길이를 잼
            print("플레이어",i,"는 패가 모두 공개되어 있습니다.")
        
"""
pn=3
public_field = list(range(0,pn))
winlose_condition()
"""