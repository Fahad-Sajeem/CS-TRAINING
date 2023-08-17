s = int(input("Enter the array size: "))
a = []
for i in range(s):
    a.append(int(input()))

for i in range(s - 1):
    for j in range(i + 1, s):
        if a[i] == a[j]:
            for k in range(j, s-1):
                a[k] = a[k + 1]
            s -= 1
            j -= 1

for i in range(s):
    print(a[i], end=" ")
