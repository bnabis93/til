# Pytorch -> ONNX Deployment
- https://gaussian37.github.io/dl-pytorch-deploy/

## Pytorch model save & load
- torch에서는 weights 값만 저장하는걸 추천
- Model 전체를 저장하게 되면, 내부 저장 방식(pickle module)으로 인해 해당 모델을 import 하는 부분까지 같이 저장됨
    - 따라서 폴더 자체를 저장할게 아니면, weights 값만 저장하는것을 추천한다.
```
python
torch.save(model.state_dict(), PATH)

model = TheModelClass(*args, **kwargs)
model.load_state_dict(torch.load(PATH))
model.eval()
```

## ONNX (Open Neural Net eXchange)
- https://onnx.ai/
- https://github.com/onnx/onnx
- Open Neural Network Exchange (ONNX) is an open ecosystem that empowers AI developers to choose the right tools as their project evolves. ONNX provides an open source format for AI models, both deep learning and traditional ML. 
- Facebook + MS가 개발을 주도함
- 특정 framework에서 작성한 모델을 다른 프레임워크에서 사용가능하게 해줌 (e.g. pytorch -> onnx ->tf / pytorch -> onnx -> Caffe2) 

### ONNX export
- torch는 동적 계산 그래프를 사용하므로, export 할 때, 네트워크 계산을 한번 해야한다.
- 입력 데이터에 대해 dummpy data를 만들어 이를 이용한다.


