# cook your dish here
t=int(input())
for _ in range(t):
    x=int(input())
    if x<3:
        print("LIGHT")
    elif x>=3 and x<7:
        print("MODERATE")
    else:
        print("HEAVY")