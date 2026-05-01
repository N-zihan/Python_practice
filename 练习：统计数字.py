total = 0
count = 0
file_name = r"C:\Users\NZH\Desktop\python入门编程训练处\numbers"

try:
    with open(file_name, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line == "":
                continue
            try:
                num = float(line)
                total += num
                count += 1
            except ValueError:
                print(f"跳过非数字行：{line}")
except FileNotFoundError:
    print(f"文件：{file_name} 不存在！")

if count == 0:
    print("无有效数字！")
else:
    print(f"总和：{total},平均数：{total/count}")

with open("result", "w", encoding="utf-8") as a:
    a.write(fr"""来自 C:\Users\NZH\Desktop\python入门编程训练处\numbers 文件的计算结果！

总和：{total}
平均数：{total/count}""")