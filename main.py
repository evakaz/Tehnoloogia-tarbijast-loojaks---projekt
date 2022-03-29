#autor: eva kazakovskaia
#Kaheksanda klassi õpilane Marta tahab alati teada saada, kui palju on tunni lõpuni aega jäänud.
#Et teha seda kiiremini, Marta kirjutas programmi, mis:
#*küsib kasutajalt mis kell praegu on
#Funktsioon "arvutamised" teisendab tundidest minutitesse.
#Funktsioon "tundi_leidmine" arvutab mis tund(1-7) praegu käib.
#Funktsioon "kui_palju_on_jaanud"  leiab, kui palju on jäänud tunni lõpuni.
#Ekraanile väljastatakse funktsiooni "kui_palju_on_jaanud" tulemuse

#1. õppetund 8.00 - 8.45
#2. õppetund 8.55 - 9.40
#3. õppetund 9.55 - 10.40
#4. õppetund 11.00 - 11.45
#5. õppetund 12.05 - 12.50
#6. õppetund 13.10 - 13.55
#7. õppetund 14.05 - 14.50


import time
import math


#                0     1     2     3      4      5       6
tundide_algus = [8.00, 8.55, 9.55, 11.00, 12.05, 13.10, 14.05]
tundide_lopp = [8.45, 9.40, 10.40, 11.45, 12.50, 14.00, 14.50]


# 8.00 -> 480
# 8.55 -> 480 + 55 = 535
# 9.55 -> 540 + 55 = 595
def arvutamised(kell):
    m = math.modf(kell)
    return m[1] * 60 + m[0] * 100;


# 8.00 -> 0
# 8.20 -> 0
# 8.50 -> -1
# 9.00 -> 1
def tundi_leidmine(current_time):
    z = arvutamised(current_time)
    # len(tundide_algus) = 7
    # for 0..6
    for i in range(len(tundide_algus)):
        algus = arvutamised(tundide_algus[i])
        lopp = arvutamised(tundide_lopp[i])
        if algus <= z and z <= lopp:
            return i

    return -1


# 0, 8.34 -> 11
# 0, 8.45 -> 0
def kui_palju_on_jaanud(tund, current_time):
    lopp = arvutamised(tundide_lopp[tund])
    return lopp - arvutamised(current_time)


# Kasutajalt küsimine
current_time = float(input("Mis kell on? "))

tund = tundi_leidmine(current_time)
if tund == -1:
    print("Tund ei leindnud")
else:
    jaanud = kui_palju_on_jaanud(tund, current_time)
    print("Tunni lõppuni on jäänud " + str(round(jaanud)) + " minutit.")



