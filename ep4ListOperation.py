salesAmount = [1000,2000,3000,4000]

print(len(salesAmount))

# Avg = salesAmountAll/Counting

sum = 0;
totalItem = 0;
# For alias in collection
for x in salesAmount:
    sum += x #sum = sum + x
    totalItem += 1 
avg = sum / totalItem
print(avg)