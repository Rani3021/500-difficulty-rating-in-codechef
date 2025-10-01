# cook your dish here
T=int(input())
for _ in range(T):
    x,N=map(int,input().split())
    print((x//10)*N)