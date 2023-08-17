# # arrange the zero to the end of the array company specific arrangement

s = int(input("Enter the array size"))
print("Enter the elements: ")
a = []
for i in range(s):
    a.append(int(input()))
count = 0
q = 0
for i in range(s):
    if a[i] == 0:
        count = count + 1
    else:
        a[q] = a[i]
        q = q+1
for i in range(count):
    a[q] = 0
    q = q+1
    # a.append(0)
for i in range(s):
    print(a[i], end=" ")
