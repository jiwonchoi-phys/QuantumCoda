# QuantumCoda: GUI Branch

Wecome to visit our repository! This repository is for QuantumCoda (양자 다빈치 코드) development. Our goal is making a new game including physics phenomenon on Capstone Design I Class at 2020 fall semester.

2020 PKNU Capstone Design
Team "Explorer" repository
Project: QuantumCoda (a.k.a Quantum Da Vinci Code '양자 다빈치 코드')
Members: Jong hee Kim, Yong chul Lee, Yong Kwon, Sae hyeong Cho, Ji won Choi

This branch is GUI branch for development. If you want to watch all process of our game, see master branch.

We'll write our tasks here. 

## 201007 용
- util.py의 printtext를 이용해서 턴넘기기 버튼을 작동하게 할 위치 GUI 생성하기
- 생성완료되면 Button Class 작동여부 확인해서 집어넣기

### 201107(09:10~19:15) 세형 패치노트
GUI branch: util.py, shtesr.py, main_test.py

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

TODO) 턴 관련 모든 것
    - 1. 누가 첫 턴(생략)
    - 2. 카드 휙득
    - 3. 지목 (플레이어를 지목 x. 바로 특정 플레이어의 카드 지목)
    - 4. 유추
    - 5. 붕괴