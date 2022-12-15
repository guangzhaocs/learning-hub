# File



```
# filepath为文件路径
import os
# 判断文件是否存在
if (os.path.exists(filepath)) :
	#存在，则删除文件
	os.remove(filepath)

# 判断目录是否存在
if not os.path.exists(dirs):
    os.makedirs(dirs)
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

```
    from csv import reader
    with open("debug_tmp_realdata/0.csv", 'r') as read_obj:
        csv_reader = reader(read_obj)
        for i, row in enumerate(csv_reader):
            if i == 0:
                signal_arr = np.array([float(i) for i in row])
                break
```
