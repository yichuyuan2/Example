#类、对象与继承
import random as r

class Fish:
    def __init__(self):
        self.x = r.randint(0,10)
        self.y = r.randint(0,10)
    
    def move(self):
        #假设所有鱼都是一路向西游，不考虑场景边界检查和方向移动问题
        self.x -= 1
        print("我的位置是:", self.x, self.y)
    
class Goldfish(Fish):
    pass

class Carp(Fish):
    pass

class Salmon(Fish):
    pass

class Shark(Fish):
    def __init__(self):
        Fish.__init__(self)
        #super().__init__()
        self.hungry = True
    def eat(self):
        if self.hungry:
            print("吃货的梦想就是天天有的吃^_^")
            self.hungry = False
        else:
            print("太撑了，吃不下！")

def test():
    fish = Fish()
    fish.move()
    goldfish = Goldfish()
    goldfish.move()
    goldfish.move()
    goldfish.move()
    shark = Shark()
    shark.eat()
    shark.eat()
    shark.move()
    shark.move()

if __name__ == '__main__':
    test()
