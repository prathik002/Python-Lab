my_dict={'banana':3,'apple':1,'cherry':2,'date':4}
print("Original list: ",my_dict)
asorted_dict=dict(sorted(my_dict.items()))
dsorted_dict=dict(sorted(my_dict.items(), reverse=True))
print(f"Ascending order: {asorted_dict}\nDescending order: {dsorted_dict}")
