## Prerequisites
```bash
$ make env
$ conda activate basic-model-serving

$ make setup
```

## Download ImageNet pretrained resnet model
```bash
$ python src/ml/download_model.py
```

## Run the server
```bash
$ uvicorn main:src.server:app --reload

# If server is healthy
$ curl localhost:8000/healthcheck
true
```

