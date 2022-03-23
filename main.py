#autor: eva kazakovskaia
#gets an input from a user(what it is) and finds out how much tume there is left till the end of the lesson
#1. gets an input(what day it is), import daytime, finds current time 
#2. finds what lesson it is(1-7)
#3. finds how much time left till the end of the lesson

#possible easygui solution?

#1.	õppetund	8.00 - 8.45
#2.	õppetund	8.55 - 9.40
#3.	õppetund	9.55 - 10.40
#4.	õppetund	11.00 - 11.45
#5.	õppetund	12.05 - 12.50
#6.	õppetund	13.10 - 13.55
#7.	õppetund	14.05 - 14.50

from locale import currency
import time 

#class Tunnid:   ???

def tundi_leidmine(current_time):
    if lopp1 >= current_time >= tundide_algus[0]:    #find out how to compare floats?
        tund = 1
        print("See on esimene tund!")
    else:
        print("See ei ole esimene tund")


def kui_palju_on_jaanud(tund):
    if tund == 1:
        jaak = lopp1 - current_time
        return jaak



#while True:
    #continue

tundide_algus = [8.00, 8.55, 9.55, 11.00, 12.05, 13.10, 14.05]
tundide_lopp = [8.45, 9.40, 10.40, 11.45, 12.50, 14.00, 14.50]


algus1 = 8.00
lopp1 = 8.45

t = time.localtime()
current_time = time.strftime("%H:%M:", t)
print(current_time)

day = input('What day is it today: ')

tundi_leidmine(current_time)

