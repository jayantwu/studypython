class TestClassDemoInstance:
    value = 0

    def test_one(self):
        self.value = 1
        assert self.value == 1
        #print(self.value)

    def test_two(self):
        assert self.value == 1
        #print(self.value)
## pytest 执行时， 会创建两个 实例， ins1 执行test_one(), ins2 执行 test_two(), test_one 中改变的是实例的value,
'''
ins1 = TestClassDemoInstance()
ins2 = TestClassDemoInstance()

ins1.test_one() # 1
ins1.test_two() # 1
ins2.test_two() # 0

print(TestClassDemoInstance.value)   # 0
'''

