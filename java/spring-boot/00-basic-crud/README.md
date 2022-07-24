# 00.Basic CRUD
## How to start?
### Prerequisites
- java : 17.0.1
- gradle : 7.4.2

### Generate spring boot project 
- Init the spring boot project using [start.spring.io](https://start.spring.io/)
  - Project : Gradle Project
  - Language : Java
  - Spring Boot : 2.7.2
  - Packaging : Jar
  - Java : 17
  - Dependencies : Spring Web, Thymeleaf

### How to build and start?
```aidl
$ ./gradlew build 
$ java -jar build/lib/<SNAPSHOT>.jar
```

## 사용하는 pattern
- 사실 어떤 패턴을 사용하는지 정확히 모르겠다.
- Clean architecture와 mvc의 혼합된 형태인것같기도하고, 아닌것 같기도 하고.
### Controller
  - Controller : Client와 소통하는 부분. 여러 Client로부터 오는 요청 및 응답에 대해 대응하는 부분. 
    Client로 부터 온 요청을, DTO(Data Transfer Object)등을 이용하여, 형태로 가공하여 BE가 사용 할 수 있도록 해주기도 하고, 
    비지니스 로직을 거친 응답을 위한 데이터를 보내주기도 한다.   
  - DTO (Data Tranfer Object) : Data를 BE가 사용 가능한 형태로 변환 할 수 있게 해준다. (Data가 정의되어 있다.)
### Service
  - Domain과 application layer의 역할이 햇갈린다.  
  - Service : 비지니스에 가까운 로직
### Domain 
  - Domain : 
### Repository
  - Repository :

## Spring bean
- Spring bean은 spring container가 관리하는 자바 객체.
  - 정확히는 Spring IoC (Inversion Of Control)에 의해 관리된다고 한다. 
- Spring bean은 기본적으로 컨테이너에 singleton으로 등록된다. 
### @Component annotation
- @Component annotation을 이용하여 spring bean 등록 가능

## API
### Web server health check
- Request
  - `localhost:8080/healthcheck`
- Response
  - Status code : 200 
  - return :`healthy`

## Reference
- 김영한, [스프링 입문 - 코드로 배우는 스프링 부트, 웹 MVC, DB 접근 기술](https://www.inflearn.com/course/%EC%8A%A4%ED%94%84%EB%A7%81-%EC%9E%85%EB%AC%B8-%EC%8A%A4%ED%94%84%EB%A7%81%EB%B6%80%ED%8A%B8)
- [Spring Beans in Depth](https://medium.com/javarevisited/spring-beans-in-depth-a6d8b31db8a1#:~:text=By%20definition%2C%20a%20Spring%20bean,many%20objects%20in%20your%20application.)