# List 와 Tuple에 관하여
- 메모리와 연관지어 자료구조를 이해해야한다.

## List와 tuple의 생성
- 배열을 생성하기 위해서는 시스템 메모리 블록을 할당해야함
    - A "memory block" is a contiguous chunk of memory.
    - 연속된 메모리 덩어리라고 보면 됨
- List와 tuple도 일종의 배열이므로, 생성하기 위해서는 먼저 시스템 메모리 블록을 할당해야함.
- 메모리에 할당했으면 해당 메모리의 주소를 가리키는 포인터가 생성되어야한다.
- 각 블록에는 포인터값이 저장됨 (실제 메모리 주소)

## 탐색
- 메모리 블록에 저장된 포인터값을 따라가면 실제 저장된 값을 알 수 있다. 
- 포인터값은 같은 크기를 가질것이다.
- 따라서 List, Tuple의 탐색은 선형 탐색은 O(n), indexing (특정 위치 찾기)은 O(1)이 걸릴 것

## 정렬
- Python list는 내장함수로 sorting 가능.
- Tim sort, O(nlogn)
- Tim sort는 insertion sort + merge sort
- 리스트가 정렬된 상태라면 이진 탐색 O(logn) 이 효율적일것


## List와 Tuple
- 동적이냐 (List), 정적이냐 (Tuple)
- 즉, List는 크기등의 변화가 가능하지만 Tuple은 선언한 이후로 크기 조작 불가능하다. (데이터 수정도 안됨)
- Tuple은 python runtime에서 caching 한다. -> 즉, tuple 선언때마다 kernel에 메모리 요청을 하지않으므로, 잘쓰면 메모리를 굉장히 효율적으로 쓸 수 있을것이다. 

## List 
- List는 동적이다. 따라서 데이터를 추가 할 수 있다.
- 크기 2의 List를 선언 한 후, 지속적으로 데이터를 넣어주면 어떻게 될 것인가?
- 크기를 넘어가게 되면 List는 resize하게 된다. 그렇다면 이 resize 연산은 어떻게 동작하는가?
- Resize는 먼저 원래 담고 있던 N개 (이때는 2개가 됨)와 새로 추가된 element를 담기 충분한 List를 새로 만든다.
- N+1의 크기가 아닌 넉넉하게 M (더블링 될수도?) 즉, N+M 크기의 메모리를 할당한다. 
- 새롭게 할당된 List에 값을 복사하고, 기존의 List는 삭제한다.
- 즉, 메모리 할당 -> 복사 -> 삭제의 과정을 거치게 된다. 

## Tuple
- Tuple은 정적이다. 한번 선언하면 그 크기가 고정된다.
- 물론 두 tuple을 합친다던지, append도 가능은 O(n)의 시간이 걸릴것이다. 
- 왜냐하면 새로운 tuple을 메모리 할당하고, 복사를 해야하기 때문이다. 
    - List는 여유공간을 잡아놓기 때문에 O(1)이 걸릴것
- 이러면 Tuple 왜쓰냐 싶기도한데 잘쓰면 메모리를 굉장히 효율적으로 관리 할 수 있다. 
- 또한 python 내부적을 사용하는 리소스 caching에 의하여 tuple을 굉장히 효과적으로 사용 할 수 있다.
- 크기 20이하인 tuple은 GC에 의해 메모리가 반환되지 않고 남아있게 된다. 
- 즉, 크기 20이하인 tuple은 재선언없이 caching된 리소스를 이용한다는 말이다. 
```
from timeit import timeit

print(timeit("[1,2,3,4,5,6,7,8,9]", number=10000000))
print(timeit("(1,2,3,4,5,6,7,8,9)", number=10000000))

0.342708458
0.04108704099999999
```

## 최적화 팁
- List, tuple내 element들의 data type이 다른경우, 통일해주는것이 성능면에서 좋긴하다. 
- List의 메모리 복사는 cost가 크다. 이를 고려할것.
- 크기가 20 이하인 tuple은 python runtime에의하여 caching 된다. 이를 잘 쓰면 메모리를 굉장히 효율적으로 사용 할 수 있다. 



## Reference
- 고성능 파이썬