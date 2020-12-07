# QuantumCoda

Wecome to visit our repository! This repository is for **QuantumCoda (양자 다빈치 코드)** development. Our goal is making a new game including physics phenomenon on Capstone Design I Class at 2020 fall semester.

- 2020 PKNU Capstone Design
- Team "Explorer" repository
- Project: QuantumCoda (a.k.a Quantum Da Vinci Code '양자 다빈치 코드')
- Members: Jong hee Kim, Yong chul Lee, Yong Kwon, Sae hyeong Cho, Ji won Choi

# Download: v0.12

Now we released QuantumCoda version 0.12. This version is currently test version so we focused on being able to play the QuantumCoda. 

**[Download](https://github.com/jiwonchoi-phys/QuantumCoda/releases)**

Download latest version on zip file from **'Assets'**

You can play our game in English and Korean. 

게임 언어는 영어와 한국어로 제공됩니다.

## System Requirements
- Windows 10, Linux (Ubuntu) (We tested only two OS. It will probably run on macOS too.)
    > **FOR WSL USERS**; If you want to run our game you'll need to set X11 Forwarding and PulseAudio to send GUI & audio information to your PC. If you not set them, you can not run the game due to an interpreter error.
- Python 3.8.5
- Python Modules
    > Pygame
    >> maybe you'll need to install using pip.
    >
    > Python tkinter, Pillow
    >> maybe you'll need to install this module if you are Linux user. Turn on the bash and type 'apt install python3-tk'. With same context type 'pip3 install pillow' using pip.
    >
    > math, random, numpy, time, platform
    >> This modules are provided by python. If the modules are not installed, use pip to get modules.
- System fonts (for Korean Users)
    > Windows: 'Calibri' or 'malgungothic'
    >
    > macOS: 'AppleSDGothicNeo'
    >
    > Linux: 'notosanscjkkr'

    If you don't have the fonts above in your PC then written words in Hangul may look broken. Sure, there is no problem with running the game.

## Release Notes
### v0.12
* Single Player game
    - Now you can control the volume of background music. Use arrow keys on your keyboard (Up arrow: Turn up the Volume, Down arrow: Turn down the Volume, Left arrow: Pause, Right arrow: Play).
* System
    - Modified a text position on the win page.
    - Fixed an issue where the new game button function was incorrectly linked on the win page.

## QuantumCoda Legacy
You can play the CLI-based version of Quantum Coda. Just download 'QCodalegacy.py (No joker card version)' then execute the file. this game used only 4 modules - random, numpy, copy, math. But the game is available in Korean only.

CLI 기반의 Quantum Coda를 즐겨볼 수 있습니다. 현재 브랜치에 있는 'Qcodalegacy.py'를 다운로드 하고 실행하면 됩니다. 또한 GUI 버전에 비해서 요구하는 모듈은 단지 random, numpy, copy, math 밖에 없어 쾌적하게 게임할 수 있습니다. 이 게임은 한국어로만 제공됩니다.

# Development Notes

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
    >
    > 정상 수치 입력시 자동으로 창 닫힘 추가.
- starting tile # 입력 함수 추가 및 오류 테스트 완. (2 ~ 4인의 가능 범위 내 정상작동. 범위 이탈시 무한루프)
    > 가능한 모든 경우에서 타일 위치 자동으로 지정하게 설정(붕괴 구현 후 더 업데이트 예정) 및 오류 테스트 완.
- 턴넘김 버튼 구현 및 이상 없음 확인.
    > 턴함수 main_loop 함수 밖으로 빼지 말 것(util; impoer time 추가).
    >
    > 턴의 플레이어 패 아래 고정. 상대 플레어 패 상대적인 위치 반영.
    >
    > 턴수 위에 표기(기존 text와 곂침 발생 > 기존 text 배경색으로 지움).
    >
    > 턴넘김 버튼 무한클릭 문제 delay 2초 걸어서 임시 해결.   
- 가시성 강화
    > 폰트 글씨체 변경 consolas >> calibri
    >
    > class CARD 폰트 크기 키움 15 >> 20
- 이론창의 이미지 삽입 정상 작동 확인.

### 201108~201109(15:00) 세형 패치노트
GUI branch: util.py, shtest.py, main_test.py

- util.py; CARD.get_color가 타일 그림색상을 출력하는 문제 해결. [ex. 회색 (201,201,201)]
    > 타일의 색상 숫자를 출력하게 수정 및 추가. [ex. 흰색: 0, 검정: 1]
- 필드에 남아있는 타일 색상 분류 함수 추가.
    > main_loop 함수 밖으로 빼지 말고, 위치도 고정할 것.
    >
    > 남아있는 타일 색상에 따른 갯수 기록.
- 'take a tile' 버튼과 패를 먹는 함수 추가.
    > main_loop 함수 밖으로 빼지 말고, 위치도 고정할 것.
    >
    > 버튼에 남아있는 수 표기.
    >
    > 이미 이번 턴에 한개 먹었으면, 더 휙득 불가.
    >
    > 0개 남은 타일 선택 불가.
- 플레이어가 가진 패의 수에 따라 상대적인 위치 지정.
    > 현재 임시로 max_spooky # = 5 인데 7 이상시 게임 화면 밖으로 타일이 나갈 수 있는 문제 발견.
        새로운 방식의 상대 패 표기방법 검토중..  
- 게임 플레이시 메인음악 재생 추가.
    > 게임 끌때까지 반복.
    >
    > 파일 다운 받을 것.

## 11th Week (11.09~11.15)

### 201111 세형 패치노트
GUI branch: util.py, main_test.py

- 나가는 버튼 카드 위치와 곂쳐 위로 올림. y값 200 > 50
    > 카드 최적의 위치 구상 완.
- util.py; make_spooky 함수 최신화.
    > 따라서 CARD 클래스 확률 표기 추가.
    >
    > 두 spooky 숫자가 모두 2자리 수일 때 카드 밖으로 텍스트 이탈.
    >
    > 폰트 크기 수정 20 > 18
    >
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
    >
    > 추측 실패시 먹은 타일 붕괴 후 오픈 (구현중..)
    >
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
    >
    > main_loop;f_next_turn; 자신의 턴에 타일 먹어도 상대방 타일 추측안하면 턴넘김 불가. (텍스트 출력)
    >
    > class CARD; 타일 먹고 추측할 때, 내 타일 클릭 안되게 수정.
    >
    > class CARD; 타일 안먹으면 추측 못하게 수정.
    >
    > class CARD; 추측 실패시 더 추측 못하게 수정.
    >
    > class CARD; 필드에 타일이 없어서 못먹은 경우 바로 추측 가능하게 설정.
    >
    > main_loop;f_next_turn; 추측 성공시 또는 추측 실패시에만 턴넘김 버튼 활성화 되게 수정.
- option room 기타 정리.
    > 버튼 위치 및 이름 수정
    >
    > 이론 팝업창 내용 텍스트 왼쪽에 붙여 쓰게 수정.
    >
    > 체크박스 팝업창 임시 생성. (체크 기록 저장하지 못하는 문제 발견 txt 등에 저장, 불러오기 상용 해야할 듯)
- 기존 모든 tk 영문화.

지원;
- 연쇄 붕괴
    > collapse_loop 함수 생성
    >
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
    >
    > tkinter.ttk 에서 Notebook 도입. (해당 모듈 import)
    >
    > option room에서 추가되었고 용이가 이론 부분을 도움말로 옮김(def theory_desc).
- point제 도입
    > PLAYER class는 point 정보를 포함.
    >
    > 붕괴 실패 +2점, 붕괴 성공 & 추측 실패 + 10점, 붕괴 성공 & 추측 성공 +20점 (임시)
    >
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
    >
    > 기타 초기 변수들 사용되는 함수 내부로 이동.
    >
    > 제작 완성된 함수 Util-Test에서 Util로 이동.
- Notice system 도입.
    > 알림이 필요할 때 Notice 수정하여 사용.
- 음악 플레이 함수 개편 및 승리 음악 추가.
    > 음악은 New_main.py 최상위에서 정의.
    >
    > 함수는 이름을 임력하여 해당 음악을 연속 재생하게 수정.
    >
    > 현재 모든 음향 효과 주석처리로 음소거 상태.
    >
    > 새 음악 파일 다운 받을 것.
- win-page 1차 완.
    > 현재 point와 rank가 player 기준으로 순서대로 정렬 됨. (이후 rank 기준으로 player, point 표기방법 구상중..)
    >
    > 동일 점수가 있을시 고려하여 중복된 rank 등급 결정하게 수정.
    >
    > 승리 페이지에서 배경음악 승리 음악으로 변경.
    >
    > 승리 조건이 미구현 되어, main_loop 안에 버튼으로 접근(임시).
- 난이도 설정 인터페이스 구현 1차 완.
    > 팝업시 기존 체크 사항 정보를 가져오게 수정.
    >
    > 내용 영문화 진행 예정.
    >
    > 닫는 버튼 추가 예정.
    >
    > 현재 색상 변경 사용여부만 게임함수와 연결 되어있음. (확률 보기 사용과 아이템 사용은 이후 연결 예정.)
    >
    > 체크 정보는 'states' list에 저장 (수정 엄금).
    >
    > 옵션룸 가던 버튼에 연결(임시).
- 색상 정렬 오류 수정
    > 두 spooky 숫자 모두 중복시 검정 타일이 왼쪽에 가게 의도하였으나 반대로 하양 타일이 왼쪽에 가던 현상 수정.
    >
    > 난이도 설정 여부에 따라 on/off 되게 추가.
    >
    > 붕괴된 타일(1개의 숫자)와 붕괴되지 않은 타일(2개의 숫자) 비교시 항상 붕괴된 타일이 오른쪽에 위치.

### 201120 용 패치노트
server branch, server.py, client.py, player.py, network.py

- 서버 관련 파일 작업을 게임에 연동하기 위해, server branch 새로 생성
- 실질적인 네트워크 플레이로 필요한 파일들은 player.py를 제외한 파일
- 2인 플레이어는 코드에 적용하면 되겠지만 3인 플레이 이상은 어떻게 할지 테스트 중

### 201120(14:00) 세형 패치노트
GUI branch, New_main.py

- **게임 1차 완성**
- 승리 조건 함수(f_end_conditions) 생성 및 적용.
    > 한 플레이어의 모든 패가 오픈될 경우 게임을 끝냄.
- 모든 음악 활성화.
- Notice 활성화 되지 않는 문제 수정.
    > 첫 값 선언 main_loop 함수 밖으로 이동.
- 포인트 수치 변경.
    > 붕괴 실패 +20점, 붕괴 성공 & 추측 실패 + 100점, 붕괴 성공 & 추측 성공 +200점.
- 붕괴 되었으나 오픈은 되지 않은 카드를 추측하는 경우, 정상적으로 진행 되지 않던 오류 수정.
    > 추측 수로 하나 남은 수도 맞추면 오픈하게 함.
    >
    > 틀리면 자신이 먹은 타일 붕괴(타일이 없어 턴 시작시 먹은 것 없으면 생략).
- 난이도 설정 중 상대방 확률 보기 on/off 기능 게임 내 연결.
- 기타 게임룰 적용.
    > 난이도 설정 중 상대방 확률 보기 on 시 상대방 확률 표기.
    >
    > 내 확률은 상시 표기.
    >
    > 내 숫자는 상시 표기.
    >
    > 오픈된 숫자는 'opened' 텍스트와 숫자를 함께 모두에게 표기.
    >
    > 붕괴 되었으나 오픈은 되지 않은 타일은 '붕괴' 로 표기 예정.    
- 관련하여 이제 타일 숫자가 안보여 테스트에 어려움이 있을 수 있으므로 클릭시 tk상에서는 정상적으로 숫자 표기 허용 함(디버깅용).
    > 붕괴 되었으나 오픈은 되지 않은 타일를 추측하는 경우, 하나의 숫자에  확률이 2개 표시 되는 문제가 있으나 100확률로 정상 붕괴됨. (수정 예정.)

### 201120(24:00) 세형, 지원 패치노트
GUI branch, New_main.py

- 불필요한 코드 삭제 및 주석 추가.
- 붕괴된 타일 숫자 아래 붕괴 여부 표기 추가.
- 추측 실패시, 이번턴에 먹은 타일이 붕괴된 타일인 경우 발생하던 문제 수정.
    > 추측에 성공하였으나 내가 먹은 타일이랑 루프라 먹은 타일이 붕괴되어 일으키던 문제 동일.
- 추측 성공하여 연속 추측시, 지목한 타일의 숫자가 아닌(틀린 수) 입력 불가능한 문제 수정.
- 음악 재생 함수 볼륨값도 입력받아 적용하게 수정.

### 201120 알고리즘 패치노트
ability_main.py

- 진행중인 GUI 코드에 능력을 추가
    > 능력 : 1.평균 보여주기, 2.차이 보여주기, 3.침묵, 4.유추한 대로 붕괴

### 201121 알고리즘 패치노트
ability_main.py

- 디자인의 변화 (배경, 폰트, 버튼 컬러 변경), 음악 재선정

- 능력 추가
    > 5.확률 보여주기, 6. 카드 1장 뽑기
    
=====================================================================
- TO-DO) >> 포인트와 능력을 연결시키기, 능력을 더 추가하기, 디자인을 좀 더 개선하기

### 201121 세형 패치노트
GUI branch, New_main.py
- 오픈된 카드 클릭 막음
- 불필요한 코드 정리

### 201122 용 패치노트
GUI branch, New_main.py
- 이론에 대한 영문, 한글 설명 추가 완료
- 영문 설명 문법적 오류 바로 잡음
- 닫히는 창을 Tk에서 제공하는 Message로 변경
    > OS에서 나타나는 경고창, 정보창으로 띄우게 변경
- 이제 PRINTTEXT상으로 나타나는 것은 영어로 통일
    > 맑은 고딕의 폰트 문제로 인해 안티앨리어싱이 적용되지 않아 글씨가 안좋게 나타남.

### 201122 세형 패치노트
GUI branch, New_main.py
- 게임 시작시 Tk에 입력 안하면 pygame 종료되는 문제에 대해 핫픽스.
- Tk창 입력 및 문장 위치 개선.
- 난이도 Tk 버튼 위치 변경.

## 13th Week (11.23~11.29)
### 201124 용 패치노트
GUI branch, New_main.py
- 싱글 플레이 시험판 배포를 위한 준비 작업
- 인게임 상에서 붕괴 부분에 대한 한국어 설명 추가
- 인게임 상에서 타이틀로 돌아갈 수 있도록 버튼 추가
    > Tk message를 이용하여, 게임 승리 화면에서도 나타나는 타이틀로 돌아가는 버튼에 대해서도 한 번 더 확인할 수 있도록 띄움
- 인트로 화면에서 멀티 플레이, 게임 설정 버튼 추가
    > 다른 버튼의 위치와 크기가 조정되었음
- 버튼에 기능이 없는 것들은 '차후 업데이트 예정'이라는 것을 띄우는 정보창 추가 (tk message 이용)
- 카드 숫자 추정시 카드 숫자 보이는 부분 제거
    > 디버깅을 위한 부분이고 차후 확인 바람

### 201128 세형 패치노트
GUI branch, New_main.py
- 불필요한 변수 제거.

sever branch, client.py, sever.py, New_client.py, player.py, network.py
- 방 3개 생성 완(서버에서 터미널 3개 열어야함).
- 각각의 방에서 레디 실시간으로 데이터 정상 이동 확인.
    > 레디 버튼; 한번만 클릭되는 코드 적용.   
- 방에 2인 모두 레디 시 서버에서 정상적으로 확인 가능.
    > 서버에서 클라이언트 변수 변경 불가능한 문제 발견.
- New_client.py 생성.
    > 멀티 - 방 버튼 클릭시 서버 연결(멀티 제외 모든 활동 인터넷 없이 가능).

----
========== TODO ==========

용, 세형;
- 2인 플레이 시도중.
    > **24일 싱글 플레이 시험판 배포**, 이후로는 치명적인 버그나 자잘한 수정사항을 제외하고는 업데이트가 없으며 서버 작업에 몰두할 예정
    >
    > 코드가 터무늬없이 길기 때문에 다시 분리 작업이 필요해 보임

## 14th Week (11.30~12.06)
### 201202 용, 세형 패치노트
server branch, testgame 폴더
- 클라이언트 실행은 nclient.py로 실행
- 사용자 준비 완료되면 QuantumCoda으로 접속이 되도록 패치함
- Room은 3개를 만들었음. 포트별로 분리가 된 것이고 따라서 서버에서 3개의 터미널을 실행해야 함.

= TODO =
> 일단은 게임 불러오는 것까지 해결은 되었으나, 게임 불러올 때 각 클라이언트에서 카드가 각자
생성되어 각 클라이언트에서 보는 플레이어의 카드 숫자가 다름. 아마도 단순히 정보전달 없이 함수를 실행해서
발생한 문제로 확인. 따라서 main -> redraw 함수 넘어 가기 전에 카드 덱을 만들어야 할 것으로 보임. 
>
> redraw에서는 멀티 메인을 연결시키는데 멀티 메인에서는 패를 생성할 필요는 없어 보임. 또한 redraw에서
> while은 현재로선 필요없어 보임. 왜냐하면 main에서 while이 있기 때문.
>
> nclient에서 game.py를 받고 있지 않는데 어떻게 game.py의 함수가 사용 가능할까?

### 201204 세형 패치노트
gui branch, New_main.py
- 음악 컨트롤 추가. 키보드 방향키 사용(위: 볼륨업, 아래: 볼륨다운, 왼쪽: 일시정지, 오른쪽: 재생).
- 승리 페이지 텍스트 위치 수정.

### 201205 용 패치노트
gui branch, New_main.py
- 승리 페이지에서 새 게임 버튼 함수가 잘못 연결된 문제 수정.
- 그외 자잘한 부분 수정.
- v0.12 Release

### 201206 영철 패치노트
구이 메인 파일에 능력을 추가함
1. 평균을 보여준다
2. 차이를 보여준다
3. 1턴 동안 상대방의 능력을 못쓰게 한다
4. 유추한대로 붕괴한다.
5. 뽑을 타일 더미에서 랜덤타일을 1개 가져온다
6. 내 타일에 페이크를 걸어 정확히 유추 못하게 한다
7. 지목한 상대방의 랜덤한 타일 1개를 본다
