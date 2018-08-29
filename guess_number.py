import random
import easygui as g
import sys
g.msgbox('嗨，欢迎进入第一个界面游戏^_^')
secret = random.randint(1,10)
msg = '不妨猜一下小甲鱼现在心里想的是哪个数字(1-10):'
title = '猜数字小游戏'
guess = g.integerbox(msg,title,lowerbound=1,upperbound=10)
try:
      while True:
            if guess == secret:
                  g.msgbox('哇哦，你是小甲鱼心里的蛔虫吗？！')
                  g.msgbox('哼，猜中了也没奖励！')
                  msg = '你希望重新开始小游戏吗？'
                  title = '请选择'
                  choices = ('是','否')
                  if g.ccbox(msg,title,choices):
                        secret = random.randint(1,10)
                        msg = '不妨猜一下小甲鱼现在心里想的是哪个数字(1-10):'
                        title = '猜数字小游戏'
                        guess = g.integerbox(msg,title,lowerbound=1,upperbound=10)
                  else:
                        sys.exit(0)
            else:
                  if guess > secret:
                        g.msgbox('哥，大了大~~~')
                  else:
                        g.msgbox('黑，小了小小了~~~')
                  guess = g.integerbox(msg,title,lowerbound=1,upperbound=10)
except:
	print('结束了')          


