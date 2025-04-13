# def century(year):
#     if year <= 100: 
#         return 1
#     elif year > 100  and (year // 10) % 10 == 0 and year % 10 == 0:
#         return year // 100
#     else: return (year // 100) + 1

# print(century(500))

def century(year):
    return (year + 99) // 100

print(century(501))