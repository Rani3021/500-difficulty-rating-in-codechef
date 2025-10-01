# cook your dish here
t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    if x*(107/100)>=y:
        print("YES")
    else:
        print("NO")