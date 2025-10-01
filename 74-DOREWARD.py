# cook your dish here
t=int(input()) 
for _ in range(t):
    x=int(input())
    if x<=3:
        print ("bronze")
    elif x>3 and x<=6:
        print("silver")
    else:
        print("gold")