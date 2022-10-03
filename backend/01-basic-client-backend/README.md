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

# Get output from client.py
$ ~/bono/til/backend/fastapi/baisc-client-backend main*
$ basic-client-backend ❯ python src/client.py
$ response : "packet id : 3 msg : helloworld"

```

## Optional
- Formatting also possibile in this project
```
make format

```