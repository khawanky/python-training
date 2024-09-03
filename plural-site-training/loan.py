
money_owed = float(input('How much do you owe in dollars?\n'))
annual_rate = float(input('What is the annual rate?\n'))
payment = float(input('How much will you pay monthly?\n'))
months = int(input('Result for how many months?\n'))

monthly_rate = annual_rate/100/12


for i in range(months):
    interest_paid = money_owed*monthly_rate
    money_owed += interest_paid
    money_owed -= payment

    if (money_owed-payment < 0):
        print('last payment is ', money_owed, 'of which', interest_paid, 'was interest', end='. ')
        print('You paid off the loan in', i+1, 'months')
        break

    print('Paid', payment, 'of which', interest_paid, 'was interest', end='. ')
    print('Now I owe', money_owed)


# total_months = 0
# last_payment = 0

# while True:
#     interest_paid = money_owed*monthly_rate
#     money_owed += interest_paid
#     money_owed -= payment

#     if money_owed<=0:
#         last_payment = money_owed+1000

#     if money_owed>0:
#         print('Paid', payment, 'of which', interest_paid, 'was interest', end='. ')
#         print('Now I owe', money_owed)
#     else:
#         print('Paid', last_payment, 'of which', interest_paid, 'was interest', end='. ')
#         break

#     total_months+=1

# print(f"Payments finished in {total_months} Months")
