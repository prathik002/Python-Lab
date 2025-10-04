list1=[3,5,7,11,13]
list2=[2,3,5,7,17]
#a. Check if the list have the same length.
if len(list1)==len(list2):
    print("a.The lists have same length.")
else:
    print("a.The lists have different length.")
#b. Check if the lists have same sum.
print(f"b.Sum of list1: {sum(list1)}  & sum of list2: {sum(list2)}")
if sum(list1)==sum(list2):
    print("  The lists sum to the same value")
else:
    print("  The lists do not sum to the same value")
#c. Check if there are any common values in both the lists
common_value= set(list1) & set(list2)
if common_value:
    print(f"c. Common values in both lists: {common_value}")
else:
    print("c. There are no common values in both the lists.")
