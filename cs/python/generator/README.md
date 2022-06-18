# Generator
- Generator를 사용한 [sentence class](./sentence03.py)

## Generator의 동작 방식
- 본체 안에 yield 함수 가지면 모두 geneator 함수 이다.
    - Q. 본체는 무엇인가?
        - A. 그냥 어디에선가 yield 키워드를 쓰는것을 의미한다. 함수 내부에서 yield 키워드가 나온다면 그것은 generator 함수이다.
- Geneator는 값을 반환하는것이 아닌 객체를 반환하는 것이다.
- 내부에 return 문 있으면 stop iterator 예외 발생한다.

## Iterator는 Lazy하게 동작한다.
- Lazy <-> eager (와 이건 처음알았네. 한번에 올리겠다는거겠네.)
- Lazy한 sentence class를 만들어보자.
- [sentence class 04 example](./sentence04.py)

## Generator 표현식 사용
- e.g. `(match.group() for match in RE_WORD.finditer(self.text))`
- [sentence class 05 example](./sentence05.py)
- 아무래도 Lazy 하기 때문에 메모리 사용량에서 이점이 있다. (지능형 list에 비해)


