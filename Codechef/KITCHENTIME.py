# cook your dish here
def chef(x,y):
    return y - x
    
t = int(input())

for i in range(0,t):
    x,y = input().split(" ")
    print(chef(int(x), int(y)))