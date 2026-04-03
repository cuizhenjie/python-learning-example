# Python 学习计划 — 崔总专属（Java 专家转型）

> 基于 10 年 Java 经验，3 个月精通 Python

---

## 学习思路

Java 是"一切皆对象"、强类型、编译型语言；Python 是"一切皆对象"、动态类型、解释型语言。
**你的优势**：已掌握 OOP、设计模式、并发编程，Python 学的是语法糖和生态，不是编程思想。

---

## 阶段划分

| 阶段 | 周次 | 主题 |
|------|------|------|
| 第一阶段 | 第 1-2 周 | Python 基础与 Java 差异 |
| 第二阶段 | 第 3-4 周 | Python 面向对象与 Java 对比 |
| 第三阶段 | 第 5-7 周 | Python 高级特性（装饰器/生成器/协程） |
| 第四阶段 | 第 8-9 周 | Python 框架：FastAPI + Django |
| 第五阶段 | 第 10-11 周 | 数据处理与 AI 工具链 |
| 第六阶段 | 第 12 周 | 综合项目 + 求职技能 |

---

## 📅 每日学习内容

### 第一阶段：Python 基础与 Java 差异（第 1-2 周）

---

#### **Day 1 — 环境搭建 & Python vs Java 思维切换**

**今日主题**：Python 环境管理 & 解释器原理

**核心知识点**：
- Python 解释器 CPython/Jython/IronPython（对比 Java JVM）
- `venv` 虚拟环境 = Java Maven/Gradle 的依赖隔离
- `pip` = Java 的 Maven Central
- pyenv 管理多版本（类似 Java 的 JAVA_HOME）

**实战代码**：
```python
# Java: public static void main(String[] args)
# Python: 脚本直接运行，不需要类包装

name = "崔总"          # Java: String name = "崔总"; （动态类型，不需要声明类型）
age = 18               # Python 是动态类型，一个变量可以随时改类型
age = "十八岁"         # 完全合法，Java 绝对不允许

# print 替代 System.out.println
print(f"你好，{name}，年龄={age}")

# 列表 List = Java ArrayList
arr = [1, 2, 3, 4, 5]
arr.append(6)          # 类似 Java ArrayList.add()
print(arr[-1])         # Python 支持负索引，最后一个元素，Java 需要 arr.get(size-1)

# 切片 slice，Java 没有等价物
print(arr[1:4])        # [2, 3, 4]  左闭右开区间
print(arr[::2])        # [1, 3, 5]  步长为2
```

**作业验收**：
- [ ] 安装 Python 3.11+ 并配置 venv 虚拟环境
- [ ] 用 `pip install requests` 安装第三方库并成功调用
- [ ] 将上述代码跑通，理解负索引和切片

---

#### **Day 2 — 数据类型系统：动态类型 vs 强类型**

**今日主题**：Python 数据类型与 Java 的核心区别

**核心知识点**：
- Python 有 6 种基本数据类型：int/float/str/bool/list/dict
- **没有** `byte/short/long` 细分，int 是任意精度（Java 要选 int/long）
- **没有** `char` 类型，单字符也是 str
- 布尔值 `True/False`（首字母大写，Java 是小写）
- 字符串是 Unicode 原生支持（Java 1.7 前要处理编码问题）
- 列表/字典/元组/集合 vs Java 的集合框架

**实战代码**：
```python
# Java: int x = 5; long y = 5L;
# Python: 全部 int，自动精度

x = 5
y = 5 ** 100  # Python int 可以存超大数，Java 需要 BigInteger
print(y)     # 5 的 100 次方，轻松算

# 字符串：Java 是字节数组，Python 是 Unicode
s = "中文和English混排"
print(len(s))        # Python: 11（按字符计），Java: 要注意编码

# 格式化：Python f-string vs Java String.format
name = "崔总"
age = 30
print(f"{name}今年{age}岁")   # f-string，Java 15+ 才有 text block
print("{}今年{}岁".format(name, age))  # format 方法

# 字典 = Java HashMap；列表 = ArrayList
d = {"name": "崔总", "skill": "Java"}
print(d["name"])              # d.get("name")
d["new_skill"] = "Python"    # d.put()

# 集合 set = Java HashSet
s = {1, 2, 3, 3, 3}
print(s)   # {1, 2, 3}  自动去重，Java 要手动处理
```

**作业验收**：
- [ ] 写出 Python 的 6 种基本数据类型
- [ ] 用字典模拟一个简单的"员工信息表"（增删改查）
- [ ] 比较 `list.append()` 和 `list.extend()` 的区别

---

#### **Day 3 — 控制流：条件 & 循环**

**今日主题**：Python 的控制结构

**核心知识点**：
- `if/elif/else` — 注意冒号和缩进（Java 用 `{}`）
- `for` 循环：Python 的 `for` 是迭代器模式（Java 1.5+ 的增强 for循环类似）
- `while` 循环 — 和 Java 基本一致
- `range()` vs Java 的 `for(int i=0; i<n; i++)`
- 列表推导式 — Python 特有，Java 没有

**实战代码**：
```python
# 缩进就是作用域！Java用{}，Python用缩进
x = 10
if x > 5:
    print("大于5")        # 4个空格缩进
    if x > 8:
        print("大于8")    # 嵌套缩进

# elif 替代 Java 的 else if（更简洁）
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "D"

# range() — Java 的 IntStream.range()
for i in range(5):           # 0到4，不含5
    print(i)

for i in range(2, 8, 2):     # 2, 4, 6（步长2）
    print(i)

# 列表推导式 — 超级实用，Java 8 Stream 可以做到但更冗长
nums = [1, 2, 3, 4, 5]

# 传统写法
squares = []
for n in nums:
    squares.append(n * n)

# Python 列表推导式（一行搞定）
squares = [n * n for n in nums]   # [1, 4, 9, 16, 25]

# 带条件的列表推导式
even_squares = [n * n for n in nums if n % 2 == 0]  # [4, 16]

# Java Stream 等价写法（参考对比）：
# List<Integer> squares = nums.stream().map(n -> n * n).collect(Collectors.toList());
```

**作业验收**：
- [ ] 用列表推导式找出 1-100 中能被 3 和 5 同时整除的数
- [ ] 写一个猜数字游戏（while 循环 + if/elif/else）
- [ ] 比较列表推导式和普通 for 循环的性能（用 time.time() 计时）

---

#### **Day 4 — 函数：Python 函数与 Java 方法**

**今日主题**：函数定义、参数机制、lambda

**核心知识点**：
- `def` 定义函数（Java 用 `void/返回类型 方法名()`）
- 默认参数（Java 要用重载）
- 可变参数 `*args` / `**kwargs`（Java 没有直接等价物）
- 匿名函数 `lambda`（Java 1.8+ 的 Lambda 类似）
- 函数的一等公民：函数可以赋值给变量、作为参数传递

**实战代码**：
```python
# Java: public int add(int a, int b) { return a + b; }
# Python:
def add(a, b):
    return a + b

# 默认参数（Java 要重载）
def greet(name, greeting="你好"):
    return f"{greeting}，{name}！"

print(greet("崔总"))              # 你好，崔总！
print(greet("崔总", "早上好"))    # 早上好，崔总！

# *args 可变位置参数（类似 Java 的 String... args）
def sum_all(*numbers):
    total = 0
    for n in numbers:
        total += n
    return total

print(sum_all(1, 2, 3, 4, 5))   # 15

# **kwargs 可变关键字参数（Java 没有）
def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="崔总", company="AI公司", title="CTO")
# name: 崔总
# company: AI公司
# title: CTO

# Lambda 表达式（类似 Java 1.8+ Lambda）
square = lambda x: x * x
print(square(5))   # 25

# Java: BiFunction<Integer, Integer, Integer> add = (a, b) -> a + b;

# 函数是一等公民（Java 方法不是）
def double(x):
    return x * 2

def triple(x):
    return x * 3

operations = [double, triple]  # 函数可以放列表里
for op in operations:
    print(op(5))   # 10, 15

# 高阶函数（接受函数作为参数）
def apply_twice(func, x):
    return func(func(x))

print(apply_twice(double, 3))   # 12 (3*2*2)
```

**作业验收**：
- [ ] 实现一个 `make_multiplier(factor)` 函数，返回一个乘以 factor 的函数
- [ ] 用 `*args` 实现可变参数求最大值函数 `max_of(*nums)`
- [ ] 用 `sorted()` + lambda 对员工列表按薪资排序（类比 Java Comparator）

---

#### **Day 5 — 模块与包：import 机制**

**今日主题**：Python 模块系统 vs Java package

**核心知识点**：
- `import` vs `from ... import`（Java 的 import 完全限定名）
- `__init__.py` vs Java 的 package（初始化时机不同）
- `if __name__ == "__main__":` = Java 的 `public static void main`
- Python 的 `sys.path` = Java 的 CLASSPATH
- 相对导入 vs 绝对导入（Python 3+ 的变化）

**实战代码**：
```python
# 假设文件结构：
# mypackage/
#   __init__.py
#   utils.py
#   math_ops.py

# import 完全体（类似 Java 完整包名）
import mypackage.utils
mypackage.utils.add(1, 2)

# from...import（更常用，类似 Java 静态导入）
from mypackage.utils import add, subtract
add(1, 2)   # 直接用，不用加模块名

# 别名
import numpy as np
import pandas as pd

# __name__ == "__main__" 是什么？
# 当文件直接运行 python xxx.py 时，__name__ == "__main__"
# 当文件被 import 时，__name__ == "模块名"

# mymodule.py
def main():
    print("这是主程序")

if __name__ == "__main__":
    main()    # 只有直接运行才执行，import 时不执行

# Java 的等价逻辑：
# public static void main(String[] args) { }
```

**作业验收**：
- [ ] 创建自己的 Python 包，包含 `__init__.py` 和至少 2 个模块
- [ ] 了解 `pip list` / `pip show` / `pip freeze` 的区别
- [ ] 在 Python REPL 中尝试 import 机制

---

#### **Day 6 — 文件操作与异常处理**

**今日主题**：Python I/O 和异常机制 vs Java

**核心知识点**：
- `try/except/finally`（Java 有相同结构，但语法更简洁）
- `with open()` 自动关闭文件（Java 要 try-with-resources）
- 读取：read()/readlines()/readline()（Java 有 FileReader/BufferedReader）
- 写入：write()/writelines()（Java 有 PrintWriter/FileWriter）
- `raise` 主动抛出异常（类似 Java `throw`）

**实战代码**：
```python
# 异常处理：Python vs Java
try:
    result = 10 / 0
except ZeroDivisionError:
    print("除数不能为零")
except Exception as e:
    print(f"其他错误: {e}")
finally:
    print("无论是否出错都执行")

# Java 等价：
# try {
#     int result = 10 / 0;
# } catch (ArithmeticException e) {
#     System.out.println("除数不能为零");
# } finally {
#     System.out.println("清理资源");
# }

# with 自动资源管理（Python 更简洁）
# Java: try (FileReader fr = new FileReader("file.txt")) { ... }
with open("test.txt", "w", encoding="utf-8") as f:
    f.write("你好，世界\n")
    f.write("第二行")

with open("test.txt", "r", encoding="utf-8") as f:
    content = f.read()       # 读取全部
    print(content)

# 按行读取
with open("test.txt", "r") as f:
    for line in f:           # 类似 Java 的 BufferedReader.lines()
        print(line.strip())

# 主动抛出
def divide(a, b):
    if b == 0:
        raise ValueError("除数不能为零")
    return a / b

try:
    divide(10, 0)
except ValueError as e:
    print(f"捕获异常: {e}")
```

**作业验收**：
- [ ] 写一个"文件复制器"，读取源文件内容并写入目标文件
- [ ] 捕获 `FileNotFoundError` 并打印友好提示
- [ ] 用 Python 读取一个 CSV 文件（先了解 csv 模块）

---

#### **Day 7 — 第一周复盘 + 综合练习**

**今日主题**：用 Java 对比法做综合练习

**综合练习：员工管理系统（控制台版）**

```python
# 这是一个简单的员工信息管理 CLI 程序
# 对比 Java 实现来理解 Python 的简洁

employees = []

def add_employee():
    name = input("姓名: ")
    age = int(input("年龄: "))     # Python 动态类型，不需要强制转换签名
    salary = float(input("薪资: "))
    emp = {"name": name, "age": age, "salary": salary}
    employees.append(emp)
    print(f"✅ 添加成功：{name}")

def list_employees():
    if not employees:
        print("暂无员工数据")
        return
    for i, emp in enumerate(employees):
        print(f"{i+1}. {emp['name']} | 年龄:{emp['age']} | 薪资:{emp['salary']}")

def find_by_name():
    name = input("输入要查找的姓名: ")
    results = [e for e in employees if name in e["name"]]
    if results:
        for emp in results:
            print(f"找到了: {emp}")
    else:
        print("未找到该员工")

while True:
    print("\n=== 员工管理系统 ===")
    print("1. 添加员工")
    print("2. 查看所有员工")
    print("3. 按姓名查找")
    print("4. 退出")
    choice = input("选择操作: ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        list_employees()
    elif choice == "3":
        find_by_name()
    elif choice == "4":
        print("再见!")
        break
    else:
        print("无效选择，请重试")
```

**作业验收**：
- [ ] 补全"删除员工"和"修改薪资"功能
- [ ] 添加数据持久化（JSON 文件存储，重启后数据不丢失）
- [ ] 对比：如果用 Java 实现同样的功能，大概需要多少行代码？

---

### 第二阶段：Python 面向对象与 Java 对比（第 3-4 周）

> 提示：你是 Java OOP 高手，这阶段重点是理解 Python 的 OOP 差异而非重新学 OOP。

---

#### **Day 8 — 类与对象：Python 的 OOP vs Java**

**今日主题**：class 定义、self、构造函数

**核心知识点**：
- `__init__` = Java 构造函数（但 Python 的 `__init__` 不是真正的构造函数，`__new__` 才是）
- `self` = Java 的 `this`（但 self 必须显式声明，Java 的 this 是隐式的）
- 实例属性 vs 类属性（Python 和 Java 的 static 变量类似但不完全相同）
- Python 没有 `public/private/protected`，用 `_` 和 `__` 做约定（Java 有真正的访问修饰符）

**实战代码**：
```python
# Java:
# public class Person {
#     private String name;
#     private int age;
#     public Person(String name, int age) { this.name = name; this.age = age; }
# }

# Python:
class Person:
    species = "人类"          # 类属性，所有实例共享（类似 Java static）

    def __init__(self, name, age):  # __init__ 不是构造器，__new__ 才是
        self.name = name      # 实例属性
        self.age = age        # self = Java 的 this，但必须显式写

    def say_hello(self):       # Java 的普通方法
        return f"你好，我是{self.name}，今年{self.age}岁"

    def __str__(self):         # Java 的 toString()
        return f"Person({self.name}, {self.age})"

    def __repr__(self):        # 调试用的表示
        return f"Person(name={self.name!r}, age={self.age!r})"

# 创建对象（不需要 new）
p = Person("崔总", 30)
print(p.say_hello())
print(p)              # 自动调用 __str__
print(repr(p))        # 自动调用 __repr__

# 访问权限：Python 用约定，Java 用关键字
class Account:
    def __init__(self, balance):
        self._protected_field = "受保护的"   # _ 表示子类可访问，外部可访问但不推荐
        self.__private_field = balance       # __ 名字重整为 _Account__private_field，外部难访问

    def __secret_method(self):               # 私有方法
        return "这是私有方法"

# Python 的封装是"约定性"的，Java 是"强制性"的
acc = Account(1000)
print(acc._protected_field)   # 可以访问，但 IDE 会警告
# print(acc.__private_field)  # 报错，NameError
print(acc._Account__private_field)  # Java 反射可以绕过，Python 名字重整也可以绕过
```

**作业验收**：
- [ ] 实现一个 `BankAccount` 类，包含 `deposit()`、`withdraw()`、`get_balance()` 方法
- [ ] 用 `@property` 装饰器实现 Java Bean 式的 getter/setter
- [ ] 理解 `__new__` 和 `__init__` 的区别

---

#### **Day 9 — 继承与多态：Python 的 MRO**

**今日主题**：继承机制、方法解析顺序 vs Java

**核心知识点**：
- Python 支持多继承（Java 只支持单继承 + 接口）
- `super()` 调用父类方法（Java 也有 super）
- `isinstance()` / `issubclass()` vs Java 的 `instanceof`
- Python 的多态：鸭子类型（Java 用接口实现）
- MRO（方法解析顺序）— Python 2.3+ 的 C3 线性化算法（Java 没有）

**实战代码**：
```python
# Java:
# class Animal { void speak() {} }
# class Dog extends Animal { @Override void speak() { System.out.println("汪"); } }
# class Cat extends Animal { @Override void speak() { System.out.println("喵"); } }

# Python:
class Animal:
    def speak(self):
        raise NotImplementedError("子类必须实现")

class Dog(Animal):
    def speak(self):
        return "汪汪汪"

class Cat(Animal):
    def speak(self):
        return "喵喵喵"

# 多态：Python 的方式是"鸭子类型"
# Java: Animal a = new Dog(); a.speak();
# Python:
def make_noise(animal: Animal):     # 类型注解，Java 也类似
    print(animal.speak())

dog = Dog()
cat = Cat()
make_noise(dog)   # 汪汪汪
make_noise(cat)   # 喵喵喵

# Python 可以不继承任何类，只要你有 speak 方法就行——这就是"鸭子类型"
class Duck:
    def speak(self):
        return "嘎嘎嘎"

make_noise(Duck())  # 嘎嘎嘎，Java 做不到（必须继承 Animal）

# isinstance vs instanceof
print(isinstance(dog, Animal))   # True（Java: dog instanceof Animal）
print(isinstance(dog, Dog))       # True
print(issubclass(Dog, Animal))    # True（Java: Dog.class.isAssignableFrom(Animal.class)）

# super() 调用父类
class GoldenRetriever(Dog):
    def speak(self):
        parent_sound = super().speak()  # 先调用父类
        return f"{parent_sound} + 摇尾巴"

gr = GoldenRetriever()
print(gr.speak())   # 汪汪汪 + 摇尾巴
```

**作业验收**：
- [ ] 实现一个 `Vehicle` 基类，`Car` 和 `Bike` 子类覆写 `run()` 方法
- [ ] 理解 Python 多继承时的 MRO，用 `类名.__mro__` 查看
- [ ] 用"鸭子类型"实现一个不继承 Animal 的 Bird 类，但也能传给 make_noise

---

#### **Day 10 — 特殊方法（魔术方法）**

**今日主题**：Python 的双下划线方法

**核心知识点**：
- `__init__`/`__new__` 构造
- `__str__`/`__repr__` 字符串表示
- `__len__`/`__getitem__` 让对象可迭代
- `__eq__`/`__hash__`/`__lt__` 运算符重载
- `__call__` 让实例可以像函数一样调用

**实战代码**：
```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):          # 调试表示
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):    # + 运算符重载
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):   # * 运算符重载
        return Vector(self.x * scalar, self.y * scalar)

    def __eq__(self, other):     # == 运算符
        return self.x == other.x and self.y == other.y

    def __len__(self):           # len() 函数
        return abs(self.x) + abs(self.y)

    def __call__(self):          # 实例可以像函数一样调用
        return (self.x, self.y)

v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(v1)            # Vector(3, 4)
print(v1 + v2)       # Vector(4, 6)
print(v1 * 3)        # Vector(9, 12)
print(v1 == v2)      # False
print(len(v1))       # 7
print(v1())          # (3, 4) — 像函数一样调用
```

**作业验收**：
- [ ] 实现一个 `Fraction` 类，支持加减乘除运算（分数形式，如 1/2 + 1/3 = 5/6）
- [ ] 实现 `__lt__`（小于）让分数可以排序
- [ ] 用 `functools.total_ordering` 简化比较运算符实现

---

#### **Day 11 — 组合与聚合 vs 继承**

**今日主题**：何时用继承、何时用组合

**核心知识点**：
- "组合优先于继承"（Effective Java 也这么说）
- Python 的 mixin 模式（Java 的默认方法 + 接口组合 vs Python 多继承）
- `has-a` vs `is-a`（Java OOP 同一原则）

**作业验收**：
- [ ] 用组合模式重构之前的"员工管理系统"（员工拥有部门，部门拥有员工列表）
- [ ] 设计一个 `Engine` + `Car` 的组合关系

---

#### **Day 12 — 枚举与数据类**

**今日主题**：Python 3.4+ 的 Enum 和 3.7+ 的 dataclass

**核心知识点**：
- `enum.Enum`（Java 的 enum 更强大，Python 的 enum 较轻量）
- `@dataclass`（Python 3.7+，大大简化 POJO 类，Java 14+ 有 record）
- `__slots__` 优化内存（Java 没有，直接有 JVM 优化）

**实战代码**：
```python
from enum import Enum, auto
from dataclasses import dataclass, field
from typing import List

# Java: enum Status { ACTIVE, INACTIVE, DELETED }
class Status(Enum):
    ACTIVE = auto()
    INACTIVE = auto()
    DELETED = auto()

# @dataclass 替代手写 __init__ __repr__ __eq__
# Java 16+: record EmployeeRecord(String name, int age) {}
@dataclass
class Employee:
    name: str
    age: int
    salary: float
    skills: List[str] = field(default_factory=list)  # Java: List.of()
    status: Status = Status.ACTIVE

    def has_skill(self, skill: str) -> bool:
        return skill in self.skills

emp = Employee("崔总", 30, 50000.0, ["Java", "Python"])
print(emp)        # 自动 __repr__
print(emp.name)   # 崔总
print(emp.has_skill("Java"))  # True

# __slots__ 限制实例属性，禁止动态添加属性（性能优化）
class Point:
    __slots__ = ["x", "y"]
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(1, 2)
p.z = 3   # AttributeError: 'Point' object has no attribute 'z'
```

**作业验收**：
- [ ] 用 `@dataclass` 重构 Day 8 的 `BankAccount` 类
- [ ] 了解 `@dataclass` 的 `eq=False`、`frozen=True`、`order=True` 参数的作用
- [ ] 对比 Java `record` 和 Python `@dataclass`

---

### 第三阶段：Python 高级特性（第 5-7 周）

---

#### **Day 13 — 装饰器 Decorator（核心重点）**

**今日主题**：Python 装饰器 — Java AOP 思想的 Python 实现

**核心知识点**：
- 装饰器是函数柯里化+闭包的语法糖
- `@decorator` = 装饰器模式（Java Spring AOP 拦截器类似）
- `@functools.wraps` 保留原函数元信息
- 类装饰器（Java 注解 + 拦截器的思想）
- 装饰器带参数（三层嵌套）

**实战代码**：
```python
import functools
import time

# Java AOP: @Around("execution(* com.example.*.*(..))")
# Python 装饰器：用函数包装另一个函数

# 最简单的装饰器
def log_decorator(func):
    @functools.wraps(func)   # 保留原函数名字和文档
    def wrapper(*args, **kwargs):
        print(f"[LOG] 调用函数: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"[LOG] 函数结束: {func.__name__}")
        return result
    return wrapper

@log_decorator
def add(a, b):
    """两数相加"""
    return a + b

# 等价于：add = log_decorator(add)
print(add(1, 2))

# 带参数的装饰器（装饰器工厂）
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

print(greet("崔总"))  # ['你好，崔总！', '你好，崔总！', '你好，崔总！']

# 计时装饰器（常用）
def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} 执行耗时: {end-start:.4f}秒")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    return "完成"

slow_function()

# 类作为装饰器（实现 __call__）
class CallCounter:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"{self.func.__name__} 被调用了 {self.count} 次")
        return self.func(*args, **kwargs)

@CallCounter
def hello():
    return "Hello!"

hello()  # hello 被调用了 1 次
hello()  # hello 被调用了 2 次
```

**作业验收**：
- [ ] 实现一个 `@cache` 装饰器（Python 内置 `functools.lru_cache` 的简化版），缓存函数结果
- [ ] 实现一个 `@retry(max_attempts=3)` 装饰器，失败时自动重试
- [ ] 理解 `@functools.wraps` 的作用，对比不用它时的区别

---

#### **Day 14 — 生成器与迭代器**

**今日主题**：惰性计算 vs Java Stream

**核心知识点**：
- `yield` 生成器（Java 没有直接等价物，Java 的 Iterator + 懒加载类似）
- `iter()` / `next()` 协议
- 生成器表达式（类似列表推导式但惰性）
- `range()` 在 Python 3 是生成器（Python 2 是列表）

**实战代码**：
```python
# Java: for (int i : new int[]{1,2,3,4,5}) { System.out.println(i); }
# Python:
for i in [1, 2, 3, 4, 5]:
    print(i)

# 生成器：用 yield 产出值（惰性，不一次性加载到内存）
# Java 的 Iterator 只有"消费"语义，Python 的 yield 还有"暂停"语义
def count_up_to(n):
    i = 1
    while i <= n:
        yield i   # 暂停并返回值，下次调用从这里继续
        i += 1

counter = count_up_to(5)   # 创建生成器对象，不执行函数体
print(next(counter))  # 1
print(next(counter))  # 2
print(next(counter))  # 3

# 用 list() 一次性消费
counter2 = count_up_to(3)
print(list(counter2))  # [1, 2, 3]

# 斐波那契生成器
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
for _ in range(10):
    print(next(fib), end=" ")  # 0 1 1 2 3 5 8 13 21 34

# 生成器表达式 vs 列表推导式
# 列表推导式：立即计算，返回列表（占内存）
squares_list = [x*x for x in range(1000000)]  # 占用大量内存

# 生成器表达式：惰性，用多少算多少
squares_gen = (x*x for x in range(1000000))  # 只占用生成器对象本身

# itertools 库（Java 没有等价的标准库）
import itertools
# itertools.islice 惰性切片
# itertools.takewhile 条件截止
# itertools.chain 链接迭代器
```

**作业验收**：
- [ ] 实现一个 `lazy_range(start, end, step)` 生成器，不要用 `range()`
- [ ] 实现一个流式处理数据的管道：生成 1-100 → 过滤偶数 → 平方 → 求和
- [ ] 比较列表推导式和生成器表达式的内存占用差异

---

#### **Day 15 — 上下文管理器与资源管理**

**今日主题**：`with` 语句 vs Java try-with-resources

**核心知识点**：
- `with` 语句（Python 2.6+，Java 7+ 的 try-with-resources 类似）
- `__enter__` / `__exit__` 协议
- `@contextmanager` 装饰器（用生成器实现上下文管理器）
- `contextlib` 模块（简化自定义上下文管理器）

**实战代码**：
```python
# Java: try (BufferedReader br = new BufferedReader(new FileReader("file.txt"))) { ... }
# Python:
with open("test.txt", "r") as f:
    content = f.read()

# 自定义上下文管理器
class DatabaseConnection:
    def __enter__(self):
        print("连接数据库...")
        self.conn = "数据库连接对象"
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("关闭数据库连接...")
        # exc_type/exc_val/exc_tb 捕获异常信息
        if exc_type:
            print(f"发生异常: {exc_val}")
        return False  # 返回 True 表示吞掉异常

with DatabaseConnection() as conn:
    print(f"使用 {conn} 进行操作")

# @contextmanager 简化版（用生成器实现）
from contextlib import contextmanager

@contextmanager
def timer_context(name):
    start = time.time()
    try:
        yield name
    finally:
        print(f"{name} 耗时: {time.time()-start:.2f}秒")

with timer_context("计算"):
    time.sleep(1)
    print("执行中...")

# @contextmanager 实现文件操作的简化写法
from contextlib import contextmanager

@contextmanager
def open_file(path, mode):
    f = open(path, mode)
    try:
        yield f
    finally:
        f.close()

# 使用 suppress 忽略特定异常
from contextlib import suppress
with suppress(FileNotFoundError):
    os.remove("not_exist.txt")  # 不会抛异常
```

**作业验收**：
- [ ] 用 `@contextmanager` 实现一个"计时上下文管理器"
- [ ] 用 `@contextmanager` 实现一个"嵌套事务"（进入时打印 BEGIN，退出时 COMMIT/ROLLBACK）
- [ ] 理解 `contextlib.closing()` 的用途

---

#### **Day 16 — 并发编程：线程与进程**

**今日主题**：GIL 困境与多线程/多进程 vs Java

**核心知识点**：
- Python GIL（Global Interpreter Lock）— Java 没有，每个线程真正并行
- CPU 密集型用多进程（`multiprocessing`），IO 密集型用多线程（`threading`）
- `concurrent.futures`（Python 3.2+，类似 Java ExecutorService）
- asyncio（协程，Python 3.5+，Java 有 Project Loom 但未成主流）

**实战代码**：
```python
import threading
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

# IO 密集型任务：多线程（不受 GIL 影响）
def fetch_url(url):
    time.sleep(1)  # 模拟网络请求
    return f"获取: {url}"

urls = [f"http://example.com/{i}" for i in range(5)]

# ThreadPoolExecutor