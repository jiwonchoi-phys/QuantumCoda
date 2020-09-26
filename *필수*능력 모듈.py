#################################################################  패시브 능력 - 항시 발동하는 능력

def average_ability(p,choice_player,choice_card): # 1번 패스브 능력 - 지목한 카드의 평균을 보여줌
    ability_num = (p[choice_player-1][choice_card-1][1][0]+p[choice_player-1][choice_card-1][1][1])/2    
    print("지목하신 카드의 평균값은",ability_num,"입니다.")

def diffrence_ability(p,choice_player,choice_card): # 2번 패시브 능력 - 지목한 카드의 스포키 넘 차이를 보여줌
    diffrence_num = abs(p[choice_player-1][choice_card-1][1][0]-p[choice_player-1][choice_card-1][1][1])
    print("지목하신 카드의 스포키 숫자의 차이는",diffrence_num,"입니다.")

#################################################################

#################################################################  엑티브 능력 - 대부분 한번만 사용가능

def silence(pn,public_field,turn,player_ablilty): # 1번 엑티브 능력 - 상대방 전체에 침묵을 걸어 다음 턴동안 능력을 못쓰게 함
    p_qm = []                                     # 발동 조건 : 나의 오픈된 패가 상대방들 중에서 가장 많을 때 활성화 됨
    for i in range(0,pn):
        p_qm.append(count_qm(public_field[i]))
    if min(p_qm) == p_qm[turn-1]:
        print("침묵 능력이 활성화 되었습니다")
        while 1:
            silence_use = input("사용하시겠습니까? (y/n)")
            if silence_use == "n":
                print("사용하지 않으셨습니다")
                break
            elif silence_use == "y":
                print("침묵 능력을 사용합니다 다음 한턴 동안 상대방들은 능력을 사용할 수 없습니다.")
                for i in range(0,pn):
                    if i != turn-1:
                        player_ablilty[i] = [-1,-1]
                    else:
                        player_ablilty[i][1] = 0
                break
            else:
                print("입력오류")

def bulldozer(bulldozer_count,pn): # 2번 엑티브 능력 - 내가 유추한 숫자가 있으면 그 숫자대로 붕괴 함
    if bulldozer_count >= pn:       # 발동 조건 : 카드유추를 플레이어 수만큼 실패하면 활성화 됨
        while 1:
            bulldozer_use = input(pn,"번의 카드유추 실패로 불도저가 활성화 되었습니다. 사용하시겠습니까? (y/n)")
            if bulldozer_use == "y":
                print("불도저를 사용하셨습니다")
                bulldozer_count = 0 # 몇번 틀렸는지 안려주는 숫자
                bulldozer_num = 1 # 불도저 붕괴를 일어나게 하기위한 숫자
                return bulldozer_num, bulldozer_count
                break
            elif bulldozer_use == "n":
                print("사용하지 않았습니다")
                break
            else:
                print("입력오류")

################################################################# 부속품

def count_qm(x): # x는 알고 싶은 플레이어의 공개필드 리스트
    qm_num = 0
    for i in range(0,len(x)-1):
        if x[i][1] == "?":
            qm_num += 1
    return qm_num

def bulldozer_collapse(x,y,p): # x는 choice_player y는 불도저 붕괴 숫자
    print("불도저 능력으로 인해 유추한 숫자로 붕괴합니다")    
    collapse_num = y                       
    if collapse_num == p[x-1][y-1][1][0]:
        p[x-1][y-1][1][1] = p[x-1][y-1][1][0]
        recent_collapse_num = p[x-1][y-1][1][0]     
        recent_collapse_color = p[x-1][y-1][0]
    elif collapse_num == p[x-1][y-1][1][1]:
        p[x-1][y-1][1][0] = p[x-1][y-1][1][1] 
        recent_collapse_num = p[x-1][y-1][1][1]
        recent_collapse_color = p[x-1][y-1][0]
    return recent_collapse_num, collapse_num, recent_collapse_color
          
