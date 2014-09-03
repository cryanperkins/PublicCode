__author__ = 'student'
a = input("Give me a number")
#b = 0
if a == 0:
    print("Sorry, try again.")
#test if a is even or odd
elif a % 2 == 0:
    print("We're even!")
    for i in range(1, a + 1):
        if i % 2 == 0:
            print (i)
#if a % 2 != 0:
else:
    print("We're odd!")
    for i in range(1, a + 1):
        if i % 3 == 0:
            print (i)






#to do- make counting stop at input number
#  if b == a:
    #    print(a)
   # else:
    #    print(i)
#We could also do it this way:
#
#
#
#
#