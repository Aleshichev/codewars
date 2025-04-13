#  Let P be the Principal = 1000.00      
#   Let I be the Interest Rate = 0.05      
#   Let T be the Tax Rate = 0.18      
#   Let D be the Desired Sum = 1100.00
#   test.assert_equals(calculate_years(1000, 0.05, 0.18, 1100), 3)
#   test.assert_equals(calculate_years(1000,0.01625,0.18,1200), 14)


def calculate_years(principal, interest, tax, desired):
    years = 0
    while principal < desired:
        principal += principal * interest * (1 - tax)
        years += 1
    print(years)

calculate_years(1000,0.01625,0.18,1200)
