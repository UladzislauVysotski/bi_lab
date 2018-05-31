list1 = [a + b for a in 'ab' for b in 'bcd']
list2 = list1[::2]
list3 = [str(i + 1) + "a" for i in range(4)]
print(list3)
list3.remove('2a')
list3_copy = list3 + ['2a']
print(list3_copy)
