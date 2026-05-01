import time
Error = 0
while True:
    try:
        user_age_str = input("请输入你的年龄：")
        user_age = int(user_age_str)
    except ValueError:
        print("给我输入数字啊混蛋！\n重来！")
        Error += 1
        continue
    try:
        if user_age <= 0:
            raise ValueError("666,年龄竟然 <= 0！逆天！\n给我重来！")
    except ValueError as e:
        print(e)
        Error += 1
    else:
        print(f"了解！你今年{user_age}岁了！")
        user_10years_age = user_age + 10
        print(f"你十年后将会是{user_10years_age}岁！")
        answer = input("是否再次使用？（y/n）：")
        if answer == "y" or answer == "Y" or answer == "YES" or answer == "yes":
            print("没问题，接着来吧！")
            continue
        else:
            print("好的，再会！")
        time.sleep(3)
        if Error >= 3:
            print("""作者OS：
你特么居然能错这么多次，建议去脑科看看🤣""")
            break
input("按回车键退出...")
