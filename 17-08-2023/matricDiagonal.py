r = int(input("Enter the no.of rows: "))
c = int(input("Enter the no.of columns: "))
mat = []

for i in range(r):
    a = []
    for j in range(c):
        a.append(int(input()))
    mat.append(a)

# for i in range(r):
#     for j in range(c):
#         print(mat[i][j], end=" ")
#     print()
#
# print("Diagonal elements: ")
# for i in range(r):
#     for j in range(c):
#         if i == j:
#             print(mat[i][j], end=" ")
#         else:
#             print(end=" ")
#     print()
#
# print("Upper diagonal")
# for i in range(r):
#     for j in range(c):
#         if i < j:
#             print(mat[i][j], end=" ")
#         else:
#             print(end=" ")
#     print()
#
# print("lower diagonal")
# for i in range(r):
#     for j in range(c):
#         if i > j:
#             print(mat[i][j], end=" ")
#         else:
#             print(end=" ")
#     print()
#
# print("Non diagonals: ")
# for i in range(r):
#     for j in range(c):
#         if i == j:
#             print(end=" ")
#         else:
#             print(mat[i][j], end=" ")
#     print()
for i in range(r):
    for j in range(c):
        print(mat[i][j], end=" ")
    print()

print("Diagonal elements: ")
for i in range(r):
    for j in range(c):
        if i == j:
            print(mat[i][j], end=" ")
        else:
            print(end=" ")
    print()

print("Upper diagonal")
for i in range(r):
    for j in range(c):
        if i < j:
            print(mat[i][j], end=" ")
        else:
            print(end=" ")
    print()

print("lower diagonal")
for i in range(r):
    for j in range(c):
        if i > j:
            print(mat[i][j], end=" ")
        else:
            print(end=" ")
    print()

print("Non diagonals: ")
for i in range(r):
    for j in range(c):
        if i == j:
            print(end=" ")
        else:
            print(mat[i][j], end=" ")
    print()