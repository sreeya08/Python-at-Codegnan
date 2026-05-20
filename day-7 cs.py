#find the largest number among three numbers by using nested if
n1 = int(input())
n2 = int(input())
n3 = int(input())
if n1 > n2:
    if n1 > n3:
        print("n1 is greater")
    else:
        if n2 > n3:
           print("n2 is greater")
        else:
           print("n3 is greater")
