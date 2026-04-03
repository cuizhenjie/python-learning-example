# Python 学习计划 — 前两周"手把手"教学方案

> 崔总专属 · Java 专家转型 · 老师手把手模式

---

## 📐 教学闭环设计

```
每日学习 → 实战作业 → 提交反馈 → 老师点评/调整 → 次日针对性补充
```

### 反馈提交方式
每天学完后，把你的**代码截图 / 代码文本 / 疑问**发给我（直接在聊天里发），我会：
- ✅ 验收作业是否达标
- 🔍 指出代码问题
- 📝 提供个性化补充材料
- 🎯 调整次日内容（薄弱点加强）

---

## 📅 第一周：Python 基础与 Java 差异

---

### Day 1（今天）— 环境搭建 & Python vs Java 思维切换

#### 🎯 今日目标
- [ ] 安装 Python 3.11+ 和配置虚拟环境
- [ ] 理解 Python 解释器 vs Java JVM 的本质区别
- [ ] 写出第一行 Python 代码

#### 📚 学习资料
**视频推荐**（选一个即可）：
- [Python 入门教程 W3Cschool](https://www.w3cschool.cn/python3/) — 适合零基础快速过一遍
- [Python Tutorial - GeeksforGeeks](https://www.geeksforgeeks.org/python-tutorial/) — 偏工程向

**核心概念**（必读）：
```
Java:  .java → 编译 → .class → JVM 运行
Python: .py  → 解释器(CPython) → 直接运行
       ↑ 没有编译环节，解释器逐行执行
```

**你的 Java 经验对应**：
- venv 虚拟环境 = Maven/Gradle 的 dependency 隔离
- pip = Maven Central / Gradle dependency
- pyenv = JAVA_HOME 版本管理

#### 💻 实战作业

**作业 1：环境验收**
```bash
# 在终端运行以下命令，把结果截图发给我
python3 --version
which python3
# 如果用 pyenv：
pyenv versions
# 创建虚拟环境：
python3 -m venv ~/.venv/py3
source ~/.venv/py3/bin/activate
pip --version
pip install requests
python -c "import requests; print('requests 安装成功')"
```

**作业 2：运行以下代码，理解输出**
```python
# -*- coding: utf-8 -*-
name = "崔总"
age = 30

# 1. 动态类型演示
age = "三十岁"  # 从 int 变成 str，Java 不允许
print(f"类型演示: name={name}, age={age}, type(age)={type(age)}")

# 2. 负索引演示
arr = [1, 2, 3, 4, 5]
print(f"arr[-1]={arr[-1]}")      # Java: arr.get(arr.size()-1)
print(f"arr[1:4]={arr[1:4]}")     # 切片，左闭右开 [2,3,4]

# 3. f-string vs Java String.format
print(f"{name}今年{age}岁")      # Java 15+ 才有的 text block
```

#### ❓ 今日疑问
学完后，有什么疑问直接在聊天里问我。

---

### Day 2 — 数据类型系统：动态类型 vs 强类型

#### 🎯 今日目标
- [ ] 说出 Python 6 种基本数据类型
- [ ] 理解 Python int 是任意精度的（无 long/short/byte 区分）
- [ ] 熟练使用 list/dict/tuple/set

#### 📚 学习资料
**对比速查表**（重点）：

| Python | Java | 区别 |
|--------|------|------|
| `int` | `int/long/short/byte` | Python int 无大小限制，Java 要选 |
| `float` | `float/double` | Python 只有 float，Java 有两种 |
| `bool` | `boolean` | Python True/False 首字母大写 |
| `str` | `String` | Python str 是 Unicode 原生 |
| `list` | `List` | Python 用 `[]` 字面量 |
| `dict` | `Map` | Python 用 `{}` 字面量 |
| `tuple` | `List`（只读）| 不可变，Java 没有真正等价 |
| `set` | `Set` | 自动去重 |

**代码示例重点**：
```python
# int 无上限
x = 5 ** 100  # Java: BigInteger
print(x)

# 字典操作对比
d = {"name": "崔总", "skill": "Java"}
d["new_skill"] = "Python"  # d.put()
print(d.get("name2", "默认值"))  # Java: d.getOrDefault()
```

#### 💻 实战作业

**作业 1：数据类型判断**
```python
# 写出以下值的类型（不要运行，先猜，再运行验证）
a = type(10)
b = type(10.0)
c = type("10")
d = type(True)
e = type([1, 2, 3])
f = type({"a": 1})
g = type((1, 2))
h = type({1, 2})
# 验证方法: print(a, b, c, d, e, f, g, h)
```

**作业 2：员工信息管理（字典版）**
```python
employee = {
    "name": "你的名字",
    "age": 你的年龄,
    "skills": ["Java"],  # 已有技能
    "salary": 30000.0
}

# 实现以下操作（不查文档，看提示）：
# 1. 添加一个新技能 "Python"
# 2. 把年龄加 1
# 3. 打印所有技能（用 join 连接）
# 4. 如果没有"title"字段，打印"无职位"，否则打印职位
```

**作业 3：对比思考**
- Python 的 `list.append()` vs `list.extend()` 区别是什么？
- 什么时候用 tuple 而不是 list？

---

### Day 3 — 控制流：条件 & 循环 & 列表推导式

#### 🎯 今日目标
- [ ] 理解 Python 缩进 = Java 的 `{}`
- [ ] 熟练使用 `range()` 替代 Java 的 C-style for
- [ ] 掌握列表推导式（一行替代 for 循环）

#### 📚 学习资料
**列表推导式 — 这是 Python 最实用的语法**：

```python
# Java: List<Integer> squares = nums.stream().map(n -> n*n).collect(Collectors.toList());
# Python:
nums = [1, 2, 3, 4, 5]
squares = [n * n for n in nums]   # 一行

# 带条件
even_squares = [n * n for n in nums if n % 2 == 0]

# 嵌套
matrix = [[1,2,3], [4,5,6]]
flat = [x for row in matrix for x in row]  # 嵌套列表展平
```

#### 💻 实战作业

**作业 1：FizzBuzz（程序员入门题）**
```python
# 打印 1-100，
# 能被 3 整除打印 "Fizz"，
# 能被 5 整除打印 "Buzz"，
# 能被 3 和 5 同时整除打印 "FizzBuzz"
# 其他打印数字

# 限制：一行代码完成（用列表推导式 + print）
# 提示：[print("FizzBuzz" if i%15==0 else "Fizz" if i%3==0 else "Buzz" if i%5==0 else i) for i in range(1, 101)]
```

**作业 2：九九乘法表**
```python
# 用嵌套列表推导式生成九九乘法表
# 格式：[(i, j, i*j) for i in range(1, 10) for j in range(1, i+1)]
# 打印成漂亮格式
```

**作业 3：计时对比**
```python
import time

# 比较列表推导式 vs 普通 for 循环速度
n = 1000000

# 方式1：普通 for
start = time.time()
squares = []
for i in range(n):
    squares.append(i*i)
t1 = time.time() - start

# 方式2：列表推导式
start = time.time()
squares2 = [i*i for i in range(n)]
t2 = time.time() - start

print(f"for循环: {t1:.4f}秒, 列表推导式: {t2:.4f}秒")
# 结果发给我
```

---

### Day 4 — 函数：def & 参数机制 & lambda

#### 🎯 今日目标
- [ ] 理解 `*args` 和 `**kwargs`（Java 没有）
- [ ] 理解 Python 函数是一等公民（Java 方法不是）
- [ ] 掌握 lambda 表达式

#### 📚 学习资料
**函数参数速查**：

```python
def func(a, b,           # 位置参数（必填）
          c=10,           # 默认参数（Java 用重载）
          *args,         # 可变位置参数
          d=20,          # 默认参数
          **kwargs):     # 可变关键字参数
    pass

# 调用方式
func(1, 2)                    # 位置参数
func(a=1, b=2)                # 关键字参数
func(1, 2, c=3, d=4)          # 混合
func(1, 2, 3, 4, 5, name="崔总", age=30)  # args=(3,4,5), kwargs={'name':'崔总','age':30}
```

#### 💻 实战作业

**作业 1：实现 `make_multiplier`（高阶函数）**
```python
def make_multiplier(factor):
    # 返回一个新函数，新函数会把输入乘以 factor
    pass  # 你来实现

double = make_multiplier(2)
triple = make_multiplier(3)
print(double(5))   # 10
print(triple(5))   # 15

# Java 等价：BiFunction<Integer, Integer, Integer> makeMultiplier(int factor) {
#     return (a, b) -> a * factor; }
```

**作业 2：实现 `max_of(*nums)`**
```python
def max_of(*nums):
    # 不用内置 max()，自己实现
    # 提示：假设第一个是最大值，遍历比较
    pass

print(max_of(3, 1, 4, 1, 5, 9, 2, 6))  # 9
print(max_of(1, 3))                    # 3
print(max_of(42))                      # 42
```

**作业 3：lambda 排序**
```python
employees = [
    {"name": "张三", "salary": 30000, "age": 28},
    {"name": "李四", "salary": 50000, "age": 35},
    {"name": "王五", "salary": 40000, "age": 32},
]

# 用 lambda 按薪资降序排序
# sorted(employees, key=..., reverse=...)
# 把结果打印出来
```

---

### Day 5 — 模块与包：import 机制

#### 🎯 今日目标
- [ ] 理解 `import` vs `from ... import`
- [ ] 理解 `if __name__ == "__main__":`
- [ ] 能创建自己的 Python 包

#### 💻 实战作业

**作业 1：创建你的第一个 Python 包**
```bash
mkdir -p ~/python_learn/mypackage
cd ~/python_learn/mypackage
touch __init__.py
```

创建 `math_utils.py`：
```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

if __name__ == "__main__":
    # 直接运行这个文件时执行这里
    print("math_utils 自测:")
    print(f"3 + 5 = {add(3, 5)}")
    print(f"10 - 3 = {subtract(10, 3)}")
```

创建 `string_utils.py`：
```python
def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    return sum(1 for c in s if c in "aeiouAEIOU")

if __name__ == "__main__":
    print(reverse_string("Hello"))  # olleH
```

**作业 2：使用你创建的包**
```python
# 在 ~/python_learn/ 目录下创建 test_package.py
import mypackage.math_utils as math
from mypackage.string_utils import reverse_string

# 用 math.add 做计算
# 用 reverse_string 反转任意字符串
# 打印结果
```

**作业 3：pip 实战**
```bash
# 安装并使用一个工具库（选一个）
# 选项A: pip install requests  → 抓取网页
# 选项B: pip install arrow     → 日期时间处理
# 选项C: pip install tqdm      → 进度条
pip install requests
python -c "import requests; r = requests.get('https://httpbin.org/get'); print(r.status_code, r.json())"
```

---

### Day 6 — 文件操作与异常处理

#### 🎯 今日目标
- [ ] 熟练使用 `with open()` 管理文件
- [ ] 掌握 `try/except/finally`
- [ ] 能读写 CSV 文件

#### 💻 实战作业

**作业 1：文件复制器**
```python
def copy_file(src, dst):
    """复制文件（不能用 shutil）"""
    with open(src, 'rb') as f_src:   # 二进制模式
        content = f_src.read()
    with open(dst, 'wb') as f_dst:
        f_dst.write(content)
    print(f"复制完成: {src} → {dst}")

# 测试：复制任意文件，验证 MD5 一致
# 用 hashlib.md5() 验证
```

**作业 2：CSV 数据处理**
```python
import csv

# 假设有一个 employees.csv 文件，内容如下：
# name,age,salary
# 张三,28,30000
# 李四,35,50000
# 王五,32,40000

def read_csv(path):
    with open(path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(row)

def write_csv(path, data):
    """data 是字典列表 [{"name": "...", "age": ..., "salary": ...}]"""
    # 实现写入逻辑
    pass
```

**作业 3：异常处理练习**
```python
def safe_divide(a, b):
    """安全除法，出错返回 None 并打印友好提示"""
    try:
        return a / b
    except ZeroDivisionError:
        print("错误：除数不能为零")
    except TypeError:
        print("错误：只能对数字做除法")
    except Exception as e:
        print(f"未知错误: {e}")
    return None

# 测试以下调用
print(safe_divide(10, 2))    # 5.0
print(safe_divide(10, 0))    # None + 友好提示
print(safe_divide(10, "2")) # None + 友好提示
```

---

### Day 7 — 第一周综合练习 & 复习

#### 🎯 今日目标
- [ ] 完成综合练习：命令行员工管理系统
- [ ] 回顾本周所有代码，对比 Java 实现
- [ ] 提交本周学习反馈

#### 📝 综合练习：员工管理系统 CLI

**功能要求**：
1. 添加员工（姓名、年龄、薪资、技能列表）
2. 列出所有员工
3. 按姓名查找员工
4. 删除员工
5. 修改员工薪资
6. 数据持久化（JSON 文件存储，重启不丢数据）
7. 退出

**参考结构**（可以参考 Day 7 的代码示例）

#### 📝 第一周学习反馈表

学完后请告诉我：

```
1. 本周最难理解的概念是？
2. 哪些代码示例最有用？
3. 哪些地方感觉学得不够扎实？
4. Java 和 Python 的最大思维差异是什么？（你觉得哪个更别扭）
5. 下周最想深入学什么？
```

---

## 📅 第二周：Python 面向对象与 Java 对比

---

### Day 8 — 类与对象：Python 的 OOP

#### 🎯 今日目标
- [ ] 理解 `__init__` vs `__new__` 的区别
- [ ] 掌握实例属性 vs 类属性
- [ ] 理解 Python 的"约定式"封装 vs Java 的"强制性"封装

#### 💻 实战作业

**作业 1：BankAccount 类**
```python
class BankAccount:
    def __init__(self, account_id, balance=0.0):
        self.account_id = account_id
        self.balance = balance
        self.transaction_count = 0  # 类属性？实例属性？

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("存款金额必须为正")
        self.balance += amount
        self.transaction_count += 1

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("取款金额必须为正")
        if amount > self.balance:
            raise ValueError("余额不足")
        self.balance -= amount
        self.transaction_count += 1

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"账户{self.account_id}，余额={self.balance}，交易次数={self.transaction_count}"

# 测试
acc = BankAccount("ACC001", 10000)
acc.deposit(5000)
acc.withdraw(3000)
print(acc)  # 期望：账户ACC001，余额=12000，交易次数=2
```

**作业 2：@property 实现 Java Bean 风格**
```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary   # 用 _ 表示受保护

    # 用 @property 实现 getter（Java: public Salary getSalary())
    @property
    def salary(self):
        return self._salary

    # 用 @setter 实现 setter（Java: public void setSalary(Salary s)）
    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("薪资不能为负")
        self._salary = value

# 测试
emp = Employee("崔总", 30000)
print(emp.salary)   # 调用 getter
emp.salary = 35000  # 调用 setter
print(emp.salary)
emp.salary = -1000  # 触发 ValueError
```

---

### Day 9 — 继承与多态：MRO vs Java 单继承

#### 🎯 今日目标
- [ ] 理解 Python 多继承 vs Java 单继承
- [ ] 掌握 `super()` 调用父类
- [ ] 理解 Python "鸭子类型"（Java 接口 vs Python 动态类型）

#### 💻 实战作业

**作业 1：继承体系练习**
```python
class Animal:
    def speak(self):
        raise NotImplementedError

class Dog(Animal):
    def speak(self):
        return "汪汪汪"

class Cat(Animal):
    def speak(self):
        return "喵喵喵"

# 用 for 循环让动物叫
animals = [Dog(), Cat(), Dog()]
for a in animals:
    print(a.speak())
```

**作业 2：多继承 & MRO**
```python
class A:
    def hello(self): return "A"

class B(A):
    def hello(self): return "B"

class C(A):
    def hello(self): return "C"

class D(B, C):
    pass

d = D()
print(d.hello())       # B（方法解析顺序）
print(D.__mro__)       # 查看完整的 MRO
```

**作业 3：鸭子类型练习**
```python
# Python 特有的：不需要继承，只要你有 speak() 方法就能用

class Duck:
    def speak(self):
        return "嘎嘎嘎"

class Robot:
    def speak(self):
        return "我是机器人，不会说话"

def make_them_speak(things):
    """只要有 speak() 方法就能传进来"""
    for thing in things:
        print(thing.speak())

# 测试
make_them_speak([Dog(), Duck(), Robot()])
```

---

### Day 10 — 特殊方法（魔术方法）

#### 🎯 今日目标
- [ ] 理解 `__str__` vs `__repr__`
- [ ] 掌握运算符重载（`__add__`/`__eq__`/`__lt__`）
- [ ] 理解 `__call__` 把对象变成可调用的

#### 💻 实战作业

**作业 1：Fraction 分数类**
```python
from math import gcd

class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("分母不能为零")
        g = gcd(abs(numerator), abs(denominator))
        self.numerator = numerator // g
        self.denominator = denominator // g

    def __repr__(self):
        return f"Fraction({self.numerator}, {self.denominator})"

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        # a/b + c/d = (ad+bc)/bd
        pass  # 你来实现

    def __eq__(self, other):
        pass  # 你来实现

    def __lt__(self, other):
        pass  # 你来实现

# 测试
f1 = Fraction(1, 2)
f2 = Fraction(2, 4)   # 应该化简为 1/2
f3 = Fraction(1, 3)

print(f1 == f2)   # True（化简后相同）
print(f1 + f3)    # 5/6
print(f1 < f3)    # True（1/2 > 1/3）
```

---

### Day 11 — 组合 vs 继承 + 数据类

#### 🎯 今日目标
- [ ] 理解"组合优先于继承"（Effective Java 也这么说）
- [ ] 掌握 `@dataclass`（Python 3.7+，类似 Java record）

#### 💻 实战作业

**作业 1：用 `@dataclass` 重构 BankAccount**
```python
from dataclasses import dataclass, field

@dataclass
class BankAccountDC:
    account_id: str
    balance: float = 0.0
    transaction_count: int = 0

    def deposit(self, amount: float):
        self.balance += amount
        self.transaction_count += 1

    # 等价补充：__eq__/__hash__ 默认基于所有字段
```

**作业 2：组合练习**
```python
# 部门和员工的双向组合关系
from dataclasses import dataclass, field
from typing import List

@dataclass
class Employee:
    name: str
    salary: float

@dataclass
class Department:
    name: str
    employees: List[Employee] = field(default_factory=list)

    def add_employee(self, emp: Employee):
        self.employees.append(emp)

    def total_salary(self):
        return sum(e.salary for e in self.employees)

    def find_by_name(self, name: str):
        return [e for e in self.employees if name in e.name]

# 测试
dept = Department("技术部")
dept.add_employee(Employee("张三", 30000))
dept.add_employee(Employee("李四", 40000))
print(dept.total_salary())   # 70000
print(dept.find_by_name("张"))  # [Employee(name='张三', ...)]
```

---

### Day 12-13 — 装饰器（重点！）

#### 🎯 今日目标
- [ ] 理解装饰器是"高阶函数 + 闭包"的语法糖
- [ ] 能写带参数的装饰器
- [ ] 理解 `@functools.wraps` 的作用

#### 💻 实战作业

**作业 1：基础装饰器**
```python
import functools

def log_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] 调用 {func.__name__}({args}, {kwargs})")
        result = func(*args, **kwargs)
        print(f"[LOG] {func.__name__} 返回 {result}")
        return result
    return wrapper

@log_calls
def add(a, b):
    return a + b

# 测试
add(1, 2)
# 期望输出：
# [LOG] 调用 add((1, 2), {})
# [LOG] add 返回 3
```

**作业 2：计时装饰器**
```python
import time

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"{func.__name__} 耗时 {elapsed:.4f}秒")
        return result
    return wrapper

@timer
def slow_sum(n):
    total = 0
    for i in range(n):
        total += i
    return total

slow_sum(1000000)
```

**作业 3：`@lru_cache` 实现斐波那契（理解缓存）**
```python
import functools

# Python 内置的缓存装饰器
@functools.lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# 对比：不缓存 vs 缓存的时间差异
# 不缓存的版本你自己写一个
# 用 time.time() 计时，对比 fibonacci(30) 的耗时
```

**作业 4：带参数的装饰器（装饰器工厂）**
```python
def repeat(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(times):
                results.append(func(*args, **kwargs))
            return results
        return wrapper
    return decorator

@repeat(times=3)
def greet(name):
    return f"你好，{name}！"

print(greet("崔总"))
# 期望：['你好，崔总！', '你好，崔总！', '你好，崔总！']
```

---

### Day 14 — 第二周综合 & 复习

#### 🎯 今日目标
- [ ] 完成第二周综合练习
- [ ] 理解装饰器在 Django/Flask 中的实际应用场景
- [ ] 提交第二周学习反馈

#### 📝 第二周综合练习

**挑战：用装饰器实现一个简单的 API 速率限制器**

```python
# 目标：实现 @rate_limit decorator
# 每个用户（用 user_id 标识）每分钟最多调用 3 次

call_log = {}  # {user_id: [timestamp1, timestamp2, ...]}

def rate_limit(max_calls=3, window_seconds=60):
    """每 max_calls 次调用在 window_seconds 秒内"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(user_id, *args, **kwargs):
            now = time.time()
            # 1. 从 call_log 清理过期记录
            # 2. 检查 user_id 的调用次数
            # 3. 如果超限，抛出异常
            # 4. 否则记录本次调用并执行
            pass  # 你来实现
        return wrapper
    return decorator

@rate_limit(max_calls=3, window_seconds=60)
def api_call(user_id, data):
    return {"status": "ok", "user": user_id, "data": data}

# 测试：模拟连续 5 次调用，只有前 3 次成功
for i in range(5):
    try:
        result = api_call("user_123", {"request": i})
        print(f"请求{i}: 成功")
    except Exception as e:
        print(f"请求{i}: 失败 - {e}")
```

#### 📝 第二周学习反馈表

```
1. 装饰器最难理解的地方是什么？（闭包？语法糖？参数传递？）
2. @dataclass 和 Java record 你觉得哪个更好用？为什么？
3. Python 的"鸭子类型"和你理解的"多态"有什么不同？
4. 这两周学习下来，你觉得 Python 最让你不适应的地方是什么？
5. 下一步最想学什么？（框架/数据处理/AI/爬虫/自动化？）
```

---

## 📊 验收标准总览

| 天数 | 验收重点 | 核心产出 |
|------|---------|---------|
| Day 1 | 环境可用，第一行代码 | 环境截图 + 代码运行结果 |
| Day 2 | 数据类型理解 | 作业 2 员工字典 CRUD |
| Day 3 | 列表推导式 + 计时对比 | FizzBuzz 一行版 + 计时截图 |
| Day 4 | lambda + 高阶函数 | make_multiplier + max_of |
| Day 5 | 包创建 + pip | 自己的包可 import |
| Day 6 | 文件 + 异常 | 员工数据 CSV 读写 |
| Day 7 | 综合 CLI 系统 | 完整可运行的员工系统 |
| Day 8-9 | OOP 继承+多态 | BankAccount + 鸭子类型 |
| Day 10 | 魔术方法 | Fraction 完整运算符 |
| Day 11 | dataclass + 组合 | 部门员工系统 |
| Day 12-13 | 装饰器 | rate_limit 装饰器 |
| Day 14 | 综合 + 反馈 | 完整练习 + 学习反馈 |

---

## 🔧 学习工具推荐

**Python 编辑器**（选一个）：
- **VS Code** + Python 插件（免费，推荐）
- **PyCharm**（专业，Java 开发者熟悉）
- **Jupyter Notebook**（数据分析/AI 相关）
- **Cursor**（AI 代码助手）

**练习平台**：
- [LeetCode Python](https://leetcode.com/problemset/python/)（刷算法）
- [HackerRank Python](https://www.hackerrank.com/domains/python)（入门练习）
- [Real Python](https://realpython.com/)（高质量教程）

**AI 辅助学习**（推荐）：
- 用 Cursor/Windsurf 等 AI IDE 学习，遇到不懂的直接问 AI
- 把崔总的经验：AI 是你的老师，但要自己动手敲代码
