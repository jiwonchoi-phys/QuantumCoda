import random
import numpy
import copy

################################# 카드 숫자를 색깔별로 2개씩 창조

max_card_num = 5
card_num_kind = list(range(0,max_card_num+1))
card_num = []    #양자 번호
for i in range(0,max_card_num+1):
    card_num.append(card_num_kind[i])
    card_num.append(card_num_kind[i])
random.shuffle(card_num)

################################# 변수지정

field_black = []
field_white = []                             #뽑기전에 카드들이 놓여 있는 판
field_num = list(range(0,max_card_num+1))   #숫자 종류 내림차순
field_count = list(numpy.zeros(max_card_num+1))   
y = []                                  #1개의 패
loop_check = list(numpy.zeros(max_card_num+1))
loop_num = 1

################################# 카드 뽑기

reset_card_num = card_num

while 1:                                #1개의 패에 숫자 2개를 넣기
    while 1:
        loop_e = 0                      #에러 판별 숫자 0이면 에러 없고 1이면 에러 있다
        count_sum_1 = 0
        count_sum_2 = 0
        x = card_num.pop()              #임의로 숫자 뽑기
        x1 = card_num.pop()
        count_sum_1 = count_sum_1+field_count.count(1)
        count_sum_2 = count_sum_2+field_count.count(2)
        if x == x1:                     #같은 수를 뽑았을 때 대처
            card_num.append(x)
            card_num.append(x1)
            random.shuffle(card_num)
            loop_e = 1
        if loop_e == 0:                          #나온 숫자의 개수를 카운트 하고  패에 뽑은 숫자 2개를 추가
            field_count[field_num.index(x)] += 1
            field_count[field_num.index(x1)] += 1
            y.append(x)
            y.append(x1)
            break
    if len(field_black) == max_card_num +1:                             #필드에 패를 추가함
        field_white.append(y)
    elif len(field_white) == 0:
        field_black.append(y)
    if len(field_black) == max_card_num +1 and len(field_white) == 0:
        loop_e = 1                   
    y = []
    count_sum_1_a = field_count.count(1) 
    count_sum_2_a = field_count.count(2)
    if count_sum_1_a == count_sum_1 + 2:
        loop_check[field_num.index(x)] = loop_num
        loop_check[field_num.index(x1)] = loop_num
        loop_num += 1
    elif count_sum_2_a == count_sum_2 + 1:
        if field_count[field_num.index(x)] == 2 and field_count[field_num.index(x1)] != 2:
            loop_check[field_num.index(x1)] = loop_check[field_num.index(x)]
        elif field_count[field_num.index(x1)] == 2 and field_count[field_num.index(x)] != 2:
            loop_check[field_num.index(x)] = loop_check[field_num.index(x1)]
    else:
        x1_loop_num = loop_check[field_num.index(x1)]
        check_num = 0
        while 1:
            if check_num == len(loop_check):
                break
            if loop_check[check_num] == x1_loop_num:
                loop_check[check_num] = loop_check[field_num.index(x)]
            check_num += 1
            
    if len(card_num) == 2 and card_num[0] == card_num[1]:   # 무힌 루프에 빠지지 않게 하기위해 무한 루프에 빠지는 
        loop_e = 1
    if loop_check.count(0) == 0:
        loop_max_num = max(loop_check)
        max_count = 0
        while 1:
            if loop_check.count(loop_max_num - max_count) == len(loop_check):
                loop_e = 1
            elif loop_check.count(loop_max_num - max_count) == 2:
                loop_e = 1
            max_count += 1
            if max_count == loop_max_num:
                break
    if loop_e == 1:
        if len(field_black) != max_card_num + 1:                                              # 조건이 오면 초기화를 시킴
            field_black = []
        elif len(field_black) == max_card_num + 1:
            field_white = []
        card_num = []    
        for i in range(0,max_card_num+1):
            card_num.append(card_num_kind[i])
            card_num.append(card_num_kind[i])
        random.shuffle(card_num)
        field_count = list(numpy.zeros(max_card_num+1))
        loop_check = list(numpy.zeros(max_card_num+1))
        loop_num = 1
    if len(field_black) == max_card_num + 1 and len(field_white) == max_card_num + 1:              #패를 다 분배하면 멈춤
        break                             

print("field black:",field_black)
print("field white:",field_white)
print("field_count",field_count)
print("숫자:",field_num)
print("루프:",loop_check)

#   1$ 게임 시작시 배분과 정열@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


#   1) 타일에 색상 정보 추가 및 섞기======================================
tb = list(range(0,max_card_num+1))  #타일 블랙: 검은 타일 묶음 생성
tw = list(range(0,max_card_num+1))  #타일 화이트

fcn=(max_card_num+1)*2              #full card number

ti = []                             #전체 타일 묶음

for i in range(0,max_card_num+1):   #색상 정보 추가 (검정 1, 흰색 0)
    tb[i]=[1,field_black[i]]
    tw[i]=[0,field_white[i]]
    ti.append(tb[i])
    ti.append(tw[i])

random.shuffle(ti)                  #모든 타일 섞음
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
p = list(range(0,pn))   #플레이 묶음 생성
public_field = list(range(0,pn))  #공개된 카드 필드

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
    p[i] = []
    public_field[i] = []
    for k in range(0,stn): #플레이어 리스트에 타일 배분
        qwer = random.choice(ti)
        p[i].append(qwer)
        ti.pop(ti.index(qwer))
        public_field[i].append("?") # 공개 필드에 알수없는(?)카드를 추가
    
############################################################################   게임 진행을 위한 함수지정
#   3) 정렬===============================================================

#   3-1) spooky 숫자 정렬-------------------------------------------------
def spooky_arrange(i):
    dummy = p[i]            #임시 리스트 생성
    for k in list(range(0,len(dummy))): 
        if dummy[k][1][0] < dummy[k][1][1]: # 두 spooky 수 고려 작으면 놔둠
            pass
        else:   #다르면 교환 후 저장
            dummy[k][1][0], dummy[k][1][1] = dummy[k][1][1], dummy[k][1][0]
            p[i]= dummy


#   3-2) 평균값 정렬-------------------------------------------------------
turn_n = 0                          #턴 수, 2$-2) 참고

def tile_arrange(i):
    dummy = p[i]    #임시 리스트 생성
    for q in range(0,len(dummy)):   #총 길이만큼 교환 실행
        for k in list(range(0,len(dummy)-1)):   #모든 원소에 대해
            if dummy[k][1][0]+dummy[k][1][1] <= dummy[k+1][1][0]+dummy[k+1][1][1]: # 두 spooky 수 평균값 고려 작으면 놔둠
                if dummy[k][1][0]+dummy[k][1][1] == dummy[k+1][1][0]+dummy[k+1][1][1]: # 평균값 중복시 작은spooky 수 비교
                    if  dummy[k][1][0] < dummy[k+1][1][0]:
                        pass
                    else:
                        dummy[k+1], dummy[k] = dummy[k], dummy[k+1]
            else:   #다르면 교환 후 저장
                    dummy[k+1], dummy[k] = dummy[k], dummy[k+1]
                    p[i]= dummy

# 턴넘기기 함수

def next_turn(i):
    global turn
    turn = i+1 # 턴을 다음 플레이어에게 넘김.
    if turn == pn+1:
        turn = 1

# 전체적인 진행 함수

def action(turn):                                                               
    global choice_player, choice_card
    print("플레이어",turn,"차례 입니다")
    ti_b = []  # 검은색을 뽑을건지 흰색을 뽑을건지 플레이어가 정함
    ti_w = []  # 그래서 따로 검은색 흰색 그룹을 생성
    for i in range(len(ti)-1):  # 검은색 흰색 그룹에 색에 맞게 넣음
        if ti[i][0] == 1:
            ti_b.append(ti[i])
        elif ti[i][0] == 0:
            ti_w.append(ti[i])
    while 1:
        choice_color = input("가져갈 카드의 색깔을 골라주세요 (b,w):")    # 검은색이면 검은색 뽑고 흰색이면 흰색 뽑게함
        if choice_color == "b":                                         # 입력받은 색깔이 b,w에 따라 그에 맞는 색카드를
            recent_card = random.choice(ti_b)                           # 뽑고 패에 추가 최근 카드는 이후 틀렸을 때
            p[turn-1].append(recent_card)                               # 카드를 넘기기 위해 가져옴
            public_field[turn-1].append("?")
            break
        elif choice_color == "w":
            recent_card = random.choice(ti_w)
            p[turn-1].append(recent_card)
            public_field[turn-1].append("?")
            break
        else:
            print("입력오류")
    ti.pop(ti.index(recent_card))   # 뽑은 카드를 다시 뽑으면 안되니 뽑은 카드는 필드에서 삭제함
    spooky_arrange(turn-1)          # 뽑았으니 재배열함
    tile_arrange(turn-1)
    print("뽑은 후 플레이어",turn,"의 패:",p[turn-1])
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
    while 1:                        # 지목한 플레이어의 카드를 지목하고 유추한 후 상황을 전개하는 코드
        print("플레이어",choice_player,"의 패:",public_field[choice_player-1])
        choice_card = float(input("맟추고 싶은 카드 번호를 고르세요 상대방 기준 왼쪽부터 1번입니다:"))     # 이제 카드를 고르게 하고
        choice_card = int(choice_card)                                                                 # 제대로 골랐는지 확인함
        if choice_card > len(p[choice_player-1]) or choice_card < 1:
            print("존재하지 않는 카드입니다")
        elif public_field[choice_player-1][choice_card-1] != "?":
            print("그 카드는 이미 공개되었습니다")
        elif choice_card <= len(p[choice_player-1]) or choice_card >= 1:
            print(choice_card,"번째 카드를 선택했습니다")
            choice_num = float(input("그 카드의 숫자는 무엇입니까:"))       # 제대로 골랐으니 숫자를 찍어라 함 
            choice_num = int(choice_num)                                  # 유추한 다음 룰에 맞게 상황을 조정
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
                    break
                elif choice_num != collapse_num:
                    print("유추한 숫자로 붕괴하지 않았습니다 룰에 따라 아무런 조치없이 넘어갑니다")
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
          break
           
# 카드 공개 함수

def public(x,y): # 카드 공개 함수, 공개될 플레이어 x의 y카드를 공개
    public_field[x-1][y-1] = p[x-1][y-1]
    public_field[x-1][y-1][1][0] = collapse_num
    public_field[x-1][y-1][1][1] = collapse_num
    print("붕괴 후 플레이어",x,"의 패:",public_field[x-1])


################################################################################# 게임 진행

for i in list(range(0,pn)): # 플레이어 전체에 대해 스포키 수 배열
    spooky_arrange(i)

for i in list(range(0,pn)): # 플레이어 전체에 대해 타일을 배열
    tile_arrange(i)
    print("결과) 플레이어",i+1,"의 타일과 spooky 수", p[i])

while 1: # 순서 정하기
    print("오름차순으로 턴을 결정합니다. 먼저 플레이할 플레이어를 지정해주세요 (ex 1: 플레이어 1)")
    turn = float(input("먼저 시작할 플레이어 설정: "))
    turn= int(turn)
    if turn > pn:
        print("존재하지 않는 플레이어 번호입니다. 다시 입력해주세요")
    elif turn < 1:
        print("존재하지 않는 플레이어 번호입니다. 다시 입력해주세요")
    else:
        print("첫 턴의 플레이어가",turn,"으로 결정 되었습니다.")
        break

turn_count = 0
while 1:
    action(turn) # 게임 1번 진행
    overall_collapse(recent_collapse_num,recent_collapse_color) # 전체적인 컴퓨터 오토 붕괴
    spooky_arrange(turn-1) # 재배열
    tile_arrange(turn-1)
    next_turn(turn) # 턴바꿈
    turn_count += 1
    if turn_count == 2: # 일단 게임 2번만 진행
        break


# 상대 숫자 맞추는 코드 시작

# 상대 숫자 맞추는 코드 > 붕괴 코드  끝


    


#   2$  끝)@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
