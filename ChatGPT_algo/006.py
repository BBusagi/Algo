'''
## 题目描述
给定一个只包括 `'('，')'，'{'，'}'，'['，']'` 的字符串 `s`，判断字符串是否有效。

有效字符串需满足：
1. 左括号必须用相同类型的右括号闭合。
2. 左括号必须以正确的顺序闭合。

## 示例
### 示例 1:         输入：s = "()"              输出：true
### 示例 2:         输入：s = "()[]{}"          输出：true
### 示例 3:         输入：s = "(]"              输出：false
### 示例 4:         输入：s = "([)]"            输出：false
### 示例 5:         输入：s = "{[]}"            输出：true

## 解题提示
你可以使用一个栈来解决这个问题。
'''

# 自己的方法 失败
def def1(s: str) -> bool:
    s_list = list(s)
    print(s_list)
    i = 0
    j = len(s_list) - 1
    result = False
    while (i < j):
        if s[i] == "(" and s[j] == ")":
            result = True
        elif s[i] == "[" and s[j] == "]":
            result = True
        elif s[i]  == "{" and s[j] == "}":
            result = True
        else:
            return False

        i += 1
        j -= 1

    return result

# 栈方法
def def2(s: str) -> bool:
    stack = []
    for i in range(len(s)):
        current = s[i]
        if s[i] == "(" or s[i] == "[" or s[i] == "{" :
            stack.append(s[i])
        elif s[i] == ")" or s[i] == "]" or s[i] == "}" :
            if len(stack) == 0:
                return False
            check = stack.pop()
            if s[i] == ")" and check != "(":
                return False
            elif s[i] == "]" and check != "[":
                return False
            elif s[i] == "}" and check != "{":
                return False
    
    if len(stack) == 0:
        return True

# 字典方法
#()[]{}
def def3(s: str) -> bool:
    stack = []
    dic = {')':'(',']':'[','}':'{'}

    for i in range(len(s)):
        current = s[i]

        if current in dic.values():
            stack.append(current)
        elif current in dic:
            if len(stack) == 0:
                return False
            check = stack.pop()
            if dic[current] == check :

            
    

    print(dic)

    pass



s1 = "()"
s2 = "()[]{}" 
s3 = "(]" 
s4 = "{[]}"
s5 = "([)]" 

print(def3(s1))
print(def3(s2))
print(def3(s3))
print(def3(s4))
print(def3(s5))
