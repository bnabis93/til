## What is the TensorRT
- Nvidia에서 만든 high performance inference를 위한 SDK이다. 
- TensorRT는 Deep learning framework (pytorch, tf, mxnet 등)과 호환가능하도록 디자인 되었다.
- 결국, TensorRT의 목적은, 위와 같은 deep learning framework에서 만들어진 모델을 Nvidia hardware에 최적화 하여 효율적이고 빠르게 (high performance) inference 하게 하는것이 그 목적이다.


## Basic TensorRT workflow
- 기본적인 workflow는 5단계로 이루어진다. 
1. Export Model : Onnx 혹은 tf saved model 형태를 가진 모델로 변환. 즉 torch 썻으면 onnx로 변환시켜야 한다. - [ref](https://docs.nvidia.com/deeplearning/tensorrt/quick-start-guide/index.html#save-model)
2. Select Batch Size : Batch size를 정하는 단계. 런타임까지 batch를 fix하지 않으면 TensorRT가 dynamic batching을 한다. 이게 더 좋은거아냐? 할 수도 있는데, Fixed batch를 가지면 high performance를 위한 추가적인 최적화를 할 수 있다. 
3. Select Precision : TensorRT supports TF32, FP32, FP16, and INT8 precisions.
4. Convert The Model : Onnx to TensorRT engines이 일반적으로 TensorRT engine으로 컨버팅 하는 방식이다. e.g. resnet50/model.onnx -> resnet_engine.trt. (using `trtexec`)
5. Deploy The Model : TensorRT를 어떻게 run 할지 결정해야 한다. (runtime 결정). 두개의 일반적인 runtime ->  runtime which has C++ and Python bindings, and a native integration into TensorFlow