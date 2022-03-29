## test
- https://en.wikipedia.org/wiki/Software_testing

- Test는 개발자의 관점과 사용자의 관점에서 소프트웨어를 검증하는 행위이다.
    - Validation은 사용자 관점에서의 시스템 검증이다
    - Verification은 개발자의 관점에서 시스템 검증이다.

### Static test & dynamic test
- 정적인 환경이 뭐냐, 동적인 환경이 뭐냐를 정의하면 이해하기 쉽다.
- 기준은 프로그램의 동작 여부다. 프로그램이 동작하고 있는 환경에서 테스트를 하면 동적 테스트고, 프로그램이 동작하지 않는 환경에서 테스트를 하면 정적 테스트다.
- 말그대로 정적 test. Static test는 linting 과 같은것을 생각하면 된다.

### Static test
- https://towardsdatascience.com/static-code-analysis-for-python-bdce10b8d287

### Dynamic test

### Unit test
- 소스 코드의 특정 모듈이 개발자가 의도한 대로 잘 동작하는지를 검증하는 절차이다.
- Module test라고도 한다.

----

## Static test tools (python)
### Code complexity 
- radon
```
pip install radon
radon cc <FILE PATH> -s

./cs/python/radon_example.py
    F 1:0 test_radon - A (3)
    F 10:0 test_radon2 - A (1)
```

### Style guide
- pycodestyle
```
pip install pycodestyle

pycodestyle --first ./cs/python/radon_example.py 
./cs/python/radon_example.py:5:20: W291 trailing whitespace
./cs/python/radon_example.py:11:9: E225 missing whitespace around operator
./cs/python/radon_example.py:13:1: E305 expected 2 blank lines after class or function definition, found 1
./cs/python/radon_example.py:16:13: W292 no newline at end of file

```
- pyflake
```
pip install --upgrade pyflakes

pyflakes ./cs/python/radon_example.py
./cs/python/radon_example.py:11:5 local variable 'temp' is assigned to but never used
```

- flake8
```
pip install flake8

flake8 ./cs/python/radon_example.py 
./cs/python/radon_example.py:5:20: W291 trailing whitespace
./cs/python/radon_example.py:7:20: W291 trailing whitespace
./cs/python/radon_example.py:11:5: F841 local variable 'temp' is assigned to but never used
./cs/python/radon_example.py:11:9: E225 missing whitespace around operator
./cs/python/radon_example.py:13:1: E305 expected 2 blank lines after class or function definition, found 1
./cs/python/radon_example.py:16:13: W292 no newline at end of file
```

### Git hook
- https://techblog.woowahan.com/2530/