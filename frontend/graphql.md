[TODO] : Union, Interface
[TODO] : Data paging (schema)

# GraphQL
- API를 만들 때 사용 할 수 있는 쿼리언어.
- 쿼리에 대한 데이터를 받을 수 있는 런타임.
- 사전 정의된 데이터의 Type 시스템을 사용하여 Query를 실행하기 위한 server-side 런타임이다. 
    - 런타임이란 어떤 언어가 동작 할 수 있는 환경이다. 
- 밑의 예제에 대한 실습은 여기서 -> http://snowtooth.moonhighway.com/

## Why GraphQL?
- 웹 클라이언트가 데이터를 서버로부터 효율적으로 가져오는 것을 목적으로 하는 query 언어이다.
### 1. Over-fetching
- 예를 들어 RESTful 하게 api를 구현하여 이를 통하여 데이터를 받아온다고 하자.
    - 특정한 데이터만을 받아오고 싶은데, 때때로 그 데이터를 위해 통째로 데이터를 받는 겨웅가 있다.
    - 필요한 데이터만 가져오고 싶다. 
- Over-fetching이라는 것은 불필요하게 많은 정보를 얻게 되는것을 말한다. 
### 2. Under-fetching
- 예를 들어 RESTful 하게 api를 구현하여 이를 통하여 데이터를 받아온다고 하자.
    - A라는 데이터를 얻고 그로부터 B라는 데이터를 얻을 수 있다고 하자.
    - 우리는 B라는 데이터를 여러번 요청하려한다.
    - 바로 B를 얻을 수 없기 때문에 요청횟수가 많아지게 된다. 
- Unver-fetching은 한번에 정보를 얻을 수 없기 때문에 요청의 횟수가 늘어나는것을 말한다.

### 3. Endpoints 관리의 용이성
- N개의 endpoints를 만들어 관리해야하는 RESTful 방식과 달리 설계상 하나의 endpoints로 끝낼 수 있다.
- 이 부분은 생각을 좀 더 해봐야 겠다. 

## SQL과의 차이
- SQL
    - 데이터는 오직 읽고(Read, SELECT), 쓰고(Wirte, INSERT), 갱신하고(Update, UPDATE), 삭제(Delete, DELETE)만 할 수 있다.
    - Query를 DB로 날린다. 
- GraphQL
    - 웹 적용에 최적화된 쿼리 언어. 쿼리를 API로 보낸다. 
    - Query를 여러 환경에 날릴 수 있다. (DB, REST API, 다른 GraphQL api 등)
    - SQL의 SELECT -> GraphQL의 Query와 같음 / INSERT, UPDATE, DELETE -> GraphQL의 Mutation과 같음
    - Subscription 이라는게 존재함 (웹에서 쓰기 위해서)

### Query overview
- Query 작업으로 데이터를 요청 할 수 있다. (== SELECT)
    - 이때 요청 할 데이터를 field로 적어놓는다.    
    - field란 DB에서 세로방향의 col 값. 각 record에 대한 개별적인 속성값이라 보면 된다.
    - 다음 코드를 보면 name과 status라는 field를 요청 하고 있다. 
    - query를 root type이라고도 하는데, 쿼리 하나가 하나의 작업을 하고, 이게 곧 쿼리작업의 root를 의미하기 때문이다.
```
query{
    allLifts{
        name
        status
    }
}
//여러 종류의 데이터 한번에 요청
query liftsAndTrails{
    liftCount(status : OPEN){
        allLifts{
            name
            status
        }
    }
    allTrails{
        name
        difficulty
    }
}
```
#### Selection set
- 필요한 field를 중괄호로 감싸는데, 이를 selection set라 한다. 
    - allLifts field에서 name, status라는 field를 요청하고 있다. name, status는 allLifts의 selection set이다. 
```
query{
    allLifts{
        name
        status
    }
}
```

#### Alias
- 응답 객체의 field명을 다르게 받고 싶을 때 사용. field에 별명을 부여한다.
- alias name : filed name 의 형태로 alias를 지정한다.
- query에 대한 답을 우리가 지정한 alias name으로 받게된다.
```
query liftsAndTrails{
    open : liftCount(status: OPEN)
    chairlifts : allLifts{
        liftName : name
        status
    }
    skiSlopes: allTrails {
        name
        difficulty
    }
}
```

#### Query filtering
- query에 arguments를 넘기는 방식으로 query 응답에 대한 필터링을 할 수 있다.
- 다음은 liftCount가 OPEN인 데이터만 보게 된다.
```
query liftsAndTrails{
    open : liftCount(status: OPEN)
    chairlifts : allLifts{
        liftName : name
        status
    }
```

#### Field type -> Scalar & Object
- GraphQL 쿼리어에서 Field는 Scalar 혹은 Object type을 가진다.
- Scalar는 일종의 원시타입. 다음의 5가지 타입이 가능하다.
    - Int, Float, String, Boolean, ID
    - ID는 유일 문자열 반환
- Object는 스키마에 정의한 필드를 그룹으로 묶어놓은 것
- 다음 쿼리는 jazz-cat이라는 아이디를 가지는 Lift에 대한 데이터를 요청하고 있다.
    - Lift의 Selection set을 보면 capacity가 있다. 이는 Scalar type이다.
    - trailAccess는 Object type이다. 
    - 하나의 필드값을 특정 지을 수 있으면 Scalar type을 가지고, 여러 필드가 합쳐진 형태라면 Object type이라 볼 수도 있을 것 같다.
- 이를 Edge-Node의 관계로 볼수도 있다.
```
query trailsAccessedByJazzCat{
    Lift(id : "jazz-cat"){
        capacity
        trailAccess{
            name
            difficulty
        }
    }
}
```

#### Fragment
- Selection set의 일종이다. 재사용이 가능하다.
- 중복되는 정보가 있는 경우 fragment 를 이용하여 중복을 줄일 수 있다.
- 밑의 쿼리를 보면 name, status, capacity, night, elevationGain이 중복되는것을 확인 할 수 있다.
```
query {
    Lift(id : "jazz-cat){
        name
        status
        capacity
        night
        elevationGain
        trailAccess{
            name
            difficulty
        }
    }
    Trail(id : "river-run"){
        name
        difficulty
        accessedByLifts{
            name
            status
            capacity
            night
            elevationGain
        }
    }
}
```
- 이럴때 Fragment를 생성한다. 
- liftInfo라는 fragment를 생성하였으며 이는 Lift type에 대한 selection set이다.
- 관리의 편의성을 위하여 중복되는것이 있으면 fragment를 사용하면 좋을듯
```
fragment liftInfo on Lift{
    name
    status
    capacity
    night
    elevationGain
}
query {
    Lift(id : "jazz-cat){
        ...liftInfo
        trailAccess{
            name
            difficulty
        }
    }
    Trail(id : "river-run"){
        name
        difficulty
        accessedByLifts{
            ...liftInfo
        }
    }
}

```

#### Interface & Union type
- [TODO]

### Mutation overview
- INSERT, UPDATE, DELETE 을 위해서는 mutation을 사용해야함. (쿼리는 읽기전용)
- 이 역시도 사전 정의된 필드를 사용한다.
- API 스키마에서 mutation에서 사용 할 수 있는 필드를 정의한다.
- 다음의 mutation은 다음과 같이 동작한다.
    - title:"No Scrubs", numberOne : true, performerName : "TLC"인 음악을 DB에 추가한다.
    - Selection-set이 존재하는데, 이런 경우 음악 생성이 완료되면 selection-set에 있는 필드값을 반환받는다.
    - 예를 들어 id : "~~~~" , title"~~~", numberOne: "~~~" 을 반환받게 된다.
- $ 키워드를 이용하여 변수 사용 가능
```
mutation createSong{
    addSong(title:"No Scrubs", numberOne : true, performerName : "TLC"){
        id
        title
        numberOne
    }
}
```


### Subscription overview
- 실시간 데이터 변경 내역을 알 수 있다. 말그대로 구독해버리는 것이다. 
- 특정 데이터를 계속해서 관찰(observe)하고, 상태 혹은 값이 변경되면 알려준다. 
- 예를 들어 다음과같이 subscription을 작성하고 mutation 하여 데이터를 바꾸어 주게 될 때, subscription은 값을 반환한다.
```
subscription{
  liftStatusChange{
    name
    capacity
    status
  }
}


mutation closeLift{
  setLiftStatus(id: "astra-express", status : HOLD){
    name
    status
  }
}

```

### Introspection
- 현재 API 스키마의 세부 사항에 관한 쿼리 작성 가능
- 스키마에 대해 알 수 있다. 
- 문서를 보는것. 해당 스키마에 어떤 타입들이 있는지 등 정보를 알 수 있다.

### Abstract syntax tree
- GraphQL API로 쿼리르 ㄹ보낼 때 문자열은 Abstract syntax tree로 파싱된다.
- 파싱된 결과를 유효성 검사한다.
- 이름 그대로 트리구조, 계층화 된 구조를 하고 있다.
    1. 쿼리를 받으면 어떤 거대한 문자열이 온다고 보면 된다.
    2. 이를 더 작은 단위로 쪼갠다. (lexing, lexical analysis, 어휘화)
    3. 충분히 작은 단위로 쪼갠 후, AST로 가공한다. (트리구조로 바꾼다.)
    
### Schema
- 어떤 Type을 가질지, 어떤 mutation, query를 가질지 사전 설계를 하는 것
- 이를 위하여 SDL(Schema Definition Language) 을 지원한다.

### Type
- GraphQL의 핵심 단위
- 객체에 대한 이름. 
- Type 내에는 field가 존재한다. field는 특정 종류의 데이터를 반환한다.
- 다음은 Photo 라는 type을 정의하고, 내부에 여러 field를 정의한 것 이다. 
    - !는 null을 허용하지 않겠다는 의미이다. 
```
type Photo{
    id : ID!
    name : String!
    url : String!
    description : String
}
```
### Scalar type과 enumeration type
- 커스텀 scalar type 지정 가능. 이또한 어딘가에 사전 정의된것으로 추정되는데... 확실하지 않음
- 예를들어 밑에는 DataTime이라는 scalar type을 만들었음.
- 열거또한 일종의 scalar typeㅇ다. 
- 반환해야 하는 문자열 값을 미리 지정 할 수 있다. 
- PhotoCategory는 SELFIE, PORTRAIT, ACTION, LANDSCAPE, GRAPHIC 중 하나만 값으로 반환이 가능하다. 
```
scalar DataTime

enum PhotoCategory{
    SELFIE
    PORTRAIT
    ACTION
    LANDSCAPE
    GRAPHIC
}
```
### 연결과 리스트
- GraphQL 타입의 리스트도 반환 가능하다. [String] 처럼 [] 로 감싸면 된다. 
- GraphQL의 연결에는 최대한 방향성이 없도록 설계하는것이 좋다. 
### 일대일 연결
- A라는 타입이 B라는 타입에 종속적일 때.
- 예를 들어 A타입 내부에 B라는 타입이 들어있을때. (이럴때는 방향성이 생긴다.)
### 일대다 연결

### 다대다 연결

### 인자
- Schema에도 인자를 넣을 수 있다. 
- 만약 스키마 타입에 인자를 넣어줬다면 쿼리를 날릴때도 꼭 그 인자값을 포함해야한다. (물론 스키마에서 null 허용하면 괜춘)
    - 만약 null 반활 할 수 있게 만들면, 쿼리 날릴 때 인자는 옵션이 된다.
- 커스텀 스칼라 타입을 인자로 넣어주고, 해당 값중 하나를 가지도록 할 수도 있다. 
- Data paging 이라는 기능도 있는데, 하나의 웹 페이지에 나올 데이터의 양을 정해준다. -> 여러개의 인자값으로 조절하는데, 뭔가 명확하지 않다.
- sort, sortBy 값으로 소팅도 가능하다. 
```
enum PhotoCategory{
    SELFIE
    PORTRAIT
    ACTION
    LANDSCAPE
    GRAPHIC
}

type Query{
    allPhotos(category : PhotoCategory): [Photo!]!
}
```
### 뮤테이션(mutation)
- 뮤테이션도 반드시 스키마에 사전 정의해야 한다.
```
type Mutation{
    postPhoto{
        name: String!
        description : String
        category : PhotoCategory = PORTRAIT
    }:Photo!
}

schema{
    query : Query
    mutation : Mutation
}
```

### Input 타입
- 인자에서만 사용된다. 
- 뭔가 mutation에서 사용하는 커스텀한 타입을 만드는 것 같다. (쿼리의 enum같이) 

### Return 타입


## Reference
- 웹 앱 API 개발을 위한 GraphQL