
def topla(sayi1, sayi2):
    return sayi1 + sayi2

def cıkar(sayi1, sayi2):
    return sayi1 - sayi2

def carp(sayi1, sayi2):
    return sayi1 * sayi2

def bol(sayi1, sayi2):
    return sayi1 / sayi2



print("Operasyonlar.")
print("1 : Topla")
print("2 : Çıkar")
print("3 : Çarp")
print("4 : Böl")

secenek = input("Operasyon Seçiniz ")
sayi1 = int(input("1. Sayıyı Giriniz : "))
sayi2 = int(input("2. Sayıyı Giriniz : "))

if secenek == '1':
    print("Toplam : " + str(topla(sayi1, sayi2)))
    
elif secenek == '2':
    print("Cıkarma : " + str(cıkar(sayi1, sayi2)))
    
elif secenek == '3':
    print("Carpma : " + str(carp(sayi1, sayi2)))
    
elif secenek == '4':
    print("Bölme : " + str(bol(sayi1, sayi2)))
    
else:
    print("Lütfen geçerli seçenekleri giriniz.")
