import time as t
class Mytimer:
      def __init__(self):
            self.unit = ['年','月','日','时','分','秒']
            self.begin = 0
            self.end = 0
            self.prompt = '尚未启动计时器！'
            self.last = []
            self.borrow = [0,12,31,24,60,60]
            
      def __add__(self,other):
            prompt = '两个计时器共跑了'
            result = []
            if self.last or other.last:
                  for index in range(6):
                     result.append(self.last[index] + other.last[index])
                     if result[index]:
                           prompt += (str(result[index])+self.unit[index])
            else:
                  print('有计时器未启动或启动未停止')
                  return
            return prompt

      def __repr__(self):
            return self.prompt
      

      def start(self):
            self.last = []
            self.begin = list(t.localtime())
            #self.begin = [2017, 12, 29, 11, 23, 48, 6, 28, 0]
            self.prompt = '请先用stop()停止计时'
            print('计时开始...')

      def stop(self):
            if not self.begin:
                  print('请先启动计时器！')
            else:
                  self.end = list(t.localtime())
                  #self.end = [2018, 1, 28, 10, 22, 24, 6,28,0]
                  print('计时结束！')
                  self._calc()

      def _calc(self):
            self.prompt = '计时周期是：'
            temp = []
            for index in range(6):
                  if (self.end[5-index]-self.begin[5-index])<0:
                        temp.append(self.end[5-index]+self.borrow[5-index]-self.begin[5-index])
                        self.end[4-index] -= 1
                  else:
                       temp.append(self.end[5-index]-self.begin[5-index])
            self.last = list(reversed(temp))
            for index in range(6):
                  if self.last[index]:
                        self.prompt += (str(self.last[index]) + self.unit[index])
            self.begin = 0
            self.end = 0
            return self.prompt

