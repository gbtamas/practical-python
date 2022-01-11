# mortgage.py
#
# Exercise 1.7

principal = 500000
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0

extra_payment_start_month = int(input("Extra payment start month: "))
extra_payment_end_month = int(input("Extra payment end month: "))
extra_payment = int(input("Extra payment amount: "))

while principal > 0:
    month += 1
    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        current_extra_payment = extra_payment
    else:
        current_extra_payment = 0

    if principal * (1 + rate / 12) - (payment + current_extra_payment) < 0:
        principal = 0
        total_paid += principal * (1 + rate / 12)
    else:
        principal = principal * (1 + rate / 12) - (payment + current_extra_payment)
        total_paid = total_paid + payment + current_extra_payment

    print(month, round(total_paid, 2), round(principal, 2))

print("Total paid", total_paid)
print("Months", month)
