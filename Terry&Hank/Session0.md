### Basic
+ C#
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

+ python(=python3)
```
age = 18
name = "Riku"
print (f"Hello I am {name}, I am {age} years old.")
```

### Basic2
+ C#
```
/*
C#
单行注释→ //
多行注释→ （不支持嵌套）
*/
// 多行注释→ /* ... */
    
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

+ python
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

### Basic3
+ C#
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
+ python
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

### Practice
+ C#
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
+ python  
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