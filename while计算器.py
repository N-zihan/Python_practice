"""
平均值计算器模块，提供猫娘风格的交互式平均值计算。

函数:
    run_calculator(): 启动一次计算，返回平均值或None。

注: 你可以直接打开模块直接使用 (不会执行return返回，根据"剧情需要"，可能会"退出程序") ，也可以导入到你的程序里运行
"""

import time

__all__ = ["run_calculator"]

if __name__ == "__main__":
    print("Ciallo～(∠・ω< )⌒☆ 我是平均值计算器喵！")

def run_calculator():
    total = 0
    count = 0
    result = 0
    max_error = 3
    error_count = 0
    has_any_non_q_input = False
    has_any_non_empty_input = False

    while True:
        user_input = input("请输入数字喵~（完成后还请输入字母q喵~）：")
        if user_input == "q":
            break

        has_any_non_q_input = True

        if user_input != "":
            has_any_non_empty_input = True

        try:
            num = float(user_input)
            total += num
            count += 1
            result = total / count
        except ValueError:
            if user_input == "":
                print("喵？空输入可不算数字哦，请认真输入喵～")
                continue
            error_count += 1
            if error_count == 1:
                print("主人是大笨蛋喵！居然不会输入阿拉伯数字，人家怎么会看的懂嘛！重新来过喵！不准再用其他字符了喵")
                print(f"如果累计错误{max_error}次，就说明主人太笨了，人家就不跟你玩了喵！")
            elif error_count == 2:
                print("呜……怎么又错了？主人你再这样人家要生气了喵！输入数字好不好？")
            elif error_count == 3:
                print(f"主人竟然真的累计错误了{max_error}次，你太笨了，哼！人家不跟你玩了喵！程序退出，bye~")
                if __name__ == "__main__":
                    input("请按任意键退出...")
                    exit()
                else:
                    return None
            continue

    if count == 0:
        if not has_any_non_q_input:
            print("喵？主人你什么都没输入，直接按 q 就跑了喵？")
            time.sleep(2)
            print(f"那人家只能告诉你平均值是{result}了，真是的～")
            time.sleep(2)
            print("下次至少给人家一个数字嘛，不然人家会很寂寞的喵～")
        elif not has_any_non_empty_input:
            print("喵？主人你一直按回车，然后直接 q 是想怎样啦～")
            time.sleep(3)
            print("一个数字都不给人家，平均值只能是 0 了喵！")
            time.sleep(3)
            print("下次再这样，人家就真的生气咯！哼～")
        else:
            print("诶？")
            time.sleep(2)
            print("呜……主人你一个数字都没输入就直接按q了喵？")
            time.sleep(3)
            print("那人家只能告诉你平均值是0了，真是拿你没办法喵～")
            time.sleep(5)
            print("主人你是不是在逗我玩喵！人家真的生气了喵！不理你了！")
        if __name__ == "__main__":
            input("请按任意键退出")
            exit()
        else:
            return None
    else:
        time.sleep(3)
        print(f"主人！我算出它们的平均数了！是{result}喵~")
        time.sleep(5)
        return result

if __name__ == "__main__":
    while True:
        run_calculator()
        again = input("喵～主人还想再用我一次吗？(y/n): ")
        if again == 'y' or again == 'yes':
            print("好哒！那我们重新开始喵～\n")
            time.sleep(1)
            continue
        else:
            print("喵～那好吧，主人再见啦～ Bye bye～")
            time.sleep(1)
            break

    print("\n平均值计算器已关闭，随时可以重新启动喵～")
    input("按回车键退出...")