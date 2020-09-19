# QuantumCoda

2020 PKNU Capstone Design
Team "Explorer" repository
Project: Quantum da vinci code game

200916
지원
- screen_test.py : 시작 메뉴 구현(다음에 player 수를 숫자로 받아서 입력 받고 게임 화면으로 넘어가는 코드 짤 예정)
- util.py : 색깔 RGB 정보, Obj 크기 정보

200917 종희
- making_card_복사본.py : 색깔 구분 제외한, 카드 생성
-> 이후 색깔 구분을 포함한 카드 생성 (19:52분경 )

200917 지원
- screen.py(update) : PLAYER, CARD class 생성(필요한 기능은 그때그때 추가예정)

200917 세형 (19:52분 이후 ~ 23:35분경 )
- 통합 - 09.17.py 업로드 :
  1. 기존 '배열.py' 에 색상 정보 저장 추가
  2. 'making_card_복사본.py'과 수정된 '배열.py' 연결
  * 중요!!) 이후 배열을 위해 각각의 타일 내 색상 정보가 필수적이라 판단 됨
  
200917 영철
  카드 분배 완성
  종희의 카드 생성과 바로 이어서 연동 가능하게 함

200918 세형 (업로드 시간 11:05)
- 통합 18일(11h05m).py 업로드 :
  (변경)
  1. [플레이어 수]와 [스타팅 타일 개수]를 입력 받게 변경
  2. 구동 테스트: 2~4인 설정지 양수의 모든 타일의 경우의 수에 대해 문제 없음 확인
  3. spooky 숫자 평균값 중복시 배열 조건 추가
  4. 주석설명을 2배정도 늘림

  (TODO)
  1) 패를 먹은후 배열
  2) 붕괴 후 배열
  3) 타일 넘버 제한 [2-2)부분에 해당]
  4) 정수로 입력받게 개선 [2-2)부분에 해당]
  5) 평균값도 같고 spooky 숫자도 모두 같은 경우 생상으로 우선 순위 설정 추가

200919 세형 (업로드 시간 10:25)
- 통합 19일(11h20m).py 업로드 :
  (변경)
  1. 'spooky 정렬' '타일 평균값 정렬' 을 def 함수로 개선
  2. 위의 두 정렬 함수가 자신의 타일 수 만큼 교환하며 정렬하게 개선 
  3. 게임 초기 누가 먼저 턴을 가질건지 입력 받게 추가 (입력 받은 후 오름차순으로 설정)
  4. 턴인 플레이어가 공용 타일 중 하나를 가져옴 추가
  5. 타을을 하나 먹은 후 다시 정렬 추가

  (TODO)
  1) 패를 먹고 배열 후, action (상대 숫자를 맞추거나 붕괴) 
  2) 붕괴 알고리즘 추가 (붕괴 알고리즘이 있어 붕괴후 배열 코딩이 가능할 것 같습니다!)
  4) 플레이어 수나 타일 수를 정수로 입력받게 개선 [2-2)부분에 해당]
  5) 평균값도 같고 spooky 숫자도 모두 같은 경우 생상으로 우선 순위 설정 검토 (이게 필요하다고 판단되면 그 때 추가예정. 지금은 필요성을 못 느낌.)
