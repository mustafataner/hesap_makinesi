# hesap makinesi örneği
print("""hesap makinesine hoş geldiniz!
[1]= toplama
[2]= çıkarma
[3]= bölme 
[4]= çarpma
[5]= üs alma
[6]= kök alma
[Q] = çıkış
""")

islem = input("lütfen yapmak istediğiniz işlemi seçiniz!")

if islem == "1":
    sayi1 = float(input("lütfen ilk sayıyı giriniz:"))
    sayi2 = float(input("lütfen ikinci sayıyı giriniz:"))
    print("toplama işleminin sonucu {}".format(sayi1 + sayi2))


elif islem == "2":
    sayi1 = float(input("lütfen ilk sayıyı giriniz:"))
    sayi2 = float(input("lütfen ikinci sayıyı giriniz:"))
    print("çıkarma işleminin sonucu {}".format(sayi1 - sayi2))




elif islem == "3":
    sayi1 = float(input("lütfen ilk sayıyı giriniz:"))
    sayi2 = float(input("lütfen ikinci sayıyı giriniz:"))
    print("toplama işleminin sonucu {}".format(sayi1 / sayi2))




elif islem == "4":
    sayi1 = float(input("lütfen ilk sayıyı giriniz:"))
    sayi2 = float(input("lütfen ikinci sayıyı giriniz:"))
    print("çarpma işleminin sonucu {}".format(sayi1 * sayi2))



elif islem == "5":
    sayi1 = float(input("lütfen ilk sayıyı giriniz:"))
    sayi2 = float(input("üs derecesini giriniz:"))
    print("üs alma işleminin sonucu {}".format(sayi1 ** sayi2))



elif islem == "6":
    sayi1 = float(input("lütfen ilk sayıyı giriniz:"))
    sayi2 = float(input("lütfen kök derecesini giriniz:"))
    print("kök alma işleminin sonucu {}".format(sayi1 ** (1 / sayi2)))


elif islem == "q" or "Q":
    print("görüşürüz!")