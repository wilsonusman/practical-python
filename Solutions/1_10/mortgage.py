# mortgage.py

principal = int(200000.0)
rate = float(0.05)
payment = int(1633.11)
total_paid = 0.0
month = 0
start_extra_payment_on_year = 5
extra_years = 4

extra_payment = 1000.0
extra_payment_start_month = start_extra_payment_on_year * 12
extra_payment_end_month = extra_payment_start_month + (extra_years * 12)

while principal > 0:
    month = month + 1
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment

    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment

    print(month, round(total_paid,2), round(principal, 2))
    
print('Total paid', round(total_paid, 2))
print('Months', month)



