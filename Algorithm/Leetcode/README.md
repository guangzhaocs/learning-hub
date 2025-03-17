## sorted
custom sorting: 1636
```
students = [("Alice", 85), ("Bob", 90), ("Charlie", 85), ("Dave", 95)]

sorted_students = sorted(students, key=lambda x: (-x[1], x[0]))  # 成绩降序，名字升序
print(sorted_students)
# [('Dave', 95), ('Bob', 90), ('Alice', 85), ('Charlie', 85)]
```

```
nums = [5, 2, 9, 1, 7, 8, 4, 3, 6]

sorted_nums = sorted(nums, key=lambda x: (x % 2 == 0, x))  # 偶数优先级高
print(sorted_nums)  
# [1, 3, 5, 7, 9, 2, 4, 6, 8]  （奇数在前，偶数在后）
```

```
words = ["banana", "apple", "orange", "grape", "kiwi"]

def count_vowels(word):
    vowels = "aeiou"
    return sum(1 for char in word if char in vowels)

sorted_words = sorted(words, key=lambda x: count_vowels(x))
print(sorted_words)  
# ['grape', 'kiwi', 'banana', 'apple', 'orange']  （元音字母少的排前面）
```
