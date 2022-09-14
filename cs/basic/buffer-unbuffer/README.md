# Buffer / Unbuffer
Force the stdout and stderr streams to be unbuffered. This option has no effect on the stdin stream.

일반적으로 stdout (표준 출력)은 buffer에 저장이 됩니다. (아마 I/O는 다 buffer에 저장될겁니다.) 아마 이 buffer를 사용하지 않고 바로 streaming 하겠다는 의미이다.

그냥봤을때는 unbuffer가 좋은거아닌가? 바로 streaming 되잖아? 라는 생각이 드는데요. 좀 찾아보니 그렇진 않습니다.

buffer를 사용한다는것은 kernel level에서 혹은 언어 level에서(python의 경우 PYTHONUNBUFFERED가 되겠네요) 뭔가 buffer를 사용하겠다는 말이고, unbuffer를 한다는것은 buffer 없이 바로 disk i/o를 일으킨다고 보시면 되겠습니다.

아무래도 os level 혹은 언어 level에서 처리하는것보다 disk I/O를 발생시키는게 코스트가 더 높겠죠. 그래서 unbuffer를 하게되면 disk I/O, os 레벨에서의 system call등이 발생하게 됩니다. (buffer를 사용한다는것은 batch 단위의 실행 혹은 일종의 cache로 이해해도 될것같네요.) 
예를 들어 16바이트를 모아서 disk에 쓰냐(buffer), 1바이트씩 쓰냐 (unbuffer)의 차이입니다. 

어 그럼 무조건 buffer 쓰는게 맞는거아냐? 라고 할 수 있겠지만, 즉각적으로 disk I/O (파일에 쓴는것을 생각하시면 됩니다.) 를 일으켜야 하는 경우도 있습니다. 보통 log를 찍거나 err를 발생시키는 경우가 그렇습니다. 
근데 log같은 경우에는 i/o가 꽤나 많이 일어나 buffer로 하는게 좋지않을까 하네요. 에러 같은 경우는 빈도수가 적으므로 unbuffer로 해도 될것같고요. 

Reference - https://stackoverflow.com/questions/1450551/buffered-vs-unbuffered-io

## Python
찾아보니 파이썬에서는 buffered i/o와 unbuffered i/o가 정의되어있습니다.
- bytes 단위의 object를 binary i/o라 하고, 이를 buffered io
- binary / text 단위의 stream data를 unbuffered io라 하네요.

binary io : https://docs.python.org/3/library/io.html#binary-i-o
raw io : https://docs.python.org/3/library/io.html#binary-i-o

## Example
```
# buffer
$ python example01.py

# unbuffer
$ python -u example01.py
```