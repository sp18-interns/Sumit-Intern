from salary_per_hour import Salary_slip as S_slip

if __name__ == '__main__':
    e1 = S_slip("Shalini", 100, 2000, 'Manager')
    e2 = S_slip("Sushma", 101, 2000, 'Team Lead')
    print(e1)
    print(e2)
    e1_pay = e1.salary()
    e1_da = e1.dearness_allowance()
    e1_it = e1.income_tax()
    e2_pay = e2.salary()
    e2_da = e2.dearness_allowance()
    e2_it = e2.income_tax()

    print(f'{e1.name}. Your Net Salary is {(e1_pay + e1_da) - e1_it}')
    print(f'{e2.name}. Your Net Salary is {(e2_pay + e2_da) - e2_it}')
    print(e1.print_salary_slip())
    print(e2.print_salary_slip())
