n = int(input("Masukkan bilangan (N) : "))
jumlah = 0
triplet = []

for x in range(1,n+1):
    triplet.append(x)

if n < 3:
    print("Banyaknya triplet a, b, c adalah 0.")

for i in range(0, n-2):
    k = i + 2
    for j in range(i+1,n):
        while k < n and triplet[i] + triplet[j] > triplet[k]:
            k += 1
        if k>j:
            jumlah += k - j -1

print("Banyaknya triplet a, b, c adalah " + str(jumlah))