# english_word_book
implement english_word_book using docker containers (react, django, mysql)



> 프론트 : React
> 백 : django
> 데이터베이스 : mysql


기본적인 설계 :

docker (react)
docker (django, mysql)

django와 mysql은 같은 도커 컨테이너에 둔게 아니라 각자 다른 컨테이너에 넣었고 docker-compose.yml을 통하여 만들어 같은 네트워크에 넣어주었다

맨 처음 만들 때에는 단순히 image를 다운, run만 시키고 django와 mysql을 다운 받고 실행하였으나 django의 세팅을 아무리 건드려봐도 mysql과 연동이 안됬다. 그저 소켓이 없다고 에러만 내뿜을뿐.

좀 더 찾아본 결과 django의 settings.py의

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db',
        'USER': 'root',
        'PASSWORD': 'qwe123',
        'HOST': 'project_db',
        'PORT': '3306',
    }
}
```

부분에 PORT를 아무리 3306이라고 해주어도 도커 컨테이너 내부의 3306을 찾지 실제 내 컴퓨터의 3306을 찾는게 아니라는 것을 깨달았다.

여기서 좀 더 찾아본 결과 같은 네트워크로 묶어줘야함을 알게 되었고 docker-compose를 사용하여 컨테이너를 만들었다.

React 같은 경우는 웹브라우저를 만들어주고 웹브라우저상에서 127.0.0.1:8000을 찾기 때문에 정상적으로 내 컴퓨터의 포트를 찾아가기 때문에 다른 컨테이너에 분리하였다.


React에서의 fetch api를 사용할 때 localhost:8000을 하면 django와 cors policy 이슈가 난다.
django에서 cors를 설치하고 세팅을 해주어도 오류가 난다.

크롬에서 localhost는 안된다고 봤는데 127.0.0.1:8000으로 바꿔보니 잘 되서 자세히는 안보고 넘어갔다.
이것 때문에 3일을 날렸다.

크롬말고 edge에서는 localhost가 되긴 했는데 나는 크롬에서 하고 싶어서 시간을 낭비한 것도 있긴하다.

근데 어차피 다들 크롬쓰잖아

 fetch api의 get post put delete 메소드를 사용하여 django에서도 구현을 하여서 전체적으로 프론트와 백, 데이터베이스가 어떻게 이루어나가는지 윤곽을 희미하게 느낀 것 같다.
 
 프론트에는 별 관심이 없어 clone coding 을 통해서 구현하였으나 세세한 부분은 검색하면서 뜯어 고쳤고 django와 mysql은 내가 만들었다.
 
 사실 mysql은 도커세팅하는데에만 엄청 시간오래걸리고 django도 코드 보면 알겠지만 별 기능없다...
 
 mysql에 사진을 저장하는 기능을 배워서 블로그에서의 사진을 넘겨받는 것도 해보자.
 
 어차피 나중에 s3에서 다 하긴 















