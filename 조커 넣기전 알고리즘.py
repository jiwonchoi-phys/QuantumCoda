############# 2020 09 21 패치 노트 ######################

# 1. 필드의 카드가 모자라면 뽑지 못하게 변경
# 2. 공개 필드에 있는 카드도 플레이어가 가진 카드가 배열 될때 맞춰서 배열되게 변경
# 3. "?"카드에도 색을 부여
# 4. 카드유추를 성공 했을 때 연속진행 할껀지 멈출껀지에 대한 선택지 제공

########################################################

############# 2020 09 22 패치 노트 ######################

# 1. 카드 생성 코드를 매우 단축함 과거에 비해 매우 효율적임
# 2. 공개 필드 카드도 배열을 추가하면서 카드 자체가 바뀌는 현상이 발생했으나 현재 수정후 없어짐
# 3. action함수를 없애고 분할하여 각각 따로 함수를 만듬

########################################################

############# 2020 09 23 핫픽스 ######################

# 1. 카드 생성 코드 단축화 과정에서 생긴 오류를 수정
# 2. 이전에 내가 플레이어 x의 몇번째 카드를 선택했었는지 알려주게 변경
# 3. 좀더 자주 패 상황을 보여주도록 변경

########################################################

import random
import numpy
import copy
import math

################################# 카드를 생성하는 함수

def make_spooky(x):
    global max_card_num
    max_card_num = 5
    min_loop_num = 2
    cut_num = list(range(0,math.ceil((max_card_num+1)/min_loop_num)-2))
    cut = []
    card_list = list(range(0,max_card_num+1))
    random.shuffle(card_list)
    while 1:
        cut1 = 3+random.choice(cut_num)
        cut.append(cut1)
        if sum(cut) == max_card_num + 1:
            break
        elif sum(cut) > max_card_num + 1:
            cut2 = cut.pop()
            if max_card_num + 1 - sum(cut) < 3:
                cut[len(cut)-1] += max_card_num + 1 - sum(cut) 
            else:
                cut.append(cut2)
                cut[len(cut)-1] = max_card_num + 1 - sum(cut)    
    card_num = list(numpy.zeros(len(cut))) 
    add_card_s = -cut[0]
    add_card_f = 0
    for i in range(0,len(cut)):
        card_num[i] = []
        add_card_s += cut[i] 
        add_card_f += cut[i]                   
        for k in range(add_card_s,add_card_f): 
            card_num[i].append(card_list[k])  
    for i in range(0,len(card_num)):
        for k in range(0,len(card_num[i])):   
            spooky_card_num = [card_num[i][k-1],card_num[i][k]] 
            x.append(spooky_card_num)
    return x           

############################################################################   게임 진행을 위한 함수지정
#   3) 정렬===============================================================

#   3-1) spooky 숫자 정렬-------------------------------------------------
def spooky_arrange(i):
    dummy = p[i]            # 임시 리스트 생성
    for k in list(range(0,len(dummy))): 
        if dummy[k][1][0] < dummy[k][1][1]: # 두 spooky 수 고려 작으면 놔둠 dummy[k][1][0] 의미: [k]: for문 [1]은 spooky [0]: spooky중 첫 째
            pass
        else:   # 다르면 교환 후 저장
            dummy[k][1][0], dummy[k][1][1] = dummy[k][1][1], dummy[k][1][0]
            p[i]= dummy

#   3-2) 평균값 정렬 및 색상 정렬 옵션----------------------------------------
color_arrange_on = 0 # 평균값 중복시 색상에 따라 배열 규칙을 추가할 것인가? [0: no, 1: use] # (GUI 처리 해야됨)
def tile_arrange(i):
    dummy = p[i]    #임시 리스트 생성
    for q in range(0,len(dummy)):   #총 길이만큼 교환 실행
        # print(q,"회 교환) 플레이어",i,"의 타일과 spooky 수", dummy) # 테스트용 주석처리입니다 삭제금지!!
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

def arrange(i): # 위의 spooky_arrange tile_arrange 함수 같이 실행 # 순서 중요
    spooky_arrange(i)
    tile_arrange(i)
    
# 턴넘기기 함수

def next_turn(i):
    global turn
    turn = i+1 # 턴을 다음 플레이어에게 넘김.
    if turn == pn+1:
        turn = 1

# 플레이어 지목 함수

def c_p():
    global choice_player
    while 1:                        # 플레이어를 지목하는 코드
        choice_player = float(input("맞추고 싶은 상대방을 고르세요:")) # 플레이어 수를 입력받아서 그에 맞게 선택지를 줌
        choice_player = int(choice_player)
        if choice_player > pn or choice_player < 1:
            print("그런 플레이어는 없습니다")
        elif len(p[choice_player-1]) == 0:
            print("그 플레이어는 카드가 없습니다")
        elif choice_player == turn:
            print("자신을 선택할 수 없습니다")
        elif choice_player <= pn and choice_player >= 1:
            print("플레이어",choice_player,"를 지목했습니다")
            break
        else:
            print("입력오류")

# 뽑는 카드 색깔 정하는 코드

def c_color():           
    global choice_color, recent_card
    ti_b = []  # 검은색을 뽑을건지 흰색을 뽑을건지 플레이어가 정함
    ti_w = []  # 그래서 따로 검은색 흰색 그룹을 생성
    for i in range(len(ti)-1):  # 검은색 흰색 그룹에 색에 맞게 넣음
        if ti[i][0] == 1:
            ti_b.append(ti[i])
        elif ti[i][0] == 0:
            ti_w.append(ti[i])
    while 1:
        if len(ti) != 0:
            choice_color = input("가져갈 카드의 색깔을 골라주세요 (b,w):")    # 검은색이면 검은색 뽑고 흰색이면 흰색 뽑게함
            if choice_color == "b" and len(ti_b) != 0:                      # 입력받은 색깔이 b,w에 따라 그에 맞는 색카드를
                recent_card = random.choice(ti_b)                           # 뽑고 패에 추가 최근 카드는 이후 틀렸을 때
                p[turn-1].append(recent_card)                               # 카드를 넘기기 위해 가져옴
                public_field[turn-1].append([1,"?"])
                ti.pop(ti.index(recent_card))   # 뽑은 카드를 다시 뽑으면 안되니 뽑은 카드는 필드에서 삭제함
                spooky_arrange(turn-1)          # 뽑았으니 재배열함
                tile_arrange(turn-1)
                break
            elif choice_color =="b" and len(ti_b) == 0:
                print("검은색 카드가 없습니다")
            elif choice_color == "w"and len(ti_w) != 0:
                recent_card = random.choice(ti_w)
                p[turn-1].append(recent_card)
                public_field[turn-1].append([0,"?"])
                ti.pop(ti.index(recent_card))   # 뽑은 카드를 다시 뽑으면 안되니 뽑은 카드는 필드에서 삭제함
                spooky_arrange(turn-1)          # 뽑았으니 재배열함
                tile_arrange(turn-1)
                break
            elif choice_color =="w" and len(ti_w) == 0:
                print("흰색 카드가 없습니다")
            else:
                print("입력오류")
        elif len(ti) == 0:
            print("더 이상 뽑을 카드가 없습니다 플레이어 지목 단계로 넘어갑니다.")
            break

# 지목한 플레이어의 카드 유추 코드

def c_card():            
    global choice_card
    while 1:                        # 지목한 플레이어의 카드를 지목하고 유추한 후 상황을 전개하는 코드
        if len(p[turn-1]) != stn + 1:
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
                collapse(turn,p[turn-1].index(recent_card)+1)       #미리 짜놓은 붕괴함수와 필드에 공개하는 함수를 사용
                public(turn,p[turn-1].index(recent_card)+1)
                break
            elif choice_num == p[choice_player-1][choice_card-1][1][0] or choice_num == p[choice_player-1][choice_card-1][1][1]:
                print("그런 숫자가 있습니다 룰에 따라 지목받은 플레이어는 카드를 붕괴합니다") #스포키 숫자 한개라도 맞춰서
                collapse(choice_player,choice_card)                                       # 상대가 어떻게 붕괴시킬지 고름
                if choice_num == collapse_num:                                            # 이 또한 미리 짜놓은 코드를 사용
                    print("숫자를 정확히 맞추셨습니다. 룰에 따라 카드를 공개합니다")
                    public(choice_player,choice_card)
                    while 1:
                        choice_turn = input("한번 더 맞추시겠습니까? (y/n):")
                        cpb = 0
                        if choice_turn == "y":
                            c_p()
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

def collapse(x,y): # x는 붕괴 권한이 있는 플레이어, y는 붕괴시킬 카드 번호
    global recent_collapse_num, collapse_num, recent_collapse_color
    while 1:
        print("플레이어",x,"는 붕괴시킬 숫자를 골라주세요")
        print("붕괴시킬 카드 :",p[x-1][y-1])
        print("나의 패 :",p[x-1])
        collapse_num = float(input("붕괴 숫자:"))       #붕괴 숫자를 받아서 붕괴시키고자 하는 카드의 번호와 비교 후 알맞는 숫자를 
        collapse_num = int(collapse_num)                #붕괴시킴
        if collapse_num == p[x-1][y-1][1][0]:
            p[x-1][y-1][1][1] = p[x-1][y-1][1][0]
            recent_collapse_num = p[x-1][y-1][1][0]     #최근 붕괴 숫자는 나중 연쇄 붕괴를 위해 가져옴
            recent_collapse_color = p[x-1][y-1][0]
            break
        elif collapse_num == p[x-1][y-1][1][1]:
            p[x-1][y-1][1][0] = p[x-1][y-1][1][1] 
            recent_collapse_num = p[x-1][y-1][1][1]
            recent_collapse_color = p[x-1][y-1][0]
            break
        else:
            print("입력오류")

# 전체적인 카드 붕괴

def overall_collapse(x,y): # 붕괴 숫자 x와 색깔 y를 넣으면 그와 관련된 카드들을 붕괴시킴
   print("컴퓨터가 판단해서 전체적으로 붕괴 할 것이 있으면 붕괴 시키겠습니다")
   global public_check
   for i in range(0,pn):
       for k in range(0,len(public_field[i])):
               if public_field[i][k][1] == "?":
                   public_field[i][k] = "?"
   public_check1 = copy.deepcopy(public_field) 
   public_check2 = copy.deepcopy(public_field)          #파이썬이 리스트 복사하는게 까탈스러워서 딮카피를 써야 복사한 리스트와
   omg = 0                                              #복사된 리스트가 서로 다른 주소를 할당 받아게 되어 이후 한쪽이 수정되어도
   while 1:                                             #다른쪽이 수정 안됨
       if public_check1[omg].count("?") == 0:            #공개 필드의 모름숫자는  ?로 함 omg는 플레이어 수임 예로 public_check[omg]
           omg += 1                                     #면 omg 숫자에 해당되는 플레이어 패를 검토중임
       if p[omg][public_check1[omg].index("?")][0] == y:   # 붕괴한 숫자와 색깔을 가져와서 플레이어 패를 하나하나 비교
           if p[omg][public_check1[omg].index("?")][1][0] == x:      #그래서 붕괴될께 있으면 붕괴하고 최근 붕괴 숫자를 최신화하고 
               p[omg][public_check1[omg].index("?")][1][0] = p[omg][public_check1[omg].index("?")][1][1] #처음부터 다시 스캔
               x = p[omg][public_check1[omg].index("?")][1][1]                                           # 반복
               public_check2[omg][public_check1[omg].index("?")] = "E"   # check 2,1 의 차이는 check1이 확인하면서 아닌거는 
               public_check1 = copy.deepcopy(public_check2)             # E로 표현하는데 붕괴 해야할 카드를 찾아버리면
               omg = 0                                                  # 처음부터 다시 스캔해야 하기 때문에 백업용으로
           elif p[omg][public_check1[omg].index("?")][1][1] == x:       # check2를 놔둠 그리고 붕괴한 카드는 check2에 E로 
               p[omg][public_check1[omg].index("?")][1][1] = p[omg][public_check1[omg].index("?")][1][0] #표현되어 다시 체크 할 일이 없음
               x = p[omg][public_check1[omg].index("?")][1][0]
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
       if omg == pn: # 모든 플레어의 패를 끝까지 다 훑었으면 정지 (즉 더이상 붕괴 시킬게 없으니 반복없이 브레이크로 옴)
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
make_spooky(field_black)
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

random.shuffle(ti)                  # 모든 타일 섞음
# 아래 ti는 테스트를 위한 임시 타일묶음으로 지우지 말아주세요!!
# ti = [[1, [3, 5]], [1, [1, 0]], [1, [4, 1]], [1, [2, 5]], [0, [1, 0]], [1, [2, 3]], [0, [3, 0]], [0, [2, 5]], [0, [4, 5]], [0, [3, 2]], [1, [0, 4]], [0, [4, 1]]]
print("섞은 전체 타일: ",ti)


#   2) 플레이어 수와 시작 타일 수 지정 및 배포=============================

#   2-1) 플레이어 수 지정--------------------------------------------------
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
before_choice_card = list(range(0,pn))
for i in range(0,pn):
    before_choice_card[i] = list(range(0,pn))
    for k in range(0,pn):
        before_choice_card[i][k] = 0


#   2-2) 타일수 지정--------------------------------------------------------
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
        if qwer[0] == 0:
            public_field[i].append([0,"?"]) # 공개 필드에 알수없는(?)카드를 추가
        elif qwer[0] == 1:
            public_field[i].append([1,"?"])
    
for i in list(range(0,pn)): # 플레이어 전체에 대해 스포키 수 배열
    arrange(i) # 위에 정의된 패를 정렬하는 함수
    print("결과) 플레이어",i+1,"의 타일과 spooky 수", p[i])

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
    c_color() # 검정, 흰색 색깔 결정 후 가져오는 것까지의 함수
    print("뽑은 후 플레이어",turn,"의 패:",p[turn-1])
    c_p() # 플레이어 지목
    c_card() # 카드 숫자 유추
    overall_collapse(recent_collapse_num,recent_collapse_color) # 전체적인 컴퓨터 오토 붕괴
    arrange(turn-1) # 재배열
    public_arrange() # 공개 필드도 맞춰서 재배열
    next_turn(turn) # 턴바꿈
    turn_count += 1 # 턴이 끝나서 카운트 추가
    if turn_count == 5: # 일단 게임 2번만 진행 # 실행 확인용 코드임 (추후 삭제)
        break
    


#   2$  끝)@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@