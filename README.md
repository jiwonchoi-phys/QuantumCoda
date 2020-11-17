# QuantumCoda

Wecome to visit our repository! This repository is for **QuantumCoda (양자 다빈치 코드)** development. Our goal is making a new game including physics phenomenon on Capstone Design I Class at 2020 fall semester.

- 2020 PKNU Capstone Design
- Team "Explorer" repository
- Project: QuantumCoda (a.k.a Quantum Da Vinci Code '양자 다빈치 코드')
- Members: Jong hee Kim, Yong chul Lee, Yong Kwon, Sae hyeong Cho, Ji won Choi

We'll write recent development notes here. The notes can be written in Korean. If you want to watch previous update notes, see [Here](https://github.com/jiwonchoi-phys/QuantumCoda/tree/master/UpdateNotes)

## 1st Week ~ 4th Week
Update notes of 1st week to 4th week are now moved. See [Here](UpdateNotes/1st~4th.md).

## 5th Week ~ 9th Week
Update notes of 5th week to 9th week are now moved. See [Here](UpdateNotes/5th~9th.md).

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

## 11th Week (11.09~11.15)

### 201111 세형 패치노트
GUI branch: util.py, main_test.py

- 나가는 버튼 카드 위치와 곂쳐 위로 올림. y값 200 > 50
    > 카드 최적의 위치 구상 완.

- util.py; make_spooky 함수 최신화.
    > 따라서 CARD 클래스 확률 표기 추가.
    > 두 spooky 숫자가 모두 2자리 수일 때 카드 밖으로 텍스트 이탈.
        > 폰트 크기 수정 20 > 18
    > max_card_num = 13까지 문제 없으나 gui는 완성까지 10 고정 할 것.

- 플레이어 수에 따른 타일 위치 지정 함수 생성 및 적용 완.
    > 플레이어 텍스트 위치 추가 완.

### 201113(15:00) 세형, 지원 패치노트
GUI branch: util.py, main_test.py

- 스크린 사이즈 키움.
    > 메인 루프 안의 버튼들 크기 사이즈에 따라 일반화.

- 음악 함수 주석처리. (임시)
- util; from tkinter import *

- 지목(플레이어를 지목 x. 바로 특정 플레이어의 카드 지목)시 추측 함수 생성 및 연결 1차 완.
    > 추측 숫자가 spooky 두 수에 대응하면 붕괴. (오픈 여부 주의!)
    > 추측 실패시 먹은 타일 붕괴 후 오픈 (구현중..)
    > 붕괴시 카드의 확률 표기 삭제.

- 정렬) 붕괴되어 하나로 고정된 값과 두개의 spooky 평균값을 비교하게 코드 수정.

### 201115 용 패치노트
GUI branch: util.py

- PRINTTEXT와 BUTTON 클래스에서 적용되는 폰트를 확인해야 함. 'notosanscjkkr'로 변경하였음.
    > 사용하는 폰트가 한글지원이 안되면 제대로된 텍스트가 나오지 않는 문제가 발생함. 윈도우, 리눅스(우분투) 상에서 기본 한글
    폰트 출력을 어떤걸로 해야할지 결정해야 할듯.
    
Server
- 서버 컴퓨터를 수령하였고 서버 - 클라이언트간 따로 테스트 중.

### 201116 용, 세형, 지원 패치노트
GUI branch: util.py, shtest.py, main_test.py 

    >> New_main.py 하나로 통합. (util.py와 main_test.py간 양방향 전달이 불가능 하기 때문)

### 201117 용, 세형, 지원 패치노트
GUI branch: New_main.py

용;
- 버튼 클릭 효과음 추가 완.
    > 기존 게임 메인루프 사운드, 클릭 사운드 추가됨. 앞으로 사운드는 **'.wav','.ogg'**파일 사용바람
- OS별 한글 출력 글꼴 자동 변화
    > Windows는 '맑은 고딕', macOS는 'Apple SD Gothic Neo', Linux는 'notosanscjkkr'이 기본 글꼴이 됨. 이들 글꼴은 모두 한글글꼴을 담고 있으며
    만약 OS가 이것 이외이거나, 없는 경우에는 네이버의 '나눔고딕'이 기본임.

세형;
- 한 턴에 순서 정리.
    > main_loop;f_next_turn; 자신의 턴에 타일 안먹으면 턴넘김 불가. (텍스트 출력) 
    > main_loop;f_next_turn; 자신의 턴에 타일 먹어도 상대방 타일 추측안하면 턴넘김 불가. (텍스트 출력)
    > class CARD; 타일 먹고 추측할 때, 내 타일 클릭 안되게 수정.
    > class CARD; 타일 안먹으면 추측 못하게 수정.
    > class CARD; 추측 실패시 더 추측 못하게 수정.
    > class CARD; 필드에 타일이 없어서 못먹은 경우 바로 추측 가능하게 설정.
    > main_loop;f_next_turn; 추측 성공시 또는 추측 실패시에만 턴넘김 버튼 활성화 되게 수정.

- option room 기타 정리.
    > 버튼 위치 및 이름 수정
    > 이론 팝업창 내용 텍스트 왼쪽에 붙여 쓰게 수정.
    > 체크박스 팝업창 임시 생성. (체크 기록 저장하지 못하는 문제 발견 txt 등에 저장, 불러오기 상용 해야할 듯)

지원;
- 연쇄 붕괴
    > collapse_loop 함수 생성
    > spooky 넘버 생성시 루프 정보 저장하게 수정.

- TO-DO)
    > 용; 서버관련 작업 & 승리시 페이지 구현 및 승리 조건 >> 진행 중..
    > 세형; 오픈된 타일 클릭 막기(오픈 여부 나누는 선행작업 필요). & 이론 및 난의도 팝업창 정리. >> 진행 중..
    > 지원; (연쇄 붕괴) 얽힌 타일 붕괴. >> 진행 중..
    
- 1. 붕괴;
    > 2차(지원). (연쇄 붕괴) 위의 타일의 붕괴에 따라 알고리즘 함수 생성 및 얽힌 타일 붕괴. >> 진행 중..
    > 2차(세형). 유추 실패시 먹은 타일 붕괴 후 지원이 함수에 연결 >> 진행 중..

## 13th Week (11.16~11.22)

## 14th Week (11.23~11.29)

## 15th Week (11.30~12.06)
