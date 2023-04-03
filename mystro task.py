'''
Bank :
- create client (name , age )
- withdraw
-show details
-show balance
'''
class Bank :
    def __init__(self,name,age):
        self.name =name
        self.age = age
        self.balance = 0

    def withdraw(self,amount):
        self.balance -= amount
        print(f'your corrent balance :{self.balance}')

    def deposite(self,amount):
        self.balance += amount
        print(f'your corrent balance :{self.balance}')

     def show_details(self):
         print(f'Name :{self.name}')
         print(f'Age : {self.age}')

      def show_details(self):



c1 = Bank('ahmad' , 23)


