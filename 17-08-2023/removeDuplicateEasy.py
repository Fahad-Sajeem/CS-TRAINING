s = int(input("Enter the array size: "))
a = []
for i in range(s):
    a.append(int(input()))
a2 = []
for i in a:
    if i in a2:
        continue
    else:
        a2.append(i)

for i in a2:
    print(i, end=" ")
