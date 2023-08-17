s = input("Enter the string: ")
s2 = ""
for i in s:
    if i not in s2:
        s2 += i
s2 = s2[::-1]
print(s2)
