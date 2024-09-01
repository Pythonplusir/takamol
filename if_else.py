
"""
conditional statement
      عبارت شرطی  

if condition:
    #کدی برای اجرا اگر شرط درست باشد
else:
    # code to run if the above condition is false
    
"""


""" elif

if condition1:
    # code block 1

elif condition2:
    # code block 2

else: 
    # code block 3
"""

# example elif

number = -5

if number > 0:
    print('Positive number')

elif number < 0:
    print('Negative number')

else:
    print('Zero')






# example 
x = 1
total = 0

# start of the if statement
if x != 10:
    total += x
    print(total)  
# end of the if statement














#How to Write a Nested Control Flow
ages = [78, 34, 21, 47, 9]
new = []

for i in ages:
    if i%3==0:
        new.append(i)
        print(i)
    else:
        print("by")
