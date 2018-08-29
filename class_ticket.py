class Ticket:
      def __init__(self,weekend=False,child=False):
            self.exp = 100
            if weekend:
                  self.inc = 1.2
            else:
                  self.inc = 1
            if child:
                  self.discount = 0.5
            else:
                  self.discount = 1
      def calcPrice(self,num):
            return self.exp*self.inc*self.discount*num
adult_weekday = Ticket()
adult_weekend = Ticket(weekend = True)
child_weekday = Ticket(child=True)
child_weekend = Ticket(weekend = True,child=True)
adult_num = int(input('请输入大人数量：'))
child_num = int(input('请输入小孩数量：'))
weekday = input('是否是工作日?(是请选择Y，不是选择N)')
if weekday == 'Y':
      total_price = adult_weekday.calcPrice(adult_num)+child_weekday.calcPrice(child_num)
      print('【%d】个大人和【%d】个小孩，在工作日的费用共计【%.2f元】' %(adult_num,child_num,total_price))

else:
      total_price = adult_weekend.calcPrice(adult_num)+child_weekend.calcPrice(child_num)
      print('【%d】个大人和【%d】个小孩，在周末的费用共计【%.2f元】' %(adult_num,child_num,total_price))

