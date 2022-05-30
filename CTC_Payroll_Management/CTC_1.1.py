class CTC:
    def __init__(self, pay):
        self.pay = pay
        self.obj_pay = Gross_pay(self.pay)

    def get_ctc(self):
        return self.obj_pay.month_gross()


class Gross_pay:
    def __init__(self, monthly_pay):
        self.monthly_pay = monthly_pay

    def month_gross(self):
        return self.monthly_pay * 12


a = CTC(1000)
print(a.get_ctc())
