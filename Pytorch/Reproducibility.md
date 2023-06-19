
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
