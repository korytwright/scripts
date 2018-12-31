import time
#Pushing to github

def countdown(n):
    while n > 0:
        print (n)
        n -= 1
        time.sleep(1)
    if n == 0:
        print("blast off!".title())


countdown(5)


names = ['john','sam','adam','steve','troy']


#names.reverse()
# print(names.title())
for name in names:
    print(name.title() + ", was a great person!")


#squares = []
#for value in range(1,11):
#    square = value**2
#    squares.append(square)

#print(squares)

squares = []
for value in range(1,13):
    squares.append(value**2)

print(squares)


#The end is here
