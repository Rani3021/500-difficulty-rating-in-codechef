# cook your dish here
t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    if (x*100)>=(y*10):
        print("CLOTH")
    else:
        print("DISPOSABLE")