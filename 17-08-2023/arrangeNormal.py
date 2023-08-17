# arrange the zero to the end of the array normal form

s = int(input("Enter the array size"))
print("Enter the elements: ")
a = []
for i in range(s):
    a.append(int(input()))

for i in range(s):
    for j in range(i, s):
        if a[i] < a[j]:
            temp = a[j]
            a[j] = a[i]
            a[i] = temp

for i in range(s):
    print(a[i])
