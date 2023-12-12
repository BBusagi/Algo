## 列表推导式 
List Comprehension  
[expression for item in iterable if condition]

## 常用数据结构  [URL](https://docs.python.org/3/tutorial/datastructures.html#data-structures)

### 列表 (Lists)  
特点：动态大小 有序 可迭代  
切分(slicing)： [::] = [start, stop), step  
嵌套列表

### 链表

### 元组 (Tuple)  [URL](https://docs.python.org/3/library/stdtypes.html#typesseq)  
特点：不可变但成员可变, 高效  
元组解包

### 集合(Sets)  
特点：不可重复 无序 可变  
集合运算  

#### 关联数组 —— 字典（Dictionary） [URL](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)  
特点：键 唯一 不可变，动态修改，高效  
嵌套字典

### 栈（Stack）  
特点：LIFO  
用法：  
压栈（Push）- append()      
出栈（Pop）- pop()

### 队列（Queue）  
特点：FIFO   
| 用法1 List | 用法2  Deque |  
| :--------: |:-----------:| 
|          | deque() | 
| append()| append() | 
| pop()  | popleft() | 

### 双端队列（deque）  
特点： 可以从两端操作  
用法：  
deque()  
append()  appendleft()  
pop()  popleft()

### 二叉树（binary tree）
TODO