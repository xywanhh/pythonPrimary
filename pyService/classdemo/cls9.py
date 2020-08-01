class Alipay:
    '''
    支付宝支付
    '''
    def pay(self,money):
        print('支付宝支付了%s元'%money)

class Applepay:
    '''
    apple pay支付
    '''
    def pay(self,money):
        print('apple pay支付了%s元'%money)


def pay(payment,money):
    '''
    支付函数，总体负责支付
    对应支付的对象和要支付的金额
    '''
    payment.pay(money)

class Payment:
    def pay(self):
        raise NotImplementedError

class Wechatpay(Payment):
    def fuqian(self,money):
        '''
        实现了pay的功能，但是名字不一样
        '''
        print('微信支付了%s元'%money)

p = Alipay()
pay(p,200)

p1 = Wechatpay() # 没有实现接口方法pay
pay(p1,200)   #执行会报错