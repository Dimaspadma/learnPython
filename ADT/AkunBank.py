# Abstract data type

class AkunBank():

    __nasabah = []

    def __init__(self, nama, no_rek, saldo=0):
        self.__nama = nama
        self.__history = []
        AkunBank.__nasabah.append(nama)

        self.__no_rek = no_rek
        self.__saldo = saldo

    def lihatSaldo(self):
        print(f"Nama : {self.__nama}")
        print(f"Nomer rekening : {self.__no_rek}")
        print(f"Saldo : {self.__saldo}")

    def menabung(self, uang):
        # menambahkan saldo
        self.__saldo += uang
        self.__history.append(f"nabung {uang}")
    
    def mengambil(self, uang):
        # cek uang
        if self.__saldo >= uang:
            self.__saldo -= uang
            self.__history.append(f"ambil {uang}")
        else:
            print(f"tidak bisa mengambil uang {uang}")
            print(f"saldo tersisa : {self.__saldo}")

    def lihatHistory(self):
        print(self.__history)

    def getNasabah():
        print("Nasabah : ", AkunBank.__nasabah)


if __name__ == "__main__":
    
    myakun = AkunBank("Lala",12312,100000)
    myakun.menabung(20000)
    myakun.mengambil(100000)
    

    myakun2 = AkunBank("test", 12313, 50000)
    myakun2.menabung(5000)
    myakun2.mengambil(40000)
    
    AkunBank.getNasabah()