```
squeue -u chengg1 | grep 9716 | awk '{print $1}' | xargs scancel
```

```
for dir in */; do echo -n "$dir: "; find "$dir" -type f | wc -l; done
```


解压: 将当前目录下的test.tar.gz中的文件解压到当前目录我们可以使用　
```
tar -zxvf test.tar.gz

tar -zxvf /bbs.tar.zip -C /zzz/bbs   
tar -zxvf HEK293T-Mettl3-KO-rep2.tar.gz -C HEK293T-Mettl3-KO-rep2
```

```
You can install it for yourself with

module load anaconda # If you're not using this version of anaconda-module, load your version here 
pip install --user setproctitle
```

```
cat HEK293T-WT-rep3-eventalign.txt | grep "GGACT" > HEK293T-WT-rep3-GGACT.txt
cat HEK293T-Mettl3-KO-rep3-eventalign.txt | grep "GGACT" > HEK293T-Mettl3-KO-rep3-GGACT.txt

cat HEK293T-WT-rep3-GGACT.txt | awk -F "\t" '{if($10=="GGACT" ){print $7}}' > HEK293T-WT-rep3-GGACT-all-mean.txt
cat HEK293T-Mettl3-KO-rep3-GGACT.txt | awk -F "\t" '{if($10=="GGACT" ){print $7}}' > HEK293T-Mettl3-KO-rep3-GGACT-all-mean.txt
```
