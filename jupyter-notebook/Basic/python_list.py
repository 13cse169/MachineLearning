mylist = ["apple", "banana", "orange", "cherry"]
print(mylist)
print(mylist[1], mylist[0])
print(mylist[-2])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
print(thislist[:5])
print(thislist[2:])
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

mylist[1] = "blackcurrant"
print(mylist)

mylist.append("orange")
print(mylist)

mylist.insert(1, "xyz")
print(mylist)

mylist.remove("xyz")
print(mylist)

mylist.pop()
print(mylist)

mylist.pop(1)
print(mylist)