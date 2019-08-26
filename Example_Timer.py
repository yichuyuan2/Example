#定制一个计时器的类
#start和stop代表启动计时器和停止计时
#假设计时器对象t1,print(t1)和直接调动t1均显示对象
#两计数器对象可以相加，t1+t2

import time as t

class MyTimer:
    def __init__(self):
        self.unit = ['年','月','天','小时','分钟','秒']
        self.prompt = "未开始计时!"
        self.lasted = []
        self.begin = 0
        self.end = 0

    def __str__(self):
        return self.prompt
    __repr__ = __str__

    #开始计时
    def start(self):
        self.begin = t.localtime()
        self.prompt = "提示：请先调用stop()结束计时！"
        print("计时开始")
    #停止计时
    def stop(self):
        if not self.begin:
            print("提示：请先调用start()开始计时！")
        else:
            self.end = t.localtime()
            self._calc()
            print("计时结束！")
    #计算运行时间
    def _calc(self):
        self.lasted = []
        self.prompt = "总共运行了"
        for index in range(6):
            self.lasted.append(self.end[index] - self.begin[index])
            if self.lasted[index]:
                self.prompt += (str(self.lasted[index])+self.unit[index])
        #为下一轮计算初始化变量
        self.begin = 0
        self.end = 0
    #两对象相加
    def __add__(self, other):
        prompt = "总共运行了"
        result = []
        for index in range(6):
            result.append(self.lasted[index] + other.lasted[index])
            if result[index]:
                prompt += (str(result[index]) + self.unit[index])
        return prompt
    
t1 = MyTimer()
t1 #未开始计时
t1.stop() #提示：请先调用start()开始计时！
t1.start() #计时开始
t1 #提示：请先调用stop()开始计时！
t1.stop() #计时结束！
t1 #总共运行了8秒
t2 = MyTimer()
t2.start() #计时开始
t2.stop() #计时结束！
t2 #总共运行了4秒
t1+t2 #总共运行了12秒

