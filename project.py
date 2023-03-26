'''
class Calc:
    def sum(self,x,y):
        print(x,y)

    def mul(self,x,y):
        print(x*y)

    def __init__(self,name):
         print(f'welcome {name}')


class SciCalc(Calc):


    def pow(self,x,y):
        print(x**y)

s = SciCalc('jihad')
s.sum(2,3)
s.mul(4,5)
s.pow(2,3)
'''

class A:
    def do(self):
        print('in A')

class B(A):
    pass

class C:
    def do(self):
        print('in C')

class D(B,C):
    pass

f = D()
f.do()









