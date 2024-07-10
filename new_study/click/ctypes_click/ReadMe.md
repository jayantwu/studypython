usage:
`mkdir -p build && cd build && cmake .. && make`

`cd lib`

`python3 cmd.py create --para1='a=1,b=3' --para2='cnt=5,list=(c_uint32*5)(1,2,3,4,5)'`




在 Click 中，当你创建自定义类型时，通常需要实现 `convert` 方法。这是因为 `convert` 方法负责将命令行输入转换为你自定义的类型实例。如果不实现 `convert` 方法，Click 将不知道如何将输入的字符串转换为你定义的类型

