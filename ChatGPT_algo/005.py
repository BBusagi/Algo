'''
题目：
最长公共前缀(Easy)

描述：
编写一个函数，输入是一个字符串数组，输出是这些字符串的最长公共前缀（Longest Common Prefix, LCP）。
如果不存在公共前缀，返回空字符串 `""`。

示例：
输入: ["flower", "flow", "flight"]      输出: "fl"
输入: ["dog", "racecar", "car"]         输出: ""

要求：
1. 所有输入只包含小写字母 `a-z`。
2. 请不要使用内置的库函数来直接求解。

提示：
- 你可以假设所有输入都是非空字符串。
这道题目主要考察字符串操作和数组遍历，也会涉及到一些边界条件的处理。希望你能通过这个问题更好地理解这些基础概念。

考察点：字符串操作 数组遍历 边界条件处理
'''

#1 自己的方法
def def1 (words=None):           #建议参数使用不可变类型
    if words is None: words = []
    lcp = ""
    index_max = min(len(word) for word in words )

    for j in range(index_max):
        current = words[0][j]
        for i in range(1, len(words)):
            if current != words[i][j]: 
                return lcp
        lcp += current
    return lcp

# 逐字符比较
def def1_chatGPT(strs):
    if not strs:
        return ""
    
    lcp = ""
    for i in range(len(strs[0])):
        current_char = strs[0][i]
        for string in strs[1:]:
            if i >= len(string) or string[i] != current_char:
                return lcp
        lcp += current_char
    return lcp

#2 首尾比较
def def2 (words):
    result = ""
    min_word = min(words)
    max_word = max(words)

    for i in range(len(min_word)):
        if min_word[i] == max_word[i]:
            result += min_word[i]
        else: 
            return result
    
    return result

#input1 = input()
#words_input = input1.split(",")

#words_input = ["flower", "flow", "flight"]
#words_input = ["dog", "racecar", "car"]
words_input = ["waweevrsfds", "wawfsefw", "wawdsdfer","wawfsdwqwe"]

print(words_input)
print(def2(words_input))