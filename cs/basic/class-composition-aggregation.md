## Class composition & aggregation

### Association
- 두 클래스간의 관계를 말한다. 
    
### Aggregation
- unidirectional association
- has-a relationship. 클래스간의 포함관계를 나타낸다.
- aggregation is when an object of one class can own or access the object of another class.
- 두 클래스가 aggregation 관계에 있다면, 어느 한쪽이 다른 클래스를 소유하거나, 접근 가능하다.

### Composition
- In composition, objects can not exist independently.
- whole-part relationship. Aggregation의 특수 case. 좀 더 강한 포함 관계로 이해했다. 
- 두 클래스가 Composition 관계에 있다면, 어느 한쪽이 다른 한쪽을 소유하고 있는것이다. 따라서 소유한 클래스가 소멸되면 소유당한 클래스도 소멸된다.

## 이 둘의 차이
- 위의 설명만 보았을 때는, Aggreagation이나 Composition이나 포함관계로 밖에 보이지 않는다.
- Aggregatin은 단순히 두 클래스가 연관이 있고, 그 연관관계가 has-a 관게 즉, 포함 관게를 가지는 것을 말한다.
- Composition은 여기서 더 나아가 한쪽 클래스가 ownership을 가지고 있다. 즉, class lifetime 까지 관여하는것이다. 
- 정리하자면 Aggregation 관계는 단순 포함 관계지만 두 클래스가 어떠한 주종 관계를 가지지 않아 생명주기에는 영향이 없는것이고, Composition은 좀 더 강화된 Aggregation 관계로써, lifetime까지도 관여하는 관계가 되는것.
- Aggregation 관계인 클래스 하나를 없애도 다른 한쪽에 영향을 주지 않지만, Composition 관계인 클래스를 없애면 다른 한쪽도 없어진다. (파일과 폴더의 관계를 생각하면 좋다.)
- 마치 연인과 배우자의 관계... 같다고 할 수 있다.


## Code example
### Aggregation code
- [Aggregation code](./aggregation.py)
- Student class와 Department class를 만듦.
- Department class는 Student class와 Assciation 되어있다. 정확히는 Department class는 student class를 포함한다.
- 하지만 Department class를 제거하더라도 Student class에 영향을 주지는 않는다. 
- 포함관계에 있지만, 서로의 life cycle 에는 영향을 주지 않는다. 

### Composition code
- [Composition code](./composition.py)
- Department 내부에 Student가 선언되었다.
- 내부에서 선언되었으니 Department는 student의 기능도 사용가능하다.
- 따라서 Department가 소멸되면 student도 소멸된다. 주종 관계를 가지게 된다.
- 이 상황에서 Student object는 독립적일 수 없다.



## Reference
- https://www.guru99.com/uml-aggregation-vs-composition.html
- https://faun.pub/association-aggregation-composition-python-ec9947832cbd