
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
