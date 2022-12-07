# File



```
# filepath为文件路径
import os
# 判断文件是否存在
if (os.path.exists(filepath)) :
	#存在，则删除文件
	os.remove(filepath)
```

```
def wirte(file_name, row):
    with open(file_name, 'a+', newline="") as f:
        writer = csv.writer(f)
        writer.writerow(row)     
```


```
 with open('visdial_1.0_train_all_entail.tsv', 'w', newline='') as f:
                tsv_w = csv.writer(f, delimiter='\t')
```
