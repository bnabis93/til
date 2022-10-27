# Golang tips

## Basic Golang command
1. go fmt
    - Golang 표준 형식으로 formatting 해준다. 
2. go run
    - 소스코드를 compile 한 후, 바로 실행한다.
3. go build
    - 소스 코드를 binary로 compile 한다.
4. go mod  init
    - golang에서 module 생성
    - `go mod init MODULE_NAME`
    - module의 이름은 unique 해야한다. 보통 Github 저장서 주소 or URL을 module name으로 한다.
5. go mod tidy : 사용하지 않는 의존성들 제거. 경량화시킨다. 
6. go install
    - 다운로드 된 package를 compile
7. go get
    - package 다운로드 후 go install 실행
    - `-u` : 이미 패키지가 존재하는 경우 다른 부분만 다운
    - `-d` : package만 다운받음 (go install X). golang >= 1.17 부터 default
8. go test : 내장된 테스트 프레임워크 실행

## Handling Golang
1. $GOPATH 설정 후, 해당 경로에서만 package 사용 
    
```
$ ls /usr/local/go
CONTRIBUTING.md PATENTS         SECURITY.md     api             codereview.cfg  lib             pkg             test
LICENSE         README.md       VERSION         bin             doc             misc            src
```
2. Module 선언 (go mod ~) 후, 작성
3. go venv를 이용하여 가상환경을 만든다. 

## Env variable in Golang
- GOROOT : Go와 관련된 실행파일, SDK 등이 위치하고 있음. `go env | grep GOROOT`
- GOPATH : Go의 workspace 위치를 정의하는 환경변수. `go env | grep GOPATH`
- GOARCH : 프로세서의 칩셋 환경을 설정하는 환경변수 `go env | grep GOARCH`
- GOOS : 빌드 환경의 운영체제 셋팅. `go env | grep GOOS`
- GOBIN : go install을 실행하였을 때 binary가 생성되는 디렉토리

## Some tips for golang
### Go module and package
- module이 더 상위개념. package를 모아 module을 이룬다. 
- go.mod 단위로 module이 만들어진다. 
- 패키지 외부에서 해당 소스를 접근하기 위해서는 구조체, 함수등의 이름이 대문자로 시작되어야 한다. 