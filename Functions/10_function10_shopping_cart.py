#Add function10 shopping cart

def shooping_cart(prices):
    
    total = 0

    for price in prices:
        total += price
    
    
    if total > 1000 :
        discount = (total * 0.1 )
        final_price = (total - discount)
        return(f"Total: {total}\nDiscount: {discount}\nFinal price: {final_price}")
        
    else:
        return(f"Total: {total}\nDiscount: No discount applied\nFinal price: {total}")
    
prices = [500, 300, 400, 350]

print(shooping_cart(prices))

