# list of having only integers
a = [1, 2, 3, 4, 5, 6]
print(a)

# list of having only strings
b = ["hello", "john", "reese"]
print(b)

# list of having both integers and strings
c = ["hey", "you", 1, 2, 3, "go"]
print(c)

# index are 0 based. this will print a single character
print(c[1])  # this will print "you" in list c

values =[1, 2, 'vikash', 4, 5]
print(values[0]) # 1
print(values[2])  # vikash
print(values[-1])  # 5 it will last index
print(values[1:3])  # [2, 'vikash']
values.insert(4,"keshri")
print(values) #[1, 2, 'vikash', 4, 'keshri', 5]
values.append("Endvalue")
print(values) #[1, 2, 'vikash', 4, 'keshri', 5, 'Endvalue']
values[2]="RAHUL"
print(values) #[1, 2, 'RAHUL', 4, 'keshri', 5, 'Endvalue']
del values[4]
print(values) #[1, 2, 'RAHUL', 4, 5, 'Endvalue']
print(values) #[1, 2, 'RAHUL', 4, 5, 'Endvalue']
print(values) #[1, 2, 'RAHUL', 4, 5, 'Endvalue']


