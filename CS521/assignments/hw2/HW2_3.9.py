# variables are created to assign user input.
employee_name = input("Enter employee's name: ")
number_of_hours = input("Enter number of hours worked in a week: ")
hourly_pay_rate = input("Enter hourly pay rate: ")
federal_tax = input("Enter federal tax witholding rate: ")
state_tax = input("Enter state tax witholding rate: ")

# calculates the result of each variable
gross_pay = int(number_of_hours) * float(hourly_pay_rate)
federal_tax_result = float(gross_pay) * float(federal_tax)
state_tax_result = float(gross_pay) * float(state_tax)
total_deduction = float(federal_tax_result) + float(state_tax_result)
net_pay = gross_pay - total_deduction

# prints results
print()
print("Employee Name: " + employee_name)
print("Hours Worked: " + str(float(number_of_hours)))
print("Pay Rate: $" + str(float(hourly_pay_rate)))
print("Gross Pay: $" + str(gross_pay))
print("Deductions:")
print("  Federal Witholding (" + str(float(federal_tax) * 100) + "%): $" + str(federal_tax_result))
print("  State Witholding (" + str(float(state_tax) * 100) + "%): $" + str(state_tax_result)[:-1])
print("  Total Deduction: $" + str(total_deduction)[:-1])
print("Net Pay: $" + str(net_pay)[:-1])

