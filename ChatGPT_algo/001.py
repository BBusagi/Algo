'''
题目：
反转字符串 (Easy)

描述：
编写一个函数，输入是一个字符串，输出也是一个字符串。该函数的任务是反转输入的字符串。

示例：
输入："hello"  输出："olleh"

输入："OpenAI"  输出："IAnepO"

要求：
请不要使用内置的字符串反转函数。
尝试使用不同的方法来解决这个问题，例如使用双指针或者将字符串转换为数组后进行反转。

考察点：字符串操作,数组或列表操作,双指针
'''

#1 自己的方法
def def1 ():
    str = input("")
    str_new = ""
    for i in str:
        #print(i) checkpoint
        str_new = i + str_new

    print(str_new)
'''
str_word2 都会创建一个新的字符串对象，高内存 低性能。
-> 可变的数据结构 列表
'''

#1_2 列表结构
def def1_2 ():
    str = input("")
    str_new = []
    for i in str:
        #print(i)
        str_new.insert(0,i) #插入在列表的前方

    result = ''.join(str_new) #将列表输出为字符串
    print(result)
'''
.insert 算法复杂度增加 性能较高
O(n) -> O(n^2)
'''

#2 内置反转函数
#2_1 列表切片 -> selfLearning\001.py
def def2_1():
    str = input()
    str2 = str[::-1]
    print(str2)

#2_2 reverse()方法
def def2_2():
    str = input()
    str2 = list(str)
    str2.reverse()
    
    result = ''.join(str2)
    print(result)

#2_3 reversed() 函数
def def2_3():
    str = input()
    rev_str = reversed(str) #返回的是一个反向迭代器
    str2 = ''.join(rev_str)
    print(str2)
'''
reverse()方法 列表方法 原地操作
reversed()函数 产生迭代器 返回新的
'''

#3 双指针
def def3 ():
    str = input()
    str2 = list(str)
    left, right = 0, len(str2) -1
    while left < right :
        str2[left], str2[right] = str2[right], str2[left]
        left +=1
        right -=1
    
    print(''.join(str2))
'''
时间复杂度 O(n)
空间复杂度 O(1)
'''

#4 栈
def def4 ():
    str = input()
    str_stack = list(str)
    str2 = ''
    #print(str_stack)
    while str_stack:
        str2 += str_stack.pop()
    
    print(str2)
'''
O(n) O(n)
更直观，更容易实现
'''

#5 堆
'''
不推荐
'''

#6 递归
#TODO

#main() 主程序入口
def4()