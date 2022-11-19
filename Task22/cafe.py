menu = ["item 1", "item 2", "item 3", "item 4"]
# using menu as key
stock = {menu[0]: 11,
         menu[1]: 12,
         menu[2]: 13,
         menu[3]: 14}
price = {menu[0]: 11.25,
         menu[1]: 12.25,
         menu[2]: 13.25,
         menu[3]: 14.25}
total_price = []
for i, item in enumerate(menu):  # loops through menu while having a counter starting 0
    total_price.append(price[item] * stock[item])  # appending (price x stock)
    print(total_price[i])  # display total_price by index i, staring from 0 to size of menu

