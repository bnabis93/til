### Program
- Program 이란 실행 가능한 파일이다.
    - 실행된다는 것은 OS가 메모리에 해당 파일의 공간을 할당한다는 것이다.
- Program은 저장장치(hdd, ssd)에는 저장된다.
- 실행 되기 전까지는 그냥 코드의 덩어리다.
- 이 프로그램이 실행되어 메모리에 올라간다면, Process라는 단위로 올라가게 된다.

### Process
- Process는 CPU에 의해 실행 될 수 있도록 메모리에 로드 된 프로그램 코드이다.
    - Program의 instance 라고도 한다.
    - 따라서 하나의 program에 여러 process가 실행 될 수 있다.
- Process가 생성되면, OS가 자원을 할당해준다.
- Code, Data, Stack, Heap (메모리 영역)이라는 자원을 할당받는다.
    - Code : 코드
    - Data : 변수, 구조체 등과 같은것들이 저장되는 영역
    - Stack : 프로세스가 사용하는 임시 메모리 영역. 대표적으로 함수를 호출하면 생성되고, 종료시 반환한다.
    - Heap : 동적 데이터 영역. 동적으로 메모리가 할당되는 영역이다.

### Thread
- 프로세스에서 실행되는 작업 흐름의 단위
- 프로세스가 할당받은 자원을 이용하는 '실행'의 단위
- Thread는 Stack을 독립적으로 할당받고, 나머지 영역은 공유한다.