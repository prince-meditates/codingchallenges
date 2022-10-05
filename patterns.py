"""
****
****
****
****
"""

for x in range(4):
    for y in range(4):
        print("*",end=" ")
    print()


"""
*
**
***
****

"""

a=0
for x in range(4):
    a= a + 1
    for y in range(a):
        print("*",end=" ")
    print()



"""
1
1 2
1 2 3
1 2 3 4
"""

a=0
for x in range(4):
    a= a + 1
    b=0
    for y in range(a):
        b+=1
        print(b, end=" ")
    print()


"""
1
2 2
3 3 3
4 4 4 4
"""
a=0
for x in range(4):
    a+=1
    for y in range (a):
        print(a,end=" ")
    print()



"""
* * * *
* * *
* *
*
"""
a=5
for x in range(4):
    a-=1
    for y in range(a):
        print("*",end=" ")
    print()

"""
1 2 3 4
1 2 3
1 2
1
"""
a=5
for x in range(4):
    a-=1
    b=0
    for y in range(a):
        b+=1
        print(b,end=" ")
    print()

"""
    *
   ***
  *****
 *******
"""
noOfLines=5
lengthOfALine=noOfLines*2-1;
for x in range(noOfLines-1):
    for y in range(lengthOfALine):
        startPosOfAsterisk=noOfLines-(x+1)
        endPosOfAsterisk=lengthOfALine-(noOfLines-x)
        if y>=startPosOfAsterisk and y<=endPosOfAsterisk:
            print ("*",end="")
        else:
            print(end=" ")
    print()


""""
*******
 *****
  ***
   *
"""

print()
noOfLines=5
lengthOfALine=noOfLines*2-1;

for x in range(noOfLines):
    for y in range(lengthOfALine):
        startPosOfAsterisk=x
        endPosOfAsterisk=lengthOfALine-(x+1)
        if y>=startPosOfAsterisk and y<=endPosOfAsterisk:
            print ("*",end="")
        else:
            print(end=" ")
    print()


"""
   *
  ***
 *****
*******
 *****
  ***
   *
"""

noOfLines=5
for x in range(noOfLines):
    for y in range((noOfLines*2)+1):
        if y>=noOfLines-x and y<=noOfLines+x:
            print("*",end="")
        else:
            print(" ",end="")
    print()
for x in reversed(range(noOfLines-1)):
    for y in range((noOfLines*2)+1):
        if y>=noOfLines-x and y<=noOfLines+x:
            print("*",end="")
        else:
            print(" ",end="")
    print()

"""
*
**
***
****
***
**
*
"""

noOfLines=4
for x in range(noOfLines):
    for y in range(x+1):
        print("*",end="")
    print()
for x in reversed(range(noOfLines-1)):
    for y in range(x+1):
        print("*",end="")
    print()


"""
1
0 1
1 0 1
0 1 0 1
1 0 1 0 1
"""

noOfLines=5

for x in range(5):
    for y in range(x+1):
        if y==0 and x%2==0:
            toggledValue=0
        elif y==0 and x%2 != 0:
            toggledValue=1
        toggledValue=not toggledValue
        print(int(toggledValue),end=" ")
    print()



"""
1      1
12    21
123  321
12344321
"""

noOfLines=4
for x in range(noOfLines):
    for y in range(2*noOfLines):
        if y<=x:
            print(y+1,end="")
        elif ((2*noOfLines)-1-x<=y):
            print((2*noOfLines)-y, end="")
        else:
            print(" ",end="")
    print()



"""
1
2 3
4 5 6
7 8 9 10
11 12 13 14
"""

noOfLines=4
numberToBePrinted=0
for x in range(noOfLines):
    for y in range(x+1):
        numberToBePrinted+=1
        print(numberToBePrinted,end=" ")
    print()


"""
A
B C
D E F
G H I J

"""
noOfLines=4
#ascii of 'A' is 65
alpha=64
for x in range(noOfLines):
    for y in range(x+1):
        alpha+=1
        print(chr(alpha),end=" ")
    print()

"""
A
B B
C C C
D D D D 
"""
noOfLines=4
#ascii of "A" is 65
alpha=64
for x in range(noOfLines):
    alpha += 1
    for y in range(x+1):

        print(chr(alpha),end="")
    print()



"""
      A
    A B A
  A B C B A
A B C D C B A
"""

noOfLines=7
#ascii of 'A' is 65
alpha=64
for x in range(noOfLines):
    for y in range(x+1):
        if y>=noOfLines-(x+1) and y<=(noOfLines+x-1):
            print(chr(alpha+1),end="")
        else:
            print(end=" ")
    print()