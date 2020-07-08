from typing import Tuple, Union

shop1prices = {"mango": 20, "banana": 30.4, "apple": 15.40, "orange": 40.21}
shop2prices = {"mango": 50, "banana": 26, "apple": 35.71, "orange": 15.78}
shop1priceslist = []
for value in shop1prices.values():
    shop1priceslist.append(value)
print(shop1priceslist)

shop2priceslist = []
for value in shop2prices.values():
    shop2priceslist.append(value)
print(shop2priceslist)

print((5 * shop2priceslist[-1]) + (7 * shop1priceslist[-2]))
print((5 * shop2priceslist[-1]) + (7 * shop1priceslist[-2]))

# adding a new fruit and price
shop1prices_new = {"mango": 20, "banana": 30.4, "apple": 15.40, "orange": 40.21}
shop1prices_new['Pineapple'] = 150
shop2prices_new = {"mango": 50, "banana": 26, "apple": 35.71, "orange": 15.78}
shop2prices_new['Pineapple'] = 190
print(shop1prices_new)
print(shop2prices_new)

# adding both shop prices together
shop1 = {"mango": 20, "banana": 30.4, "apple": 15.40, "orange": 40.21}
shop2 = {"mango": 50, "banana": 26, "apple": 35.71, "orange": 15.78}
sp1 = []
for values in shop1.values():
    sp1.append(values)

sp2 = []
for values in shop2.values():
    sp2.append(values)
spsum = {"mango": sp1[0] + sp2[0], "banana":sp1[1] + sp2[1], "apple":sp1[-2] + sp2[-2], "orange":sp1[-1] + sp2[-1]}
print(spsum)
# is it possible to use a for loop for spsum?
