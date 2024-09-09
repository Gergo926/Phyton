# kor = int(input("Add meg a korod"))

# print(type(kor))
# print(f"A te korod: {kor}")


# if kor > 18:
#     print("Megnézheted ezt a filmet")
# elif kor < 18:
#     print("Nem nézheted meg ezt a filmet")
# else:
#     print("Egyenlő")

# szám1 = int(input("Add meg az első számot"))
# szám2 = int(input("Add meg a második számot"))

# result = szám1 + szám2
# print(f"Az eredmény {result}")

# if result % 2 == 0:
#     print("A szám páros")
# else:
#     print("A szám páratlan")

# honap = int(input("Adj meg egy számot 1 és 12 között"))
# if honap == 12 or honap == 1 or honap == 2:
#     print("Tél")
# elif honap == 3 or honap == 4 or honap == 5:
#     print("Tavasz")
# elif honap == 6 or honap == 7 or honap == 8:
#     print("Nyár")
# elif honap == 9 or honap == 10 or honap == 11:
#     print("Ősz")
# else:
#     print("Nem jó számot adtál meg")

# szam = int(input("Adj meg egy pozitív egész számot számot:"))

# print(f"A szám kétszerese: { szam * 2 } ")
# print(f"A szám heted része: {round( szam / 7,2)}")
# print(f"3-mal osztva az egészrész: {round(szam/3)} a maradék: {szam % 3}")
# print(f"A szám páros" if szam % 2 == 0 else "A szám páratlan")

# kor = int(input("Írd be a születésednek az évét"))
# print(f"A jelenlegi életkorod: {2024- kor}")

lista = []
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[-1])
print(fruits[-2])
for fruit in fruits:
    print(fruit[:3])

for i in range(1,5+1):
    print(i)

