user_data = {'嘟嘟': '12345678987654321', '妞妞': 'red', '爷爷': '123', '奶奶': '321', 'xiao': '', '爸爸': 'orange'}

def new_user():
     prompt = '请输入用户名：'
     username = input(prompt)
     while username in user_data:
          print('用户名已被使用，请更换一个！')
          username = input(prompt)
     passwd = input('用户名可用，请输入密码：')
     user_data[username] = passwd
     print('恭喜你注册成功')

def old_user():
     prompt = '请输入用户名：'
     username = input(prompt)
     while username not in user_data:
          print('你输入的用户名不存在，请重新输入：')
          username = input(prompt)
     
     passwd = input('请输入密码：')
     while True:
               if user_data.get(username) == passwd:
                         print('登录成功，欢迎进入电脑系统')
                         break
               else:
                         passwd=input('密码输入错误！请重新输入：')
def change_passwd():
     prompt = '请输入需要修改密码的用户名：'
     username = input(prompt)
     oldpasswd = input('请输入原密码：')
     if user_data[username] == oldpasswd:
               newpasswd = input('请输入新密码：')
               user_data[username]= newpasswd
               print(username+'的密码修改成功')
     else:
               print('原密码输入错误！')

def del_user():
          prompt = '请输入需要删除的用户名：'
          username = input(prompt)
          if username not in user_data:
                    print('你输入的用户名不存在!')
          else:
                    user_data.pop(username)
                    print(username+'删除成功！')

def showmenu():
     prompt = '''
|---删除用户：      0---|
|---新建用户：      1---|
|---登录账号：      2---|
|---修改密码：      3---|
|---显示所有用用户：4---|
|---退出程序：      5---|
|---请输入正确指令：'''
     while True:
          while True:
               choice = input(prompt)
               if choice not in '012345':
                    print('输入指令有误')
               else:
                    break
          if choice=='1':
               new_user()
          elif choice == '0':
                    del_user()
          elif choice=='2':
               old_user()
          elif choice=='3':
               change_passwd()
          elif choice=='4':
               for key,value in user_data.items():
                         print(key,value)
          else:
               break

showmenu()
     
               
          
