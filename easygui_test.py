import easygui as g
msg = '请填写以下信息(带*是必填项)'
title = '账号中心'
fieldNames =['*用户名','固定电话','手机号码','QQ号']
fieldValues = g.multenterbox(msg,title,fieldNames)
while True:
      if fieldValues == None:
            break
      errmsg = ''
      for i in range(len(fieldNames)):
            option = fieldNames[i].strip()
            if fieldValues[i].strip() =='' and option[0]=='*':
                  errmsg += ('【%s】为必填项' %fieldNames[i])
      if errmsg == '':
            break
      fieldValues = g.multenterbox(msg,title,fieldNames,fieldValues)
g.msgbox('您填写资料如下：%s' %str(fieldValues))
