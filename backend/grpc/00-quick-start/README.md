# gRPC Quick Start

## gRPC
- gRPC는 protocol buffer를 IDL(Interface Definition Language)로 정의하여 이를 주고받는 형식으로 통신한다.
    - IDL은 일종의 중간언어이다. 
- 따라서 먼저 protocol buffer를 정의해야한다. 

### Python gRPC
- python gRPC는 `protoc` 라는 protocol buffer compiler를 사용한다. 


## How to play?
### Setup
- `conda` is required.
```
make env
make setup
```

### Clone the repo
```
git clone -b v1.56.0 --depth 1 --shallow-submodules https://github.com/grpc/grpc
```



## Reference
- https://grpc.io/docs/languages/python/quickstart/