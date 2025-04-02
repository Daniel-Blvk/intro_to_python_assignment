#empty list
my_list=[]
print(my_list)
# adding elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

print(my_list)

#adding 15 to the second position in the list
my_list.insert(1, 15)

print(my_list)

#removing the last element from the list
my_list.pop(4)
print(my_list)

#sorting in ascending order
my_list.sort()
print(my_list)

#index of item number 30
print(my_list.index(30))