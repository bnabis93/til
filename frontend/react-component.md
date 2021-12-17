## React-component
- props를 input으로 하고, React element를 output으로 하는 일종의 함수

### props
- Component 간에는 무조건 props 로 정보를 주고 받는다. props는 Componenet 내부에서 변경되지 않는다.
- 즉, 어떠한 트리구조가 존재하고 한쪽 방향으로만 데이터가 전달된다고 이해하면 된다.
- 예를 들어 다음과 같은 코드가 있다고 하자.
- Clock이라는 component를 tick()에서 호출하고 있다. 이때 props이라는 파라미터에 child처럼 date라는게 달려있다고 이해함.

```
function Clock(props) {
  return (
    <div>
      <h1>Hello, world!</h1>
      <h3>It is {props.date.toLocaleTimeString()}.</h3>
    </div>
  );
}

function tick() {
  ReactDOM.render(
    <Clock date={new Date()} />,
    document.getElementById('root')
  );
}

setInterval(tick, 1000);
```

### state

