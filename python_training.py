from itertools import *
from Tkinter import *
print 'test_start'
# root = Tk()
# some = Label(root, text="Tk's job!!", width="30", height="5")
# some.pack()
# root.mainloop()
# 
# -------------------------------------------------------------------


# !!! importtant
# with open("msg","r") as f:

# for line in file.readlines():



# -------------------------------------------------------------------
#!!!!!!!!!!!!!!!!!!
# results = [chr(d) if chr(d) in string.letters else ">?" for d in possible ]

# versus (all work) >> STACKOVERFLOW SAYS :You got the order wrong. The if should be after the for (unless it is unless in an if-else ternary operator)

# results = [chr(d) for d in possible if chr(d) in string.letters ]
# -------------------------------------------------------------------


# for i in product('ABCD', repeat=3):
#     print "".join(i),'@'
# for i in permutations('ABCD',3):
#     print "".join(i)

# print 'xd'+str(5 if raw_input()=='l' else 2)

# numbers = [l0, 20, 30]
# print [number ** 2 for number in numbers]

# lts = [[l, 2, 3], [4, 5, 6], [7, 8, 9]]
# print [ele for lt in lts for ele in lt]

# -------------------------------------------------------------------
# class Account:
#     def __init__(self, name, number, balance):
#         self.name = name
#         self.number = number
#         self.balance = balance
 
#     def deposit(self, amount):
#         if amount <= 0:
#              raise ValueError('amount must be positive')
#         self.balance += amount
 
#     def withdraw(self, amount):
#         if amount > self.balance:
#             raise RuntimeError('balance not enough')
#         self.balance -= amount
 
#     def __str__(self):
#         return 'Account({0}, {l}, {2})'.format(
#             self.name, self.number, self.balance)
# acct = Account('Justin', 'l23-4567', l000)
# acct.deposit(500)
# acct.withdraw(200)
# print acct
# -------------------------------------------------------------------

# min = lambda a, b: a if a < b else b
# print min(30,50)

# def fn(x):
#     return x if x > 5 else None
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print filter(fn, a)

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# def fn(x):
#     return x*2
# print map(fn, a)

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# def fn(x, y):
#     return x+2*y
# print reduce(fn, a)

# -------------------------------------------------------------------
