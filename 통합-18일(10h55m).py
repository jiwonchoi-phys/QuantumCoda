import random
import numpy

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

#게임 시작시 배분과 정열@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


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
    print("\033[32m"+"플레이 최소 인원은 2명이고 최대 인원은",player_num_max,"명 입니다"+"\033[0m")
    print("\033[32m"+"플레이어 수를 소수로 입력하면 앞에 있는 숫자로 결정됩니다. ex)2.5는 2명"+"\033[0m")
    pn = float(input("플레이어 수를 입력해주세요:"))
    pn = int(pn)
    if pn > player_num_max:
        print("\033[31m"+"플레이어 수가 너무 많습니다 다시 입력해주세요"+"\033[0m")
    elif pn < 2:
        print("\033[31m"+"플레이어 수가 너무 적습니다 다시 입력해주세요"+"\033[0m")
    else:
        print("플레이어 수가",pn,"명으로 결정되었습니다.")
        break
p = list(range(0,pn))   #플레이 묶음 생성

#   2-2) 타일수 지정---------------------------------------------------------
while 1:
    print("\033[32m"+"시작시 가져갈 초기 타일 수를 결정해 주세요(3 권장))"+"\033[0m")

    stn = float(input("스타팅 타일 수:"))
    stn = int(stn)
    if stn > fcn/pn:
        print("\033[31m"+"패를 나누기 위한 전체 타일 수가 부족합니다. 작은 수로 다시 입력해주세요"+"\033[0m")
    elif stn < 2:
        print("\033[31m"+"타일 수가 너무 적습니다 다시 입력해주세요"+"\033[0m")
    else:
        print("플레이어가 받는 타일 수가",stn,"개로 결정되었습니다.")
        break
    
for i in range(0,pn): # 플레이어 수만큼 리스트 생성
    p[i] = []
    for k in range(0,stn): #플레이어 리스트에 타일 배분
        p[i].append(ti[k+i*stn])
        

for i in list(range(0,pn)):
    print("player",i," 타일: ",p[i])


#   3) spooky 숫자 정렬===================================================
for i in list(range(0,pn)): # 플레이어 전체에 대해
    dummy = p[i]            #임시 리스트 생성
    for k in list(range(0,stn)):
        if dummy[k][1][0] < dummy[k][1][1]: # 두 spooky 수 고려 작으면 놔둠
            pass
        else:   #다르면 교환 후 저장
            dummy[k][1][0], dummy[k][1][1] = dummy[k][1][1], dummy[k][1][0]
            p[i]= dummy

for i in list(range(0,pn)):
    print("spooky 숫자 정렬 후) 플레이어",i," 타일", p[i])


#   4) 평균값 정렬========================================================
for q in range(0,stn+1):          #완전히 정렬 위해 반복 횟수 stn+1 수로 설정
    for i in list(range(0,pn)): # 플레이어 전체에 대해
        dummy = p[i]            #임시 리스트
        print(q,"회 교환) 플레이어",i,"의 타일과 spooky 수", dummy) #변경 확인
        for k in list(range(0,stn-1)):
            if dummy[k][1][0]+dummy[k][1][1] <= dummy[k+1][1][0]+dummy[k+1][1][1]: # 두 spooky 수 평균값 고려 작으면 놔둠
                if dummy[k][1][0]+dummy[k][1][1] == dummy[k+1][1][0]+dummy[k+1][1][1]: # 평균값 중복시 작은spooky 수 비교
                    if  dummy[k][1][0] < dummy[k+1][1][0]:
                        pass
                    else:
                        dummy[k+1], dummy[k] = dummy[k], dummy[k+1]
            else:   #다르면 교환 후 저장
                    dummy[k+1], dummy[k] = dummy[k], dummy[k+1]
                    p[i]= dummy

for i in list(range(0,pn)):
    print("후) 플레이어",i+1,"의 타일과 spooky 수", p[i])


#   끝)===================================================================

#TODO 1) 패를 먹은후 배열
#TODO 2) 붕괴 후 배열
#TODO 3) 타일 넘버 제한
#TODO 4) 정수로 입력받게 개선
#TODO 5) 평균값도 같고 spooky 숫자도 모두 같은 경우 생상으로 우선순위 설정 추가

