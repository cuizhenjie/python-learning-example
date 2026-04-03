# Day 1 作业提交

## 作业 1：环境验收 ✅

```bash
$ python3 --version
Python 3.14.3

$ pip --version
pip 26.0 from /Users/cuizhenjie/.venv/py3/lib/python3.14/site-packages/pip

$ pip install requests
Successfully installed requests-2.33.1

$ python -c "import requests; print('requests 安装成功')"
requests 安装成功
```

## 作业 2：运行结果

```
类型演示: name=崔总, age=三十岁, type(age)=<class 'str'>
arr[-1]=5
arr[1:4]=[2, 3, 4]
崔总今年三十岁岁
```

## 老师点评

### ✅ 通过
- 环境配置完全正确
- 代码运行正常
- 理解输出结果

### ⚠️ 小问题
`age` 赋值为 `"三十岁"` 后，f-string 里又加了 `岁`，导致输出有两个"岁"。正确写法：
- 方案1：`f"{name}今年{age}"` （age 本身带"岁"）
- 方案2：`age = 30; f"{name}今年{age}岁"`

### 💡 核心收货
1. **动态类型** — 同一变量可赋不同类型，Java 强类型不允许
2. **负索引** — Python 独有，Java 没有
3. **切片** — `[start:end]` 左闭右开，比 Java subList 更简洁
4. **f-string** — `f"{var}"` 格式化，比 `String.format()` 更直观
