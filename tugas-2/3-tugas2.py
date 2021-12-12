# Buatlah sebuah program Most Appear Item yang dapat mengurutkan barang berdasarkan jumlah kemunculannya dari yang paling jarang. Jika ada barang yang duplicate kamu hanya perlu memunculkan sekali, namun kamu perlu menampilkan total kemunculan barang tersebut

# Tulis fungsi untuk mengembalikan tiap item dengan jumlah item tersebut yang ada di dalam sebuah list yang diberikan sebagai parameternya.

# Test Case:
# Input: [“js”, “js”, “golang”, “ruby”, “ruby”, “js”, “js”]
# Output: 
# golang: 1 
# ruby: 2 
# js: 4

inputan = list(map(str, input().split()))

# strip [], "", and space
for i in ("[", "]", "\"", " ", ","):
    inputan = [x.strip(i) for x in inputan]

# make dictionary with key as item and value as count
d = {}
for i in inputan:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

# sort dictionary by value
d = sorted(d.items(), key=lambda x: x[1], reverse=True)

# print result
print("\n".join(["{}: {}".format(x[0], x[1]) for x in d]))
