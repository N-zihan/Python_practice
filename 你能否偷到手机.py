your_parents_mood = int(input("你的父母的心情值："))
if 60 <= int(your_parents_mood) < 80:
    print("可以偷到，但是，你给我小心点！")
elif int(your_parents_mood) >= 80:
    print("放心大胆地去偷吧！")
else:
    print("别做梦了！0")
