print("--------------chenwei-------------")
temp = input("不妨猜测一下我心里想的是哪个数字：")
guess = int(temp)
while guess != 8:
    if guess > 8:
        temp = input("啊，猜错了，大了大了，再猜一次啦：")
        guess = int(temp)
    else:
        temp = input("啊，猜错了，小了小了，再猜一次啦：")
        guess = int(temp)
print("我草，你是我心里的蛔虫吗？！")
print("猜中了也没奖励!")
print("游戏结束，不玩了！")
