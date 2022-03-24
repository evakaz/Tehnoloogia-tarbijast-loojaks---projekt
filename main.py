#autor: eva kazakovskaia
#1. gets an input(what day it is), import daytime, finds current time 
#2. finds what lesson it is(1-7)
#3. finds how much time left till the end of the lesson, and what lesson it is

#possible easygui solution?

#1.	õppetund	8.00 - 8.45
#2.	õppetund	8.55 - 9.40
#3.	õppetund	9.55 - 10.40
#4.	õppetund	11.00 - 11.45
#5.	õppetund	12.05 - 12.50
#6.	õppetund	13.10 - 13.55
#7.	õppetund	14.05 - 14.50

#on vaja tsykklit

import time


def tundi_leidmine(current_time, tundide_lopp, tundide_algus):
    if tundide_lopp[0] >= current_time >= tundide_algus[0]:
        print("see on esimene tund!")
        tund = 1
        return tund
    if tundide_lopp[1] >= current_time >= tundide_algus[1]:
        print("teine!")
        tund = 2
        return tund
    if tundide_lopp[2] >= current_time >= tundide_algus[2]:
        print("kolmas!")
        tund = 3
        return tund
    if tundide_lopp[3] >= current_time >= tundide_algus[3]:
        print("neljas!")
        tund = 4
        return tund
    if tundide_lopp[4] >= current_time >= tundide_algus[4]:
        print("viies!")
        tund = 5
        return tund
    if tundide_lopp[5] >= current_time >= tundide_algus[5]:
        print("kuues!")
        tund = 6
        return tund
    if tundide_lopp[6] >= current_time >= tundide_algus[6]:
        print("seitsmes!")
        tund =7
        return tund
    else:
        print('tund praegu ei käi')
        tund = 0
        return tund



def kui_palju_on_jaanud(tund, tundide_lopp, current_time):
    if tund == 1:
        jaak = tundide_lopp[0] - current_time
        arvutamised()
        #return jaak
    if tund == 2:
        jaak = tundide_lopp[1] - current_time
        return jaak


def arvutamised(tundide_lopp):
    tundide_lopp_list = []
    for i in str(tundide_lopp[0]):
        if i != '.':
            tundide_lopp_list.append(int(i))
    print(tundide_lopp_list)
    
    
t = time.localtime()
#current_time = float(time.strftime("%H.%M", t))
current_time = 8.34
print(current_time)

tundide_algus = [8.00, 8.55, 9.55, 11.00, 12.05, 13.10, 14.05]
tundide_lopp = [8.45, 9.40, 10.40, 11.45, 12.50, 14.00, 14.50]

while tundide_lopp[6] >= current_time >= tundide_algus[0]:
    tundi_leidmine(current_time)
    vastus = input("kas sa tahad teada kui palju on vahetunnini jaanud:(jah/ei): ")
    if vastus == 'jah':
        print(kui_palju_on_jaanud(1))
    else:
        break


#paev = input('Mis kuupäev täna on: ')


