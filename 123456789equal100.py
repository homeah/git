
for i in range(6561): #123456789九个数字之间有8个位置可以插入符号，'','+','-',有6561种可能
      s = 0 #求和
      m = 1 #操作数
      n = i # 确保i操作数不变化
      op = '+'  #记录上一次操作符
      string = '' #算式按字符打印
      for j in range(2,10):              
            if n%3:           # 出现操作符，需要打印算式和操作符
                  string += str(m)  #打印操作数
                  if op =='+':         
                        s += m
                        m = j
                  else:
                        s -= m           
                        m =j
                  
            if n%3 == 0:      # 第一种情况，''，m需要
                  m = m*10+j  
                  
            elif n%3 ==1:     # 第二种情况，'+'
                  op = '+'

            else:             # 第二种情况，'-'
                  op = '-'
            if n%3:
                  string += op   #打印操作数
                  
            n = n // 3          # n三进制轮
      if op =='+':            # 最后一次符号，还需要补加m
            s += m
            string += str(m)
      else:
            s -= m
            string += str(m)
            
      if s ==100:
            print('%s = %d\n' %(string,s))
      
                  
            
                  
            
