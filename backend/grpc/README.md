# gRPC

## gRPC Fundamentals
- gRPC는 protocol buffer를 IDL(Interface Definition Language)로 정의하여 이를 주고받는 형식으로 통신한다.
    - IDL은 일종의 중간언어이다. 
- gRPC 서버측에서 protocol buffer를 정의한다. 일종의 통신 규약을 약속한다고 생각하면 된다.
- gRPC 클라이언트에서는 서버와 동일한 메서드를 제공하는, 서버의 Protocol buffer 통신 규약에 대한 정보를 가지고 있는 stub을 가진다. 
    - 언어가 다르더라도 (e.g. Server: python / Client01: ruby, Client02: go) 동일한 통신 규약에 대해 약속을 하고 있으므로 통신이 가능하다. 

### Protocol Buffers
- `.proto` 의 확장자를 가진다.
- 해당 파일에 통신하고자 하는 데이터의 구조를 정의한다. 
- 정의된 데이터는 `field`라고 하는 name-value pairs 형태이다. 다음은 예시이다. 
```
message Person {
  string name = 1;
  int32 id = 2;
  bool has_ponycopter = 3;
}
```
- 정의된 protocol buffer를 `protoc` 컴파일러가 컴파일하여 데이터 엑세스 클래스를 생성한다.
    - 해당 클래스는 데이터의 입/출력(getter, setter)가 정의된 단순한 클래스이다.
- 이제 서버와 클라이언트는 동일한 protocol buffer를 사용하므로 통신이 가능하다.


## Why gprc is fast than REST API?
- gRPC도 http2.0 protocol 사용
- 데이터를 serialization 하기 위하여 protocol buffer를 사용한다. / REST API는 json / xml(string)을 사용한다.
    - protocol buffer는 data를 binary로 encoding한다.
    - Protocol buffer를 통해 효율적인 serialization이 가능하다. json / xml등에 비햐여 encoding / decoding 속도가 향상된다.
    - 즉, 데이터를 준비하는 시간, 읽는 시간등에서 효율적이다.
- 스트리밍이 가능하다. 

## Reference
- https://grpc.io/docs/languages/python/basics/