# -*- coding: utf-8 -*-
"""
Day 1 代码示例：Python 基础 vs Java 差异

核心概念：
1. 动态类型 — 变量类型随赋值变化，不需要声明
2. f-string — Python 格式化字符串，Java 15+ text block 类似
3. 负索引 — arr[-1] = 最后一个元素，Java 没有
4. 切片 — arr[start:end] 左闭右开，Java 用 subList()
"""

name = "崔总"
age = 30

# ==================== 1. 动态类型演示 ====================
# Java: int age = 30;  age = "三十岁"; // ❌ 编译报错！
# Python: 变量类型随赋值变化，完全合法
age = "三十岁"
print(f"类型演示: name={name}, age={age}, type(age)={type(age)}")
# 输出: type(age)=<class 'str'>  age 从 int 变成了 str

# ==================== 2. 负索引 ====================
arr = [1, 2, 3, 4, 5]
print(f"arr[-1]={arr[-1]}")      # 5, Java: arr.get(arr.size()-1)
print(f"arr[-2]={arr[-2]}")      # 4, 倒数第二个，Java 没有
print(f"arr[1:4]={arr[1:4]}")     # [2, 3, 4], 切片左闭右开

# ==================== 3. f-string 格式化 ====================
# Java 15+: String s = f"{name}今年{age}岁";
# Python: 更早版本就支持 f""
print(f"{name}今年{age}岁")
# 注意：这里 age 已经是"三十岁"了，所以输出有两个"岁"
