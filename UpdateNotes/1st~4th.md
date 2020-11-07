## 3rd Week (09.14~09.20)
### 200916 지원
- screen_test.py : 시작 메뉴 구현(다음에 player 수를 숫자로 받아서 입력 받고 게임 화면으로 넘어가는 코드 짤 예정)
- util.py : 색깔 RGB 정보, Obj 크기 정보

### 200917 종희
- making_card_복사본.py : 색깔 구분 제외한, 카드 생성
-> 이후 색깔 구분을 포함한 카드 생성 (19:52분경 )

### 200917 지원
- screen.py(update) : PLAYER, CARD class 생성(필요한 기능은 그때그때 추가예정)

### 200917 세형 (19:52분 이후 ~ 23:35분경 )
- 통합 - 09.17.py 업로드 :
  1. 기존 '배열.py' 에 색상 정보 저장 추가
  2. 'making_card_복사본.py'과 수정된 '배열.py' 연결
  * 중요!!) 이후 배열을 위해 각각의 타일 내 색상 정보가 필수적이라 판단 됨
  
### 200917 영철
  카드 분배 완성
  종희의 카드 생성과 바로 이어서 연동 가능하게 함

### 200918 세형 (업로드 시간 11:05)
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

### 200919 세형 (업로드 시간 11:00)
- 통합 19일(11h00m).py 업로드 :
  (변경)
  1. 'spooky 정렬' '타일 평균값 정렬' 을 def 함수로 개선
  2. 위의 두 정렬 함수가 자신의 타일 수 만큼 교환하며 정렬하게 개선 
  3. 게임 초기 누가 먼저 턴을 가질건지 입력 받게 추가 (입력 받은 후 오름차순으로 설정)
  4. 턴인 플레이어가 공용 타일 중 하나를 가져옴 추가
  5. 타일을 하나 먹은 후 다시 정렬 추가
  6. (11:00 추가) 턴을 넘기는 함수 def로 변경

  (TODO)
  1) 패를 먹고 배열 후, action (상대 숫자를 맞추거나 붕괴) 
  2) 붕괴 알고리즘 추가 (붕괴 알고리즘이 있어 붕괴후 배열 코딩이 가능할 것 같습니다!)
  4) 플레이어 수나 타일 수를 정수로 입력받게 개선 [2-2)부분에 해당]
  5) 평균값도 같고 spooky 숫자도 모두 같은 경우 생상으로 우선 순위 설정 검토 (기존 다비치 룰에 따라 추가 예정)
  
### 200919 영철 
대략적인 게임 진행까지 업로드
  
  1.카드를 맞췄을 때 연속진행할껀지 턴을 넘길껀지에 대한 코드를 안짰었음
  
  2.숫자입력상활에서 문자를 입력하게 되면 에러쯤 
  
  3.아직 실행해서 여러 시도를 안해봐서 문제점을 찾지 못함

## 4th Week (09.21~09.27)
### 200921 영철 조커카드 넣기 전 알고리즘에 해당 

############# 패치 노트 ######################

 1. 필드의 카드가 모자라면 뽑지 못하게 변경
 2. 공개 필드에 있는 카드도 플레이어가 가진 카드가 배열 될때 맞춰서 배열되게 변경
 3. "?"카드에도 색을 부여
 4. 카드유추를 성공 했을 때 연속진행 할껀지 멈출껀지에 대한 선택지 제공

#############################################

이후 문제점이 발견될시 다시 고칠 예정

확인용 print와 함수설명 txt파일 만들 예정

#############################################

### 200922 세형 (업로드 시간 15:30)
- 조커 넣기 전 알고리즘 파일 (22일 15.30 수정) 업로드 :
  (변경)
  1. 타일 평균값 정렬 중 평균값이 같고 spooky 숫자 모두 중복시 검정 타일이 왼쪽에 정렬되게 추가
  2. 1 의 기능은 color_arrange_on 값이 1이여만 작동됨[기본설정 0]. (기존 다비치 코드에 해당 룰을 적용시키고 안시키고가 취향이라, 사용자 설정 옵션으로 고려)
  3. 배열 파트의 확인용 print 추가 후 주석 처리함
  4. 기타 주석 추가
  5. spooky_arrnage 이후 tile_arrange를 수행하는 arrange def 함수 정의 -> 진행에 해당부분 적용

  (TODO)
  1. 여러번 실행하며 코드 검토 & 경량화

############# 2020 09 22 패치 노트 ######################

  1. 카드 생성 코드를 매우 단축함 과거에 비해 매우 효율적임
  2. 공개 필드 카드도 배열을 추가하면서 카드 자체가 바뀌는 현상이 발생했으나 현재 수정후 없어짐
  3. action함수를 없애고 분할하여 각각 따로 함수를 만듬

########################################################
  
  이전에 지목했던 카드를 확인할 수 있게 변경예정
  
  조커 넣을 예정
  
##########################################################

############# 2020 09 23 패치노트 ######################

  1. 카드 생성 코드 단축화 과정에서 생긴 오류를 수정
  2. 이전에 내가 플레이어 x의 몇번째 카드를 선택했었는지 알려주게 변경
  3. 좀더 자주 패 상황을 보여주도록 변경
  4. 색깔 선택 단계에서 카드를 다 뽑으면 무한 루프에 걸리는 현상을 수정 
  5. 이전에 내가 지목했던 카드를 알려주는 과정에서 생겼던 오류 수정
  6. 필드에 남아있는 카드가 없어서 더 이상 못뽑을 때 카드 지목에 실패하면 오픈될 카드가 없어서 생기는 오류를 
     아무런 카드도 오픈 안하고 진행하도록 변경

########################################################



################ 2020 09 23 gui(지원) ##################
  
  BUTTON 클래스 구현
  게임 메인화면 구현 시작 예정

############# 2020 09 24 패치노트 ######################

  1. 아웃된 플레이어를 제외하고 턴을 넘기게 변경
  2. 1을 하는 과정중 의도치 않게 승리 코드를 넣음
  3. 2를 넣어서 플레이 했을 때 패가 다 까지면 컴퓨터 오토붕괴에서 오류가 나던 현상을 수정
  4. 연속해서 맞추려고 할 때 컴퓨터 오토붕괴가 이루어 지지 않고 배열도 다시 진행되지 않던 문제를 수정
  5. 조커카드 추가,  인식을 위해 숫자 100을 조커로 함 조커카드를 뽑은 처음에만 위치를 정할 수 있게함 이후에는 컨트롤 불가
     
     ㄴ조커카드는 배열을 무시하도록 해야함

########################################################

########################################################
  
  능력을 생각하고 만들어낸 후 추가할 예정이라 한동안 패치가 없을 예정
  
########################################################

############# 2020 09 24 패치노트 ######################

  임시버전으로 능력을 추가하였음
  
########################################################

############# 2020 09 26 패치노트 ######################

능력 추가 버전.py에 대한 패치노트
 1. 능력 모드 추가 및 주석 추가
 2. 조커를 2개 동시에 뽑으면 배열이 안되는 문제를 발견
 3. 능력 소개를 안함
 4. 침묵 능력을 너무 빨리 사용할 수 있음 - 조정이 필요

########################################################

### 200927 세형 (업로드 시간 14:50)

 1. 조커는 배열에서 무시하도록 추가. > 검토 완.
 2. '조커의 자리를 플레이어가 정하는 과정'에서 오류 발견. >> 수정필요.
 3. 한 플레어이가 시작 시 두 색상의 조커 카드를 모두 가져가는 경우 고려안됨. >> 추가필요.