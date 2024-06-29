使用问题记录：

1. pytest 如何指定某个文件的test？
   `pytest path/to/test_file.py` 这可以执行这个文件中所有以test为前缀的test
   `pytest path/to/test_file.py::test_function`  执行选定的这个test

2. pytest 执行test时， 如何显示test中的print 输出
   `pytest -s path/to/test_file.py` 使用 -s 选项即可


3. 在conftest.py 中定义了一个这个函数 ， 在自己的测试文件中也定义了， 怎么选择
具体来说，`pytest` 通过以下方式选择 `pytest_generate_tests` 函数：

1. **当前测试文件中的 `pytest_generate_tests` 函数**：如果在当前测试文件中定义了 `pytest_generate_tests` 函数，`pytest` 会优先使用这个函数来生成测试用例。

2. **`conftest.py` 文件中的 `pytest_generate_tests` 函数**：如果当前测试文件中没有定义 `pytest_generate_tests` 函数，`pytest` 会向上查找最近的 `conftest.py` 文件，并使用其中定义的 `pytest_generate_tests` 函数。

3. **多个 `conftest.py` 文件中的 `pytest_generate_tests` 函数**：如果有多个 `conftest.py` 文件，`pytest` 会根据目录层级，从测试文件所在目录开始，逐层向上查找，直到找到一个定义了 `pytest_generate_tests` 函数的 `conftest.py` 文件。

这种机制允许你在不同层级定义不同的 `pytest_generate_tests` 函数，从而实现灵活的测试用例生成策略。





example

```
mport pytest


# Arrange
@pytest.fixture
def first_entry():
    print("call fisrt_entry")
    return "a"


# Arrange
@pytest.fixture
def order():
    print("call order")
    return []


# Act
@pytest.fixture
def append_first(order, first_entry):
    print("call append_first")
    return order.append(first_entry)


def test_string_only(append_first, order, first_entry):
    # Assert
    assert order == [first_entry]

''' out put: 
test_append.py call order
call fisrt_entry
call append_first
'''
```

### 分析调用顺序

1. `test_string_only` 需要 `append_first`、`order` 和 `first_entry` 这三个fixture。
2. `pytest`发现`append_first`依赖于`order`和`first_entry`。
3. `pytest`会首先调用`order`和`first_entry`这两个fixture，因为它们不依赖于其他fixture。

具体步骤如下：

1. **调用 `order`**：
   - `order` fixture被调用，输出`"call order"`。
   - `order` fixture返回一个空列表 `[]`。

2. **调用 `first_entry`**：
   - `first_entry` fixture被调用，输出`"call first_entry"`。
   - `first_entry` fixture返回字符串`"a"`。

3. **调用 `append_first`**：
   - `append_first` fixture被调用，因为它依赖于`order`和`first_entry`，此时这两个依赖都已经准备好。
   - `append_first` fixture内部调用了 `order.append(first_entry)`，将`"a"`添加到空列表`[]`中，结果是`["a"]`。
   - `append_first` fixture输出`"call append_first"`。

4. **执行 `test_string_only` 测试函数**：
   - `test_string_only` 测试函数被调用，传入的参数已经准备好：`append_first=None`（因为`append_first`的返回值是`None`），`order=["a"]`，`first_entry="a"`。
   - 在测试函数中，断言 `order == [first_entry]` 通过。

### 为什么 `order` 先于 `first_entry`？

`pytest`在处理fixture调用顺序时，默认是按照它们在代码中出现的顺序来解析和调用的，除非有显式的依赖关系。因为`order`在代码中位于`first_entry`之前，因此它会先被调用。

在没有显式依赖关系的情况下，`pytest`按照以下策略来决定fixture的调用顺序：

1. 解析测试函数的参数，确定需要哪些fixture。
2. 按照fixture在代码中定义的顺序来解析和调用它们。


fixture 默认的scope是什么？

在 pytest 中，fixture 是一种用于在测试函数执行之前准备测试环境的机制。fixture 的 `scope` 参数用于定义 fixture 的作用范围。pytest 提供了四种作用范围：

1. **function**: 每个测试函数都会调用一次 fixture，这是默认的作用范围。
2. **class**: 在每个测试类中调用一次，即在类中所有测试方法共享同一个 fixture 实例。
3. **module**: 在每个模块中调用一次，即在模块中所有测试函数共享同一个 fixture 实例。
4. **session**: 在整个测试会话中调用一次，即所有测试函数共享同一个 fixture 实例。


examples

```python
import pytest


@pytest.fixture(params=[0, 1, pytest.param(2, marks=pytest.mark.skip)])
def data_set(request):
    return request.param


def test_data(data_set):
    pass
```

分析
- `@pytest.fixture`: 这是一个装饰器，用于将函数标记为fixture。
- `params=[0, 1, pytest.param(2, marks=pytest.mark.skip)]`: `params`参数指定了要传递给fixture的参数列表。在这个例子中，参数列表包含三个值：`0`、`1` 和 `2`。其中，`2` 被标记为 `pytest.mark.skip`，这意味着在运行测试时，使用参数 `2` 的测试会被跳过。
- `request`: 这是一个内置的fixture，提供了对当前测试请求的访问，包括传递给fixture的参数。
- `return request.param`: 返回当前参数值。

### 2. 测试函数 `test_data`
```python
def test_data(data_set):
    pass
```
- `def test_data(data_set)`: 定义了一个测试函数 `test_data`，它使用 `data_set` fixture 作为参数。
- `pass`: 这是一个占位符语句，表示什么也不做。可以在这里添加实际的测试逻辑。

### 执行过程
当运行测试时，Pytest 会为每个参数值单独运行 `test_data` 测试函数。

1. **第一次运行**:
   - `data_set` 参数为 `0`。
   - `data_set` fixture 返回 `0`。
   - `test_data` 函数接收 `0` 作为参数并执行（什么也不做，因为是 `pass`）。

2. **第二次运行**:
   - `data_set` 参数为 `1`。
   - `data_set` fixture 返回 `1`。
   - `test_data` 函数接收 `1` 作为参数并执行（什么也不做，因为是 `pass`）。

3. **第三次运行**:
   - `data_set` 参数为 `2`。
   - 由于 `2` 被标记为 `pytest.mark.skip`，Pytest 会跳过这个测试。