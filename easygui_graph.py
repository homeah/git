import sys
import easygui as g
#if g.ccbox('亲爱的还玩吗？',choices=['还要玩','算了吧^_^']):
#      g.msgbox('还是不玩了，快睡觉吧！')
#else:
#      sys.exit(0)
#x = g.buttonbox('你喜欢什么水果？','选择水果',['西瓜','香蕉','橙子'])
#g.msgbox('你选择的是'+x)
#y = g.multchoicebox(msg = '你喜欢多种水果吗？',title = '选水果',choices = ('西瓜','香蕉','橙子','菠萝','葡萄'))    
#g.msgbox('你选择的是'+str(y))

#z = g.enterbox(msg='请说出你的悄悄话',title = '悄悄话',default = '')
#g.msgbox(z)
#a = g.integerbox(msg = '请输入你的得分',title = '分数',lowerbound = 0,upperbound = 150)
#g.msgbox('你的得分是'+str(a))

#b = user_info = g.multpasswordbox(msg = '请输入用户名和密码',title='用户登录接口',fields=('用户名','密码'))
#g.msgbox(b)
#
"""c = g.textbox(msg='测试一下',title='海子的诗',text ='''从明天起，做一个幸福的人
喂马、劈柴，周游世界
从明天起，关心粮食和蔬菜
我有一所房子，面朝大海，春暖花开
从明天起，和每一个亲人通信
告诉他们我的幸福
那幸福的闪电告诉我的
我将告诉每一个人
给每一条河每一座山取一个温暖的名字
陌生人，我也为你祝福
愿你有一个灿烂的前程
愿你有情人终成眷属
愿你在尘世获得幸福
我只愿面朝大海，春暖花开。''',codebox = 1)
g.msgbox(c)"""
#g.msgbox('你好')
#g.diropenbox(msg='打开2个文件夹',title="文件夹",default='D:\python\练习')
#a = g.fileopenbox(msg='打开文件',title='py结尾文件',default='D:\python\练习\*.py')
#g.msgbox(a)
#a = g.filesavebox()
#g.msgbox(a)
try:
      print('I love you !')
      int('fishC')
except:
      g.exceptionbox()




