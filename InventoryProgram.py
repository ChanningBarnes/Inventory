#
# Channing Barnes
# COMP 163
# 8/3/2022
# Object Oriented Management System

#Define class and constructor
class Manage:
    def __init__(self, num_stock,num_sold):
        self.num_stock = num_stock
        self.num_sold = num_sold
#Define print function
    def print_report(self):
        print("")
        print("Items sold:")
        print("---------------")
        for key,value in self.num_sold.items():
            print(f'{value} {key} sold')
        print("")
        print("Current stock:")
        print("----------------")
        for key, value in self.num_stock.items():
            print(f'{key} : {value}')

if __name__ == "__main__":
    #Defining empty dictionaries
    stock_dict= dict()
    sold_dict = dict()
    #Read in user input
    user_input = input("Enter item: (enter 'q' to quit and show inventory) ")
    while user_input != "q":
        user_num = int(input(f'Enter amount of {user_input} in stock: '))
        user_sold = int(input(f'Enter amount of {user_input} sold: ' ))
        user_num -= user_sold
        #Add User input to dictionaries
        if user_input not in stock_dict.keys():
            stock_dict[user_input]= user_num
        else:
            stock_dict[user_input]+=user_num
        if user_input not in sold_dict.keys():
            sold_dict[user_input] = user_sold
        else:
            sold_dict[user_input] += user_num
        user_input = input("Enter item: (enter 'q' to quit and show inventory) ")
    #Output inventory
    user_system = Manage(stock_dict, sold_dict)
    user_system.print_report()

