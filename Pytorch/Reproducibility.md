
For Python random, read [this file](https://github.com/guangzhaocs/learning-hub/blob/main/Python/Ramdom.md) first.


torch.use_deterministic_algorithms(True)


### All seeds

```
def setup_seed(seed):
   torch.manual_seed(seed)  # for CPU
   if torch.cuda.is_available():  # for GPU
        torch.cuda.manual_seed(seed)  # 为当前GPU设置
        torch.cuda.manual_seed_all(seed)  # 为所有GPU设置
   os.environ['PYTHONHASHSEED'] = str(seed)
   np.random.seed(seed)
   random.seed(seed)
   torch.backends.cudnn.benchmark = False
   torch.backends.cudnn.deterministic = True
   torch.backends.cudnn.enabled = True
setup_seed(20)
```

torch.backends.cudnn.benchmark是python调用cudnn来加速卷积的一个机制。假如你设置这个为True的话。然后你的code出现一些地方使得这个机制被不停触发的话，可能就会导致结果不一样。

Attention
```
- 对random设定seed，但是对random.Random().sample()是不管用的，也就是说中间多了一层Random()后这个种子就传不到sample()中去了
- 上述setup_seed函数要放到调用其他文件的import之前
- torch.backends.cudnn.deterministic = True 会让训练变得非常慢
```

pytorch是基于CUDA API的，CUDA在不同设备上的伪随机数生成器不会是完全一样的，这是由设备决定的。
