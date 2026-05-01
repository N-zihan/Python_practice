import time
from openai import OpenAI

# ========== 硅基流动配置 ==========
API_KEY = ""          # 替换成你的真实 API Key
BASE_URL = "https://api.siliconflow.cn/v1"

client = OpenAI(
    api_key = API_KEY,
    base_url = BASE_URL,
)

def get_ai_message(prompt: str) -> str:
    """调用硅基流动 AI，生成猫娘语气的一句话"""
    try:
        response = client.chat.completions.create(
            model="Qwen/Qwen2.5-72B-Instruct",   # 可用免费模型
            messages=[
                {"role": "system", "content": "你是一只可爱的猫娘，说话语气要带上'喵~'，句子简短生动，带有撒娇和吐槽的感觉。"},
                {"role": "user", "content": prompt}
            ],
            max_tokens=50,        # 控制回复长度，节省额度
            temperature=0.9,      # 随机性，让每次回复不同
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        # API 调用失败时返回默认话术，程序不崩溃
        print(f"[AI调用失败，使用默认回复] 错误：{e}")
        return "主人又搞错了喵～真是拿你没办法！"

# ========== 平均值计算器主程序 ==========
total = 0.0
count = 0
max_error = 3
error_count = 0

print("Ciallo～(∠・ω< )⌒☆ 我是平均值计算器喵！")
print("输入数字就可以累加喵，最后输入字母 q 就能得到平均数～\n")

while True:
    user_input = input("请输入数字喵～（完成后输入q）：")
    if user_input == "q":
        break

    try:
        num = float(user_input)
        total += num
        count += 1
        print(f"✓ 收到 {num}，当前共 {count} 个数字喵～\n")
    except ValueError:
        error_count += 1
        # 根据错误次数，让 AI 生成不同的话
        if error_count == 1:
            prompt = "主人第一次输入了非数字的内容，用猫娘语气吐槽他一下，要求句子很短（20字以内），带'喵~'"
            ai_msg = get_ai_message(prompt)
            print(f"【猫娘】{ai_msg}")
            print(f"（提示：如果再连续错 {max_error - error_count} 次，人家就真的要生气了喵！）\n")
        elif error_count == 2:
            prompt = "主人又第二次输入错误，你作为猫娘有点小生气了，用短句警告他，带'喵~'，要可爱"
            ai_msg = get_ai_message(prompt)
            print(f"【猫娘】{ai_msg}")
            print(f"（⚠️ 警告：已经连续错了 {error_count} 次，再错 {max_error - error_count} 次我就退出啦！）\n")
        elif error_count >= max_error:
            print(f"【猫娘】哼！竟然连续错了 {max_error} 次，主人是笨蛋喵！我不跟你玩了，再见！")
            print("程序将在 3 秒后退出...")
            time.sleep(3)
            exit(1)
        continue

# 计算并输出结果
if count == 0:
    print("\n喵？主人你一个数字都没给人家，就直接按 q 了……")
    time.sleep(1)
    print("那平均值只能是 0 了喵，真是的～")
else:
    avg = total / count
    print(f"\n✨ 主人！我算出来了，这 {count} 个数字的平均值是 {avg:.2f} 喵～ ✨")

time.sleep(1)
print("\n主人我累了，先去睡啦～如果想再用我，重新启动程序就好喵～")
time.sleep(0.8)
print("Bye bye～ ฅ^•ﻌ•^ฅ")
input("\n按回车键退出...")