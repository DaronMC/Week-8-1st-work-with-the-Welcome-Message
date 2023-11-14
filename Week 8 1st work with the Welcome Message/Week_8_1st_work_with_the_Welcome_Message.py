import sys
from datetime import date
print("\n")
print("Welcome! ")
print("I hope you have a great and wonderful time here and if you have any type of problems please address the helpers that are located around the area wearing bright orange! ")
print("Dont forget make sure and have a lot of fun! ")
print("Parking Pass will be free so dont worry about that! :) ")
print("These are the prices for the Tickets: ")
prices = ["Adult: £20", "Child: £12", "Senior Citizen: £11", "Wristbands: £20"]
for x in prices:
    print(x)
Surname=input("\nAre you the person who the person who will be booking these tickets if so i need your Surname: ")
print("Okay I will be needing some information: ")
tickets=int(input("\nHow many Adult tickets will you need? "))*20
purchased = tickets/20
tickets+=int(input("How many Child tickets will you need? "))*12
purchased += int((tickets-(purchased*20))/12)
tickets2=int(input("How many Senior Tickets will you need? "))*11
purchased+=int(tickets2/11)
tickets+=tickets2
wristbands=int(input("How much visitors will need wristbands for the rides? "))
tickets+=int(wristbands*20)
print_pass=input("Do you require a parking pass for your car? ")
print("\nThe total prices for all this is: ")
print(tickets)
print("Im sorry for inconvienience but the machine only accepts £10 notes and £20 notes if you need a ATM there is one over to your right. ")
Change=int(input("How much money will you be paying with today? "))
Change=(Change-tickets)
if Change<=0:
    sys.exit()
print("Your total change is: ")
print(Change)
print("\nTicket: ")
print(f"Display Booker Name: {Surname}")
print(f"Tickets Purchased: {int(purchased)}")
print(f"Wristbands Purchased: {wristbands}")
date=date.today()
print(date)
if print_pass == "yes":
    print("Here is your parking pass! ")
else:
    print("Okay have a Good day until your time. ")
print("Thank you customer for you purchase you helped me to eat some Mc Donalds so much appreciated! ")