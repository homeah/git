import time as t
class MyTimer:
      def __init__(self,func,number=1000000):
            self.prompt = '未开始计时@！'
            self.lasted = 0.0
            self.default_timer = t.perf_counter
            self.func = func
            self.number = number

      def __str__(self):
            return self.prompt

      __repr__ = __str__

      def __add__(self,other):
            result = self.lasted + other.lasted
            prompt = '总共运行了 %0.2f秒' %result
            return prompt

      def timing(self):
            self.begin = self.default_timer()
            for i in range(self.number):
                  self.func()
            self.end = self.default_timer()
            self.lasted = self.end-self.begin
            self.prompt = '总共运行了%0.2f秒' %self.lasted

      #设置计时器
      def set_timer(self,timer):
            if timer =='process_time':
                  self.default_timer = t.process_time
            elif timer == 'perf_counter':
                  self.default_timer = t.perf_counter
            else:
                  print('输入无效，请输入perf_counter 或process_timer')
                        
            
