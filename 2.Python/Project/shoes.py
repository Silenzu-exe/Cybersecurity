#

class shoes:
    def __init__(self, name, price):
        self.name = name
        self.price = float(price)
        
    def budget_check(self, budget):
        if not isinstance(budget,(int, float)):
            print("Please enter number!!")
            exit()
        
    def change(self, budget):
        return (budget-self.price)
    
    def buy(self, budget):
        if budget >= self.price:
            print(f"You can buy this shoe {self.name}")
            
            if budget == self.price:
                print("You hav the exact price")
        
            else:
                print(f"you can buy these {self.name}shoes and have {self.change(budget)} left over")
           
            exit("Thank you for using our app")
    