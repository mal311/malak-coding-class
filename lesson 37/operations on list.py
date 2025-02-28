fruit_list = ['Apple', 'Guava', 'Mango', 'Banana', 'Kiwi' ]
list_size = len(fruit_list)

print("Length of list:", list_size)
print("First element:", fruit_list[0])
print("last element:", fruit_list[-1])

#add papaya on te last element
fruit_list.append('Papaya')
print("updated list after adding papaya:", fruit_list)
print()

#add stawberry between guava and mango
fruit_list.insert(2,"strawberry")# number 2 is the index number(position)
print("updated list after adding strawberry:", fruit_list)
print()

#remove guava
fruit_list.remove("Guava")
print("updated list after removing guava:", fruit_list)
print()

#remove element index 1
fruit_list.pop(1)
print("updated list after removing index 1:", fruit_list)
print()

#sorting list
fruit_list.sort()
print("sorted list:", fruit_list)
print()

#reverse list
fruit_list.reverse()
print("reversed list:", fruit_list)
print()