################능력 or 아이템(추가 예정) ###############

# 1. 카드유추를 실패해도 이어서 한번 더 유추할 수 있음 이경우 두번 틀려도 패를 한개만 깜
# 2. 유추한 숫자가 있을 경우 무조건 그 숫자로만 붕괴
# 3. 상대방에게 침묵을 걸어 아이템 or 능력 및 카드 지목을 못하게함

############# 2020 09 27 패치노트 ######################

# 1. 조커는 배열에서 무시하도록 추가
# 2. '조커의 자리를 플레이어가 정하는 과정'에서 오류 발견. > 수정필요
# 3. 한 플레어이가 시작시 두 색상의 조커 카드를 모두 가져가는 경우 고려안됨. > 추가필요

########################################################

############# 2020 10 01 패치노트 ######################

# 1. 승패코드 근본 오류 수정
# 2. 컴퓨터 오토 붕괴에서 뽑을 카드 더미는 붕괴 안하던 현상을 수정
# 3. 아웃된 플레이어는 지목할 수 없도록 변경
# 4. 모두 아웃 시켰을 때 더이상 게임을 진행 못하도록 해야함

########################################################

############# 2020 10 04 패치노트 ######################

# 1. 컴퓨터 오토 붕괴에서 인덱스 아웃 오브 레인지가 일어나던 현상을 수정
# 2. 공개필드와 실제 패가 안맞는 현상을 수정

########################################################

############# 2020 10 07 패치노트 ######################

# 1. 카드 생성에서 카드수를 늘리면 무한루프와 에러뜨던 현상을 수정하였습니다.

########################################################

############# 2020 10 08 패치노트 ######################

# 1. 확률성분을 넣고 그 확률을 보여주며 확률에따라 붕괴하도록 함

########################################################

import random
import numpy
import copy
import math

################################# 카드를 생성하는 함수

def make_spooky(x): # x라는 리스트를 넣으면 스포키 카드를 생성해서 x에 추가하고  x를 리턴 
    global max_card_num # 패의 최대 숫자 전역변수
    max_card_num = 13
    min_loop_num = 3 # 최소 루프 개수
    cut_num = list(range(0,math.ceil((max_card_num+1)/min_loop_num)-2)) # math.ceil함수는 숫자 올림
    cut = []                     # cut1을 보관하는 장소
    card_list = list(range(0,max_card_num+1)) # 0~5 총 6개
    random.shuffle(card_list) # 섞는다 (shuffle 함수 기능)
    while 1:  # 얽힐 숫자들을 정하는 코드
        cut1 = 3+random.choice(cut_num) # cut_num의 임의 원소 선택, 루프 안에 들어가는 숫자의 개수, 3+가 있는 이유는 최소 루프 안에 들어있는 카드 숫자가 3이상이어야 하기 때문에. cut_num에서 숫자를 가져오는 이유는 루프 안에 있는 숫자의 개수를 다양화하기 위해 가져옴.
        cut.append(cut1) # 3 아님 4 추가
        if sum(cut) == max_card_num + 1:         # 총 얽힘수가 총 카드수랑 같으면 멈춤
            break
        elif sum(cut) > max_card_num + 1:            # cut수가 총 카드수보다 크면 마지막 cut1을 cut에서 뺀 후 뺀 것을 cut2라고 지정
            cut2 = cut.pop()
            if max_card_num + 1 - sum(cut) < 3:         # 남아 있는 수가 최소 얽힘수(3)보다 작다면 이전에 있던 cut1의 숫자를 늘려서 루프에 포함시킨다.
                cut[len(cut)-1] += max_card_num + 1 - sum(cut) 
                break
            else:                                       # 반대로 남아 있는 카드 수가 최소 얽힘수(3)보다 크거나 같으면 이전에 없앴던 cut1을 줄여서 남은 카드 수만큼 맞춘 다음, 다시 cut에 집어넣는다.          
                cut2 = max_card_num + 1 - sum(cut)   
                cut.append(cut2)
                break
    card_num = list(numpy.zeros(len(cut)))       # 루프 수만큼 방을 생성
    cut.append(0)
    add_card_s = 0
    add_card_f = cut[0]
    for i in range(0,len(cut)-1):          # 얽혀 있는 카드들끼리 한 방을 쓰도록 배정
        card_num[i] = []
        for k in range(add_card_s,add_card_f): 
            card_num[i].append(card_list[k])
        add_card_s += cut[i]
        add_card_f += cut[i+1]
    for i in range(0,len(card_num)):                # 각 방에 배정받은 숫자를 짝지어 spooky 카드를 만들도록 함
        for k in range(0,len(card_num[i])):   
            if k == 0:
                spooky_card_num = [card_num[i][k-1],card_num[i][k]] 
                alpha = max(spooky_card_num)
                spooky_card_num.append(int((spooky_card_num[0]+alpha/2)/(spooky_card_num[0]+spooky_card_num[1]+alpha)*100))
                beta = 100 - int((spooky_card_num[0]+alpha/2)/(spooky_card_num[0]+spooky_card_num[1]+alpha)*100)
                spooky_card_num.append(beta)
                x.append(spooky_card_num)
            else:
                gama = int(x[len(x)-1][3]+random.random()*20-10)
                spooky_card_num = [card_num[i][k-1],card_num[i][k],gama,100-gama]
                x.append(spooky_card_num)
    return x           

def player_p(x): # x는 알고자 하는 플레이어 번호
    global p_p
    p_p = []
    for i in range(0,len(p[x-1])):
        if p[x-1][i][1][0] == p[x-1][i][1][1]:
            p_p.append([i+1,[100,100]])
        else:
            p_p.append([i+1,pro[ti_p.index(p[x-1][i])]])

############################################################################   게임 진행을 위한 함수지정
#   1) 정렬===============================================================

#   1-1) spooky 숫자 정렬-------------------------------------------------
def spooky_arrange(i):
    dummy = p[i]            # 임시 리스트 생성
    for k in list(range(0,len(dummy))): 
        if dummy[k][1][0] < dummy[k][1][1]: # 두 spooky 수 고려 작으면 놔둠 dummy[k][1][0] 의미: [k]: for문 [1]은 spooky [0]: spooky중 첫 째
            pass
        else:   # 다르면 교환 후 저장
            dummy[k][1][0], dummy[k][1][1] = dummy[k][1][1], dummy[k][1][0]
            p[i]= dummy

#   1-2) 평균값 정렬 및 색상 정렬 옵션----------------------------------------
color_arrange_on = 0 # 평균값 중복시 색상에 따라 배열 규칙을 추가할 것인가? [0: no, 1: use] # (GUI 처리 해야됨)
def tile_arrange(i):
    dummy = p[i]    #임시 리스트 생성
    for q in range(0,len(dummy)):   #총 길이만큼 교환 실행
        #print(q,"회 교환) 플레이어",i,"의 타일과 spooky 수", dummy) # 테스트용 주석처리입니다 삭제금지!!
        for k in list(range(0,len(dummy)-1)):   #모든 원소에 대해
            if dummy[k][1][0]+dummy[k][1][1] <= dummy[k+1][1][0]+dummy[k+1][1][1]: # 두 spooky 수 평균값 고려 작거나 같으면 놔둠
                if dummy[k][1][0]+dummy[k][1][1] == dummy[k+1][1][0]+dummy[k+1][1][1]: # 평균값 중복시 작은 spooky 수 비교
                    if  dummy[k][1][0] <= dummy[k+1][1][0]:                            
                        if dummy[k][1][0] == dummy[k+1][1][0] and color_arrange_on == 1: # 평균값 중복에 스푸키 숫자도 모두 겹치는 경우 + 색상 배열 사용시 검정이 왼쪽에 오게 설정
                            if  dummy[k][0] < dummy[k+1][0]:                             #ㄴ 따라서 평균값 3으로 [0,[1,5]][1,[2,4]] [0,[2,4]] 의 배열이 가능
                                dummy[k+1], dummy[k] = dummy[k], dummy[k+1]              #ㄴ 우선순위 spooky 정렬 > 색상 정렬 : 이유 색상을 우선순위 먼저 두면 평균값이 동일한 애들이 많을때 "블블블화화화" 같은 배열이 생김
                    else: #아니면 바꿔
                        dummy[k+1], dummy[k] = dummy[k], dummy[k+1]
            else:   #앞에 놈이 더크면  교환 후 저장
                    dummy[k+1], dummy[k] = dummy[k], dummy[k+1]
                    p[i]= dummy #

#   1-3) 조커 파악------------------------------------------------------------

#   1-4) 정렬 통합------------------------------------------------------------
def arrange(i): # 위의 spooky_arrange tile_arrange 함수 같이 실행 # 순서 중요
    spooky_arrange(i)
    #print("jn[i]", jn[i]) # 확인용 삭제금지
    tile_arrange(i)

#   2) 턴 넘기기===============================================================
def next_turn(i):
    global turn, win
    turn = i+1 # 턴을 다음 플레이어에게 넘김.
    win = 0
    if turn == pn+1:
        turn = 1
    while 1:
        if count_qm(public_field[turn-1]) == 0:
            turn += 1
            win += 1
            if turn == pn+1:
                turn = 1
        else:
            break


    #탈락한 플레이어를 제외 하고 턴 넘김 필요.

# 공개 필드의 알려지지 않은 카드 숫자 세는 함수

def count_qm(x): # x는 알고 싶은 플레이어의 공개필드 리스트
    qm_num = 0
    for i in range(0,len(x)):
        if x[i][1] == "?":
            qm_num += 1
    return qm_num

# 플레이어 지목 함수

def c_p():
    global choice_player
    while 1:                        # 플레이어를 지목하는 코드  
        choice_player = float(input("맞추고 싶은 상대방을 고르세요:")) # 플레이어 수를 입력받아서 그에 맞게 선택지를 줌
        choice_player = int(choice_player) 
        if choice_player > pn or choice_player < 1:
            print("그런 플레이어는 없습니다")
        elif count_qm(public_field[choice_player-1]) == 0:
            print("그 플레이어는 아웃되었습니다")
        elif choice_player == turn:
            print("자신을 선택할 수 없습니다")
        elif choice_player <= pn and choice_player >= 1:
            print("플레이어",choice_player,"를 지목했습니다")
            break
        else:
            print("입력오류")

# 뽑는 카드 색깔 정하는 코드

def c_color():           
    global choice_color, recent_card, c_color_e
    c_color_e = 0
    ti_b = []  # 검은색을 뽑을건지 흰색을 뽑을건지 플레이어가 정함
    ti_w = []  # 그래서 따로 검은색 흰색 그룹을 생성
    for i in range(len(ti)-1):  # 검은색 흰색 그룹에 색에 맞게 넣음
        if ti[i][0] == 1:
            ti_b.append(ti[i])
        elif ti[i][0] == 0:
            ti_w.append(ti[i])
    while 1:
        if len(ti_b) == 0 and len(ti_w) == 0:
            print("더 이상 뽑을 카드가 없습니다 플레이어 지목 단계로 넘어갑니다.")
            c_color_e = 1
            break
        else:
            choice_color = input("가져갈 카드의 색깔을 골라주세요 (b,w):")    # 검은색이면 검은색 뽑고 흰색이면 흰색 뽑게함
            if choice_color == "b" and len(ti_b) != 0:                      # 입력받은 색깔이 b,w에 따라 그에 맞는 색카드를
                recent_card = random.choice(ti_b)                           # 뽑고 패에 추가 최근 카드는 이후 틀렸을 때
                p[turn-1].append(recent_card)                               # 카드를 넘기기 위해 가져옴
                public_field[turn-1].append([1,"?"])
                field_count.pop(ti.index(recent_card))
                ti.pop(ti.index(recent_card))   # 뽑은 카드를 다시 뽑으면 안되니 뽑은 카드는 필드에서 삭제함
                arrange(turn-1)          # 뽑았으니 재배열함
                break
            elif choice_color =="b" and len(ti_b) == 0:
                print("검은색 카드가 없습니다")
            elif choice_color == "w"and len(ti_w) != 0:
                recent_card = random.choice(ti_w)
                p[turn-1].append(recent_card)
                public_field[turn-1].append([0,"?"])
                field_count.pop(ti.index(recent_card))
                ti.pop(ti.index(recent_card))   # 뽑은 카드를 다시 뽑으면 안되니 뽑은 카드는 필드에서 삭제함
                arrange(turn-1)          # 뽑았으니 재배열함
                break
            elif choice_color =="w" and len(ti_w) == 0:
                print("흰색 카드가 없습니다")
            else:
                print("입력오류")


# 지목한 플레이어의 카드 유추 코드

def c_card():            
    global choice_card, one_more, rcn
    while 1:                        # 지목한 플레이어의 카드를 지목하고 유추한 후 상황을 전개하는 코드
        if len(before_choice_card[turn-1][choice_player-1]) != 0:
            print("이전에 지목했던",choice_player,"플레이어의 카드는",p[choice_player-1].index(before_choice_card[turn-1][choice_player-1])+1,"번째 카드입니다.")
        print("플레이어",choice_player,"의 패:",public_field[choice_player-1])
        print("나의 패:",p[turn-1])
        choice_card = float(input("맟추고 싶은 카드 번호를 고르세요 상대방 기준 왼쪽부터 1번입니다:"))     # 이제 카드를 고르게 하고
        choice_card = int(choice_card)                                                                 # 제대로 골랐는지 확인함
        if choice_card > len(p[choice_player-1]) or choice_card < 1:
            print("존재하지 않는 카드입니다")
        elif public_field[choice_player-1][choice_card-1][1] != "?":
            print(public_field[choice_player-1][choice_card-1][1])
            print("그 카드는 이미 공개되었습니다")
        elif choice_card <= len(p[choice_player-1]) or choice_card >= 1:
            print(choice_card,"번째 카드를 선택했습니다")
            print("플레이어",choice_player,"의 패:",public_field[choice_player-1])
            print("나의 패:",p[turn-1])
            choice_num = float(input("그 카드의 숫자는 무엇입니까:"))       # 제대로 골랐으니 숫자를 찍어라 함 
            choice_num = int(choice_num)                                  # 유추한 다음 룰에 맞게 상황을 조정
            before_choice_card[turn-1][choice_player-1] = p[choice_player-1][choice_card-1]
            if choice_num != p[choice_player-1][choice_card-1][1][0] and choice_num != p[choice_player-1][choice_card-1][1][1]:
                print("그런 숫자는 없습니다 룰에 따라 방금 뽑은 카드를 붕괴하고 공개 합니다")    # 스포키 숫자중 한개도 못맞힘
                if c_color_e == 1:
                    print("이번 턴에 뽑은 카드가 없습니다 공개없이 진행합니다")
                    rcn = 1
                else:
                    collapse(turn,p[turn-1].index(recent_card)+1)       #미리 짜놓은 붕괴함수와 필드에 공개하는 함수를 사용
                    public(turn,p[turn-1].index(recent_card)+1)
                break
            elif choice_num == p[choice_player-1][choice_card-1][1][0] or choice_num == p[choice_player-1][choice_card-1][1][1]:
                print("그런 숫자가 있습니다 룰에 따라 확률로 카드를 붕괴합니다")            #스포키 숫자 한개라도 맞춰서
                collapse(choice_player,choice_card)                                       # 컴퓨터가 확률로 붕괴
                before_choice_card[turn-1][choice_player-1][1][0] = collapse_num          # 이 또한 미리 짜놓은 코드를 사용
                before_choice_card[turn-1][choice_player-1][1][1] = collapse_num
                if choice_num == collapse_num:                                            
                    print("숫자를 정확히 맞추셨습니다. 룰에 따라 카드를 공개합니다")
                    public(choice_player,choice_card)
                    
                    while 1:
                        choice_turn = input("한번 더 맞추시겠습니까? (y/n):")
                        cpb = 0
                        if choice_turn == "y":
                            one_more = 1
                            cpb = 1
                            break
                        elif choice_turn == "n":
                            print("턴을 넘기셨습니다 다음 사람이 플레이 합니다.")
                            cpb = 1
                            break
                        else:
                            print("입력오류")
                elif choice_num != collapse_num:
                    print("유추한 숫자로 붕괴하지 않았습니다 룰에 따라 아무런 조치없이 넘어갑니다")
                    break
                if cpb == 1:
                    break

# 카드 1개 붕괴 함수

def collapse(x,y): # x는 붕괴 되려는 플레이어, y는 붕괴시킬 카드 번호
    global recent_collapse_num, collapse_num, recent_collapse_color
    collapse_num = numpy.random.choice(p[x-1][y-1][1],p=[pro[ti_p.index(p[x-1][y-1])][0]/100,pro[ti_p.index(p[x-1][y-1])][1]/100])
    qaz = ti_p.index(p[x-1][y-1])
    if collapse_num == p[x-1][y-1][1][0]:
        p[x-1][y-1][1][1] = p[x-1][y-1][1][0]
        recent_collapse_num = p[x-1][y-1][1][0]     #최근 붕괴 숫자는 나중 연쇄 붕괴를 위해 가져옴
        recent_collapse_color = p[x-1][y-1][0]
    elif collapse_num == p[x-1][y-1][1][1]:
        p[x-1][y-1][1][0] = p[x-1][y-1][1][1] 
        recent_collapse_num = p[x-1][y-1][1][1]
        recent_collapse_color = p[x-1][y-1][0]
    ti_p[qaz] = copy.deepcopy(p[x-1][y-1])

# 전체적인 카드 붕괴

def overall_collapse(x,y): # 붕괴 숫자 x와 색깔 y를 넣으면 그와 관련된 카드들을 붕괴시킴
   print("컴퓨터가 판단해서 전체적으로 붕괴 할 것이 있으면 붕괴 시키겠습니다")
   for i in range(0,pn): # 오토 붕괴를 하기 위해 카드 형식을 수정
       for k in range(0,len(public_field[i])):
               if public_field[i][k][1] == "?":
                   public_field[i][k] = "?"
   public_check1 = copy.deepcopy(public_field) 
   public_check2 = copy.deepcopy(public_field)          #파이썬이 리스트 복사하는게 까탈스러워서 딮카피를 써야 복사한 리스트와
   omg = 0                                              #복사된 리스트가 서로 다른 주소를 할당 받아게 되어 이후 한쪽이 수정되어도
   while 1:                                             #다른쪽이 수정 안됨
       fkdo = 0    
       if public_check1[omg].count("?") == 0:            #공개 필드의 모름숫자는  ?로 함 omg는 플레이어 수임 예로 public_check[omg]
           omg += 1                                     #면 omg 숫자에 해당되는 플레이어 패를 검토중임
       elif p[omg][public_check1[omg].index("?")][0] == y:   # 붕괴한 숫자와 색깔을 가져와서 플레이어 패를 하나하나 비교
           if p[omg][public_check1[omg].index("?")][1][0] == x:      #그래서 붕괴될께 있으면 붕괴하고 최근 붕괴 숫자를 최신화하고 
               wsx = ti_p.index(p[omg][public_check1[omg].index("?")])    
               p[omg][public_check1[omg].index("?")][1][0] = p[omg][public_check1[omg].index("?")][1][1] #처음부터 다시 스캔
               x = p[omg][public_check1[omg].index("?")][1][1]                                           # 반복
               ti_p[wsx] = copy.deepcopy(p[omg][public_check1[omg].index("?")])
               public_check2[omg][public_check1[omg].index("?")] = "E"   # check 2,1 의 차이는 check1이 확인하면서 아닌거는 
               public_check1 = copy.deepcopy(public_check2)             # E로 표현하는데 붕괴 해야할 카드를 찾아버리면
               omg = 0                                                  # 처음부터 다시 스캔해야 하기 때문에 백업용으로
           elif p[omg][public_check1[omg].index("?")][1][1] == x:       # check2를 놔둠 그리고 붕괴한 카드는 check2에 E로 
               wsx = ti_p.index(p[omg][public_check1[omg].index("?")])    
               p[omg][public_check1[omg].index("?")][1][1] = p[omg][public_check1[omg].index("?")][1][0] #표현되어 다시 체크 할 일이 없음
               x = p[omg][public_check1[omg].index("?")][1][0]
               ti_p[wsx] = copy.deepcopy(p[omg][public_check1[omg].index("?")])
               public_check2[omg][public_check1[omg].index("?")] = "E"
               public_check1 = copy.deepcopy(public_check2)
               omg = 0
           else:
               public_check1[omg][public_check1[omg].index("?")] = "E" # 여기서 E는 ?카드를 뒤집어 봤다는 표시로 
               if public_check1[omg].count("?") == 0:
                   omg += 1
       elif p[omg][public_check1[omg].index("?")][0] != y:
            public_check1[omg][public_check1[omg].index("?")] = "E"
            if public_check1[omg].count("?") == 0:
                omg += 1
       if omg == pn: # 모든 플레어의 패를 끝까지 다 훑었으면 뽑을 패 더미도 확인
          if len(ti) == 0: # 뽑을 패 더미가 없으면 카드 형식을 다시 원래대로 함
              for i in range(0,pn):
                  for k in range(0,len(public_field[i])):
                      if public_field[i][k] == "?":
                          public_field[i][k] = [p[i][k][0],"?"]    
              break
          else:
              ti_c = 0 # 뽑을 패 더미를 하나하나 확인해서 붕괴시킴
              while 1:
                  if ti[ti_c][0] == y:
                      if ti[ti_c][1][0] == x and field_count[ti_c] != "E":
                          wsx = ti_p.index(ti[ti_c])
                          ti[ti_c][1][0] = ti[ti_c][1][1]
                          x = ti[ti_c][1][1]
                          ti_p[wsx] = copy.deepcopy(ti[ti_c])
                          omg = 0
                          field_count[ti_c] = "E"
                          break
                      elif ti[ti_c][1][1] == x and field_count[ti_c] != "E":
                          wsx = ti_p.index(ti[ti_c])
                          ti[ti_c][1][1] = ti[ti_c][1][0]
                          x =ti[ti_c][1][0]
                          ti_p[wsx] = copy.deepcopy(ti[ti_c])
                          omg = 0
                          field_count[ti_c] = "E"
                          break
                      else:
                          ti_c += 1
                  else:
                      ti_c += 1
                  if ti_c == len(ti):
                      fkdo = 1
                      break
       if fkdo == 1:
           for i in range(0,pn):
                  for k in range(0,len(public_field[i])):
                      if public_field[i][k] == "?":
                          public_field[i][k] = [p[i][k][0],"?"] 
           break
                      
# 카드 공개 함수

def public(x,y): # 카드 공개 함수, 공개될 플레이어 x의 y카드를 공개
    public_field[x-1][y-1] = copy.deepcopy(p[x-1][y-1])
    public_field[x-1][y-1][1][0] = collapse_num
    public_field[x-1][y-1][1][1] = collapse_num
    print("붕괴 후 플레이어",x,"의 패:",public_field[x-1])


# 공개 필드 정렬함수
def public_arrange():
    for i in range(0,pn):
        for k in range(0,len(public_field[i])):
            if public_field[i][k][1] != "?" and public_field[i][k] != p[i][k]:
                omg2 = copy.deepcopy(public_field[i][k])
                public_field[i][k][0] = public_field[i][p[i].index(omg2)][0]
                public_field[i][k][1] = "?"
                public_field[i][p[i].index(omg2)] = copy.deepcopy(omg2)
                
################################################################################# 게임 진행


field_black = []
field_white = []
make_spooky(field_black)            # 검,흰 타일 만듬
make_spooky(field_white)
fcn=(max_card_num+1)*2              # full card number

ti = []                             # 전체 타일 묶음
tb = []                             # Tile Black
tw = []                             # Tile White

for i in range(0,max_card_num+1):   # 색상 정보 추가 (Black: 1, While: 0 으로 구분하는 for문)
    tb.append([1,field_black[i]])
    tw.append([0,field_white[i]])
    ti.append(tb[i])
    ti.append(tw[i])                # ti에 0과 1로 구분하고 넣음

pro = [] # 확률을 저장하는 리스트
for i in range(0,len(ti)):
    pro.append([ti[i][1][2],ti[i][1][3]])
    ti[i][1].pop()
    ti[i][1].pop()

for i in range(0,len(ti)):    
    if ti[i][1][0] > ti[i][1][1]:
        ti[i][1] = [ti[i][1][1],ti[i][1][0]]
        
ti_p = copy.deepcopy(ti) # 저장된 확률에 매치되는 카드

random.shuffle(ti)                  # 모든 타일 섞음
 
# 아래 ti는 테스트를 위한 임시 타일묶음으로 지우지 말아주세요!!
# ti = [[1, [3, 5]], [1, [1, 0]], [1, [4, 1]], [1, [2, 5]], [0, [1, 0]], [1, [2, 3]], [0, [3, 0]], [0, [2, 5]], [0, [4, 5]], [0, [3, 2]], [1, [0, 4]], [0, [4, 1]]]
print("섞은 전체 타일: ",ti)

#   3) 플레이어 수와 시작 타일 수 지정 및 배포===============================

#   3-1) 플레이어 수 지정--------------------------------------------------
player_num_max = 4  #게임 가능 플레이어 수 제한
while 1:
    print("플레이 최소 인원은 2명이고 최대 인원은",player_num_max,"명 입니다")
    print("플레이어 수를 소수로 입력하면 앞에 있는 숫자로 결정됩니다. ex)2.5는 2명")
    pn = float(input("플레이어 수를 입력해주세요:"))
    pn = int(pn)
    if pn > player_num_max:
        print("플레이어 수가 너무 많습니다 다시 입력해주세요")
    elif pn < 2:
        print("플레이어 수가 너무 적습니다 다시 입력해주세요")
    elif pn >=2 and pn <= player_num_max:
        print("플레이어 수가",pn,"명으로 결정되었습니다.")
        break
    else:
        print("입력오류")

p = list(range(0,pn))   # 플레이어 묶음 생성
public_field = list(range(0,pn))  # 공개된 카드 필드
before_choice_card = list(range(0,pn)) # 이전에 어떤 카드를 픽 했는지 알려주기 위한 리스트
for i in range(0,pn):
    before_choice_card[i] = list(range(0,pn))
    for k in range(0,pn):
        before_choice_card[i][k] = []

#   3-2) 타일수 지정--------------------------------------------------------
while 1:
    print("시작시 가져갈 초기 타일 수를 결정해 주세요(3 권장))")

    stn = float(input("스타팅 타일 수:"))
    stn = int(stn)
    if stn > fcn/pn:
        print("패를 나누기 위한 전체 타일 수가 부족합니다. 작은 수로 다시 입력해주세요")
    elif stn < 2:
        print("타일 수가 너무 적습니다 다시 입력해주세요")
    elif stn >= 2 and stn <= fcn/pn:
        print("플레이어가 받는 타일 수가",stn,"개로 결정되었습니다.")
        break
    else:
        print("입력오류")
    
for i in range(0,pn): # 플레이어 수만큼 리스트 생성
    p[i] = []                           # 플레이어 i가 가지고 있는 패 (공개되지 않은것)
    public_field[i] = []                # 플레이어 i가 가지고 있는 패중 공개된 것들
    for k in range(0,stn): #플레이어 리스트에 타일 배분
        qwer = random.choice(ti)
        p[i].append(qwer)
        ti.pop(ti.index(qwer))
    
for i in list(range(0,pn)): # 플레이어 전체에 대해 배열    
    arrange(i) # 위에 정의된 패를 정렬하는 함수
    # print(p[i]) # 확인용 삭제금지
    print("결과) 플레이어",i+1,"의 타일과 spooky 수", p[i])

for i in range(0,pn): # 공개필드에 미지수 ?를 넣음
    for k in range(0,stn):
        if p[i][k][0] == 0:
            public_field[i].append([0,"?"])
        elif p[i][k][0] == 1:
            public_field[i].append([1,"?"])

field_count = list(range(len(ti))) # 오토 붕괴에서 뽑을 카드 더미를 스캔하기 위한 리스트

while 1: # 순서 정하기
    print("오름차순으로 턴을 결정합니다. 먼저 플레이할 플레이어를 지정해주세요 (ex 1: 플레이어 1)")
    turn = float(input("먼저 시작할 플레이어 설정: "))
    turn = int(turn)
    if turn > pn:
        print("존재하지 않는 플레이어 번호입니다. 다시 입력해주세요")
    elif turn < 1:
        print("존재하지 않는 플레이어 번호입니다. 다시 입력해주세요")
    else:
        print("첫 턴의 플레이어가",turn,"으로 결정 되었습니다.")
        break

turn_count = 0 # Turn Count
while 1:
    print("플레이어",turn,"차례 입니다")
    print("나의 패:",p[turn-1]) # turn-1은 단순하게 list가 0부터 시작하므로 -1을 넣은 것
    player_p(turn)
    print("패 확률:",p_p)
    c_color() # 검정, 흰색 색깔 결정 후 가져오는 것까지의 함수
    arrange(turn-1) # 재배열
    print("뽑은 후 플레이어",turn,"의 패:",p[turn-1])
    player_p(turn) # turn플레이어의 패에 있는 숫자에 맞는 확률을 가져옴
    print("패 확률:",p_p)
    while 1:
        one_more = 0 # one_more 는 연속해서 카드를 맞출껀지에 대한 변수로 1이면 연속해서 맞추겠다는 뜻
        rcn = 0 # 붕괴가 일어났는지 유무 판단 변수
        c_p() # 플레이어 지목
        c_card() # 카드 숫자 유추
        if rcn != 1:
            overall_collapse(recent_collapse_num,recent_collapse_color) # 전체적인 컴퓨터 오토 붕괴
            arrange(turn-1) # 재배열
            public_arrange() # 공개 필드도 맞춰서 재배열
        if one_more == 0:
            break
    next_turn(turn) # 턴바꿈
    turn_count += 1 # 턴이 끝나서 카운트 추가, 몇턴이 지났는지 알아보기 위해서 꼭 필요함
    if win == pn-1: 
        print("플레이어",turn,"의 승리")
        break
    
#   끝)@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
