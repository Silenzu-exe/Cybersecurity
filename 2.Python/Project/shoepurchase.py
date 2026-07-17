from shoes import shoes

low = shoes("goldstar", 1000)
medium = shoes("calibar", 3000)
high = shoes("Air force", 7000)

try: 
    shoes_budget = float(input("what is you budget?"))
    
except ValueError:
    exit("Please enter a number!!")

for shoes in [high, medium, low]:
    shoes.buy(shoes_budget)
    