def mylist():
    my_list = [11, 3, 23, 7]
    my_list.pop(2)
    my_list.pop(2)
    my_list.append(100)
    my_list.insert(2, 100)
    my_list.remove(3)
    print(my_list)


if __name__ == '__main__':
    mylist()

'''
Python provides some very useful list methods that we can use to perform list operation very easily.

Below are the list of python built-in methods which we can use on list:

append(x)
Adds an element at the end of the list

Example
#Append
lst = ['Hello', 'Python']
print(lst)
lst.append('Tutorialspoint')
print(lst)
Output
['Hello', 'Python']
['Hello', 'Python','Tutorialspoint']
clear()
Removes all the elements from the list

Example
#clear
lst = ['Hello','Python','Tutorialspoint']
print(lst)
lst.clear()
print(lst)
Output
['Hello', 'Python', 'Tutorialspoint']
[]
copy()
Returns a shallow copy of the list.

Example
#COPY()
#Without copy
lst = ['Hello', 'Python', 'Tutorialspoint']
lst1 = lst
lst1.append('Java')
print(lst)
print(lst1)
#With copy
lst = ['Hello', 'Python', 'Tutorialspoint']
lst1 = lst.copy()
lst1.append("Java")
print(lst)
print(lst1)
Output
['Hello', 'Python', 'Tutorialspoint', 'Java']
['Hello', 'Python', 'Tutorialspoint', 'Java']
['Hello', 'Python', 'Tutorialspoint']
['Hello', 'Python', 'Tutorialspoint', 'Java']
count()
Returns the number of elements with the specified value.

Example
lst = ['Hello', 'Python', 'Tutorialspoint', 'Python']
print(lst.count("Python"))
print(lst.count("Tutorialspoint"))
print(lst.count(" "))
Output
2
1
0
extend (iterables)
Add the elements of a list (or any iterable), to the end of the current list

Example
#extend(iterables)
lst = ['Hello', 'Python']
print(lst)
lst.extend(['Java', 'CSharp'])
print(lst)
Output
['Hello', 'Python']
['Hello', 'Python', 'Java', 'CSharp']
index(x[,start[, end]])
Returns the index of the first element with the specified value

Example
#index()
lst = ['Hello', 'Python', 'Tutorialspoint', 'Python']
print(lst.index('Python'))
print(lst.index("Python", 2))
Output
1
3
insert(i, x)
Adds an element at the specified position

Example
lst = ['Hello', 'Python', 'Tutorialspoint', 'Python']
print(lst)
lst.insert(0, "CPlusPlus")
print(lst)
lst.insert(3, "Java")
print(lst)
Output
['Hello', 'Python', 'Tutorialspoint', 'Python']
['CPlusPlus', 'Hello', 'Python', 'Tutorialspoint', 'Python']
['CPlusPlus', 'Hello', 'Python', 'Java', 'Tutorialspoint', 'Python']
pop([i])
Removes the element at the specified position

Example
#pop()
lst = ['CPlusPlus', 'Hello', 'Python', 'Java', 'Tutorialspoint', 'Python']
print(lst)
#Without index
lst.pop()
print(lst)
#With Index
lst.pop(3)
print(lst)
Output
['CPlusPlus', 'Hello', 'Python', 'Java', 'Tutorialspoint', 'Python']
['CPlusPlus', 'Hello', 'Python', 'Java', 'Tutorialspoint']
['CPlusPlus', 'Hello', 'Python', 'Tutorialspoint']
remove(x)
Removes the first item with the specified value

Example
#Remove
lst = ['CPlusPlus', 'Hello', 'Python', 'Java', 'Tutorialspoint', 'Python']
print(lst)
lst.remove('Python')
print(lst)
Output
['CPlusPlus', 'Hello', 'Python', 'Java', 'Tutorialspoint', 'Python']
['CPlusPlus', 'Hello', 'Java', 'Tutorialspoint', 'Python']
reverse()
Reverses the order of the list

Example
#reverse()
lst = ['CPlusPlus', 'Hello', 'Python', 'Java', 'Tutorialspoint', 'Python']
print(lst)
lst.reverse()
Output
['CPlusPlus', 'Hello', 'Python', 'Java', 'Tutorialspoint', 'Python']
['Python', 'Tutorialspoint', 'Java', 'Python', 'Hello', 'CPlusPlus']
sort(key = None, reverse = False)
Sorts the list

Example
#sort()
lst = [2, 3, 7, 1, 13, 8, 49]
print(lst)
#default
lst.sort()
print(lst)
#reverse = True
lst.sort(reverse = True)
print(lst)
Output

Method	Description
list[i] = x	Replaces the element at index i with x
list.append(x)	Inserts x at the end of the list
list.insert(i, x)	Inserts x at index i
list.pop(i)	Returns the element a index i, also removing it from the list. If i is omitted, the last element is returned and removed.
list.remove(x)	Removes the first occurrence of x in the list
list.sort()	Sorts the items in the list
list.reverse()	Reverses the order of items of the list
list.clear()	Removes all the items of the list
list.copy()	Creates a copy of the list
list.extend(other_list)	Appends all the elements of other_list at the end of list

https://learntocodetogether.com/big-o-cheat-sheet-for-common-data-structures-and-algorithms/
'''
