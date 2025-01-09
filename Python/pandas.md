
## pands to dict
```
data = {'Fruit': ['Apple', 'Pear', 'Banana'],
        'Num':  [3, 2, 5],
        'Price': [10, 9, 9]}
df = pd.DataFrame(data)

name2num_dict = df.set_index('Fruit')['Num'].to_dict()
# {'Apple': 3, 'Pear': 2, 'Banana': 5}

num2name_dict = df.set_index('Num')['Fruit'].to_dict()
# {3: 'Apple', 2: 'Pear', 5: 'Banana'}

price2name_dict = df.set_index('Price')['Fruit'].to_dict()
# {10: 'Apple', 9: 'Banana'}
```

```
for index, row in df.iterrows():
    if row['flag'] == 3:
        df.loc[index, 'model_stdv_un'] = 0.0
```

```
>>> df_dict = df.to_dict('records')
[{'Fruit': 'Apple', 'Num': 3, 'Price': 10}, {'Fruit': 'Pear', 'Num': 2, 'Price': 9}, {'Fruit': 'Banana', 'Num': 5, 'Price': 9}]

>>> df_dict_select = df[df['Price'] == 9].reset_index().to_dict('records')
[{'index': 1, 'Fruit': 'Pear', 'Num': 2, 'Price': 9}, {'index': 2, 'Fruit': 'Banana', 'Num': 5, 'Price': 9}]
```
