def winlose_condition (turn):
    global public_field # 플레이어 i가 가지고 있는 패 (공개되지 않은것), 플레이어 i가 가지고 있는 패중 공개된 것들
    if "?" not in public_field[turn]: # 플레이어 자신이 가지고 있는 패중 숨겨진 패가 없을 때. len으로 원소의 길이를 잼
        print("플레이어",turn,"는 패가 모두 공개되어 있습니다. 턴을 넘김니다.")
        next_turn(turn)
        turn_count += 1
        break
    if win == pn-1:
        print("플레이어", turn,"의 승리입니다.")
        print("게임을 종료합니다.")
        raise SystemExit



"""
pn=3
public_field = list(range(0,pn))
winlose_condition()
"""