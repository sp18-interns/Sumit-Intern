class Gross_pay:
    def __init__(self, monthly_pay):
        self.monthly_pay = monthly_pay

    def month_gross(self):
        return int(self.monthly_pay / 12)


class Benifit_Deductions:
    def __init__(self, pay):
        self.pay = pay

    def medical(self):
        return int(self.pay * 0.0005)

    def pf(self):
        return int(self.pay * 0.010)


class Deductions:
    def __init__(self, pay):
        self.pay = pay

    def income_tax(self):
        return int(self.pay * 0.005)

    def professional_tax(self):
        return int(self.pay * 0.002)


class CTC:
    def __init__(self, pay):
        self.pay = pay
        self.obj_pay = Gross_pay(self.pay)
        self.object_medical = Benifit_Deductions(self.pay)
        self.object_pf = Benifit_Deductions(self.pay)
        self.object_IT = Deductions(self.pay)
        self.object_Prof_tax = Deductions(self.pay)

    def get_ctc(self):
        return (
            f'''Your Monthly Gross Pay is           : {self.obj_pay.month_gross()}
            Your Medical Monthly Installment is : {self.object_medical.medical()}
            Your PF Monthly Installment is      : {self.object_pf.pf()}
            Your IT Monthly Installment is : {self.object_IT.income_tax()}
            Your Professional Tax Monthly Installment is      : {self.object_Prof_tax.professional_tax()}
            Your Net salary is : {(self.obj_pay.month_gross()) - ((self.object_medical.medical()) + (self.object_pf.pf()) + (self.object_Prof_tax.professional_tax()))} ''')

    def fixed(self):
        return int((self.obj_pay.month_gross()) - ((self.object_medical.medical()) + (self.object_pf.pf()) + (
            self.object_Prof_tax.professional_tax())))


class Fixed:
    pass


class Variable:
    pass


class Bonus_or_performance_incentive:
    pass


a = CTC(500000)
print(a.get_ctc())
print(a.fixed())
