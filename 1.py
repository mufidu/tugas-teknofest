# Input merupakan variable string berisi kumpulan angka. Output merupakan list / array berisi angka yang hanya muncul 1 kali pada input.

# Tulis fungsi untuk mengembalikan sebuah array berisi angka angka yang hanya muncul sekali dalam sebuah string yang ada pada parameter fungsi tersebut.

n = input()

def unique(n):
    n = list(n)
    for i in range(len(n)):
        if n.count(n[i]) == 1:
            print(n[i], end=" ")

unique(n)
