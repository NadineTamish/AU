x = int(input("EGP="))
ones=0
fives=0
tens=0
twenties=0
fifties=0
hundreds=0
twohundreds=0

while x - 200 >= 0:
    twohundreds += 1
    x = x - 200
while x - 100 >= 0:
    hundreds += 1
    x = x - 100
while x - 50 >= 0:
    fifties += 1
    x = x - 50
while x - 20 >= 0:
    twenties += 1
    x = x - 20
while x - 10 >= 0:
    tens += 1
    x = x - 10
while x - 5 >= 0:
    fives += 1
    x = x - 5
while x - 1 >= 0:
    ones += 1
    x = x - 1

if twohundreds>0:
    print(twohundreds,"x200 L.E. +",end="")
if hundreds>0:
    print(hundreds,"x100 L.E +",end="")
if fifties>0:
    print(fifties,"x50 L.E +",end="")
if twenties>0:
    print(twenties,"x20 L.E +",end="")
if tens>0:
    print(tens,"x10 L.E +",end="")
if fives>0:
    print(fives,"x5 L.E +",end="")
if ones>0:
    print(ones,"x1 L.E")
