print("--------------chenwei-------------")

anothertime = 'Y'
while anothertime == 'Y':
    import random
    secret = random.randint(1,20)
    temp = input("不妨猜测一下我心里想的是哪个数字1-20之间哦：")
    guess = int(temp)
    while guess != secret:
        if guess > secret:
            temp = input("啊，猜错了，大了大了，再猜一次啦：")
            guess = int(temp)
        else:
            temp = input("啊，猜错了，小了小了，再猜一次啦：")
            guess = int(temp)
    print("哇哦，你是我心里的蛔虫吗？！")
    print("猜中了也没奖励!")
    anothertime = input('还想再玩一次吗？Y or N\n')
print("游戏结束，不玩了！")
import os
os.system("pause")
