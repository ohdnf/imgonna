# imgonna

> 귀찮으니까 암거나(imgonna) 추천해주는 영화 추천 서비스입니다.
> 사실 TMDB API를 활용해 영화 정보를 제공하고 영화를 추천해드립니다.



## 목차
- [기능](#기능)
- [기술 스택](#기술-스택)
- [기술 설명](#기술-설명)
	- [ERD](#erd)
	- [디렉토리 구조도](#디렉토리-구조도)
- [테스트 방법](#테스트-방법)


## 기능

<img src="assets/01_landing.png" style="zoom:50%;" />

![](assets/02_movies.png)

![](assets/03_detail.png)

<img src="assets/04_recommend.png" style="zoom:50%;" />

<img src="assets/05_community.png" style="zoom:50%;" />

<img src="assets/06_article.png" style="zoom:50%;" />



## 기술 스택
- Backend - Django
- Frontend - Vue.js



## 기술 설명

### ERD

<img src="assets/erd.png" style="zoom:50%;" />

### 디렉토리 구조도

```
📁imgonna
├─📁backend
│   ├─📁accounts
│   ├─📁articles
│   ├─📁backend
│   ├─📁movies
│   ├─📁reviews
│   ├─db.sqlite3
│   └─manage.py
└─📁frontend
    ├─📁node_modules
    ├─📁public
    ├─📁src
    │   ├─📁components
    │   ├─📁router
    │   ├─📁views
    │   ├─App.vue
    │   └─main.js
    ├─.env.local
    └─packages.json
```



## 테스트 방법
> 로컬 테스트

### Backend

1. Python 설치

2. 가상 환경 설정 및 의존성 주입

    ```shell
    $ cd backend
    $ python -m venv venv
    $ source venv/bin/activate
    (venv) $ python -m pip install -r requirements.txt
    ```

### Frontend

1. node.js 설치

2. 환경 설정 및 의존성 주입

    ```shell
    $ cd frontend
    $ npm install --silent
    ```

3. `.env.local` 설정

    ```shell
    VUE_APP_TMDB_API_KEY=TMDb API에서 계정을 생성하여 받은 키를 넣으시면 됩니다
    ```

4. 실행

    ```shell
    $ npm run serve
    ```
