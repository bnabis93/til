# Iterator & Generator
- Python interpretor가 x 객체를 반복 할때는 언제나 iter(x)를 호출한다.

## iter()
- iter() 객체는 다음의 과정을 수행한다.
1. 객체에 `__iter__()` 메서드가 구현되어있는지 확인한다.
2. `__iter__()` 대신 `__getitem__()` 이 구현되어 있으면 index 기반으로 순서대로 가져오는 반복자 생성한다.
3. 1,2 과정이 실패하면 즉, `__iter__()` , `__getitem__()` 둘다 구현이 안되어있으면 `Type Error` 발생 (object not iterable)
- Iteralbe에 대한 에러는 항상 위의 type error이기 때문에 이에 따른 예외처리 염두하면 된다. 

## 반복형
- iter() 객체가 반복자를 가져 올 수 있는 모든 객체. (`__iter__()`, `__getitem__`), 반복자를 반환하는 `__iter__()` 메서드를 구현하는 객체가 반복형이다. -> 즉, `__iter__()`, `__getitem__`가 구현되어있음 반복형이다. 라고 말할 수 있을듯
- [Iter example01 참조](./iter_example01.py)

## example로 본 반복자에 대한 표준 인터페이스
- [Iter example01 참조](./iter_example01.py)
- next / stopiteratio이 가능해야 가장 간단한 반복자를 만들 수 있다.
- 1. `__next__()` : 다음 사용할 항목 반환, 만약 없으면 `StopIteration`
- 2. `__iter__()` : self 반환. 이친구가 있어야 반복자 사용 가능
- Iteralbe 하기 위해서는 `__iter__()` 메서드가 필요하다.
    - `__iter__()`객체는 iterator 객체를 반환한다.
    - `iterator` 객체는 `__next__()` 메서드와 `__iter__()` 메서드가 구현되어 있어야 한다.
    - `iterator.__iter__()`는 self 반환.
    - 대충 이런것들이 있구나 하고 넘어가자. 

## 반복자 (Iterator)
- Python 의 반복자 (Iterator)는 type이 아닌 protocol이다.
- 따라서 typecheck가 아닌 `__next__()`, `__iter__()` 속성, 메서드 구현에 대한 검사를 해야 한다.
- [Iter example02 참조](./iter_example02.py)

## 반복자 패턴의 반복자 
- 디자인 패턴의 반복자 패턴에 맞춘 sentence class 구현 [Sentence02](./sentence02.py)
- 반복자 구현하기위해서는 `__next__()`, `__iter__()` 필요. 하지만 구현에서는 `__iter__()`가 없어도 되긴하지만 반복자 패턴에 맞추기 위하여 구현하였다.
- `Sentence class` 내에 `__next__()` 넣으면 안되나? -> 전형적인 안티패턴이라 한다.
    - 다중반복이 가능해야되기 때문이다. `__iter__()` 호출 할 때마다 새로운 Iterator가 만들어져야 다중 반복이 가능하다. 
    - `Sentence class` 내부에 구현해버리면 하나의 Iterator만을 가지고 컨트롤하게 될 것 이다. -> 안티패턴인 이유

## More pythonic version
- [Sentence03](./sentence03.py)



## reprlib 
- https://docs.python.org/3/library/reprlib.html

## Reference
- 전문가를 위한 Python