My_list =['a','b','c']
print(type(My_list))

My_list =['a','b','c']
Other_list=['hello', 55,6.1]
print(type(My_list))

My_list =['a','b','c']
result = len(My_list)
print(result)

My_list =['a','b','c']
result = My_list [0]
print(result)

My_list =['a','b','c']
result = My_list [0:]
print(result)

My_list =['a','b','c']
My_list2=['d','e','f']
result = My_list [0]
print(My_list + My_list2)

My_list =['a','b','c']
My_list2=['d','e','f']
My_list3= My_list + My_list2
result = My_list[0:]
print(My_list3)

My_list =['a','b','c']
My_list2=['d','e','f']
My_list3= My_list + My_list2

My_list3[0] = 'alfa'
print(My_list3)

My_list =['a','b','c']
My_list2=['d','e','f']
My_list3= My_list + My_list2

My_list3.append ('g')
print(My_list3)

My_list =['a','b','c']
My_list2=['d','e','f']
My_list3= My_list + My_list2

My_list3.pop(0)
print(My_list3)

My_list =['a','b','c']
My_list2=['d','e','f']
My_list3= My_list + My_list2
delete = My_list3.pop(0)
print(My_list3)
print(delete)

list=['g','o','b','m','c']
list.sort()
print(list)

list=['g','o','b','m','c']
new_list = list.sort()
print(new_list)

list=['g','o','b','m','c']
new_list = list.sort()
print(type(new_list))