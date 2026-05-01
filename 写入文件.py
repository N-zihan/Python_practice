with open("C:/Users/NZH/Desktop/python入门编程训练处/文本",'a+',encoding="utf-8") as f:
    f.write("""\n我欲乘风归去，
又恐琼楼玉宇，
高处不胜寒。""")
    f.seek(0)
    print(f.read())