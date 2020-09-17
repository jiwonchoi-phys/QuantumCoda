import random
import numpy
card_num = [0,0,1,1,2,2,3,3,4,4,5,5]    #양자 번호
card = []
random.shuffle(card_num)

################################# 변수지정

field = []                              #뽑기전에 카드들이 놓여 있는 판
field_num = list(range(0,int(len(card_num)/2)))   #숫자 종류 내림차순
field_count = list(numpy.zeros(int(len(card_num)/2)))   
y = []                                  #1개의 패
loop_check = list(numpy.zeros(int(len(card_num)/2)))    #루프를 판별하기위한 배열 이 배열한에 같은 숫자가 있으면 그에 해당
loop_num = 1                                            #되는 숫자끼리 엮여있다

################################# 카드 뽑기

while 1:                                #1개의 패에 숫자 2개를 넣기
    while 1:
        loop_e = 0                      #에러 판별 숫자 0이면 에러 없고 1이면 에러 있다
        count_sum_1 = 0
        count_sum_2 = 0
        x = card_num.pop()              #임의로 숫자 뽑기
        x1 = card_num.pop()
        count_sum_1 = count_sum_1+field_count.count(1)  #뽑기 전 숫자 카운트 수
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
    field.append(y)                         #필드에 패를 추가함
    y = []
    count_sum_1_a = field_count.count(1)    #뽑은 후 숫자 카운트 수
    count_sum_2_a = field_count.count(2)
    if count_sum_1_a == count_sum_1 + 2:                #뽑기 전후의 숫자 카운트를 비교해서 현재 루프 상황을 알아보고
        loop_check[field_num.index(x)] = loop_num       #루프 상황을 최신화
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
            
    if len(card_num) == 2 and card_num[0] == card_num[1]:   # 루프에 제한을 거는 코드 제한 범위를 벗어나면 에러 숫자를 1 
        loop_e = 1                                          # 로 설정
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
        field = []                                              # 에러코드가 1이면 초기화를 하여 다시 뽑기 진행
        card_num = [0,0,1,1,2,2,3,3,4,4,5,5]
        random.shuffle(card_num)
        field_count = list(numpy.zeros(int(len(card_num)/2)))
        loop_check = list(numpy.zeros(int(len(card_num)/2)))
        loop_num = 1
    if len(card_num) == 0:              #패를 다 분배하면 멈춤
        break                             

print("field:",field)                   #필드는 패가 어떤식으로 분배 되어있는지를 보여주고
print("field_count",field_count)        #필드 카운트는 각 숫자가 몇번 나왔는지 보여주고
print("숫자:",field_num)                #숫자 밑에 있는 루프 숫자는 그 숫자에 해당되는 루프로 이 루프숫자가 같은 숫자
print("루프:",loop_check)               #끼리 엮여 있음

