### Generate mask according to the sequence length
```
seq_lengths = torch.Tensor([7,10,4])
mask = torch.arange(seq_lengths.max().item())[None, :] < seq_lengths[:, None]
```
![image](https://github.com/user-attachments/assets/9ac29d9d-9e7a-45e9-ac27-56d972a71d4a)


```
mask.float()
```
![image](https://github.com/user-attachments/assets/477b4aa2-49f1-491c-94cd-2f1165b9b187)


### Reference
- 1. https://blog.csdn.net/xiangduixuexi/article/details/108631890
  
