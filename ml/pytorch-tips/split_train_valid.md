## Split train and validation dataset code example
- Using SubsetRandomSampler

```python
import numpy as np
from torch.utils.data import Dataset, DataLoader
from torch.utils.data.sampler import SubsetRandomSampler

indices = list(range(len(train_img_names)))
split = int(np.floor(conf.valid.valid_size * len(train_img_names)))
if conf.valid.shuffle_dataset:
    np.random.seed(random_seed)
    np.random.shuffle(indices)
train_indices, val_indices = indices[split:], indices[:split]
# Creating PT data samplers and loaders:
train_sampler = SubsetRandomSampler(train_indices)
valid_sampler = SubsetRandomSampler(val_indices)


train_dataloader = DataLoader(
    salobj_dataset,
    batch_size=conf.train.batch_size,
    num_workers=conf.train.num_worker,
    sampler=train_sampler,
)
valid_dataloader = DataLoader(
    salobj_dataset,
    batch_size=conf.train.batch_size,
    num_workers=conf.train.num_worker,
    sampler=valid_sampler,
)
```