def str_to_calc(string):        #算式字符串计算结果
      length = len(string)
      all_op = '+-*/'
      op0 =' '
      operator = '+'
      s = 0
      temp0 = 0
      pos0 = -1
      pos1 = 0
      for i in range(length):
            if string[i] in all_op:
                  pos1 = i
                  temp1 = float(string[pos0+1:pos1])
                  op1 = string[i]
                  if op0 not in all_op:
                        op0 = op1
                        pos0 = pos1
                        temp0 =temp1
                        
                  elif op0 in ('*/'):
                        if op0 =='*':
                              temp0 *= temp1
                        else:
                              try:
                                    temp0 /= temp1
                              except:
                                    return
                        op0 = op1
                        pos0 = pos1
                              
                  else:
                        if operator =='+':
                              s += temp0
                                    
                        else:
                              s -= temp0
                        operator = op0
                        
                        op0 = op1
                        pos0 = pos1
                        temp0 =temp1
                        
      temp1 = float(string[pos0+1:])
      if not pos1:
            s += temp1
      elif op0 in ('*/'):
            if op0 =='*':
                  temp0 *= temp1
            else:
                  try:
                        temp0 /= temp1
                  except:
                        return
                  
            if operator =='+':
                  s += temp0                          
            else:
                  s -= temp0
      else:
            if operator =='+':
                  s += temp0                          
            else:
                  s -= temp0
            if op0 =='+':
                  s += temp1
            else:
                  s -= temp1
      return s


def strN_to_cal(numbers,total):
         str_numbers = str(numbers)
         length1 = len(str_numbers)
         length2 = length1 - 1
         length = 5**length2
         num = 0 #统计符合条件打印次数
         for i in range(length): #123456789九个数字之间有8个位置可以插入符号，'','+','-',有6561种可能
                  string = '' #算式按字符打印
                  n = i
                  for j in range(1,length2+1):
                           if n%5 == 0:  # ''
                                    string += str_numbers[j-1] 
                           elif n%5 == 1:# 第二种情况，'+'
                                    op = '+'
                                    string += (str_numbers[j-1] +op)
                           elif n%5 == 2:             # 第二种情况，'-'
                                    op = '-'
                                    string += (str_numbers[j-1] +op)
                                 
                           elif n%5 == 3:
                                    op = '*'
                                    string += (str_numbers[j-1] +op)

                           else:
                                    op = '/'
                                    string += (str_numbers[j-1] +op)
                                 
                           n = n // 5          # n五进制轮
                  string +=  str_numbers[-1]
                  if total == str_to_calc(string):
                           num += 1
                           print('%s = %d'%(string,total))
         print('符合要求的算式一共有%d条' %num)
         
while True:
      choose = input('想玩数字游戏吗？退出请按1,按其他键继续')
      if choose == '1':
            break
      else:
            numb = input('请输入一串数字:')
            tot = int(input('请输入你想要的结果:'))
            strN_to_cal(numb,tot)
                           
 

            
                  
            
                  
            
