
def Menunggu(n,des):
    #basis
    if n == 0:
        return 0
    #rekuren
    print(des)
    return Menunggu(n-1,des)

def MySum(n):
    #basis
    if n == 0:
        return 0
    #rekuren
    return n+MySum(n-1)

def main():
    # solusi iteratif/pengulangan dengan teknik for loop
    #n = 10
    #for i in range(n):
    #    print("Menunggu si dia.")
    # solusi rekursif
    Menunggu(10,"Menunggu si dia.")

    # solusi iteratif penjumlahan
    # sum = 0
    # n = 10
    # for i in range(n+1):
    #    sum+=i
    # print(sum) #55
    
    # solusi rekursif
    print(MySum(10)) #55?

if __name__=="__main__":
    main()
