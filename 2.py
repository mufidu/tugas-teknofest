# Diberikan array angka yang diurutkan dan jumlah target, temukan pasangan dalam array yang jumlahnya sama dengan target yang diberikan.

# Tulis fungsi untuk mengembalikan indeks dari dua angka (yaitu pasangan) sedemikian rupa sehingga mereka menambahkan hingga target yang diberikan.

# Test Case:
# Input: [1, 2, 3, 4, 6], target=6
# Output: [1, 3]

num = list(map(int, input().split()))
target = int(input("target="))

for i in range(len(num)):
    for j in range(i+1, len(num)):
        if num[i] + num[j] == target:
            print(i, j)