### 列表的可变性 (Mutability of Lists):

列表的内容可以在它们被创建之后被更改
-> 字符串或元组在创建后其内容是固定的

由于列表的可变性，当您传递一个列表给一个函数，该函数实际上是接收到该列表的引用，而不是它的副本。因此，如果函数修改了列表（例如，添加或删除元素），这些更改会反映到调用函数外部的原始列表上。但是，如果你将一个新的列表赋值给该引用，原始的引用不会更改。

例如：
```python
def modify_list(lst):
    lst[0] = 99  # This modifies the original list
    lst = [1,2,3]  # This assigns a new list to lst, but doesn't change the original list

my_list = [10, 20, 30]
modify_list(my_list)
print(my_list)  # Output: [99, 20, 30] and not [1,2,3]
```

### 递归的方式 (Nature of Recursion):

递归是一个函数调用自身的过程。在归并排序中，主函数`mergeSort`递归地调用自己来处理数组的子部分。

在递归调用中，每次调用都有它自己的局部变量。尽管递归调用可以修改它接收的列表（由于上述的可变性），但如果它为列表的引用分配了一个新的值，那么这个更改仅在当前的递归级别有效，不会影响到上一级或其他递归级别。

```python
left = arr[:mid]
right = arr[mid:]
mergeSort(left)  # This modifies the 'left' inside the function but doesn't replace the 'left' outside
mergeSort(right)  # Similarly for 'right'
arr = merge(left, right)  # This assigns a new list to 'arr' but doesn't affect the passed 'arr' outside
```
尽管`mergeSort(left)`和`mergeSort(right)`递归地排序了子数组，并返回了排序后的子数组，但这些返回的数组并没有真正替代原始的`left`和`right`。再加上`arr = merge(left, right)`，它为`arr`分配了一个新列表，但这个更改并没有影响到调用函数的外部`arr`。因此，原始`arr`仍然保持不变。

为了使递归工作，您需要确保在每次递归调用中，您真正地修改并更新传入的数组/子数组，而不是仅仅为它们的引用赋予新的列表。