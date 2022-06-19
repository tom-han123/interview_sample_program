principle  = 500000      # Initial principle
payment    = 499         # Monthly payment
rate       = 0.04        # The interest rate
total_paid = 0           # Total amount paid
months     = 0           # Number of months

while principle > 0:
    principle = principle*(1+rate/12) - payment
    total_paid += payment
    months     += 1
    if months == 24:
        rate    = 0.09
        payment = 3999

print("$",total_paid)
print(months,"Months")        