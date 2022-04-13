## TensorRT는 implicit / explicit batch 를 지원한다.
- implicit, explicit 이름만 봐도 짐작이 간다.
- implicit batch는 알아서 해주는 dynamic batch와 같은 녀석일 것 같고, explicit batch는 우리가 사전 설정한 batch 값을 가질 것 같다.

### Implicit batch
- every tensor has an implicit batch dimension and all other dimensions must have constant length.
- This mode was used by early versions of TensoRT, and is **now deprecated** but continues to be supported for backwards compatibility.
- Deprecated 되긴 했지만 지원은 한다.


### Explicit batch
- all dimensions are explicit and can be **dynamic** that is their length can change at execution time.
- It is also required by the ONNX parser.
- Explict batch의 설명을 보니 이해가 간다. expicit 하게 지정하지만, dynamic batching이 가능하다. 일종의 범위 혹은 최대값을 지정하는게 아닐까 싶다.


### Implicit vs explicit
- For example, consider a network that processes N images of size HxW with 3 channels, in NCHW format. At runtime, the input tensor has dimensions [N,3,H,W].
    - In explicit batch mode, the network specifies [N,3,H,W].
    - In implicit batch mode, the network specifies only [3,H,W]. The batch dimension N is implicit.
- 아에 런타임에서 input을 줄 때, 배치부분을 implicit하게 선언해버리네.
- 예를 들어 다음과 같이 input config를 선언하면 explicit batch를 사용하게 된다.
```
input [
  {
    name: "input"
    data_type: TYPE_FP32
    dims: [1, 3, 320, 320 ]
  }
]
```
### Implicit batch의 단점
- Implicit batch mode에서는 다음의 것들을 할 수 없다.
    - reducing across the batch dimension
    - reshaping the batch dimension
    - transposing the batch dimension with another dimension
- Batch가 내부적으로 포함되지만, implicit하게 선언되기 때문에 생기는 문제가 아닐까 한다.

### Explicit batch mode erases the limitations - the batch axis is axis 0.
- Explicit batch를 하면 위와 같은 문제가 사라진다.

### trtexec example
- Resnet example https://github.com/triton-inference-server/dali_backend/tree/main/docs/examples/resnet50_trt
```
trtexec --onnx=model.onnx --saveEngine=./model_repository/resnet50_trt/1/model.plan --explicitBatch --minShapes=input:1x3x224x224 --optShapes=input:1x3x224x224 --maxShapes=input:256x3x224x224 --fp16
```
- --minShapes and --maxShapes specify the range of dimensions for each network input and --optShapes specifies the dimensions that the **auto-tuner should use for optimization.** For more information, refer to the Optimization Profiles section in the NVIDIA TensorRT Developer Guide.
- optShape는 optimization에 사용되는 auto-tuner이다. 이를 어떻게 써야할까. 

### 주의사항
- onnx 모델을 저장 할 때, explicit batch를 위한 명시를 해주어야 한다. 예를 들어 다음과 같다.
```
torch.onnx.export(
        model,
        dummy_input,
        save_path,
        opset_version=12,
        input_names=["input"],
        output_names=["output"],
        dynamic_axes={
            "input": {0: "batch_size", 2: "height", 3: "width"},
            "output": {0: "batch_size"},
        },
    )
```


## Reference
- https://docs.nvidia.com/deeplearning/tensorrt/developer-guide/index.html#explicit-implicit-batch