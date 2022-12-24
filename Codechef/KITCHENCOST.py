# cook your dish here
# freshness value greater than equal to x

def total_cost(N, X, fresh, cost):
    final_cost = 0
    for i in range(0,N):
        if int(fresh[i]) >= X:
            final_cost = final_cost + int(cost[i])
    
    return final_cost
            


T = int(input())

def main():
    for i in range(0, T):
        N, X  = map(int, input().split())
        fresh = input().split()
        cost = input().split()
        print(total_cost(N,X,fresh,cost))
    
main()