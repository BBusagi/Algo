## Python 常用语法

### 循环控制
+ break: 直接终止整个循环
+ continue: 跳过本次循环，进入下一轮

### 无穷大
- `float("inf")` / `float("-inf")`
  - `int` 没有固定上限，不像 C# 的 `int` 会受位数限制

### 除法
- `/` 有小数，**永远**返回float类型
- `//` 向下取整
  > -7 // 3   # -3   （不是 -2）
- int(a/b) 去尾
  > 设计原理，确保恒等式一致 `a == (a // b) * b + (a % b)`

### 整除与取余
- `q, r = divmod(a, b)` 等价于 `(a // b, a % b)` (整除 + 取余)

### 平方后排序
- `result = sorted(x * x for x in nums)`

### 字符处理
+ `s[::-1]` - 反转
+ `for i, c in enumerate(s):` - enumerate迭代器

+ 大小写互换
  - `s.lower()` - 大写转小写
  - `s.upper()` - 小写转大写

+ 找目标索引
  - `s.find()`: 第一个符合条件的索引位置
  - `s.rfind()`: 最后一个符合条件的索引位置
  
+ 拼接和分割
  - `"".join(iterable)` - 拼接
  - `"".join(reversed(words))` - 反转后拼接
  - `s.split()` - 默认按任意空白字符分割，并自动忽略多余空格

+ 去除字符
  - `s.lstrip()` - 连续去左边
  - `s.rstrip()` - 连续去右边
  - `s.strip()` - 两边都去

+ 常用字符判断
  - `c.isdigit()` 判断数字
  - `c.isalpha()` 判断字母
  - `c.isalnum()` 判断为字母或数字
  - `c.isspace()` 判断空格
  - `c.islower()` 判断小写
  - `c.isupper()` 判断大写

### 找目标索引
- array.index(): 找list中第一个符合条件的索引位置
- string.find(): 找第一个符合条件的索引位置
- string.rfind(): 找最后一个符合条件的索引位置

### 找最值
- `max(a, b, c, key=len)`
- `key=` 常用于“按什么规则比较”，例如按长度、绝对值、自定义字段

### `for ... else` / `while ... else`
- Python特有
- 循环如果没有执行 `break`，结束后才会进入 `else`
- 常用于“查找失败”的场景

### 创建列表 / 矩阵
- `[None] * 10`
- `matrix = [[0] * n for _ in range(n)]` 生成 `n * n` 矩阵
- 二维列表不要写成 `[[0] * n] * n`，否则每一行引用的是同一个列表

### 排序 API
- `nums.sort()` / `nums.sort(reverse=True)`
- 原地修改，返回 `None`
- `nums = sorted(nums)` / `nums = sorted(nums, reverse=True)`
- 返回新列表，不修改原对象
- 一般记为 `O(nlogn)`；Python 底层是 Timsort

### 反转 API
- `nums.reverse()`: 原地修改，返回 `None`
- `reversed(nums)`: 返回迭代器，不修改原对象

### 数据结构：队列
- queue：`from collections import deque`
- API：append() / appendleft() / pop() / popleft()
- 特点：双端操作 O(1)

- Queue：`from queue import Queue`
- API：put() get() qsize() 
- 特点：阻塞/非阻塞控制，线程安全
- 常用于：多线程控制

### 数据结构：`set`
- `s = set()`
- `s.add(x)`
- `s.remove(x)` 不存在会报错
- `s.discard(x)` 不存在也不会报错
- 特性
  - 元素唯一，自动去重
  - 支持交集、并集、差集等集合操作

### 数据结构：`SortedList`
- 有序列表结构，内部始终保持元素 自动排序
```python
from sortedcontainers import SortedList
window = SortedList()

window.add(x)
window.remove(x)
window.pop(index)  # 按下标删除
window.pop(0)      # 删除最小
window.pop(-1)     # 删除最大
```

### 数据结构：`dict`
- `d = {}`
- `len(d)` 统计的是键值对数量，和 value 是不是 `0` 无关
- `del d[c]` 删除键值对
- `d.pop(c[, default])` 删除并返回键值对
- 遍历 key: `for k in d:`
- 遍历 value: `for v in d.values():`
- 遍历键值对: `for k, v in d.items():`
- 统计频率: `d[c] = d.get(c, 0) + 1`

### 数据结构：优先级队列
```python
import heapq
heap = []

heapq.heappush(heap, x) # 插入
heapq.heappop(heap)     # 弹出最小值
heap[0]                 # 查看最小值（不弹出）
heapq.heapify(nums)     # 原地建堆
```
- Python 的 `heapq` 本质上是基于列表实现的最小堆
- 如果想模拟最大堆，常见写法是存入负优先级

```python
heapq.heappush(heap, (-priority, value))
```

- 元组会按字典序比较：先比第 1 项，再比第 2 项: `(priority, value)`

- 如果第 1 项相同，Python 会继续比较后面的值
- 所以当后面的对象不可比较时，通常要额外加一个可比较字段避免报错

## Python vs C#
### tuple
- Python 的 `tuple` 更像“轻量、不可变记录”
- 对照 C# 时，可以先类比 `ValueTuple`
- 但不完全等价：Python `tuple` 强调不可变，C# `ValueTuple` 是值类型

### 方法定义
```csharp
private int Function(int x)
{
    return 100;
}
```

```python
# Python 是动态类型
def function(x):
    return 100

# 类型注解只提供提示，不会默认强制校验
def function(x: int) -> int:
    return 100
```

### 访问修饰符
- C#: `public / protected / private / internal`
- Python 没有真正强制的访问修饰符，更多是约定
- `name`: 公共成员
- `_name`: 约定为“内部使用”
- `__name`: 触发 name mangling，不等于真正的 private

### 优先级队列
- Python [→ 数据结构：优先级队列](不同语言的语义映射表.md#数据结构：优先级队列)

```csharp
var pq = new PriorityQueue<TElement, TPriority>();

// 插入
pq.Enqueue(element, priority);

// 弹出优先级最高（默认是最小 priority）
pq.Dequeue();

// 查看队首
pq.Peek();

// 元素数量
pq.Count;

// 安全弹出
pq.TryDequeue(out var element, out var priority);
```
