import time
def bmi():
    user_weight = int(input("请输入你的体重（单位：kg）（整数）："))
    user_height = float(input("请输入你的身高（单位：m）："))
    user_mbi = float(str(user_weight)) / float(str(user_height)) ** 2
    print("你的MBI指数为：" + str(user_mbi))
    if user_mbi <= 18.5:
        result = "偏瘦"
    elif user_mbi <= 25:
        result = "正常"
    elif user_mbi <= 30:
        result = "偏胖"
    elif 30 < user_mbi:
        result = "肥胖"
    print(f"您的身体状况为{result}")
    return 0
while True:
    bmi()
    time.sleep(1)
    answer = input("是否继续使用（y/n）：")
    if answer == "y" or answer == "Y" or answer == "yes":
        print("好的，请继续")
        time.sleep(1)
        continue
    else:
        print("好的，感谢您的使用，再见！")
        time.sleep(1)
        break
input("请按回车键退出程序...")
exit()