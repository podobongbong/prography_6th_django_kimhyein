# 프로그라피 6기 사전과제 (김혜인)

## URL 및 기능
- / : 게시물 목록 조회
  - 게시물 포함 요소
    - URL
    - 게시물 id
    - 제목
    - 작성자
    - 작성 시간
    - 내용
  - 정렬 기준 : 최신순
- /create : 게시물 작성 (로그인 필요)
- /\<int:pk\> : 게시물 상세 정보 조회
- /\<int:pk\>/edit/ : 게시물 수정 (작성자 또는 관리자만 수정 가능)
  - 수정 페이지까지는 누구나 진입 가능하지만, 실제로 수정은 권한이 있는 유저만 가능합니다.
- /\<int:pk\>/delete/ : 게시물 삭제 (작성자 또는 관리자만 삭제 가능)
- /registration/ : 회원가입
  - 회원가입을 시도하면 '[WinError 10061] 대상 컴퓨터에서 연결을 거부했으므로 연결하지 못했습니다'
    라는 오류가 뜨지만 일단 정보 저장은 정상적으로 되는 것을 확인했습니다.
- /login/ : 로그인
- /logout/ : 로그아웃
- /password/reset/ : 비밀번호 초기화
- /password/reset/confirm/ : 비밀번호 초기화 확인
- /password/change/ : 비밀번호 변경 (로그인 필요)
- /user/ : 현재 사용자 상세 정보 조회 (로그인 필요)


## 파일 정보
- auth : 회원가입 및 로그인, 로그아웃
  - urls.py : 인증 URL 패턴
- post : 게시글
  - models.py : 게시글 모델
  - permissions.py : 작성자 확인 권한
  - serializers.py : 게시글 serializer
  - urls.py : 게시글 URL 패턴
  - views.py : 게시글 뷰
- config : 설정
- venv_laptop : Python 가상환경
   
## DB 정보
테스트용 DB를 첨부했습니다.
- 계정
  - 관리자
    - username : admin
    - email : admin@admin.com
    - password : prography
  - 일반 계정
    - username : commonuser
    - email : test@test.com
    - password : prography
- 게시물
  - 11개의 테스트 게시물
  
## 사용한 패키지
- Django
- Django Rest Framework
- Django Rest Auth
- Django Allauth
