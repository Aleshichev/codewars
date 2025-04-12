def people_with_age_drink(age):
    if age < 14:
        return "drink toddy"
    elif age < 18:
        return "drink coke"
    elif age < 21:
        return "drink beer"
    else:
        return "drink whisky"
    
#return "drink" + ("toddy" if age < 14 else "coke" if age < 18 else "beer" if age < 21 else whisky)