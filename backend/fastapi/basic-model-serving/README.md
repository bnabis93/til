## Prerequisites
```bash
$ make env
$ conda activate basic-model-serving

$ make setup
```

## Download ImageNet pretrained resnet model
```bash
$ python src/ml/download_model.py
$ curl -O https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt
```

## Run the server
```bash
$ uvicorn main:src.server:app --reload

# If server is healthy
$ curl localhost:8000/healthcheck
true
```

## Client
```bash
$ python src/client.py --data data/dog.jpeg
{"prediction":"Pembroke"}

# If you want to decodeing test
$ python src/client.py --data data/dog.jpeg --decode_test 1
Decoding test
Pembroke
{"prediction":"Pembroke"}
```


## Dataset
- Use google open image
- https://storage.googleapis.com/openimages/web/visualizer/index.html?set=train&type=segmentation&r=false&c=%2Fm%2F0wdt60w
