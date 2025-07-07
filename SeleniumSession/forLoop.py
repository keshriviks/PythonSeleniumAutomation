obj=[2,3,5,7,9]

for i in obj:
    print(i)
    print(i*2)
print("=============================")
# sum of natural number
add=0
for j in range(1,6):
    add=add+j
    print(add)
print("=============================")
for k in range(1,10,5):
    print(k)
print("=============================")

for m in range(10):
    print(m)
print("========Naveen=====================")
abc ="I love python"
for i in abc:
    print(i)

list=["Naveen", "Automation", "Labs"]
for index in range(len(list)):
    print(list[index])

# for loop with else:
countryList=["India","USa","UK","Russia"]
for index in range(len(countryList)):
    print(countryList[index])
else:
    print("Country list is over")

#nested loop
for i in range(1,5):
    for j in range(i):
        print(i, end='')
    print()

xyz=["Java","Python","Csharp","JavaScript","Golang"]
for i in range(len(xyz)):
    print(abc[i])
    if abc[i]== "Python":
        print("found the language")
        break

name ="Alexander"
for i in name:
    print(i)
    if i=='x':
        break

