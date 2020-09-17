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
