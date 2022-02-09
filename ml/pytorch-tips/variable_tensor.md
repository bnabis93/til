## Variable (Deprecated, torch >= 0.4.0)
- Variable은 torch==0.4.0부터 deprecated 되었다.
    - https://pytorch.org/blog/pytorch-0_4_0-migration-guide/
    - Tensors and Variables have merged.
    - (torch >= 0.4.0) torch.Tensor and torch.autograd.Variable are now the same class.
    - (torch >= 0.4.0) torch.Tensor가 기존 variable 처럼 history 추적이 가능하다. 즉 Tensor가 variable 대체한다.
- Tensor의 wrapper
- Variable은 연산을 위한 history를 가지고 있다. (기울기 등의 값 정보를 이야기하는 듯.)
- a가 variable이라 할 때, a.data는 Tensor
```
import torch
from torch.autograd import Variable

a = Variable() #variable
b = a.data # tensor

```