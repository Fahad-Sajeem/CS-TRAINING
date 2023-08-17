
capacity = 200


def vending(pep,stock):

    if pep < stock:
        stock = stock - pep
        for i in range(pep):
            print("Take your pepsi :)")


    else:
        out = pep - stock

        for i in range(stock):
            print("Take your pepsi :) ")
        stock = 0
        for i in range(out):
            print("out of stock :(")

    print("Have a good drink")
    # print("no.of pepsi in stock: ", stock)

stock = 10
a = 'y'
while a == 'y':
    b = input("do you want pepsi (y/n): ")
    a = b.lower()
    if a == 'y':
        num = int(input("How many pepsi bottles you want?  "))
        vending(num,stock)
    else:
        break
