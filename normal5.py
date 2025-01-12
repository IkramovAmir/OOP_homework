class ShoppingCart:
    def __init__(self, item=None, price=0) -> None:
        self.item = item
        self.price = price
    
    def add_item(self):
        self.item = input("\nEnter product: ")
        self.price = int(input("Enter price: "))
        products.append(self)
    
    def remove_item(self):
        self.item = input("Enter product name: ")
        if self.item in products:
            products.remove(self.item)
            print("Product removed successfully!!!")
        else:
            print('Product is not found!')
                
    
    def get_total(self):
        total = 0
        for product in products:
            total += product.price
        
        return total
            
product1 = ShoppingCart("Chocolate", 11.000)
product2 = ShoppingCart("Vegetable", 25.000)
product3 = ShoppingCart("Kefir", 9.000)
products = [product1, product2, product3]

n = 0
while n != 4:
    print("\nTo add item enter - 1",
          "To remove item enter - 2",
          "To get total enter - 3",
          "To stop enter - 4", sep="\n")
    
    n = int(input("Your choice: "))
    
    if n == 1:
        r = int(input("\nHow many items do you add: "))
        for i in range(r):
            cart = ShoppingCart()
            cart.add_item()
    
    if n == 2:
        product_num = int(input("How many product do u remove: "))
        for i in range(product_num):
            remove = ShoppingCart()
            remove.remove_item()
            
    if n == 3:
        product_prnt = ShoppingCart()
        print(f"\nTotal price: {product_prnt.get_total()}")
        
