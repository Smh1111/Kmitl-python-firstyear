name = input("Enter employee's name: ")
hours = float(input("Enter number of hours worked in a week: "))
pay_rate_per_hr = float(input("Enter hourly pay rate: "))
fed_tax = float(input("Enter federal tax withholding rate: "))
state_tax = float(input("Enter state tax withholding rate: "))

gross_pay = pay_rate_per_hr * hours
fed_witholding = gross_pay * fed_tax
state_witholding = gross_pay * state_tax
total = fed_witholding + state_witholding

net_pay = gross_pay - total

print("\n")
print("Employee Name:", name)
print("Hours Worked:", hours)
print("Pay Rate: $", end = "")
print(pay_rate_per_hr)

print("Gross Pay: $", end = "")
print(gross_pay)

print("Deductions:")
print("  Federal Witholding (", end = "")
print(fed_tax * 100, end = "")
print("%): $", end = "")
print(fed_witholding)

print("  State Witholding (", end = "")
print(state_tax * 100, end = "")
print("%): $", end = "")
print(format(state_witholding, ".2f"))

print("  Total Deduction: $", end = "")
print(format(total, ".2f"))
print("Net Pay: $", end = "")
print(format(net_pay, ".2f"))

print("\n")