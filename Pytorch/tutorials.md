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

### Masked fill
```
a = torch.arange(0, 30).view(3, 10)
a_fill = a.masked_fill(mask, 100)
```
![image](https://github.com/user-attachments/assets/719e0b49-19f4-49ec-a670-7af4f4c9dd52)


### Masked select
```
a_select = a.masked_select(mask)
```
![image](https://github.com/user-attachments/assets/cb935f7e-d991-45a3-9330-7a9720e9d349)



### Reference
- https://blog.csdn.net/xiangduixuexi/article/details/108631890
  
