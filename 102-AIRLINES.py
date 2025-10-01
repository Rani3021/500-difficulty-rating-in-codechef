# cook your dish here
t=int(input())
for _ in range(t):
    x,y,z=map(int,input().split())
    if y<=10*x:
        print(y*z)
    else:
        print(10*x*z)