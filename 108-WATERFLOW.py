# cook your dish here
t=int(input())
for _ in range(t):
    w,x,y,z=map(int,input().split())
    if w+y*z>x:
        print("Overflow")
    elif w+y*z==x:
        print("filled")
    else:
        print("unfilled")