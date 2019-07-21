def exchangeRate(dollar):
    """美元->人民币
    汇率暂定为6.5
    """
    return dollar*6.5

print(exchangeRate(10))
print(exchangeRate.__doc__)
print(help(exchangeRate))