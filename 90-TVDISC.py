# cook your dish here
t=int(input())
for _ in range(t):
    a,b,c,d=map(int,input().split())
    if a-c<b-d:
        print("First")
    elif a-c==b-d:
        print("Any")
    else:
        print("Second")
    