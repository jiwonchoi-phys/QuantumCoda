def winlose_condition (player):
    global player, opplayer # player: 플레이어 자신 opplayer: 상대 플레이어
    if len(player.closed_deck) == 0: # 플레이어 자신이 가지고 있는 패중 자신의 덱이 모두 보여진 경우. len으로 원소의 길이를 잼
        print("이런! 게임에서 졌습니다!")
        lose_game() # 게임 종료 (게임 종료 후 새게임을 할지 프로그램을 종료할지 선택) # pygame에서 처리해야 할 듯함
    if len(opplayer.closed_deck) == 0:
        stop_game() # 게임을 멈춤 (즉 패는 공개되어 있는채로 종료) # pygame에서 처리해야 할 듯함
    if all(len(player.closed_deck)) == True:
        win_game() # 게임을 이긴 것으로 처리 # 이것 역시 pygame에서 처리해야 할 듯?