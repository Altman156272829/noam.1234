
books = "Harry-Potter,3,40\nDa-Vinci-Code,5,60\nDiary-of-a-Wimpy-Kid,2,50\nAli-Baba,4,25"
first = books.split("\n")
all = []
names = []
num = []
money = []
for i in first:
    all.append(i.split(","))

for i in all:
    names.append(i[0])
    num.append(i[1])
    money.append(i[2])
print("the number of books is:  ", len(names))
sum =0
for i in range(len(num)):
    sum+= int(num[i])*int(money[i])
print(sum)
numIsclosib = []
count = 0
for i in num:
    if int(i)<10:
        numIsclosib.append(names[count])
    count+=1
print(numIsclosib)

      
