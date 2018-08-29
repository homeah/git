class Stack:
      def __init__(self,start=[]):
            self.stack = []
            for x in start:
                  self.push(x)
                  
      def isEmpty(self):
            return not self.stack
                  
      def push(self,obj):
            self.stack.append(obj)
            print(self.stack)
            
      def top(self):
            if not self.stack:
                  print('堆栈空了，没有元素了！')
            else:
                  return self.stack[-1]
             
      def pop(self):
            if not self.stack:
                  print('堆栈空了，没有元素了！')
            else:
                  self.stack.pop()
                  print('当前栈数据为：',self.stack)                 

      def bottom(self):
            if not self.stack:
                  print('堆栈空了，没有元素了！')
            else:
                  print('栈底数据为：',self.stack[0])
            
                  
