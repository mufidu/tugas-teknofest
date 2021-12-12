#     *    
#    * *   
#   * * *  
#  * * * * 
# * * * * *

N = int(input("Masukkan angka: "))

for i in range(1, N+1):
    print(" "*(N-i), end="")
    for j in range(i):
        print("*",end=" ")
    print(" "*(N-i), end="")
    print()
