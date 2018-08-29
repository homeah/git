import easygui as g
import sys
while 1:
      g.msgbox('嗨，欢迎进入第一个界面小游戏^_^')
      msg = '请问你想学什么知识呢？'
      title = '小游戏互动'
      choices = ['编程','琴棋书画','奥数','英语','篮球']
      choice = g.choicebox(msg,title,choices)
      g.msgbox('你选择的是：'+str(choice),'结果')
      msg = '你希望重新开始小游戏吗？'
      title = '请选择'
      if g.ccbox(msg,title):
            pass
      else:
            sys.exit(0)
      
