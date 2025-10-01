# cook your dish here
t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    if(x==y):
        print("neutral")
    elif(x<y):
        print("profit")
    else:
        print("loss")