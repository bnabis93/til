## Prerequisites
```
$ make env
$ conda activate baisc-client-backend

$ make setup
```

## How to play
1. Run server
```
$ make run-server

```
2. Healthcheck api (get api)
```
$ curl localhost:8000/healthcheck
true
```

3. Client example (post api)
```
# Open new terminal 
$ python src/client.py
response : "packet id : 3 msg : helloworld"
```

## APIs
1. healthcheck
```
$ curl localhost:8000/healthcheck
```
2. helloworld
```
$ curl localhost:8000/helloworld
```
3. simplepost
```
$ curl -d '{"dummy_id": "3", "msg": "simple post example"}' -H "Content-Type: application/json" -X POST http://localhost:8000/simplepost
```

## Optional
- Formatting also possibile in this project
```
$ make format

```