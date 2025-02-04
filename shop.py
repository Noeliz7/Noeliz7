class Shop:

    # set up the shop items and prices, and other variables
    def __init__(self):
        self.products = ["Kiwi","Strawberries", "Blueberries"]
        self.prices = [.49, 5, 3]
        self.total = 0
       

    # print the name of your shop
    def displayShopName(self):
        print("Busan Market")


    # print all of the items and their prices
    # HINT - use a for loop
    def printItemsAndPrices(self):
        self.prices
        for i in range(len(self.prices)):
            print(self.products[i], self.prices[i]) 

    # add cost of item to the total
    def buy(self, item):
        idx = self.products.index(item)
        cost = self.prices[idx]
        self.total += cost
        print(self.total)                        

    # get the Total apart so far
    def getTotal(self):
        pass

        




s = Shop()
s.displayShopName()
s.printItemsAndPrices()
purch = input("What type of Items are looking for?")


while userInput != "None" :
    s.buy(userInput)
    s.displayShopName()
    s.printItemsAndPrices()
    userInput = input("What type of Items are looking for?")

print(s.getTotal())
    