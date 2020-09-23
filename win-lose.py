def winlose_condition (player):
    global p, public_field # 플레이어 i가 가지고 있는 패 (공개되지 않은것), 플레이어 i가 가지고 있는 패중 공개된 것들
    for i in range (0,pn): # pn은 선택한 플레이어 명수
        if len(p[i]) == 0: # 플레이어 자신이 가지고 있는 패중 숨겨진 패가 없을 때. len으로 원소의 길이를 잼
            print("이런! 게임에서 졌습니다!")
            lose_game() # 게임 종료 (게임 종료 후 새게임을 할지 프로그램을 종료할지 선택) # pygame에서 처리해야 할 듯함
        elif len(opplayer.closed_deck) == 0:
            stop_game() # 게임을 멈춤 (즉 패는 공개되어 있는채로 종료) # pygame에서 처리해야 할 듯함
        elif all(len(player.closed_deck)) == True:
            win_game() # 게임을 이긴 것으로 처리 # 이것 역시 pygame에서 처리해야 할 듯?