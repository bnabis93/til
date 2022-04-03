# PYTEST
- The pytest framework makes it easy to write small, readable tests, and can scale to support complex functional testing for applications and libraries.
    - test code를 위한 framework



## Conventions for Python test discovery
- pytest가 test code script를 찾는 방법.
1. 따로 입력이 없는 경우, 현재 dir 혹은 [testpath](https://docs.pytest.org/en/latest/reference/reference.html#confval-testpaths)로 준 dir 기준으로 탐색을 시작한다.
2. 위에서 설정한 dir 기준으로 recusrsive 하게 탐색한다.
3. 2에서 test_*.py or *_test.py를 찾음. 
4. test_*.py or *_test.py 파일 내에서, 다음의 test code들을 파싱한다.
    - test prefixed test functions or methods outside of class
    - test prefixed test functions or methods inside Test prefixed test classes (without an __init__ method)

## Pytest fixture


### 용어
- setup & teardown (xUnit style)
    - setup : 일반적으로 test fixture를 실행하기전 호출되는 메서드. test method 호출 바로 직전 호출됨.
    - teardown : 반대로, 끝나고 나서 호출되는 메서드.
```
def setup_method(self, method):
    """setup any state tied to the execution of the given method in a
    class.  setup_method is invoked for every test method of a class.
    """


def teardown_method(self, method):
    """teardown any state that was previously setup with a setup_method
    call.
    """
```