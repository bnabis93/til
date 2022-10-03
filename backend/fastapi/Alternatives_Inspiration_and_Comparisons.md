# Alternatives, Inspiration and Comparisons
FastAPI를 만들기 위한 여정들. 무엇을 참고했는가.   
다 보진 않을거고, 몇가지만 보려함.
## Intro
Fastapi가 만들어지기까지 많은 툴들을 참고하였고 영감을 받았다.  
왠만하면 새로운 framework를 안만들고 기존의 것들을 활용하여 개발하고 싶었지만, 결국엔 새로운 framework를 만들게 되었다.

## Previous tools
FastAPI 이전에도 Python기반의 web framework들은 있었다. 
### Django
- Python에서 가장 유명한 web famework.
- Instagram에서도 Django를 사용함.
- RDB (Relational DB, like PostgreSQL, MySQL) 에 너무 강하게 결합되어 있음
- NoSQL에 사용 어려움. (NoSQL을 고려한다면 부적합함)
- HTML을 BE에서 만드는 방식. 현대 FE framework (React, Vue 등)나 다른 시스템 (IoT 등)에서 사용되는 API를 고려하지 않음

### Django REST Framework
- Django REST Framework는 Django 기반의 가벼운 web api을 만들기위한 framework이다.
- Automatic API documentation 가능 -> FastAPI의 automatic API documentation에 영감을 주었다.
- https://github.com/encode/django-rest-framework

### Flask
- Flask는 Django에 비해 매우매우 가벼운 web framework이다. "microframework"
- NoSQL을 쓰는데도 문제없다. 
- 여러 기능들을 plug-in 형태로 추가하여 사용 할 수도 있고, 그냥 쓸 수 도 있다.
- 이러한 Decoupling이 Flask의 큰 장점이고, FastAPI에서도 이러한 "microframwork" 개념을 차용하였다. 

### Requests
- FastAPI를 Requests lib의 대안으로 개발한건 아니지만, 영감은 많이 받음
- FastAPI 내부에서 Requests lib 사용하는게 일반적. 
- Requests lib는 여러 API 상호작용(요청, 응답 등)을 위한 lib이고, FastAPI는 빠르게 api를 만들기 위한 lib이다. 
- FastAPI는 Requests lib로부터 다음의 것들을 차용함
    1. Have a simple and intuitive API. 간단하고 직관적인 API
    2. Use HTTP method names (operations) directly, in a straightforward and intuitive way. @app.get과 같이 HTTP method name을 사용하였고, 굉장히 직관적으로 사용 할 수 있음
    3. Have sensible defaults, but powerful customizations.

### 이외의 것들
1. marshmallow, data serialization, data validation 참고.
    - data serialization : code로부터 data 받아서 network로 보낼 수 있는 형태로 만드는것. e.g. `datetime` object를 string으로 만들어 보낸다던지.
    - data validation : 적절한 data가 온건지. param등을 검사하는것. e.g. int 형태로 데이터를 받아야하는데 string으로 온다던지. valiation이 없다면 직접 code 레벨에서 확인하고 예외처리 해야할것.
2. Webargs : data parsing 부분 참고. 
등등 많은데 일단 여기까지

## Used By FastAPI
### Pydantic
- Python `type hints`을 바탕으로 data validation, serialization and documentation(JSON Schema 기반)을 위한 lib

### Starlette
- Lightweight ASGI framework/toolkit, asyncio의 성능을 높이기 위하여 사용한다. 
    - ASGI : Asynchronous Server Gateway Interface. 비동기 서버 게이트웨이 인터페이스. web app과 web server 간의 공통 interface를 기술한다. 
    - 세개의 param을 가지는 application async 객체를 정의한다. 비동기쓴다는게 다르네. 
        - scope : 현재 요청에 대한 정보 
        - receive : app이 client로 메세지를 돌려보낼 수 있게 만드는 async callable 함수
        - send : app이 client로부터 메세지를 수신 할 수 있게 해주는 async callable
    ```
     async def application(scope, receive, send):
        await send({
            'type': 'http.response.start',
            'status': 200,
            'headers': [
                [b'content-type', b'text/plain'],
            ],
        })

        await send({
            'type': 'http.response.body',
            'body': b'Hello, world!',
        })
    ```

### Uvicorn
- Uvicorn is a lightning-fast ASGI server, built on uvloop and httptools.
- Starlette이 uvicorn 서버를 사용한다. 

## References
- https://fastapi.tiangolo.com/alternatives/