d={}
#copy()#
car = {"brand": "Ford","model": "Mustang","year": 1964}
x = car.copy()
print(x)
#fromkeys()#
x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x, y)
print(thisdict)
#get()#
z=car.get("model")
print(z)
#items()#
k=car.items()
print(k)
#keys()#
p=car.keys()
print(p)
#pop()#
c=car.pop("model")
print(c)
#popitem()#
l=car.popitem()
print(l)
#setdefault()#
q = car.setdefault("model", "Bronco")
print(q)
#update()#
car.update({"color": "White"})
print(car)
#clear()#
car.clear()
print(car)
#values()#
a = car.values()
print(a)
