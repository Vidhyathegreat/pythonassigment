
   
fruits = {"apple", "banana", "cherry"}
#add()#
fruits.add("orange")
print(fruits)
#copy()#
x = fruits.copy()
print(x)
#difference()#
y = {"google", "microsoft", "apple"}
z = x.difference(y)
print(z)
#difference_update()#
x.difference_update(y)
print(x)
#discard()#
fruits.discard("banana")
print(fruits)
#intersection()#
z = x.intersection(y)
print(z)
#intersection_update()#
x.intersection_update(y)
print(x)
#isdisjoint()#
z = x.isdisjoint(y)
print(z)
#issubset()#
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)
print(z)
#issuperset()#
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z)
#pop()#
fruits.pop()
print(fruits)
#remove()#
fruits.remove("apple")
print(fruits)
#symmetric_difference()#
z = x.symmetric_difference(y)
print(z)
#symmetric_difference_update()#
x.symmetric_difference_update(y)
print(x)
#union()#
z = x.union(y)
print(z)
#update()#
x.update(y)
print(x)
#clear()#
fruits.clear()
print(fruits)
