# set -not order based
# it stores different types of data
# it performs difference mathematical operation
# it does not store duplicate elements

# define s set: use {1,2,3,4,5,"chinu"}
# list : [2,3,4,5,6,"vikash",3,4]
#tuple : (4,5,8,"kittu","babu")
# dict: a = {1: "first name", 2: "last name", "age": 33}

s1={100,"Tom",23,100,45,True,"chinu"}
s2={1,2,3,4,2,3,1,7,8,9}
print(s1)
print(s2)

#set() function
s3= set("python")
print(s3)
s4= set([20,40,10,20,30,10])
print(s4)
s5= set((20,40,10,20,30,10))
print(s5)

# while creating a set object, you can store only numbers, string, tuple
# list and dictionary objects are not allowed

s6= {(10,20), 30, 40}
print(s6)

#s7= {[10,20], 30, 40} # not allowed
#print(s7)

#set operation - mathematical operation
#union
p1={1,2,3,4,5,}
p2={4,5,6,7,8}
print(p1|p2)
print(p1.union(p2))

# intersection - common elements
p3={1,2,3,4,5,}
p4={4,5,6,7,8}
print(p3&p4)
print(p3.intersection(p4))

# difference of sets - or difference
p5={1,2,3,4,5,}
p6={4,5,6,7,8}
print(p5-p6)
print(p6-p5)
print(p5.difference(p6))

# symmeteric difference unique elements  and remove duplicate
p7={1,2,3,4,5}
p8={4,5,6,7,8}
print(p7^p8)
print(p7.symmetric_difference(p8))

# add method
s1={"java","python","c++"}
s1.add("perl")
print(s1)

#update
s10={"java","python","c++"}
s10.update(["java123","chinu"])
print(s10)
s10.update(("Ruby","javaScript"))
print(s10)

#clear
s10.clear()
print(s10.clear()) #none

#copy
lang={"java","python","perl"}
lang1=lang.copy()
print(lang1)

#discard
lang={"java","python","perl"}
lang.discard("C++")
print(lang)
lang.discard("Naveen")
print(lang)


#remove
student={"Tom","Chinu","Gill","Sai"}
student.remove("Tom")
print(student)

student.remove("Vikash")
print(student) # it will throw an error, element is not present







