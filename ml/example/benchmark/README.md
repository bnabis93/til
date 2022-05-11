# Pytorch에서 확실하게 model inference speed benchmark를 하는 방법
## 한계점
- cuda_sync는 cpu-gpu bottleneck (data copy등)이 클때 더 드라마틱하게 차이를 보일 것이다. 이에 대한 실험을 못함
- 또한 Multi gpu 상황에서도 cuda_sync가 차이를 보일 것이다. 역시나 실험 못함

## 통제해야하는 변수
- GPU warmup
- GPU 동기화
- CUDA 시간 측정

## 왜 통제해야하는가?
### GPU warmup
- GPU는 여러 state를 가질 수 있다.
    - 예를 들어 오랫동안 사용하지 않고있으면 저전력 상태로 바뀐다.
    - A modern GPU device can exist in one of several different power states. When the GPU is not being used for any purpose and persistence mode (i.e., which keeps the GPU on) is not enabled, the GPU will automatically reduce its power state to a very low level, sometimes even a complete shutdown - [ref](https://towardsdatascience.com/the-correct-way-to-measure-inference-time-of-deep-neural-networks-304a54e5187f)

### GPU 동기화
```python
torch.cuda.synchronize()

# 그러니까 이렇게 측정하지 말라 이거지.
s = time.time()
 _ = model(dummy_input)
curr_time = (time.time()-s )*1000
```
- Waits for all kernels in all streams on a CUDA device to complete. - [ref](https://pytorch.org/docs/stable/generated/torch.cuda.synchronize.html)
- PyTorch automatically performs necessary synchronization when copying data between CPU and GPU or between two GPUs. - [ref](https://leimao.github.io/blog/PyTorch-Benchmark/)
- 즉, torch에서 (정확히는 CUDA에서) GPU-CPU 연산(데이터를 복사하는 등의) 혹은 두개의 GPU간의 연산은 비동기적으로 일어나므로, benchmark시 동기화를 해주어야 한다.
- 특히 Time 특정 할때 문제가 된다. time은 cpu에서, model 연산은 gpu에서 비동기적으로 진행되기 때문이다.
    - GPU의 연산이 비동기로 일어난다면, gpu 연산이 끝나기전에 시간이 측정 될 수도 있다.

### 시간 측정
- 일반적으로 cpu에서 일어나는 일은 python의 `time` 혹은 `timeit`을 이용하여 측정한다.
- CUDA / CUDA Evnet의 경우 Pytorch의 torch.cuda.Event (CUDA Evnet Wrapper)로 측정가능하다.


## Prerequisites
- You should use GPU machine for this example.
- Maybe you should modify Makefile's cudatoolkit to the version that suits your GPU.
```bash
make env
conda activate benchmark
make setup
```

## How to run
- 실험에서 if문의 context swiching 비용은 무시한다.
```bash
sh experiment.sh
```

## Experiment result
- 참고로 cuda sync false / cuda time true의 경우 에러
```
warmup False cuda sync True cuda time True
Average time: 4.93 ms

warmup False cuda sync True cuda time False
Average time: 4.95 ms

warmup False cuda sync False cuda time False
Average time: 4.95 ms

warmup True cuda sync True cuda time True
Average time: 4.67 ms

warmup True cuda sync True cuda time False
Average time: 4.48 ms

warmup True cuda sync False cuda time False
Average time: 4.51 ms
```


## Reference
- https://towardsdatascience.com/the-correct-way-to-measure-inference-time-of-deep-neural-networks-304a54e5187f
- https://leimao.github.io/blog/PyTorch-Benchmark/
- https://pytorch.org/docs/stable/generated/torch.cuda.synchronize.html