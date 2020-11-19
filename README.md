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

## 12th Week (11.16~11.22)

### 201116~201117 용, 세형, 지원 패치노트
GUI branch: util.py, shtest.py, main_test.py 
    **>> New_main.py 하나로 통합.**(util.py와 main_test.py간 양방향 전달이 불가능 하기 때문)
용;
- 버튼 클릭 효과음 추가 완.
    > 기존 게임 메인루프 사운드, 클릭 사운드 추가됨. 앞으로 사운드는 **'.wav','.ogg'**파일 사용바람
- OS별 한글 출력 글꼴 자동 변화
    > Windows는 '맑은 고딕', macOS는 'Apple SD Gothic Neo', Linux는 'notosanscjkkr'이 기본 글꼴이 됨. 
    이들 글꼴은 모두 한글글꼴을 담고 있으며 만약 OS가 이것 이외이거나, 없는 경우에는 네이버의 '나눔고딕'이 기본임.

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
- 기존 모든 tk 영문화.

지원;
- 연쇄 붕괴
    > collapse_loop 함수 생성
    > spooky 넘버 생성시 루프 정보 저장하게 수정.

### 201118 용, 지원, 세형 패치노트
GUI branch, New_main.py

용;
- 도움말(How to Play)에 대한 위치 정렬 및 option room에 있던 이론 옮김
    > 도움말에는 이론, 게임규칙, 연습게임 세 가지 버튼이 추가되었으며, 이론은 Tk, 규칙은 Pygame PRINTTEXT,
    연습게임은 기존 게임 진행을 활용할 듯

지원;
- 루프 붕괴 (Collapse) 완료.
    > 더 이상의 버그가 발견되지 않으면 끝내도 될 듯
    
세형;
- 이론창에 대한 틀 Tk로 생성 완.
    > 이미지 크기 조절이 가능하게 함. (PIL 모듈이 추가로 필요해짐)
    > tkinter.ttk 에서 Notebook 도입. (해당 모듈 import)
    > option room에서 추가되었고 용이가 이론 부분을 도움말로 옮김(def theory_desc).
- point제 도입
    > PLAYER class는 point 정보를 포함.
    > 붕괴 실패 +2점, 붕괴 성공 & 추측 실패 + 10점, 붕괴 성공 & 추측 성공 +20점 (임시)
    > 3인 이상의 경우 최초 한명 탈락시 게임 끝낼 예정. 이후 1,2,3 등수는 포인트로 정산.
- 덱 리스트 위의 플레이어 정보 그리는 코드 경량화.
- 한 턴에 타일이 없어 휙득 못한 경우, 추측 실패시 먹지 않은 타일을 붕괴해야 했던 오류 수정.
- 배경음악 밎 버튼 사운드 활성화.
    > 음악 버튼함수 경량화 및 수정. (Music & Sound 구별 주의할 것. 아니면 버튼 클릭시 배경음 꺼짐.)

### 201119 용 패치노트
GUI branch, New_main.py

- 게임 도중 Exit 버튼 또는 창닫기 눌렀을 때 경고창을 띄우도록 생성
    > 경고창에서 Exit 버튼 한 번 더 눌러야 종료 가능. 일단은 게임 진행 도중에만 적용. 인트로 화면이나 도움말
    에는 도입하지 않았음.

### 201119~201120(02:00) 세형 패치노트
GUI branch, New_main.py

- 타일 클릭 붕괴 함수 중 중복 멘트 수정.

- New_main.py; 전체 함수 위치 정리 및 경량화.
    > 첫 구동함수 game_intro() 이외 모두 제거.
    > 기타 초기 변수들 사용되는 함수 내부로 이동.
    > 제작 돤성된 함수 Util-Test에서 Util로 이동.

- Notice system 도입.
    > 알림이 필요할 때 Notice 수정하여 사용.

- 음악 플레이 함수 개편 및 승리 음악 추가.
    > 음악은 New_main.py 최상위에서 정의.
    > 함수는 이름을 임력하여 해당 음악을 연속 재생하게 수정.
    > 현재 모든 음향 효과 주석처리로 음소거 상태.
    > 새 음악 파일 다운 받을 것.

- win-page 1차 완.
    > 현재 point와 rank가 player 기준으로 순서대로 정렬 됨. (이후 rank 기준으로 player, point 표기방법 구상중..)
    > 동일 점수가 있을시 고려하여 중복된 rank 등급 결정하게 수정.
    > 승리 페이지에서 배경음악 승리 음악으로 변경.
    > 승리 조건이 미구현 되어, main_loop 안에 버튼으로 접근(임시).

- 난이도 설정 인터페이스 구현 1차 완.
    > 팝업시 기존 체크 사항 정보를 가져오게 수정.
    > 내용 영문화 진행 예정.
    > 닫는 버튼 추가 예정.
    > 현재 색상 변경 사용여부만 게임함수와 연결 되어있음. (확률 보기 사용과 아이템 사용은 이후 연결 예정.)
    > 체크 정보는 'states' list에 저장 (수정 엄금).
    > 옵션룸 가던 버튼에 연결(임시).

- 색상 정렬 오류 수정
    > 두 spooky 숫자 모두 중복시 검정 타일이 왼쪽에 가게 의도하였으나 반대로 하양 타일이 왼쪽에 가던 현상 수정.
    > 난이도 설정 여부에 따라 on/off 되게 추가.
    > 붕괴된 타일(1개의 숫자)와 붕괴되지 않은 타일(2개의 숫자) 비교시 항상 붕괴된 타일이 오른쪽에 위치.

=============================================================================================
- TO-DO) >> 진행 중..
    > 용; 서버관련 작업. & 이론 팝업창 정리.    # 현재 중첩에 더미 텍스트 같이 복붙 됨.
    > 세형; 승리 페이지 및 난이도 팝업창 개선.
            기타 디버깅 및 CARD class에서 PLAYER class로 접근 방법 구상.
    > 지원; 오픈된 타일 클릭 막기(오픈 여부 나누는 선행작업 필요).  # 주말 까지(다음주 승리 페이지 연결 및 최종 디버깅 예정).
        > 오픈 여부 CARD class 확률란에 저장!!
    

## 13th Week (11.23~11.29)

## 14th Week (11.30~12.06)
