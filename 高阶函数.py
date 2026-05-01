def calculator_square(self_power):
    return self_power ** self_power

def calculator_and_print(self_power , calculator):
    result = calculator(self_power)
    print(f"""[数字参数]:{self_power}
[计算结果]:{result}""")

calculator_and_print(3 , calculator_square)