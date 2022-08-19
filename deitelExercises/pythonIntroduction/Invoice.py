print()

itemPurchased = []
quantity = []
price = []
totalEach = []
billTotal = 0
willBuyMore = "Yes"
transactionCounter = 1

while willBuyMore == "Yes":
    itemName = str(input("What did customer buy? ").capitalize())
    itemPurchased.append(itemName)

    quantityPurchased = int(input("How many? "))
    quantity.append(quantityPurchased)

    unitPrice = int(input("How much is the item? "))
    price.append(unitPrice)

    total = unitPrice * quantityPurchased
    totalEach.append(total)

    billTotal += total

    willBuyMore = str(input("Will customer buy more? (yes or no) ").capitalize())
    if willBuyMore == "Yes":
        transactionCounter += 1
    else:
        break


def printHeader():
    header: str = """
    SEMICOLON STORES
    MAIN BRANCH
    LOCATION: 312, HERBERT MACAULAY WAY, SABO YABA, LAGOS
    TEL: 08021212121
    DATE: %s
    CASHIER: %s
    CUSTOMER NAME: %s"""
    return header


design = "=" * 50
print("\n" * 3)
print(printHeader())
print(design)
print("         Item        Qty         Price       Total")

print(design)

counter = 0
while counter < transactionCounter:
    print(f'{itemPurchased[counter]: >15s} {quantity[counter]: >10d} {price[counter]: >10d} {totalEach[counter]: >10d}')

    counter += 1
print()
print(design)
print("                             Total :     ", billTotal)
print(design)
print("             THANK YOU FOR YOUR PATRONAGE!!!      ")
print(design)
