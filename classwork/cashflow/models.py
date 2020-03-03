class CashFlow(object):

    def __init__(self, amount, t):
        self.amount = amount
        self.t = t

    def present_value(self, ir, t=0):
        pv = round(self.amount*(1+ir)**(-self.t+t), 2)
        return CashFlow(amount=pv, t=0)

    def shift(self, t, ir):
        value = self.present_value(ir=ir, t=t)
        return CashFlow(value.amount, t=t)

    def to_dict(self):
        return {
            'amount': self.amount,
            't': self.t
        }
