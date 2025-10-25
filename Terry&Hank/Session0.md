# 第一章 程式的基本概念
<br>

# 第二章 變數及資料型別
<br>

# 第三章 程式標準輸入輸出(standard input/ standard output)
### Basic - C#
```
using System;
class HelloWorld {
    static void Main() {
        int age = 18;
        string name = "Riku";
        Console.WriteLine($"Hello I am {name}, I am {age} years old.");
    }
}
```        

### Basic - python (python3)
```
age = 18
name = "Riku"
print (f"Hello I am {name}, I am {age} years old.")
```

<br>
<br>
<br>

# 第四章 註解
### Basic - C#
```
/*
C#
单行注释→ //
多行注释→ /* ... */
*/
    
using System;
class Program 
{
    static void Main() 
    {
        string name;
        int age;
        
        // 读取输入，在stdin中输入测试
        name = Console.ReadLine();
        age = int.Parse(Console.ReadLine());
        
        Console.WriteLine($"I am {name}, I am {age} years old.");
        
    }
}
```
> 多行注释不支持嵌套

### Basic - python
```
''' 
python
单行注释 → #
多行注释 → '''...'''
'''

# 定义+读取输入，在stdin中输入测试
name = input()
age = int(input())

print (f"Hello I am {name}, I am {age} years old.")
```

<br>
<br>
<br>

# 第五章 函式(function)
### Basic - C#
```
using System;
class Program 
{
    public static int add(int a, int b)
    {
        return a + b;
    }
    static void Main() 
    {
        int result = add(3, 5);
        
        Console.WriteLine("结果 " + result);
    }
}
```
### Basic - python
```
def add(a,b):
    return a + b

result = add(3, 5)
print ("结果 " + str(result))
```

```
def add(a,b):
    return a + b

def main():
    result = add(3, 5)
    print ("结果 " + str(result))

// 显式主程序入口
if __name__ == "__main__":
    main()
```
> py两种使用方式：脚本模式（直接运行）：库/模块模式（被 import）  
当没有显式入口而是顶层代码的时候，导入时也会执行

<br>
<br>
<br>

# 第六章 數字運算
### Practice - C#
```
// 華氏溫度 = 攝氏溫度 * 9 / 5 + 32
using System;

class Program
{
    public static int CelsiusConvertToFahrenheit(int celsius)
    {
        return celsius * 9 / 5 + 32;
    }

    static void Main(string[] args)
    {
        int celsius = int.Parse(Console.ReadLine());
        Console.WriteLine(CelsiusConvertToFahrenheit(celsius));
    }
}

```
### Practice - python  
```
# 華氏溫度 = 攝氏溫度 * 9 / 5 + 32

def celsius_convert_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

def main():
    celsius = int(input())
    print(celsius_convert_to_fahrenheit(celsius))

if __name__ == "__main__":
    main()
```
> //：向下取整（floor）  
int()：朝 0 方向截断  
round()：银行家舍入（.5 → 最近偶数）  
math.floor(x+0.5) 或自写函数：实现“传统四舍五入”

<br>
<br>
<br>

# 第七章 if else條件
### &&、|| 和 &、|
1. && 与 || —— 逻辑运算符（boolean）
+ &&（逻辑与，AND）
+ ||（逻辑或，OR）

2. & 与 | —— 按位运算符（bitwise）
+ &（按位与，bitwise AND）
    + 对应二进制的每一位同时为 1，结果才为 1。
    + 没有短路机制，左右表达式都会执行。
+ |（按位或，bitwise OR）
    + 对应二进制的每一位，只要有一个为 1，结果就是 1。
    + 同样没有短路，左右表达式都会执行。
+ 适用于位运算（掩码、权限控制、底层运算）。
```
int a = 6;   // 0110 (二进制)
int b = 3;   // 0011

Console.WriteLine(a & b);  // 0010 -> 2
Console.WriteLine(a | b);  // 0111 -> 7
```
### Practice - C#
```
class Program
{
    public static char GetGrade(int score)
    {
        //异常处理
        if(score < 0 || score > 100)
        {
            throw new ArgumentOutOfRangeException("score", "must in range 0 to 100.");
        }

        if(score >= 90){return 'A';}
        else if( score >= 80){return 'B';}
        else if( score >= 70){return 'C';}
        else if( score >= 60){return 'D';}
        else{return 'F';}
    }

    static void Main(string[] args)
    {
        int score = int.Parse(Console.ReadLine());
        Console.WriteLine(GetGrade(score));
    }
}
```
> throw new ArgumentOutOfRangeException → .NET异常类，参数值超出了允许的范围

### Practice - python
```
def get_grade(score):
    if score < 0 or score > 100:
        raise ValueError("score","must in range 0 to 100.")
    
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

def main():
    score = int(input())
    print(get_grade(score))

if __name__ == "__main__":
    main()
```
> raise ValueError → py参数异常类

<br>
<br>
<br>

# 第八章 迴圈(loop)
### Practice1 - C#
```
using System;

class Program
{
    public static void PrintNextLine() // 印出一個換行
    {   Console.WriteLine("");    }
    
    public static void PrintStar() // 印出一個星號
    {   Console.Write("*");    }
    
    public static void PrintSpace() // 印出一個空格
    {   Console.Write(" ");    }

    public static void PrintTriangle(int n)
    {
        for(int i = 1; i <= n; i++)
        {
            for(int j = 0; j < i; j++)
            {
               PrintStar(); 
            }
            PrintNextLine();
        }      
    }

    static void Main(string[] args)
    {
        int n = int.Parse(Console.ReadLine());
        PrintTriangle(n);
    }
}
```
### Practice1 - python
```
def print_next_line(): # 印出一個換行
    print("")

def print_star(): # 印出一個星號
    print("*", end="")

def print_space(): # 印出一個空格
    print(" ", end="")

def print_triangle(n):
    for i in range(1, n+1):
        for j in range(i):
            print_star()  
        print_next_line()

def main():
    n = int(input())
    print_triangle(n)

if __name__ == "__main__":
    main()
```
> range(start, stop, step) → 包含start,不包含stop, 步长step 默认 = 1

### Practice2 - C#
```
using System;

class Program
{
    public static void PrintNextLine() // 印出一個換行
    {   Console.WriteLine("");    }
    
    public static void PrintStar() // 印出一個星號
    {   Console.Write("*");    }
    
    public static void PrintSpace() // 印出一個空格
    {   Console.Write(" ");    }

    public static void PrintTriangle(int n)
    {
        for(int i = 1; i <= n; i++)
        {
            for (int g = 0; g < n - i; g++)
               PrintSpace(); 
            
            for(int j = 0; j < 2*i-1; j++)
               PrintStar(); 
            
            PrintNextLine();
        }      
    }

    static void Main(string[] args)
    {
        int n = int.Parse(Console.ReadLine());
        PrintTriangle(n);
    }
}
```
### Practice2 - python
```
def print_next_line(): # 印出一個換行
    print("")

def print_star(): # 印出一個星號
    print("*", end="")

def print_space(): # 印出一個空格
    print(" ", end="")

def print_triangle(n):
    for i in range(1, n + 1):
        for g in range(n - i):
            print_space()
            
        for j in range(2 * i - 1):
            print_star()  
            
        print_next_line()

def main():
    n = int(input())
    print_triangle(n)

if __name__ == "__main__":
    main()
```
### Practice3 - C#
```
using System;

class Program
{
    public static int NumberOfFactor(int n)
    {
        int num = 0;
        for(int i = 1; i * i <= n; i ++)
        {
            if(n % i == 0)
            {
                if(i * i == n)
                    num++;
                else
                    num += 2; 
            }
        }
        return num;
    }

    static void Main(string[] args)
    {
        int n = int.Parse(Console.ReadLine());
        Console.WriteLine(NumberOfFactor(n));
    }
}
```
### Practice3 - python
```
def number_of_factor(n: int) -> int:
    num = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            if i * i == n:
                num += 1
            else:
                num += 2
        i += 1
    return num

def main():
    n = int(input())
    print(number_of_factor(n))

if __name__ == "__main__":
    main()

```

<br>
<br>
<br>


# 第九章 陣列(array) & 二維陣列（2D Array）
### 一维数组
```
int[] scores = { 85, 92, 78, 96, 88 };

// 加總所有數字
int sum = 0;
for (int i = 0; i < scores.Length; i++)
{
    sum += scores[i];
}
Console.WriteLine("總分為：" + sum);

// 找出最大值
int max = scores[0];
for (int i = 1; i < scores.Length; i++)
{
    if (scores[i] > max)
    {
        max = scores[i];
    }
}
Console.WriteLine("最高分為：" + max);
```

### 二维数组
```
int[,] matrix = {
    {1, 2, 3},
    {4, 5, 6},
    {7, 8, 9}
};

// 列印二維陣列
for (int i = 0; i < matrix.GetLength(0); i++)      // 行数
{
    for (int j = 0; j < matrix.GetLength(1); j++)  // 列数
    {
        Console.Write(matrix[i, j] + " ");
    }
    Console.WriteLine();
}

```

<br>
<br>
<br>

# 第十章：結構體（struct / class）與資料封裝
+ 结构体
+ 构造函数重载（Constructor Overloading）
+ 构造函数链（Constructor Chaining）
    > 通过this/self 复用另一个构造函数

<br>
<br>
<br>



# 第十一章：泛型（Generics）－讓你的程式更通用
T 是一個「型別參數」，可替代為任何型別，也可以使用多組例如<T , P>。
### 定义泛型类
```
public class Box<T>     // <T> 是“类型参数”
{
    private T value;

    public void Set(T val)
    {
        value = val;
    }

    public T Get()
    {
        return value;
    }
}
```
### 使用泛型类
```
class Program
{
    static void Main()
    {
        Box<int> intBox = new Box<int>();
        intBox.Set(123);
        Console.WriteLine(intBox.Get());  // 输出：123

        Box<string> strBox = new Box<string>();
        strBox.Set("Hello");
        Console.WriteLine(strBox.Get());  // 输出：Hello
    }
}
```

<br>
<br>
<br>

# 附录1 Debug
Console.WriteLine($"目前 x 值: {x}");

<br>
<br>
<br>

# 附录2 Time complexity / Space Complexity
| 分类            | 代表      | 特点         |
| ------------- | ------- | ---------- |
| O(1)          | 哈希、数组下标 | 最快         |
| O(log n)      | 二分      | 极高效        |
| O(n)          | 遍历      | 常见基线       |
| O(n log n)    | 排序      | 高效通用       |
| O(n²)         | 双循环     | 可优化目标      |
| O(2ⁿ) / O(n!) | 递归暴力    | 极慢，需剪枝或 DP |

