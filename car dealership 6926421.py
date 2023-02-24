#script for car prices
#import numpy as np
cars = dict()
cars["mercedes benz"] =200000
cars["BMW X1"] =80000
cars["toyota Camry"] =20000
cars["tesla"] =80000
cars["katanka"] =2000
cars["kia rio"] =5000
cars["peugeot"] =9000
cars["suzuki celerio"] =4000
cars["daewoo"] =3500
cars["ford"] =4000
cars["rolls royce"] =9000
cars["chevrolet"] =3000
cars["ferrari"] =502000
cars["Bugatti"] =803000
cars["honda"] =2500
cars["porsche"] =405000
cars["volvo"] =30000
cars["mitsubishi"] =7000
cars["Jaguar"] =7000
cars["sonata"] =55000
cars["volkswagen"] =45000
cars["hyundai"] =4000
cars["mazda"] =7000
cars["mini"] =9000
cars["maserati"] =80000
cars["opel zafira"] =1000
cars["audi"] =3000
cars["lamborghini"] =60000
cars["range rover"] =70000
cars["nissan"] =2000
cars["land rover"] =9000
cars["renault"] =7000

print("Welcome to Benedict's car dealership")

print("Which car would you like to purchase?")

order = input()
if cars.get(order):
    print("The "+order+" costs $" + str(cars.get(order)))
else:
    print("Sorry "+order+" is unavialable")
    
    https://github.com/BenedictAkwetey/6926421.-car-dealership.git













