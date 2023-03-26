'''
Bank :
- create client (name , age )
- withdraw
-show details
-show balance
'''
class Bank :
    def __init__(self,name,age):
        print(f'welcome {name}')
        balance = 0

    def withdraw(self,amount):
        balance -= amount
        print(f'your current balance : {balance} ')

c1 = Bank('ahmad' ,23)


