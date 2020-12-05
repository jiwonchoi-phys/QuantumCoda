import random
import numpy

###################################### 변수 지정

two_player_first_handcard_num = 3                   #2명일 때 최초 뽑는 카드 숫자
three_player_first_handcard_num = 3                 #3명일 때 최초 뽑는 카드 숫자
four_player_first_handcard_num = 3                  #4명일 때 최초 뽑는 카드 숫자
player_num_max = 4                                  #최대 인원수
player_A_b = []                                     #각 플레이어들의 검(b),흰(w)카드 배열
player_A_w = []
player_B_b = []
player_B_w = []
player_C_b = []
player_C_w = []
player_D_b = []
player_D_w = []
BandW = ["B","W"]                                   #검은색을 뽑을 건지 흰색을 뽑을 건지 결정할 배열
add_card_count = 0                                  #그저 분배하기 위한 변수들
player_count = 0

###################################### 플레이어 수 결정

while 1:
    print("\033[32m"+"플레이 최소 인원은 2명이고 최대 인원은",player_num_max,"명 입니다"+"\033[0m")
    print("\033[32m"+"플레이어 수를 소수로 입력하면 앞에 있는 숫자로 결정됩니다. ex)2.5는 2명"+"\033[0m")
    player_num = float(input("플레이어 수를 입력해주세요:"))
    player_num = int(player_num)
    if player_num > player_num_max:
        print("\033[31m"+"플레이어 수가 너무 많습니다 다시 입력해주세요"+"\033[0m")
    elif player_num < 2:
        print("\033[31m"+"플레이어 수가 너무 적습니다 다시 입력해주세요"+"\033[0m")
    else:
        print("플레이어 수는",player_num,"명 으로 결정되었습니다")
        break
    
###################################### 첫 뽑는 카드수 결정

first_handcard_num = 0
if player_num == 2:
    first_handcard_num = two_player_first_handcard_num
elif player_num == 3:
    first_handcard_num = three_player_first_handcard_num
elif player_num == 4:
    first_handcard_num = four_player_first_handcard_num

#####################################  카드 분배

player_b = []                                                                       #그저 분배하기 위한 배열들
player_w = []

while 1:                                                                            #이 루프 구문은 각 플레이어에게 줄
    choose_color = random.choice(BandW)                                             #검정과 흰색 카드를 주기 쉽게 정렬
    if add_card_count == player_num*first_handcard_num:
        player_b.append("F")
        player_w.append("F")
        player_b.append("Q")
        player_w.append("Q")
        break
    if add_card_count == 0*first_handcard_num:
        player_b.append("A")
        player_w.append("A")
    elif add_card_count == 1*first_handcard_num:
        player_b.append("B")
        player_w.append("B")
    elif add_card_count == 2*first_handcard_num:
        player_b.append("C")
        player_w.append("C")
    elif add_card_count == 3*first_handcard_num:
        player_b.append("D")
        player_w.append("D")
    if len(field_black) == 0 and len(field_white) == 0:
        print("\033[31m"+"에러에러에러 뽑을 수 있는 카드가 없습니다"+"\033[0m")
    if choose_color == "B":
        if len(field_black) == 0:
            choose_color = "W"
        else:
            add_num = random.choice(field_black)
            player_b.append(add_num)
            field_black.pop(field_black.index(add_num))
    if choose_color == "W":
        if len(field_white) == 0:
            add_num = random.choice(field_black)
            player_b.append(add_num)
            field_black.pop(field_black.index(add_num))
        else:
            add_num = random.choice(field_white)
            player_w.append(add_num)
            field_white.pop(field_white.index(add_num))
    add_card_count += 1
    
add_card_count_1 = 0                                                                #그저 분배하기 위한 변수들
add_card_count_2 = 0
add_card_count_b = 0
add_card_count_w = 0
while 1:                                                                            #본격적인 분배 시작
    if player_b[add_card_count_1] == "A":
        if player_b[add_card_count_1+1] != "B" and player_b[add_card_count_1+1] != "F":
            add_card_count_b += 1
            player_A_b.append(player_b[add_card_count_b])
    if player_w[add_card_count_2] == "A":
        if player_w[add_card_count_2+1] != "B" and player_w[add_card_count_2+1] != "F":
            add_card_count_w += 1
            player_A_w.append(player_w[add_card_count_w])
    if player_b[add_card_count_b+1] == "B":
        add_card_count_b += 1
        add_card_count_1 = add_card_count_b
    if player_w[add_card_count_w+1] == "B":
        add_card_count_w += 1
        add_card_count_2 = add_card_count_w
    if player_b[add_card_count_1] == "B":
        if player_b[add_card_count_1+1] != "C" and player_b[add_card_count_1+1] != "F":
            add_card_count_b += 1
            player_B_b.append(player_b[add_card_count_b])
    if player_w[add_card_count_2] == "B":
        if player_w[add_card_count_2+1] != "C" and player_w[add_card_count_2+1] != "F":
            add_card_count_w += 1
            player_B_w.append(player_w[add_card_count_w])
    if player_b[add_card_count_b+1] == "C":
        add_card_count_b += 1
        add_card_count_1 = add_card_count_b
    if player_w[add_card_count_w+1] == "C":
        add_card_count_w += 1
        add_card_count_2 = add_card_count_w
    if player_b[add_card_count_1] == "C":
        if player_b[add_card_count_1+1] != "D" and player_b[add_card_count_1+1] != "F":
            add_card_count_b += 1
            player_C_b.append(player_b[add_card_count_b])
    if player_w[add_card_count_2] == "C":
        if player_w[add_card_count_2+1] != "D" and player_w[add_card_count_2+1] != "F":
            add_card_count_w += 1
            player_C_w.append(player_w[add_card_count_w])
    if player_b[add_card_count_b+1] == "D":
        add_card_count_b += 1
        add_card_count_1 = add_card_count_b
    if player_w[add_card_count_w+1] == "D":
        add_card_count_w += 1
        add_card_count_2 = add_card_count_w
    if player_b[add_card_count_1] == "D":
        if player_b[add_card_count_1+1] != "F":
            add_card_count_b += 1
            player_D_b.append(player_b[add_card_count_b])
    if player_w[add_card_count_2] == "D":
        if player_w[add_card_count_2+1] != "F":
            add_card_count_w += 1
            player_D_w.append(player_w[add_card_count_w])        
    if player_b[add_card_count_b+1] == "F":
        add_card_count_b += 1
        add_card_count_1 = add_card_count_b
    if player_w[add_card_count_w+1] == "F":
        add_card_count_w += 1
        add_card_count_2 = add_card_count_w
    if player_b[add_card_count_b+1] == "Q" and player_w[add_card_count_w+1] == "Q":
        break
print("A:","black:",player_A_b,"white:",player_A_w)
print("B:","black:",player_B_b,"white:",player_B_w)     
print("C:","black:",player_C_b,"white:",player_C_w)
print("D:","black:",player_D_b,"white:",player_D_w)  
    
