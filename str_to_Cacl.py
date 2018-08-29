def str_to_calc(string):
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
                              temp0 /= temp1
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
                  temp0 /= temp1
                  
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

