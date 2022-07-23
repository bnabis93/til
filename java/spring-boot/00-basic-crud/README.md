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

## API
### Web server health check
- Request
  - `localhost:8080/healthcheck`
- Response
  - Status code : 200 
  - return :`healthy`

## Reference
- 김영한, [스프링 입문 - 코드로 배우는 스프링 부트, 웹 MVC, DB 접근 기술](https://www.inflearn.com/course/%EC%8A%A4%ED%94%84%EB%A7%81-%EC%9E%85%EB%AC%B8-%EC%8A%A4%ED%94%84%EB%A7%81%EB%B6%80%ED%8A%B8)