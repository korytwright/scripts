import time


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
