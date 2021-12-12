# * * * * *
#  * * * *
#   * * *
#    * *
#     *

N = int(input("Masukkan angka: "))

for i in range(N, 1, -1):
    print(" "*(N-i), end="")
    for j in range(i):
        print("*",end=" ")
    print(" "*(N-i), end="")
    print()

print(" "*(N-i+1), end="")
print("*")
