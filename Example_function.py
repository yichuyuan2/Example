def exchangeRate(dollar):
    """美元->人民币
    汇率暂定为6.5
    """
    return dollar*6.5

print(exchangeRate(10))
print(exchangeRate.__doc__)
print(help(exchangeRate))

def test(*params, extra = "8"):
    print("收集参数是：", params)
    print("位置参数是：", extra)
    print("第二个参数是：", params[1])

a = [1,2,3,4,5,6,7,8]
print(test(*a))