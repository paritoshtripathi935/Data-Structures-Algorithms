# cook your dish here

def mahasena(weapons):
    even_s = 0
    odd_s = 0
    
    for i in range(len(weapons)):
        if int(weapons[i]) % 2 != 0:
            odd_s = odd_s + 1
        else:
            even_s = even_s + 1

    if even_s > odd_s:
        return "READY FOR BATTLE"
    else:
        return "NOT READY"

def main():
    T = int(input())
    weapons = input().split()
    print(mahasena(weapons))
    


main()