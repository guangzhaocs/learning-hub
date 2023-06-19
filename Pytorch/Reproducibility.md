### Random

```
import numpy as np
import random
seed = 1024
np.random.seed(seed)
random.seed(seed)
arr = [1, 2, 3, 4, 5]

# test case 1
for _ in range(3):
    print(random.randint(10, 20))

# test case 2
for _ in range(3):
    print(random.sample(arr, 2))

# test case 3
r = random.Random()
for _ in range(3):
    print(r.sample(arr, 2))
```

For test case 1 and test case 2, the resluts can be replicable. But test case 3 can not ! The seed(1024) only fix the first random, but not working for the second `Random()`.


### All seeds

```
def setup_seed(seed):
   torch.manual_seed(seed)
   os.environ['PYTHONHASHSEED'] = str(seed)
   torch.cuda.manual_seed(seed)
   torch.cuda.manual_seed_all(seed)
   np.random.seed(seed)
   random.seed(seed)
   torch.backends.cudnn.benchmark = False
   torch.backends.cudnn.deterministic = True
   torch.backends.cudnn.enabled = True
setup_seed(20)
```

Attention
```
- 对random设定seed，但是对random.Random().sample()是不管用的，也就是说中间多了一层Random()后这个种子就传不到sample()中去了
- 上述setup_seed函数要放到调用其他文件的import之前
```
