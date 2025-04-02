L1 = [80, 35, 90, 85, 55, 75, 60, 80, 90]
L2 = [3, 2, 4]
avg = []
count = 0
summ = 0
for i in L2:
    for b in range(i):
        summ = summ+ int(L1[int(b)+count])
    avg.append(int(summ)/i)
    summ = 0
    count +=i 
print(avg)
