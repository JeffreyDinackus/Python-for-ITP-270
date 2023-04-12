# I made these up because I do not have acces to them.

hairstyles = ["buzzcut", "bowlcut", "mullet", "bouffant"]

prices = [10, 20, 30, 30]

last_week = [2, 3, 5, 2]

total_price = 0

for price in prices:
    total_price += price

print(total_price)
average_price = total_price / len(prices)

print("Average Haircut Price: " + str(average_price))

new_prices = [price - 5 for price in prices]

print(new_prices)

total_revenue = 0

for i in range(0, len(hairstyles)):
    total_revenue += prices[i] * last_week[i]

print("Total Revenue: " + str(total_revenue))

average_daily_revenue = total_revenue / 7

print(average_daily_revenue)

print(hairstyles)
print(new_prices)

#they all get added to the cuts_under_30 because they are all less than 30. 
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]

print(cuts_under_30)
cuts_under_30_2 = []

#this is how I would do it
for x in range(len(new_prices)):
    if new_prices[x] < 30:
      cuts_under_30_2.append(hairstyles[x])

print(cuts_under_30_2)
