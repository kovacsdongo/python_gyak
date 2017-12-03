shopping_list = []


stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# Write your code below!
def compute_bill(food):
    total = 0
    for item in food:
        if stock[item] > 0:
            total = total + prices[item]
            stock[item] -= 1
            continue
        else:
            total = total
    return total

fruit = raw_input("please add some fruit (we have banana,apple,orange,pear): ")
shopping_list.append(fruit)
for items in range(0):
    try:
        if fruit not in stock.keys():
            print "no such fruit"
    except ValueError:
        print "no such fruit"
    else:
            fruit = raw_input("panything else? (we have banana,apple,orange,pear): ")
            shopping_list.append(fruit)

#print shopping_list
#
#print prices


for k,v in prices.items():
    if v == fruit:
        print v


print compute_bill(shopping_list)