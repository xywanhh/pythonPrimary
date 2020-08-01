from abc import ABCMeta,abstractmethod

class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self):
        pass

class Wechatpay(Payment):
    def fuqian(self,money):
        '''
        实现了pay的功能，但是名字不一样
        '''
        print('微信支付了%s元'%money)

p1 = Wechatpay() #不调就报错了
# TypeError: Can't instantiate abstract class Wechatpay with abstract methods pay