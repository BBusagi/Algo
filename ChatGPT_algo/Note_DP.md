### 动态规划（Dynamic Programming）

动态规划是一种用于解决最优化问题的算法技术。它的核心思想是将一个复杂的问题分解成一系列更简单的子问题，并存储这些子问题的解以避免重复计算。动态规划通常用于解决那些具有“最优子结构”和“重叠子问题”的问题。

#### 基本概念：

1. **最优子结构**：一个问题的最优解包含其子问题的最优解。
2. **重叠子问题**：在求解问题的过程中，多次遇到相同的子问题。
3. **状态**：用于描述问题的某种属性或者条件。
4. **状态转移方程**：描述状态之间如何转移的数学方程。

#### 基本对策方案：

1. **问题分解**：将原问题分解为一系列更小的子问题。
2. **定义状态**：明确状态的定义，以及状态之间如何转移。
3. **找出状态转移方程**：根据问题的具体情况，找出描述状态如何转移的方程。
4. **初始化边界条件**：确定初始状态和边界条件。
5. **自底向上计算**：从最简单的子问题开始，逐步向上计算，直到得到原问题的解。
6. **存储和复用子问题解**：使用数组或其他数据结构存储子问题的