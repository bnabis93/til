# Torch 에서의 두가지 모델 저장 방법

[https://pytorch.org/tutorials/beginner/saving_loading_models.html](https://pytorch.org/tutorials/beginner/saving_loading_models.html)

## Pytorch’s 3 core function for model save and load

1. **[torch.save](https://pytorch.org/docs/stable/torch.html?highlight=save#torch.save): Saves a serialized object to disk. This function uses Python’s [pickle](https://docs.python.org/3/library/pickle.html) utility for serialization. Models, tensors, and dictionaries of all kinds of objects can be saved using this function.**
    1. 내부적으로 저장으로 위하여 python의 pickle 을 이용한다. 
        1. pickle 공식문서 - [https://docs.python.org/3/library/pickle.html](https://docs.python.org/3/library/pickle.html)
        2. pickle은 python object structure을 serialization - deserialization 하는 binary protocol을 지원한다.
    2. Model, tensor, dict 등 모든 형태의 object 저장 가능
        1. 이거때문에 고생한거지. 
    3. Torch에서는 weight값만을 저장 할 수도 있고, model과 weight값을 같이 저장 할 수도 있다.
2. **[torch.load](https://pytorch.org/docs/stable/torch.html?highlight=torch%20load#torch.load): Uses [pickle](https://docs.python.org/3/library/pickle.html)’s unpickling facilities to deserialize pickled object files to memory. This function also facilitates the device to load the data into (see [Saving & Loading Model Across Devices](https://pytorch.org/tutorials/beginner/saving_loading_models.html#saving-loading-model-across-devices)).**
    1. unpickling (byte, binary to object)
3. **[torch.nn.Module.load_state_dict](https://pytorch.org/docs/stable/generated/torch.nn.Module.html?highlight=load_state_dict#torch.nn.Module.load_state_dict): Loads a model’s parameter dictionary using a deserialized *state_dict*. For more information on *state_dict*, see [What is a state_dict?](https://pytorch.org/tutorials/beginner/saving_loading_models.html#what-is-a-state-dict).**

### state_dict

- state_dict은 dict 이다.
- state_dict은 model의 각 layer의 parameters를 dict로 mapping 해놓은 것 이다.
    - 학습 가능한 parameters 만 가지고 있다.
    - Optimizer는 상태 및 hyperparam 저장된다.

## 공식문서에서는 킹받게도 Save/Load `state_dict` 을 추천하고 있다.

```python
torch.save(model.state_dict(), PATH)

model = TheModelClass(*args, **kwargs)
model.load_state_dict(torch.load(PATH))
model.eval()
```

- 아니 도데체 무슨이유로?
    - 혹시 용량이 좀 차이나나 싶었는데, 차이가 거의 없다.
- state_dict을 이용하여 모델을 저장하면 모델의 learnable parameters 만 저장이 된다.
- 본문에서는 이러한 방법이 유연한 구조를 가지고 갈 수 있어 좋다고 한다.

from [https://wandb.ai/wandb/common-ml-errors/reports/How-to-Save-and-Load-Models-in-PyTorch--VmlldzozMjg0MTE](https://wandb.ai/wandb/common-ml-errors/reports/How-to-Save-and-Load-Models-in-PyTorch--VmlldzozMjg0MTE)

### Pros:

PyTorch internally relies on Python's **pickle module**. Python dictionary can **easily** be pickled, unpickled, updated, and restored. Thus saving model using state_dict offers more flexibility.

You can also save the optimizer state, hyperparameters, etc., as key-value pairs along with the model's state_dict. When restored, you can access them just like your usual Python dictionary. We will see how it's done in the later section.

### Cons:

You will need the model definition to load the state_dict.


### Save/Load Entire Model

```python
torch.save(model, PATH)

# Model class must be defined somewhere
model = torch.load(PATH)
model.eval()
```

- 모델 전체를 구현하는것은 위와같이 직관적인 구현이 가능하다.
- 전체 모델을 저장한다고 하지만, 내부적으로 사용되는 pickle module은 모델 그 자체를 저장하는게 아니다.
    - Serialize 하여 저장하고, 따라서 특정 class 혹은 dir에 종속적이게 된다.
    

from [https://wandb.ai/wandb/common-ml-errors/reports/How-to-Save-and-Load-Models-in-PyTorch--VmlldzozMjg0MTE](https://wandb.ai/wandb/common-ml-errors/reports/How-to-Save-and-Load-Models-in-PyTorch--VmlldzozMjg0MTE)

### Pros:

Easiest way to save the entire model with the least amount of code.

The saving and loading API is more intuitive.

### Cons:

Since Python's pickle module is used internally, the serialized data is **bound to the specific classes and the exact directory structure** is used when the model is saved. Pickle simply saves a path to the file containing the specific class. This is used during load time.

As you can imagine, the code might break after refactoring as the saved model might not link to the same path. Using such a model in another project is hard as well since the path structure needs to be maintained.

- version dependency가 생길수 있다는 말로 들린다.
    - 내가 이해하기로는 python 0.x 버전에서 전체 model로 저장 한 후, 1.x 버전에서 사용하려고하면 문제가 생길수도 있다는 말로 보인다.
- Model Class의 경로를 저장하기 때문에 경로 문제가 생길 수 있다고하는데, 이부분은 잘 모르겠다.

해보니까...
- model class 자체를 저장해버린다.

### model.eval()

- train 할 때와, eval (inference라고 생각해도 될듯) 할 때, 다르게 동작하는 친구들을 위한것
    - `Dropout`
    - `BatchNorm`
- 위와같은 친구들을 off해주는 역할을 한다.
- eval()과 no_grad()에 대해 설명한 좋은 글
    - [https://yuevelyne.tistory.com/10](https://yuevelyne.tistory.com/10)