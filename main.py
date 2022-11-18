# ::::List Operations::::
veg = ['apple', 'orange', 'peach', 'banana', 'mango']
sta = ['pen', 'pencil', 'sheets', 'notebook', 'diary', 'eraser']
print(veg)
# [ 0,  1,  2,  3,  4]
# [-5, -4, -3, -2, -1]
# list append
veg.append('kiwi')
# extend the list  list.extend(iterable)
# meaning combine other iterables to a list
# veg.extend(sta)
# insert at a specific position in the list
# list.insert(i, x) 
veg.insert(3, 'eggplant')
print(veg)
# Remove the first item from the list whose value is equal to x. 
veg.remove('peach')

# Remove the item at the given position in the list, and return it.
x = veg.pop(2) # pops 'eggplant' and returns it

# without a position, it pops the last item
x = veg.pop() # pops kiwi

# index in the list of the first item whose value is equal to x
print(veg)
i= veg.index('banana')
# i = veg.index('buggy') # raises value error because buggy is not in the list
# count the number of times an item exists in the list
c = veg.count('banana') #returns 1

# sort the list
veg.sort()

# reverse list
veg.reverse()

# shallow copy of list
c = veg.copy()

# clear all items
veg.clear()