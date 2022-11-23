#!/usr/bin/env python3

print(
"""
            Trust Fund Buddy
Totals your monthy spending so that your trust fund doesn't  run out
(and yuo're forced to get a real job)

Please enter the requested, monthy cost, Since you're rich, ignore
    pennis and uae get and amount
"""
)

car = int(input("Lamborgini Tune-Ups: "))
rent = int(input("Manhattan Aparrment:"))
jet = int(input("Private Renta:"))
gifts = int(input("Gifts: "))
food = int(input("Dining Out: "))
staff = int(input("Staff (butlers, chef, driver, assistant): "))
guru = int(input("Personal Guru and Coach: "))
games = int(input("Computer Games: "))
total = car + rent + jet + gifts + food + staff + guru + games
print("\nGrand Total:", total)
input("\n\nPress the enter key to exit.")