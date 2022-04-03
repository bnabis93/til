# fastapi
- FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.
    - Web framework
    - Python 3.6+
    - Using python type hints

## 동작방식
- 내부적으로 fastapi backend가 생성된다.
- 지정된 main.py (굳이 main.py가 아니어도 된다.)를 지속적으로 tracking 하면서 server에 put request를 요청하여 자동으로 업데이트 되어 api server가 만들어진다.
- [basic-client-bacakend](./baisc-client-backend/) 예제의 경우 src/server에 fastapi에 있는 정보를 put하게 만들었다. 
- 경로는 /이 아닌 . 으로 잡는다.
- The server should reload automatically (because you added --reload to the uvicorn command above).

### 추가적인 설명
- ASGI(Asynchronous Server Gateway Interface) app
    - python webserver와 interface 역할을 한다.
    - web sever - framework (fastapi) - app을 비동기로 연결해주는 python 표준 interface

## Backend features
- fastapi backend automatically create api docs. 
    - http://127.0.0.1:8000/docs.


## Reference
- https://fastapi.tiangolo.com/
- https://asgi.readthedocs.io/en/latest/#:~:text=ASGI%20(Asynchronous%20Server%20Gateway%20Interface,servers%2C%20frameworks%2C%20and%20applications.