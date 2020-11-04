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