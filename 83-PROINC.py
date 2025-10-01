# cook your dish here
t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    print(int(x+(x*(10/100)))-(x-y))