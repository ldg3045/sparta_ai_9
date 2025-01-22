


- 프로젝트 파일 명 : my_first_pjt

- 파일 경로 명령어: pwd

- 프로젝트 이동 명령어 : <br>
cd /`파일경로`/my_first_pjt

- 서버 실행 명령어 : <br>
python manage.py runserver

<br><br>



## 필수 구현

### ✅ User와 Post 앱 개발 (MTV 패턴)

### **1. User 앱**

1. 사용자 모델 구현
    
    기본 Django User 모델을 확장하여 커스텀 필드 추가 (예: 프로필 이미지, 소개글)
    
    - `CustomUser`
2. 회원가입, 로그인, 로그아웃 기능 구현
    1. 회원가입
        - view: `signup` or `SignUpView`
        - template: `user/signup.html`
    2. 로그인
        - view: `login` or `LoginView`
        - template: `user/login.html`
    3. 로그아웃
        - view: `logout` or `LogoutView`
3. 사용자 프로필 페이지 구현
    - view: `user_profile` or `UserProfileView`
    - template: `user/profile.html`

### **2. Post 앱 (CRUD)**

1. Post 모델 구현
    
    필드: 제목, 내용, 작성자, 작성일, 수정일
    
    - `Post`
2. 게시판 기능
    1. 게시글 목록 보기 (Read - List)
        - view: `post_list` or `PostListView`
        - template: `post/post_list.html`
    2. 게시글 상세 보기 (Read - Detail)
        - view: `post_detail` or `PostDetailView`
        - template: `post/post_detail.html`
    3. 게시글 작성 기능 (Create)
        - view: `post_create` or `PostCreateView`
        - template: `post/post_form.html`
    4. 게시글 수정 기능 (Update)
        - view: `post_update` or `PostUpdateView`
        - template: `post/post_form.html` (작성 기능과 공유)
    5. 게시글 삭제 기능 (Delete)
        - view: `post_delete` or `PostDeleteView`
        - template: `post/post_confirm_delete.html`

### ✅ 필수앱 구현 참고사항

**View**

- views.py는 함수 or 클래스 택 1

**기본 템플릿**

- 베이스 템플릿: `base.html`
- 네비게이션 바: `navbar.html`
- 푸터: `footer.html`

**데이터베이스**

- SQLite3


<br><br>


## 도전 과제 구현

### 1. 좋아요 기능

- Post 모델에 좋아요 필드 추가
- 좋아요 개수 표시

### 2. 댓글 기능

- Comment 모델 구현
    - `Comment`
- 댓글 기능
    - 댓글 작성
    - 댓글 수정
    - 댓글 삭제
- 게시글 상세 페이지에 댓글 목록 표시


---

미구현 항목
- DRF 
- 데이터베이스 
    - SQLite3에서 PostgreSQL or MySQL로 마이그레이션
