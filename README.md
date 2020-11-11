# QuantumCoda

Wecome to visit our repository! This repository is for **QuantumCoda (양자 다빈치 코드)** development. Our goal is making a new game including physics phenomenon on Capstone Design I Class at 2020 fall semester.

- 2020 PKNU Capstone Design
- Team "Explorer" repository
- Project: QuantumCoda (a.k.a Quantum Da Vinci Code '양자 다빈치 코드')
- Members: Jong hee Kim, Yong chul Lee, Yong Kwon, Sae hyeong Cho, Ji won Choi

We'll write recent development notes here. The notes can be written in Korean. If you want to watch previous update notes, see [Here](https://github.com/jiwonchoi-phys/QuantumCoda/tree/master/UpdateNotes)

## 1st Week ~ 4th Week
Update notes of 1st week to 4th week are now moved. See [Here](UpdateNotes/1st~4th.md).

## 5th Week (09.28~10.04)

### 200928 지원 패치노트
main_test.py에 대한 패치노트
- 카드 분배 후 카드 이미지 생성
- 숫자 노출 여부, 버튼 기능 추가 예정

### 201001 영철 패치노트
조커 없는 버전.py에 대한 패치노트
 1. 승패코드 근본 오류 수정
 2. 컴퓨터 오토 붕괴에서 뽑을 카드 더미는 붕괴 안하던 현상을 수정
 3. 아웃된 플레이어는 지목할 수 없도록 변경
 4. 모두 아웃 시켰을 때 더이상 게임을 진행 못하도록 해야함

### 201002 용 패치노트
조커 없는 버전.py에 대한 패치노트
1. next_turn 함수에서 패 모두 공개시 턴 넘김 메세지 출력
2. 승리시 게임 종료하도록 하는 것을 next_turn 함수에서 실행 되도록 옮김
3. c_p while문 앞에 플레이어 한명을 제외하고 패가 공개되면 게임 끝나도록 함

### 201002 지원 패치노트
util.py
1. tile_arrange()를 PLAYER 클래스 메서드로 추가
main_test.py
1. tile_arrange()를 통해 카드가 순서대로 배열되도록 수정
+++ 턴 넘기기, 플레이어 지목, 유추, 붕괴 등 알고리즘 이식 어케하노(상의가 필요함)


### 201003 종희 패치노트
조커 없는 버전.py에서 플레이 시 오류
1. 3인 플레이 시 상대가 내 패에 있는 2개의 숫자 중 하나를 맞췄을 경우, 내가 상대가 유추한 수가 아닌 다른 수로 붕괴시킬 시 
index out of range 에러가 뜨는 현상 발견 (현재 코드 상 뽑을 카드 더미에 카드가 없어서 오류 뜬 것으로 보임)
-> 해결함
2. 3인 플레이 시 연속해서 맞추려고 y를 입력했을 때 index out of range 에러가 뜸 -> 해결함
3. 3인 플레이 시 한 플레이어가 가지고 있는 카드 색이 카드 붕괴 후 갑자기 바뀌는 현상 (ex. b타일 1개 w타일 3개 -> 붕괴 후 b타일 2개 w타일 2개가 됨)
-> 해결함
4. 4인 플레이 시 플레이어 지목 후 에러 (192, 468줄 에러) -> 해결함

## 6th Week (10.05~10.11)

### 20201005 ~ 201006 세형 패치노트
main_test.py 및 util.py에 대한 패치노트
- 주석 추가
- 정렬 오류 수정(누락된 배열 조건 수정)

### 201007 종희 패치노트
조커 없는 버전.py
1. 카드 생성시 카드 수를 늘리면 무한 루프와 에러가 뜨던 현상을 수정

### 201007 지원 패치노트
GUI branch, util.py
- BUTTON 클래스 수정 (배경과 텍스트가 따로 놀던 현상 바로잡음)
- CARD 클래스에 버튼 기능 추가(각 카드별로 action을 줄 수 있도록)
카드 유추하는 과정을 action으로 넣어야 하는데 이건 조금 고민해봐야 할 듯.

## 7th Week (10.12~10.18)

## 8th Week (10.19~10.25)
Midterm Exam Week

## 9th Week (10.26~11.01)
Midterm Presentation

### 201030 용 패치노트
GUI branch, Button_(참고용).py
- 현재 버튼 클래스에 대해서 테스트 중이며 마우스 클릭에 대한 입력을 인식하는 코드를 Forking하여 분석중

## 10th Week (11.02~11.08)

### 20101104 용 패치노트
GUI branch, main_test.py
1. 버튼 작동여부 완전하게 확인, 다음 장면 전환이 가능하게 함. 예를 들면 인트로에서 게임화면으로 전환하는 것 등.
2. 버튼작동과 장면의 구분을 위해서, 기존의 루프를 포함해 '장면'을 모두 **함수 형태로 변경**. 함수 형태의 표준을 유지하기 위해 어떻게 맞추면 좋을지 주석을 추가.
3. 코드 재정렬. 순서도에 대해 main_test.py에 주석을 달아뒀음. 일단은 *'알고리즘 -> pygame 진행에 필요한 함수 -> 기본적인 pygame 실행'* 의 순서로 배치함. 

### 201106 용 패치노트
GUI branch, util.py
- 텍스트로 받아서 표준화된 위치로 정렬할 수 있게 함. 같은 위치에 버튼을 위치하는 경우 굳이 숫자 입력을 안해도 됨.

### 201107(09:10~19:15) 세형 패치노트
GUI branch: util.py, shtest.py, main_test.py

- main_test.py fcn, num_players, stn 등에서 충돌로 코드 순서 수정.
    > functions for pygame >> Initialize pygame 순서 고정 바람. 변동시 에러 발생.

- player # 함수 추가 및 오류 테스트 완. (2 ~ 4인 정상작동. 범위 이탈시 무한 루프)
    > 입력을 그림 클릭이 아닌 텍스트로 받게 설정.(붕괴 이후 시간나면 sprite 클릭인식 추가 예정)
    > 정상 수치 입력시 자동으로 창 닫힘 추가.

- starting tile # 입력 함수 추가 및 오류 테스트 완. (2 ~ 4인의 가능 범위 내 정상작동. 범위 이탈시 무한루프)
    > 가능한 모든 경우에서 타일 위치 자동으로 지정하게 설정(붕괴 구현 후 더 업데이트 예정) 및 오류 테스트 완.

- 턴넘김 버튼 구현 및 이상 없음 확인.
    > 턴함수 main_loop 함수 밖으로 빼지 말 것(util; impoer time 추가).
    > 턴의 플레이어 패 아래 고정. 상대 플레어 패 상대적인 위치 반영.
    > 턴수 위에 표기(기존 text와 곂침 발생 > 기존 text 배경색으로 지움).
    > 턴넘김 버튼 무한클릭 문제 delay 2초 걸어서 임시 해결.
    
- 가시성 강화
    > 폰트 글씨체 변경 consolas >> calibri
    > class CARD 폰트 크기 키움 15 >> 20

- 이론창의 이미지 삽입 정상 작동 확인.

### 201108~201109(15:00) 세형 패치노트
GUI branch: util.py, shtest.py, main_test.py

- util.py; CARD.get_color가 타일 그림색상을 출력하는 문제 해결. [ex. 회색 (201,201,201)]
    > 타일의 색상 숫자를 출력하게 수정 및 추가. [ex. 흰색: 0, 검정: 1]

- 필드에 남아있는 타일 색상 분류 함수 추가.
    > main_loop 함수 밖으로 빼지 말고, 위치도 고정할 것.
    > 남아있는 타일 색상에 따른 갯수 기록.

- 'take a tile' 버튼과 패를 먹는 함수 추가.
    > main_loop 함수 밖으로 빼지 말고, 위치도 고정할 것.
    > 버튼에 남아있는 수 표기.
    > 이미 이번 턴에 한개 먹었으면, 더 휙득 불가.
    > 0개 남은 타일 선택 불가.

- 플레이어가 가진 패의 수에 따라 상대적인 위치 지정.
    > 현재 임시로 max_spooky # = 5 인데 7 이상시 게임 화면 밖으로 타일이 나갈 수 있는 문제 발견.
        새로운 방식의 상대 패 표기방법 검토중..
    
- 게임 플레이시 메인음악 재생 추가.
    > 게임 끌때까지 반복.
    > 파일 다운 받을 것.

### 201111 세형 패치노트
GUI branch: util.py, main_test.py

- 나가는 버튼 카드 위치와 곂쳐 위로 올림. y값 200 > 50
    > 카드 최적의 위치 구상중..

- util.py; mak_spooky 함수 최신화
    > 따라서 CARD 클래스 확률 표기 추가.
    > 두 spooky 숫자가 모두 2자리 수일 때 카드 밖으로 텍스트 이탈.
        > 폰트 크기 수정 20 > 18
        > max_card_num = 13까지 문제 없으나 gui는 완성까지 10 고정 할 것.
        
TODO) 붕괴 관련 모든 것.
- 0. 처음 턴 누구(일단 생략. 플레이어 1고정.)
    > 생략.
- 1. 카드 휙득 및 패 추가함수 생성.
    > 1차 완성.
- 2. 각각의 카드 패 위에 누구의 패인지 텍스트 추가. (턴넘김시 타일위치 변경에 따라 같이 변경.)
    > 진행중.. (+ 상대 플레이어의 패 표기 위치 개선중..)

===================아래  진행 바람===============================================
- 4. 지목(플레이어를 지목 x. 바로 특정 플레이어의 카드 지목)시 추측 함수 생성 및 연결.
    > 1차. 해당 값에 타일의 spooky 수 유무 검토 있으면 해당 타일 붕괴.
    > 2치. 위의 타일의 붕괴에 따라 알고리즘 쪽 함수 가져와서 얽힌 타일 붕괴.