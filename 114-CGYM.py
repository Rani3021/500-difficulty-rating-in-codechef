# cook your dish here
t=int(input())
for _ in range(t):
    x, y, z=map(int, input().split())
    if x+y>z and x<=z:
        print("1")
    elif x+y<=z:
        print("2")
    else:
        print ("0")